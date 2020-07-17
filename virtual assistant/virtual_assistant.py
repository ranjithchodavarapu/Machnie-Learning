import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

# ignore any warnings
warnings.filterwarnings('ignore')

#record audio
def record():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("say something!!!")
        audio=r.listen(source)

    data=''
    try:
     data=r.recognize_google(audio)
     print('you said:'+data)
    except sr.UnknownValueError:
        print("google speech recognition could not understand the audio ")
    except sr.RequestError as e:
        print("request results from google speech recognition service error"+e)

    return data

# response from assistant
def assistresponse(text):

    print(text)

    obj=gTTS(text=text,lang="en",slow=False)
    obj.save('assist_res.mp3')

    os.system('start assist_res.mp3')

#wake
def wake(text):
    WAKE_WORDS=['hello','rao',"computer"]

    text=text.lower()

    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False
# to give current date,day,year
def getdate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthnum=now.month
    daynum=now.day
    yearnum=str(now.year)

    month_name = ["January", "February", "March", "April", "May", "June"
        , "July", "August", "September", "October", "November", "December"]
    ordinalnumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th'
    ,'18th','19th','20th','21th','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31th']

    return 'its '+weekday+' , '+month_name[monthnum-1]+' '+ordinalnumbers[daynum-1]+' '+yearnum+' . '
# return greeting
def greeting(text):

    GREETING_INPUTS=["hi","hey","fella","whatsup","hello"]

    GREETING_RESPONSES=["hello","i'm here","hey","howdy"]

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)+'.'
    return ''
# person name last and first name

def getperson(text):
    wordlist=text.split()

    for i in range(0,len(wordlist)):
        if i+3<=len(wordlist)-1 and wordlist[i].lower()=='who' and wordlist[i+1].lower()=='is':
            return wordlist[i+2]+''+wordlist[i+3]

while True:

    text=record()
    response=''

    if (wake(text)==True):

        response=response+greeting(text)

        if "date" in text:
            get_date=getdate()
            response=response+''+get_date

        if 'time' in text:
            now=datetime.datetime.now()
            meridien=''
            if now.hour>=12:
                meridien='p.m'
                hour=now.hour-12
            else:
                meridien="a.m"
                hour=now.hour

            if now.minute<10:
                minute='0'+str(now.minute)
            else:
                minute=str(now.minute)

            response=response+' '+'it is' +str(hour)+':'+minute+' '+meridien+'.'

        if 'who is 'in text:
            person=getperson(text)
            wiki=wikipedia.summary(person)
            response=response+''+wiki

        assistresponse(response)
