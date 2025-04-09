# ============================================================
# Carleton University Challenge: Implement the "quote" command.
#
# When a user sends a message containing "quote",
# your agent should fetch a motivational quote from an external API.
#
# Hints:
# 1. Use the 'requests' library for HTTP GET requests.
# 2. A suggested endpoint is:
#    https://api.quotable.io/random
# 3. Ensure the response is successful (status code 200).
# 4. Parse the JSON to extract the "content" (the quote) and "author".
#
# Useful resources:
# - Requests documentation: https://docs.python-requests.org/en/latest/
# - Quotable API: https://api.quotable.io/
# ============================================================

import requests
from nearai.agents.environment import Environment

def handle_message(message: str) -> str:
    message = message.lower()
    if "hello" in message:
        return "Hello, welcome to NEAR AI!"
    elif "quote" in message:
        res = requests.get("https://api.breakingbadquotes.xyz/v1/quotes")
        if res.status_code == 200:
            data = res.json()
            quote = data[0]["quote"]  
            author = data[0]["author"]
            return f'"{quote}" - {author}'
        else:
            return "Sorry, I couldn't fetch a quote."
    else:
        return "I'm sorry, I didn't understand your message."

def run(env: Environment):
    prompt = {"role": "system", "content": ""}
    result = env.completion([prompt] + env.list_messages())
    env.add_reply(result)
    env.request_user_input()

run(env)
# Optional testing block:
# if __name__ == "__main__":
#    user_input = input("Enter a message for the agent: ")
#    print(handle_message(user_input))
