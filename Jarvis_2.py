import queue
import sounddevice as sd
import vosk
import json
import Words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
# from skills import *
import pyttsx3
import os
import webbrowser
import sys
import subprocess


def browser():
    webbrowser.open("C:\Program Files\Google\Chrome\Application\chrome.exe", new = 2)

def pcoff():
    os.system("shutdown /s")

def weather():
    webbrowser.open_new_tab("www.google.com/search?q=weather&oq=weather&aqs=chrome.0.69i59l3j0i131i433i512j0i512l6.4555j1j7&sourceid=chrome&ie=UTF-8")

def botoff():
    sys.exit()

def passive():
    pass

def youtube():
    webbrowser.open_new_tab("www.youtube.com/")



rate = 100
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", rate + 50)

def speaker(text):
    engine.say(text)
    engine.runAndWait()

q = queue.Queue()

device = sd.default.device
samplerate = int(sd.query_devices(device[0], "input")["default_samplerate"])
model = vosk.Model("model-small-ru")

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def recognize(data, vectorizer, clf):
    trg = Words.Token.intersection(data.split())
    if not trg:
        return
    data.replace(list(trg)[0], "")
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    print(answer)
    
    func_name = answer.split()[0]
    speaker(answer.replace(func_name, ""))
    exec(func_name + "()")





def main():
    vectorizer = CountVectorizer()
    vevtors = vectorizer.fit_transform(list(Words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vevtors, list(Words.data_set.values()))

    del Words.data_set




    with sd.RawInputStream(samplerate=samplerate, blocksize = 16000, device=device[0],
            dtype="int16", channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())["text"]
                print(data)
                recognize(data, vectorizer, clf)


if __name__== "__main__":
    main()

