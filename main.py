import speech_recognition as sp
from neuralintents import GenericAssistant
import pyttsx3 as ttc
import sys
import time
from datetime import datetime
import wikipedia
import pywhatkit as kt
import os
namecalled = False







speaker = ttc.init()
recogoniser = sp.Recognizer()

to_do_list = ["code ", "game", "intergalatic cable"]












def create_note():
    global recogoniser

    speaker.say("what do you want to write in your note sir")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with sp.Microphone() as mic2:
                audio1 = recogoniser.listen(mic2)
                note = recogoniser.recognize_google(audio1)
                note = note.lower()

                speaker.say("Choose file name")
                speaker.runAndWait()
                audio2 = recogoniser.listen(mic2)
                filename = recogoniser.recognize_google(audio2)
                filename = filename.lower()
            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename} sir")
                speaker.runAndWait()
        except sp.UnknownValueError:
            recogoniser = sp.Recognizer()
            speaker.say("cant do error")
            speaker.runAndWait()

def todo():
    global recogoniser

    speaker.say("what do you want to add in to do list sir")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with sp.Microphone() as mic1:

                audio1 = recogoniser.listen(mic1)
                list1 = recogoniser.recognize_google(audio1)
                list1 = list1.lower()

                to_do_list.append(list1)

                speaker.say(f"item {list1} added to your to do list sir ")
                speaker.runAndWait()
                done = True
        except sp.UnknownValueError:
            recogoniser = sp.Recognizer()
            speaker.say("i didnt understand please try again")
            speaker.runAndWait()

def showtodo():
    speaker.say("the items in your to do list are")
    speaker.runAndWait()
    for i in to_do_list:
        speaker.say(i)
        speaker.runAndWait()

def hello():
    speaker.say("Hello, What can i do for you sir")
    speaker.runAndWait()


def quiter():
    speaker.say("Bye sir , Aak me for any help sir")
    speaker.runAndWait()
    global namecalled
    namecalled = False


def timeteller():
    now = datetime.now()
    formatedtime = now.strftime("%I hours and:%M minutes sir")
    formatedtime = formatedtime.replace("0",'')
    speaker.say(formatedtime)
    speaker.runAndWait()

def wikiresults():
    try:
        impurity = ["what", "is", "the", "who", "is","tell","about","something","tell","me","about","an"]
        message1 = message.split()
        new_message = [x for x in message1 if x not in impurity]
        new_message = "".join(map(str, new_message))
        summary = wikipedia.summary(new_message,1)
        speaker.say(summary)
        speaker.runAndWait()
    except:
        chromesearch()

def chromesearch():
    impure = ["what","is","search","chrome","google","who","crome","browser","in","open"]
    message1 = message.split()
    searchword = [x for x in message1 if x not in impure]
    searchword = "".join(map(str,searchword))
    kt.search(searchword)

def openapp():
    try:
        impure = ["open","run","the","app","application"]
        splitmessage = message.split()
        appname = [x for x in splitmessage if x not in impure]
        appname = "".join(map(str, appname))
        filename_and_path = {
            "telegram":"C:\\Users\\ARUN\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe",
            "files":"C:\Windows\Explorer.exe",
            "explorer" :"C:\Windows\Explorer.exe",
            "file":"C:\\Windows\\Explorer.exe",
            "discord" : "C:\\Users\\ARUN\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
            "pycharm" : "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe",
            "pythoneditoe" : "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"

        }
        os.startfile(filename_and_path[appname])
    except:
        speaker.say(f"cant open {appname} sir")

def date():
    now = datetime.now()
    today = now.strftime("%A")
    speaker.say(f"today is {today} sir")

def youtube():
    impure = ["play","youtube","yt"]
    search = message.split()
    search = [x for x in search if x not in impure]
    searchfin = "".join(map(str,search))
    kt.playonyt(searchfin)



mappings = {
    "greeting": hello,
    "add_todo": todo,
    "add_note": create_note,
    "exit": quiter,
    "show_todo": showtodo,
    "time_teller": timeteller,
    "wikipedia" : wikiresults,
    "chromesearch" : chromesearch,
    "openapp" : openapp,
    "playonyt" : youtube

}


assistant = GenericAssistant('intents.json',intent_methods=mappings)

assistant.train_model()

message = "nil"




while not namecalled:
    try:
        with sp.Microphone() as mic:
            recogoniser.adjust_for_ambient_noise(mic,duration=0.8)
            name_audio = recogoniser.listen(mic,phrase_time_limit=3)
            name_text = recogoniser.recognize_google(name_audio)
            name_text = name_text.lower()
            print(name_text)
            print(type(name_text))
            if((name_text=="hello friday") or (name_text =="friday") ):
                speaker.say("At your service sir")
                speaker.runAndWait()
                namecalled = True
    except sp.UnknownValueError:
        recogoniser = sp.Recognizer()
        print("not activated yet")



while namecalled:
    try:
        with sp.Microphone() as mic:
            recogoniser.adjust_for_ambient_noise(mic, duration=0.8)
            print("listening..")
            audio = recogoniser.listen(mic,phrase_time_limit=3)
            message = recogoniser.recognize_google(audio)
            message = message.lower()
            print(message)

        assistant.request(message)
    except sp.UnknownValueError:
        recogoniser = sp.Recognizer()
        print("threshold touched")