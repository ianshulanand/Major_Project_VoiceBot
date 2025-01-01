import streamlit as st  # Import streamlit for web app
from speech_recognition import Recognizer, AudioFile  # Import speech recognition modules
from gtts import gTTS  # Import Google Text-to-Speech
import wikipedia  # Import Wikipedia API for searching
import pyjokes  # Import pyjokes for generating jokes
import time  # Import time for delays
import io  # For handling byte streams
import nltk  # Natural Language Toolkit for processing text
from nltk import word_tokenize, pos_tag  # Tokenize and POS tagging
import datetime  # For getting current date and time
import webbrowser  # For opening websites in browser

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Anshul A - Voicebot.ai",  # Set page title
    page_icon="https://voicebot.ai/wp-content/uploads/2016/10/voicebot-icon.png",  # Set page icon
    initial_sidebar_state="expanded",  # Sidebar is expanded by default
    layout="centered"  # Center the layout
)

# Title of the app
st.title("🎙️ Speech Bot")

# Adding inline CSS for styling the text and links
st.markdown("""
    <style>
    /* Style the entire text */
    .custom-text {
        font-family: 'Arial', sans-serif;
        font-size: 16px;
        color: none;
    }
    
    /* Style the "Anshul Anand" link */
    .custom-text a {
        color: #0073e6;  /* Link color */
        text-decoration: none;
    }

    /* Hover effect on the link */
    .custom-text a:hover {
        text-decoration: underline;
    }
    </style>

    <div class="custom-text">
        Implemented by <a href="https://www.linkedin.com/in/ianshulanand/" target="_blank">Anshul Anand</a> - 
        View project source code on <a href="https://github.com/ianshulanand" target="_blank">GitHub</a>
    </div>
""", unsafe_allow_html=True)

st.write("\n\n")

# Sidebar content providing instructions for the user
st.sidebar.info("To use voice features, please allow microphone access when prompted by your browser.")
st.sidebar.header("For your information:")
st.sidebar.markdown("### 📜 Instructions")
st.sidebar.markdown("""
    1. Click on the **Start** button to begin interacting with the Speech Bot.
    2. Speak clearly into your microphone when prompted.
    3. The bot will process your speech and respond accordingly.
    4. If you encounter any issues, make sure your microphone access is enabled in your browser.
""")

# Custom CSS for styling the page and sidebar
st.markdown("""
    <style>
        .stApp {  
        }

        .stMarkdown {
            font-size: 1.2rem;
            line-height: 1.8;
        }

        .stButton {
            border-radius: 4px;
            padding: 10px 20px;
            font-size: 1rem;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Initialize the recognizer for speech recognition
recognizer = Recognizer()

# Function to convert text to speech
def text_speech(text):
     tts = gTTS(text=text, lang='en-uk')  # Convert text to speech using gTTS
     speech_bytes = io.BytesIO()  # Use BytesIO to handle speech as bytes
     tts.write_to_fp(speech_bytes)  # Write speech to the byte stream
     speech_bytes.seek(0)  # Go back to the start of the byte stream
     return speech_bytes  # Return the audio in byte format

# Function to capture and transcribe audio
def takeCommand(audio_file):
    if audio_file:
        # Save the uploaded audio as a file
        audio_bytes = audio_file.getvalue()
        with open("mic_audio_string.wav", "wb") as f:
            f.write(audio_bytes)
        with AudioFile("mic_audio_string.wav") as source:
            audio_data = recognizer.record(source)  # Record the audio
        try:
            # Use Google Speech Recognition to transcribe the audio
            text = recognizer.recognize_google(audio_data, language='en-in')
            return text
        except Exception as e:
            st.error(f"Error: Unable to transcribe the audio. Please try again")
            return ""  # Return empty string if there is an error in transcription
    else:
        st.write("No audio input detected.")  # Inform user if no audio input was detected
        return ""  # Return empty string if no audio input

# Initialize session state variables
if "audio_file" not in st.session_state:
    st.session_state.audio_file = None
if "transcribed_text" not in st.session_state:
    st.session_state.transcribed_text = ""
if "response_audio" not in st.session_state:
    st.session_state.response_audio = None

# Adding styled help text
st.markdown("""
    <style>
    .help-text {
        font-size: 20px;
        text-align: center;
        color: #2D3B2F;
        font-family: 'Arial', sans-serif;
        margin-bottom: 15px;
        background-color: #F9F9F9;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    </style>
    <div class="help-text">
        🎤 How can I help you today?
    </div>
""", unsafe_allow_html=True)

# Audio input widget for capturing user audio
audio_file = st.audio_input(
    label=" ",
    help="Use your device's microphone to record your audio query.",
)

if audio_file:
    st.session_state.audio_file = audio_file  # Save audio file to session state

# Placeholder text for microphone permissions
st.markdown("""
    <div style="
        text-align: center; 
        color: #777; 
        font-family: Arial; 
        font-size: 12px; 
        margin-top: 10px;">
        <em>Tip: Ensure your microphone is enabled and permissions are granted for a seamless experience.</em>
    </div>
""", unsafe_allow_html=True)

# Styling for the 'Start Voice Bot' button
st.markdown("""
<style>
    .css-1n76uvr.e16nr0p33 {
        background-color: #4CAF50 !important;
        color: white !important;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 20px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        text-align: center;
        transition: background-color 0.3s, transform 0.2s;
    }
    
    .css-1n76uvr.e16nr0p33:hover {
        background-color: #45a049 !important;
        transform: scale(1.05);
    }

    div.stButton > button {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin: auto;
    }
</style>
""", unsafe_allow_html=True)

# Validation and logic for audio input when user presses 'Start Voice Bot' button
if st.button("Start Voice Bot ▶", help='Click to start voice bot'):
    # Check if no audio file was uploaded or recorded
    if not st.session_state.audio_file:
        st.markdown("""
        <div style="
            font-size: 16px;
            color: #D9534F;
            background-color: #FDEDEC;
            border: 1px solid #E5B5B5;
            border-radius: 5px;
            padding: 10px;
            margin-top: 10px;">
            ❗ **Validation Error:** Please enter a query or provide an audio input before starting the bot.
        </div>
    """, unsafe_allow_html=True)
    else:
        # Process the audio if it's present
        st.session_state.transcribed_text = takeCommand(st.session_state.audio_file)
    

# Process and respond based on transcribed text
try:
    if st.session_state.transcribed_text:
        transcribed_text = st.session_state.transcribed_text.lower()  # Convert text to lowercase
        st.markdown(f'<p style="text-align: right;">Anshul: {transcribed_text}</p>', unsafe_allow_html=True)  # Show transcribed text

        # Check for different keywords in the transcribed text and generate appropriate responses
        if any(word in transcribed_text for word in ['hi', 'hello', 'hey']):
            response_text = "Hey there!😊 How can I assist you?"
        
        # Wikipedia search logic
        elif any(word in transcribed_text for word in ['who', 'what', 'where', 'wikipedia', 'search']):
            try:
                query_tokens = word_tokenize(transcribed_text)  # Tokenize the transcribed text
                essential_words = [word for word, tag in pos_tag(query_tokens) if tag in ['NN', 'NNP']]  # Extract nouns
                query = " ".join(essential_words)  # Join nouns to form the query
                with st.spinner(f"Searching for.....{query}"):
                    st.write(f"Searched for {query}")
                    search_results = wikipedia.search(query)  # Perform Wikipedia search
                    if search_results:
                        best_match = search_results[0]  # Get the best match
                        response_text = wikipedia.summary(best_match, sentences=1)  # Fetch summary
                    else:
                        st.write("I couldn't find anything on Wikipedia.")
            except Exception as e:
                st.error("Oops! Your query is too broad. Please refine your search.")
                st.write("Here are some suggestions:")

        # Handle requests for opening websites like Google and YouTube
        elif "open youtube" in transcribed_text:
            msg = st.empty()
            msg.warning(
                "To use voice commands like 'Open YouTube', please ensure pop-ups are allowed in your browser."
            )
            time.sleep(3)
            msg.empty()
            st.components.v1.html("""
                <script type="text/javascript">
                    window.open("https://www.youtube.com", "_blank");
                </script>
            """, height=0)
            response_text="Opened Youtube in Browser"

        elif "open google" in transcribed_text:
            msg = st.empty()
            msg.warning(
                "To use voice commands like 'Open Google', please ensure pop-ups are allowed in your browser."
            )
            time.sleep(3)
            msg.empty()
            st.components.v1.html("""
                <script type="text/javascript">
                    window.open("https://www.google.com", "_blank");
                </script>
            """, height=0)
            response_text="Opened Google in Browser"

        # Handle time and date queries
        elif 'time' in transcribed_text or 'date' in transcribed_text:
            now = datetime.datetime.now()  # Get current date and time
            formatted_date = now.strftime("%B %d, %Y")  # Format date
            formatted_time = now.strftime("%I:%M %p").lower()  # Format time
            response_text=f"Today is {formatted_date}, and the time is {formatted_time}."

        # Handle joke requests
        elif 'joke' in transcribed_text:
            jokes = pyjokes.get_joke()  # Get a joke using pyjokes
            response_text=f"Here it comes! {jokes}"

        # Handle gratitude responses
        elif any(word in transcribed_text for word in ['thank you', 'thanks']):
            response_text="You're welcome!"

        # Handle exit commands
        elif any(word in transcribed_text for word in ['exit', 'bye', 'goodbye', 'end']):
            response_text = "Thanks for giving me your time!"
            st.stop()  # Stop the app

        else:
            response_text = "Sorry, I didn't understand that."

        # Convert bot response to speech and play it
        st.session_state.response_audio = text_speech(response_text)
        
        # Output the bot's response as audio and text
        st.write(f"Bot: {response_text}")
        st.audio(st.session_state.response_audio, format="audio/wav", start_time=0, autoplay=True)

        # Clear transcribed text after processing
        st.session_state.transcribed_text = ""

except Exception as e:
    st.error("Please refine your search")
    st.write("Please try one more time")

# Buttons to reset or exit
c1,c2 = st.columns([1, 1])
with c1:
    if st.button("Sleep", use_container_width=False):
        st.markdown('Goodbye. If you need help again, don\'t hesitate to reach out. Have a great day!', unsafe_allow_html=True)
        st.session_state.response_audio = text_speech("Goodbye! If you need help again, don't hesitate to reach out. Have a great day!")
        st.audio(st.session_state.response_audio, format="audio/wav", start_time=0, autoplay=True)
        st.stop()

with c2:
    st.button("Reset", help="Click to clear all")  # Reset button to clear everything
