import json
import os
import speech_recognition as sr
#import pyttsx3
#import asyncio
import threading
import logging

from gtts import gTTS
from .weather import get_weather
from .sentiment import analyze_sentiment
from .personalization import get_user_name, set_user_name
from .utils import log_error
from .jokes import get_joke
from .news import get_news
from .reminder import set_reminder
from .translate import translate_text
from .google_search import google_search
from .wikipedia_search import wikipedia_search

# Initialize logging
logging.getLogger('comtypes.client._code_cache').setLevel(logging.ERROR)

#recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
#engine = pyttsx3.init()

# Create a lock for thread safety when speaking
speech_lock = threading.Lock()

# Function to listen to the microphone (single query)
def listen_command(uploaded_audio):
    #recognizer = sr.Recognizer()

    # Ensure the user uploads an audio file (WAV/MP3)
    if uploaded_audio is not None:
        st.write("Audio is Recorded.")
        audio_bytes = audio_file.getvalue()
        with open("temp_audio.wav", "wb") as file:
            file.write(audio_bytes)
        with AudioFile("temp_audio.wav") as source:
            audio = recognizer.record(source)

    #with sr.Microphone() as source:
        #logging.info("Listening... Please speak your query.")
        #recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise

        try:
            # Listen for the first phrase and stop listening after that
            #audio = recognizer.listen(source)
            
            command = recognizer.recognize_google(audio)
            logging.info(f"Command Received: {command}")
            return command
        
        except sr.UnknownValueError:
            logging.error("Sorry, I could not understand the audio.")
            return None
        
        except sr.RequestError as e:
            logging.error(f"Error with the speech recognition service: {e}")
            return None
        
# Function to speak text
def speak_text(text):
    # Run the engine in a separate thread
    def speak():
        with speech_lock:  # Ensure only one thread can speak at a time
            #engine.say(text)
            #engine.runAndWait()
            
            # Use gTTS to convert text to speech and save as an audio file
            tts = gTTS(text)
            audio_path = "output.mp3"
            tts.save(audio_path)
            
            # Play the audio file in Streamlit
            st.audio(audio_path, format="audio/mp3")

            # Optionally, you can delete the file after playing to avoid accumulation of files
            os.remove(audio_path)

    # To avoid the run loop already started error, run the speech synthesis in a separate thread
    threading.Thread(target=speak).start()

# Async function to process a query
async def handle_command(command):

    print(f"Processing query: {command}")
    
    command=command.lower()

    if "hello" in command or "hi" in command or "hey" in command:
        name = get_user_name()
        speak_text(f"Hello {name}, how can I assist you today?")
        return f"Hello {name}, how can I assist you today?"

    elif "time" in command:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        speak_text(f"The time is {current_time}")
        return f"The time is {current_time}"

    elif "date" in command:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak_text(f"Today's date is {current_date}")
        return f"Today's date is {current_date}"

    elif "weather" in command:
        #city = command.split("weather in")[-1].strip() if "weather in" in command else "London"
        if "weather in" in command:
            city = command.split("weather in")[-1].strip()
        else :
            city = "London"
        print(f"City: {city}")
        #print(command.split("weather in")[-1].strip())
        #weather_info = get_weather(city)
        #city=input("Enter city for weather: ").strip()
        weather_info = get_weather(city)
        #print(weather_info)
        speak_text(weather_info)
        return weather_info

    elif "change name" in command:
        speak_text("What would you like me to call you?")
        new_name = listen_command()
        if new_name:
            set_user_name(new_name)
            speak_text(f"Your name has been updated to {new_name}.")
            return f"Your name has been updated to {new_name}."

    elif "sentiment" in command:
        sentiment = analyze_sentiment(command)
        speak_text(f"The sentiment of your statement is: {sentiment}")
        return f"The sentiment of your statement is: {sentiment}"
    
    elif "joke" in command:
        joke = get_joke()
        speak_text(joke)
        return joke
    
    elif "news" in command:
        api_key = '7065ae9fd9f6468f9b434e018614a12a'
        news = get_news(api_key)
        speak_text(news)
        return news

    elif "reminder" in command:

        try:
            # Check if 'at' is in the command to extract time
            if "at" in command:
                time_str = command.split("at")[-1].strip()
                # Call set_reminder with the extracted time string
                reminder_response = set_reminder(time_str, "Your reminder!")
                return reminder_response
            else:
                return "Please specify a time for the reminder using 'at'. For example, 'remind me at 15:30'."
        except Exception as e:
            return f"Error setting reminder: {e}"
    
    elif "translate" in command:
        #text_to_translate = command.split("translate")[-1].strip()
        #text_to_translate = input("Enter text to translate: ").strip()
        speak_text("Speak text to translate?")
        text_to_translate = listen_command()
        #print(text_to_translate)
        translation = translate_text(text_to_translate, src='auto', dest='fr')
        speak_text(translation)
        return translation
    
    elif "google search" in command.lower():
        speak_text("What do you want to search for?")
        search_query = listen_command()
        if search_query.strip():
            result = google_search(search_query)
            print(f"Search Results:\n{result}")
            speak_text("Here are the top 5 search results.")
            return result
        else:
            speak_text("I couldn't understand your query. Please try again.")

    elif "search wikipedia" in command.lower():
        speak_text("What would you like to search for on Wikipedia?")
        search_query = listen_command()  # Capture user input
        if search_query and search_query.strip():  # Validate input
            result = wikipedia_search(search_query)
            print(f"Wikipedia Result:\n{result}")
            speak_text(result)
            return result
        else:
            speak_text("I couldn't understand the query. Please try again.")
    
    elif "exit" in command:
        speak_text("Goodbye!")
        exit()
    else:
        speak_text("Sorry, I didn't understand the command.")
        return "Sorry, I didn't understand the command."
