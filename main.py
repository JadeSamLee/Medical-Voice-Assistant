import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Rapunzel' in command:
                command = command.replace('Rapunzel', '')
                print(command)
    except:
        pass
    return command
def run_assist():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('Playing', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')  
        talk('Current date is ' + current_date)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        fact = command.replace('what is', '')
        info = wikipedia.summary(fact, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'symptoms' in command:
        if 'flu' in command:
            talk("Drink hot water and get some rest")
        elif 'fever' in command:
            talk("Take antibiotics and consult a doctor")
        elif 'headache' in command:
            talk("Rest in a quiet, dark room and take pain relievers")
        elif 'cough' in command:
            talk("Sip warm tea with honey and use cough drops")
        elif 'sore throat' in command:
            talk("Gargle with salt water and stay hydrated")
        elif 'runny nose' in command:
            talk("Use a saline nasal spray and stay well-hydrated")
        elif 'earache' in command:
            talk("Apply a warm compress and take over-the-counter pain relievers")
        elif 'toothache' in command:
            talk("Rinse your mouth with warm saltwater and see a dentist")
        elif 'nausea' in command:
            talk("Eat bland foods, stay hydrated, and rest")
        elif 'vomiting' in command:
            talk("Sip clear fluids and avoid solid foods until vomiting subsides")
        elif 'diarrhea' in command:
            talk("Stay hydrated, eat bland foods, and consider over-the-counter medications")
        elif 'fatigue' in command:
            talk("Get plenty of rest, stay hydrated, and maintain a balanced diet")
        elif 'insomnia' in command:
            talk("Establish a bedtime routine, avoid caffeine, and create a comfortable sleep environment")
        elif 'muscle pain' in command:
            talk("Apply a cold or warm compress and take over-the-counter pain relievers")
        elif 'joint pain' in command:
            talk("Rest the affected joint, use ice or heat packs, and take over-the-counter pain relievers")
        elif 'back pain' in command:
            talk("Practice good posture, use hot or cold packs, and consider gentle exercises")
        elif 'stress' in command:
            talk("Practice relaxation techniques, take breaks, and engage in enjoyable activities")
        elif 'anxiety' in command:
            talk("Practice deep breathing, engage in calming activities, and consider therapy")
        elif 'depression' in command:
            talk("Reach out for support, engage in activities you enjoy, and consider therapy or counseling")
        elif 'allergies' in command:
            talk("Avoid allergens, take antihistamines, and consider nasal sprays")
        elif 'asthma' in command:
            talk("Use an inhaler as prescribed, avoid triggers, and seek medical attention if symptoms worsen")
        elif 'sunburn' in command:
            talk("Apply aloe vera gel, take cool baths, and stay hydrated")
        elif 'poison ivy' in command:
            talk("Clean the affected area, apply calamine lotion, and avoid scratching")
        elif 'insect bite' in command:
            talk("Clean the bite, apply an antihistamine cream, and avoid scratching")
        elif 'minor cut' in command:
            talk("Clean the cut, apply an antibiotic ointment, and cover with a bandage")
        elif 'burn' in command:
            talk("Cool the burn with running water, apply aloe vera, and cover with a sterile dressing")
        elif 'sprain' in command:
            talk("Rest the affected area, ice the injury, compress with a bandage, and elevate")
        elif 'concussion' in command:
            talk("Rest and avoid physical and mental exertion, seek medical attention")
        elif 'blister' in command:
            talk("Keep the blister clean, avoid popping, and use a blister bandage if necessary")
        elif 'pink eye' in command:
            talk("Apply warm compresses, avoid touching the eyes, and seek medical attention")
        elif 'toenail fungus' in command:
            talk("Keep feet clean and dry, use antifungal creams, and wear breathable shoes")
        elif 'migraine' in command:
            talk("Rest in a quiet, dark room, use cold or warm compresses, and take migraine medications")
        elif 'dizziness' in command:
            talk("Sit or lie down, stay hydrated, and avoid sudden movements")
        elif 'heartburn' in command:
            talk("Avoid trigger foods, eat smaller meals, and consider antacids")
        elif 'constipation' in command:
            talk("Increase fiber intake, stay hydrated, and consider over-the-counter laxatives")
        elif 'diabetes' in command:
            talk("Monitor blood sugar levels, maintain a healthy diet, and take medications as prescribed")
        elif 'hypertension' in command:
            talk("Maintain a low-sodium diet, exercise regularly, and take blood pressure medications")
        elif 'cold sores' in command:
            talk("Apply antiviral creams, keep the area clean, and avoid touching the sores")
        elif 'tooth sensitivity' in command:
            talk("Use desensitizing toothpaste, avoid hot or cold foods, and see a dentist")
        elif 'hay fever' in command:
            talk("Avoid allergens, take antihistamines, and use nasal sprays as recommended")
        elif 'acne' in command:
            talk("Cleanse the skin regularly, use non-comedogenic products, and consider topical treatments")
        elif 'eczema' in command:
            talk("Moisturize regularly, avoid irritants, and use prescribed creams or ointments")
        elif 'rash' in command:
            talk("Keep the area clean and dry, apply soothing creams, and avoid scratching")
        elif 'hives' in command:
            talk("Take antihistamines, avoid triggers, and seek medical attention if severe")
        elif 'motion sickness' in command:
            talk("Sit in the front of a vehicle, focus on the horizon, and consider motion sickness medications")
        elif 'ringing in the ears' in command:
            talk("Avoid loud noises, use ear protection, and consider hearing aids if necessary")
        elif 'sinus infection' in command:
            talk("Use nasal decongestants, stay hydrated, and consider antibiotics if prescribed")
        elif 'gout' in command:
            talk("Rest the affected joint, stay hydrated, and take medications as prescribed")
        elif 'gastroenteritis' in command:
            talk("Stay hydrated, eat bland foods, and avoid dairy and caffeine")
        elif 'pink eye' in command:
            talk("Apply warm compresses, avoid touching the eyes, and seek medical attention")
        elif 'plantar fasciitis' in command:
            talk("Rest the foot, use ice or heat packs, and consider orthotic inserts")
        elif 'tennis elbow' in command:
            talk("Rest the arm, use ice packs, and consider over-the-counter pain relievers")
        elif 'carpal tunnel syndrome' in command:
            talk("Take breaks from repetitive tasks, use wrist splints, and consider physical therapy")
        else:
            talk("Sorry, I couldn't find any details regarding the symptoms you are experiencing")

    else:
        talk('I beg your pardon i did not fully understand, can you please repeat again.')
while True:
    run_assist()