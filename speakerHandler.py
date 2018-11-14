import pyttsx3

botSpeaker = pyttsx3.init()

sound = botSpeaker.getProperty('voices')
# botSpeaker.setProperty('voice',sound[1].id)
botSpeaker.setProperty('rate', 150)
botSpeaker.setProperty('volume',5)

# botSpeaker.say("Hello, I am Chat_PoC")
# botSpeaker.runAndWait()
