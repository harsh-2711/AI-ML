from gtts import gTTS
import speech_recognition as sr
import webbrowser
import os
import smtplib

# Output
def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")

# Input
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am ready for your next command")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You said " + command + "\n")

        except sr.UnknownValueError:
            assistant(myCommand())

        return command


def assistant(command):
    if "open Reddit in python" in command:
        chrome_path = "Chrome Extension Path"
        url = "http://www.reddit.com/r/python"
        webbrowser.get(chrome_path).open(url)

    if "what's up" in command:
        talkToMe("Chillin bro")

    if "send email" in command:
        talkToMe("who is your recipient")
        recipient = myCommand()

        if "xyz" in recipient:
            talkToMe("What should I say")
            content = myCommand()

            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login("xyz@gmail.com", "abc123")
            mail.sendmail("Someone", "abc@gmail.com", content)
            mail.close()
            talkToMe("Mail Sent")


talkToMe("I am ready for your command")
while True:
    assistant(myCommand())