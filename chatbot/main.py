import random

user_template = "USER: {0}"
bot_template = "BOT: {0}"

# Input :
def send_message(message):
    print(user_template.format(message))
    response(message)

# Output:
def response(message):
    temp = responses(message)
    print(bot_template.format(temp))

def responses(message):
    # Possible Questions
    responses = {

        "What's the weather today?": [
            "Cloudy",
            "Foggy",
            "Sunny",
            "Rainy",
            "Clear"
        ],

        "What's your name": [
            "My name is Echo, Spidey Echo",
            "It goes by the name, Spidey Echo",
            "My name is Spidey Echo",
            "You can call me Spidey Echo"
        ],

        "default": [
            "Sorry, I can't understand you"
        ]
    }
    for i in responses:
        if i == message:
            return random.choice(responses[i])

    return random.choice(responses["default"])


while True:
    message = input()
    if message == "Exit":
        break
    else:
        send_message(message)
