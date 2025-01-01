# Anshul - Voice Bot/Speech Bot Project

## Overview

This project is a simple **Voice Bot** that leverages speech recognition, text-to-speech, and natural language processing to provide an interactive experience for users. The bot can understand and respond to voice commands, perform Wikipedia searches, tell jokes, provide the current time and date, and open websites like Google and YouTube.

## Features

- **Speech Recognition**: Capture and transcribe audio input using the microphone.
- **Text-to-Speech**: Respond with speech using Google's Text-to-Speech (gTTS).
- **Wikipedia Search**: Search and retrieve summaries from Wikipedia based on the user's query.
- **Jokes**: The bot can tell jokes using the pyjokes library.
- **Open Websites**: Open predefined websites like Google and YouTube via voice commands.
- **Current Time and Date**: The bot can tell the current time and date when asked.
- **Interactive Web Interface**: Built with Streamlit for an easy-to-use UI.

## Requirements

To run this project, make sure to install the following dependencies:

### System-level Dependencies

- **portaudio19-dev**: Required for handling audio input/output (needed for the SpeechRecognition library).
- **python3-all-dev**: Provides development headers for Python 3 to compile and install necessary extensions.

### Python Libraries

- **streamlit**: Web framework for building the app interface.
- **speechrecognition**: Used to recognize speech from the microphone.
- **gtts**: Google's Text-to-Speech library for converting text responses into speech.
- **wikipedia**: Used to query Wikipedia for summaries based on user input.
- **pyjokes**: Fetches random jokes.
- **nltk**: Natural Language Toolkit for processing and understanding text input.
- **pyaudio**: Required for capturing microphone input.
- **webbrowser**: A built-in Python library used for opening web pages.
