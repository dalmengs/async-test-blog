from AsyncExecutionTime import *
from EnvironmentVariable import env
import requests
import asyncio

"""
    [Reference] OpenAI API Reference Page
    https://platform.openai.com/docs/api-reference/making-requests
"""
API_KEY = env("API_KEY")

@ExecutionTime("Function: get_information")
def get_information(language_name: str) -> str:
    chat_completion = requests.post(
        url="https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f"Briefly explain about {language_name} programming language. Response 5 sentences maximum."
                }
            ]
        }
    )
    gpt_response = chat_completion.json()["choices"][0]["message"]["content"]
    return gpt_response


@AsyncExecutionTime("Main")
async def main():
    language_list = [
        "Python", "Java", "C++", "Javascript", "Go", "Dart", "C#", "Ruby", "PHP", "R"
    ]
    for language_name in language_list:
        response = get_information(language_name)
        print(response)


asyncio.run(main())



