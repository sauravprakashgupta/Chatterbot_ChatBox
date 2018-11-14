from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
# import botSpeaker as speaker

bot = ChatBot('Chat_PoC',
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

bot.set_trainer(ListTrainer)

for _chats in os.listdir('chats'):
    chatFile = open('chats/'+_chats,'r').readlines()
    bot.train(chatFile)

# for corpus in os.listdir('corpus_english'):
#     x = open('corpus_english/'+corpus,'r').readlines()
#     bot.train(x)

userName = input("\nHello I am Chat_PoC, may I know your name ?\n")
print("*******Hello {0}*******".format(userName))
while True:
    userInput = input("{0}: ".format(userName))
    if userInput.lower() == 'bye' or userInput.lower() == 'exit':
        print(' *******Good bye******* ')
        break
    else:
        response=bot.get_response(userInput)
        # if response.confidence < 0.7:
        #     print("This is below confidence level")
        #     for corpus in os.listdir('corpus_english'):
        #         x = open('corpus_english/'+corpus,'r').readlines()
        #         bot.train(x)

        # speaker.bs.say(response)
        print('Chat_PoC :', response)
        # speaker.bs.runAndWait()
