import pyttsx3                      #This module helps to convert text to speech
from chatterbot import ChatBot      #Cgatterbot module
import speech_recognition as sr     #To convert speech to text

#Initializing the recognizer
r=sr.Recognizer()
r.energy_threshold=400
r.dynamic_energy_threshold = False

#initializing engine which will convert text to audio
engine=pyttsx3.init()

#Defining bot name
bot=ChatBot("Jarvis")

'''
Chat bot already trained once so no need to trainit again
'''
# from chatterbot.trainers import ChatterBotCorpusTrainer
# bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train('chatterbot.corpus.english')


print("{}:Hi I am {}, How can i help?".format(bot.name,bot.name))
engine.say("Hi I am {}, How can i help?".format(bot.name))
engine.runAndWait()


while True:
    
    #Accesing microphone to record the audio
    with sr.Microphone() as source:
        print("-----------Say Something----------")
        text=r.listen(source,timeout=10.0)
    print("----------Recognizing...----------")
    
    #Using google speechrecognition to convert audio to speech
    try:
        message=r.recognize_google(text)
        print("you:{}".format(message))
    

    #Incase of fail to recognise print this message
    except sr.UnknownValueError:
        print("{}:Sorry i couldn't understand".format(bot.name))
        engine.say("Sorry i couldn't understand")
        engine.runAndWait()
        continue

    except sr.RequestError:
        print("Please Connect to Internet and try again")
        engine.say("Please Connect to Internet and try again")
        engine.runAndWait()
        break

    #getting response from the chatbot
    if(message=='BYE' or message=='bye' or message=='quit'):
        print('{}: Bye, see you later!'.format(bot.name))
        engine.say('Bye, see you later!')
        engine.runAndWait()
        break
    if(message=='What is your name'or message=='what is your name'):
        print('{}:I am Jarvis'.format(bot.name))
        engine.say('I am Jarvis.')
        engine.runAndWait()
        continue
    else:
        reply=bot.get_response(message)
        print('{}: {}'.format(bot.name,reply))
        engine.say(reply)
        engine.runAndWait()


