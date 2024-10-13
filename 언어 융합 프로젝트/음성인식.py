from speech_recognition import Recognizer, Microphone
import clipboard,pyautogui, keyboard
import time, datetime

def read_voice():
    r = Recognizer()
    m = Microphone()

    print('say somthing!')
    with m as source:
        audio = r.listen(source,phrase_time_limit=1) #음성 읽어오기    
    try:
        voice_data = r.recognize_google(audio,language= 'ko')
        print(voice_data) #읽어온 음성 출력
        return voice_data
    except:
        print('이해못함')
def typing(value):
    print(value)
    clipboard.copy(value)
    # pyautogui.hotkey('ctrl','v')

while True:
    if keyboard.is_pressed('ctrl'): #ctrl키가 눌렀을 때 실행
        voice = read_voice() # 음성인식
        time.sleep(0.1) #time 모듈
        typing(voice) # 지금 커서가 있는 곳에 출력
        f = open('C:/Users/c301-09/Desktop/언어융합/음성인식/result/input.txt','a')
        now = datetime.datetime.now() #datetime 모듈
        f.write(voice) #파일에 쓰기
        f.write(' : ')
        now = str(now)
        f.write(now)
        f.write('\n')
        f.close
