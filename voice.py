import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def get_instruction():
    global instruction
    instruction = ""  # Initialize instruction with an empty string
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)  # Corrected method name
            instruction = instruction.lower()
            if "meghs" in instruction:
                instruction = instruction.replace('meghs', "")
                print(instruction)
            
    except:
        pass        
    return instruction
    
def play_meghs():
     instruction = get_instruction()
     print(instruction)
     if "play" in instruction:
         song = instruction.replace('play' , "")
         talk("playing" + song)
         pywhatkit.playonyt(song)

     elif 'time' in instruction:
         time = datetime.datetime.now().strftime('%I:%M %p')
         talk('Current time '+ time)

     elif 'date' in instruction:
         date = datetime.datetime.now().strftime('%d /%m /%y')
         talk("Today's date " + date)
   
     elif 'how are you ' in instruction:
         talk('I am fine, how about you')
        
     elif 'what is your name' in instruction:
         talk('I am Maggi, what can I do for you? ')
    
     elif 'who is ' in instruction:
         human = instruction.replace('who is'," ")
         info = wikipedia.summary(human, 1)
         print(info)
         talk(info)
     
     else:
         talk('Please Repeat')

play_meghs()

