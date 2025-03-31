import openai

openai.api_key = "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"

while True:

    prompt = input("\nIntroduce Una pregunta:")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003",
                             prompt=prompt,
                             max_tokens=2048)

    print(completion.choices[0].text)