from AsyncExecutionTime import *
from AsyncHttpRequest import Request
from EnvironmentVariable import env
import requests
import asyncio

"""
    [Reference] OpenAI API Reference Page
    https://platform.openai.com/docs/api-reference/making-requests
"""
API_KEY = env("API_KEY")

@AsyncExecutionTime("Function: get_information")
async def get_information(language_name: str) -> str:
    chat_completion = await Request.post(
        url="https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        },
        data={
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
    tasks = []
    for language_name in language_list:
        tasks.append(asyncio.create_task(get_information(language_name)))
    response = await asyncio.gather(*tasks)
    print("\n".join(response))


asyncio.run(main())



