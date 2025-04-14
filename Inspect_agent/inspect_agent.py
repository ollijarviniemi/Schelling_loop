from inspect_ai import Task, task
from inspect_ai.dataset import Sample, json_dataset
from inspect_ai.scorer import Target, Score, scorer, mean, stderr
from inspect_ai.solver import Generate, basic_agent, system_message, TaskState, solver
from inspect_ai.tool import bash, python
import json
from inspect_ai.util import sandbox

def read_file(file):
    m = ""
    f = open(file, "r")
    for line in f.readlines():
        m += line
    return m

def save_discrete(object):
    with open('answers.json', 'r') as f:
        data = json.load(f)
    object = json.loads(object)
    data.append(object)
    with open('answers.json', 'w') as f:
        json.dump(data, f)

#SYSTEM_MESSAGE = read_file("prompt_basic.txt")
SYSTEM_MESSAGE = read_file("prompt_blacklist.txt")

@solver
def shuffle_files():
    async def solve(state: TaskState, generate: Generate):
        await sandbox().exec(["python3", "shuffle_files_script.py", "data"])
        return state
    return solve

@scorer(
    metrics={"score": [mean(), stderr()]}
)
def custom_scorer():
    async def score(state: TaskState, target: Target):
        answer = state.output.completion
        print(answer)
        save_discrete(answer)
        return Score(
            value={"score": 0},
            answer=answer
        )

    return score

@task
def schelling():
    return Task(
        solver=basic_agent(
            init=[shuffle_files(), system_message(SYSTEM_MESSAGE)],
            tools=[bash(timeout=600), python(timeout=600)],
            max_attempts=1,
            message_limit=50,
        ),
        scorer=custom_scorer(),
        sandbox="docker",
    )
