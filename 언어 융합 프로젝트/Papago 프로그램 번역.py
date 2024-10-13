'''
import os, sys
import urllib.request, json, pprint

client_id = "W_XkY2kilufRM5Q5_rdM"
client_secret = "FiyAE72X3_"

#번역할 언어와 내용에 입력
text = input("번역할 내용 입력하세요:")
encText = urllib.parse.quote(text)
srcLang = ''
data = "query=" + encText
url = "https://openapi.naver.com/v1/papago/detectLangs"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if(rescode ==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    trans_text = json.loads(response_body.decode('utf-8'))
    srcLang = trans_text['langCode']

else:
    print("Error Code:" + rescode)
print(srcLang)
'''
#음성인식 + 파파고번역

#음석인식 모듈
from speech_recognition import Recognizer,Microphone
import clipboard, keyboard, pyaudio
from pyautogui import *
import time, datetime

#파파고 번역 모듈
import urllib.request, json


def read_voice():
    r = Recognizer()
    mic = Microphone()
    print('say something!')
    with mic as source:
        audio = r.listen(source, phrase_time_limit=3)
    try:
        voice_data = r.recognize_google(audio,language="ko")
    except:
        print("이해못함")

def typing(value):
    clipboard.copy(value)
    hotkey('ctrl','v')

while True:
    if keyboard.is_pressed('ctrl'):
        voice = read_voice()
        time.sleep(0.1)
        #파파고 번역 애플리케이션 정보
        client_id =  "f7OaDIFXUOQR6U6YxgU1"
        client_secret = "6PrCsvPGAp"
        #번역할 언어와 내용 입력 
        text = voice
        encText = urllib.parse.quote(text)
        srcLang = ''
        #언어번역
        tarLang = 'en'
        data = 'source=ko&target=en&text='.format(srcLang, tarLang)+encText
        url = 'https://openapi.naver.com/v1/papago/n2mt'
        request = urllib.request.Request(url)
        request.add_header('X-Naver-Client_Id',client_id)
        request.add_header('X-Naevr-Client-Secret',client_secret)
        response = urllib.request.urlopen(request, data=data.encode('utf-8'))
        rescode = response.getcode()

        if(rescode==200):
            response_body = response.read()
            data = response_body.decode('utf-8')
            data= json.loads(data)
            trans_text = data['message']['result']['translatedText']
        
        else:
            print('error code:' + rescode)
        
        print("번역될 내용:",voice)
        print("번역될 내용:",trans_text)
        f = open("C:/Users/c301-09/Desktop/언어융합/음성인식/result/input2.txt","a")
        now = datetime.datetime.now()
        f.write(trans_text)
        f.write(' : ')
        now = str(now)
        f.write(now)
        f.write('\n')
        f.close
        press('enter') #줄바꿈
