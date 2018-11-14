from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speakerHandler as speaker

bot1 = ChatBot('Chat_PoC1',
        storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
        logic_adapters=[
            "chatterbot.logic.BestMatch",
            # "chatterbot.logic.TimeLogicAdapter",
            "chatterbot.logic.MathematicalEvaluation"
        ],
        filters=[
            'chatterbot.filters.RepetitiveResponseFilter'
        ],
        database='chatterbot-Chat_PoC')

bot2 = ChatBot('Chat_PoC2',
        storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
        logic_adapters=[
            "chatterbot.logic.BestMatch",
            # "chatterbot.logic.TimeLogicAdapter",
            "chatterbot.logic.MathematicalEvaluation"
        ],
        filters=[
            'chatterbot.filters.RepetitiveResponseFilter'
        ],
        database='chatterbot-Chat_PoC')
# conv = open('chats.txt','r').readlines()


bot1.set_trainer(ListTrainer)
bot2.set_trainer(ListTrainer)

for _chats in os.listdir('chats'):
    chatFile = open('chats/'+_chats,'r').readlines()
    bot1.train(chatFile)

for _corpus in os.listdir('corpus_english'):
    corpusFiles = open('corpus_english/'+_corpus,'r').readlines()
    bot2.train(corpusFiles)

firstGreeting = "Hello I am Chat_PoC, may I know your name ?"
speaker.botSpeaker.say(firstGreeting)
print(firstGreeting)
speaker.botSpeaker.runAndWait()
userName = input("--")

print("*******Hello {0}*******".format(userName))
speaker.botSpeaker.say("Hello {0}".format(userName))
speaker.botSpeaker.runAndWait()

while True:
    userInput = input("{0}: ".format(userName))
    if userInput.lower() == 'bye' or userInput.lower() == 'exit':
        print("*******Good bye*******")
        break
    else:
        response=bot1.get_response(userInput)
        # print(type(response))
        if response.confidence < 0.2:
            errorMsg = "Sorry, I am not sure with this"
            speaker.botSpeaker.say(errorMsg)
            print(errorMsg)
            speaker.botSpeaker.runAndWait()
            print("confidence level-{0}\n".format(response.confidence))
            continue
        elif response.confidence < 0.7:
            print("This is below confidence level - {}".format(response.confidence))
            response=bot2.get_response(userInput)

        speaker.botSpeaker.say(response)
        print('Chat_PoC : {0}\nconfidence-{1}\n'.format(response, response.confidence))
        speaker.botSpeaker.runAndWait()
