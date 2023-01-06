import speech_recognition as sr
from datetime import datetime
from playsound import playsound
from gtts import gTTS
import random
import os
import time

import translators as ts


r = sr.Recognizer()
mic = sr.Microphone()




def dinle():
    text = ''
    with mic as m:
        print("seni dinliyorum")
        audio = r.listen(m)
        try:
            text = r.recognize_google(audio,language='tr-TR')
          
            rand = random.randint(1,100000)
            file = open("text-"+str(rand)+".txt", "w" , encoding='utf-8')
            file.write(text)
            file.close()
            #translate alanı :
            cevir(file.name)
            os.remove(file.name)
         
            
             
        except sr.UnknownValueError:
            print("----seni anlayamadım---")
            
    return text,file


def cevir(a):
    dosya = open(a , 'r')
    text = dosya.read()
    result = ts.translate_text(text, to_language='en')
    print(result)
    #Konusturma
    konus(result)
    

def konus(result):
     #Konuşturma alanı : 
    tts = gTTS(result,lang='en')
    rand = random.randint(1,100000)
    file = "audio-"+str(rand)+".mp3" 
    tts.save(file)
    playsound(file)
    os.remove(file)
    


while True:
    
    text = dinle().lower()
    if "uygulamadan çık" in text:
        break
    else:
        pass
        
    

