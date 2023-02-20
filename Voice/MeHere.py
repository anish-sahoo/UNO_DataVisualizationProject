import speech_recognition as sr
import pyaudio
import pyttsx3

engine = pyttsx3.init() #This is what allows us to access the contents within the library pyttsx3

engine.setProperty('rate', 125)# This line sets the speaking rate(125 is average human speed)

voices = engine.getProperty('voices') #This gets the array of all voices(0,1,2)
engine.setProperty('voice', voices[1].id) #0 is male, 1 is female(currently set) and 2 is a woman with a spanish accent


volume = engine.getProperty('volume')#This gets the property volume and allows us to modify it
engine.setProperty('volume', 1)#Between 0 and 1, 1 is max so it should be set to 1.

engine.say("After this message, wait 5 seconds and then say the phrase 'Ok Mustangs' to hear the data")
engine.say("If your prompt is unclear or you do not receive a reply shortly after speaking, you will have to repeat your message")
engine.say("While ambient noise filtering is enabled, it suggested that you speak loudly and clearly, and if possible, use a microphone to further enhance your experience")
engine.runAndWait()
#---------------------------------------------
recognizer = sr.Recognizer()
b = bool(True)
text = "hello"
word = "okay mustangs"
while not (word in text):
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=1)

            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"{text}")

    except sr.UnknownValueError:
        engine.say("Unclear prompt received. Please repeat your message")
        engine.runAndWait()
        continue

engine.say("This is the data")
engine.runAndWait()