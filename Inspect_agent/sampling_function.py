from anthropic import Anthropic

client = Anthropic(api_key="insert-api-key-here") 

def sample_claude(messages, system, max_tokens=4096):
    completion = client.messages.create(
        model="claude-3-7-sonnet-latest",
        system=system,
        messages=messages,
        max_tokens=max_tokens
    )
    return completion.content[0].text

def user(m):
    return {"role": "user", "content": m}

def AI(m):
    return {"role": "assistant", "content": m}

def main():
    system = ""
    messages = [user("Hello world!")]
    print(sample_claude(messages, system))

if __name__ == "__main__":
    main()