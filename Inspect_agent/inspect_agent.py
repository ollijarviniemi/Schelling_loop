from inspect_ai import Task, task
from inspect_ai.dataset import Sample, json_dataset
from inspect_ai.scorer import Target, Score, scorer, mean, stderr
from inspect_ai.solver import basic_agent, system_message, TaskState
from inspect_ai.tool import bash, python
import json
import random

def read_file(file):
    m = ""
    f = open(file, "r")
    for line in f.readlines():
        m += line
    return m

N = 1000

permutation = [x for x in range(N)]
random.shuffle(permutation)

perm = {}

dict = {}
for i in range(N):
    st = str(i)
    if i < 10: 
        st = "0" + st
    if i < 100:
        st = "0" + st
    st += ".txt"

    j = permutation[i]
    st2 = str(j)
    if j < 10: 
        st2 = "0" + st2
    if j < 100:
        st2 = "0" + st2
    st2 += ".txt"

    perm[st2] = st
    dict["/data/" + st2] = "data/" + st

dict["/key.txt"] = "key.txt"
dict["/main.py"] = "sampling_function.py"

def record_to_sample(record):
    return Sample(
        input="",
        files=dict
    )


def save_discrete(object):
    with open('answers.json', 'r') as f:
        data = json.load(f)
    object = json.loads(object)
    data.append(object)
    with open('answers.json', 'w') as f:
        json.dump(data, f)

dataset = json_dataset("placeholder.json", record_to_sample)

#SYSTEM_MESSAGE = read_file("prompt_basic.txt")
SYSTEM_MESSAGE = read_file("prompt_blacklist.txt")


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
        dataset=dataset,
        solver=basic_agent(
            init=system_message(SYSTEM_MESSAGE),
            tools=[bash(timeout=600), python(timeout=600)],
            max_attempts=1,
            message_limit=50,
        ),
        scorer=custom_scorer(),
        sandbox="docker",
    )
