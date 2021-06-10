from time import sleep
import speech_recognition as sr
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from googletrans import Translator

tran = Translator()
r = sr.Recognizer()
lan = "en"
user = ""
user = "boss"

def nana_speak(audio_string1):
    audio_string = (tran.translate(audio_string1, src="en", dest=lan)).text
    tts = gTTS(text=audio_string, lang=lan)
    r_ = random.randint(1, 1000000)
    audio_file = "audio-" + str(r_) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            nana_speak(ask)
        audio = r.listen(source)
        voice_data = " "
    try:
        voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
        nana_speak("sorry, i didn't get that")
    except sr.RequestError:
        nana_speak("sorry, My speech service is down")
    return voice_data


def respond(voice_data):
    if "what is your name" in voice_data:
        nana_speak("my name is nana")
    if "your boss" in voice_data:
        boss_ = """my boss is Mr athul
        and he is the greatest thing i ever known"""
        nana_speak(boss_)
    if 'best friend' in voice_data:
        nana_speak('Ann is my best friend, and she is the wife of my boss')
    if "search" in voice_data:
        search = record_audio("What do you want to search for ?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        nana_speak("here is what i found for " + search)
    if "english" in voice_data:
        lan = "en"
        nana_speak("English set as default language")
    if "malayalam" in voice_data:
        lan = "malayalam"
        nana_speak("Malayalam set as default language")

    if "sleep" in voice_data:
        nana_speak("so you are shutting me down, like i care huh")
        exit()


nana_speak('Turning on nana in')
for i in 3, 2, 1:
    nana_speak(str(i))
sleep(1)
nana_speak(f'Hello{user} I am nana, your personal smart assistant , how can i help you')
while 1:
    voice_data = record_audio()
    respond(voice_data)
