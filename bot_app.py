import streamlit as st
import asyncio
import logging
from bot.bot import listen_command, handle_command, speak_text


# Set up logging to capture any errors
logging.basicConfig(level=logging.INFO)

if "audio_file" not in st.session_state:
    st.session_state.audio_file = None
    
# Function to start listening and handle the command
async def start_bot():

    audio_file = st.audio_input("Speak your command here.")
    if audio_file:
        st.session_state.audio_file = audio_file
        
    command = listen_command(audio_file)  # Listen for the command
    
    if command:
        # Process the command
        #response = handle_command(command)
        #response = asyncio.run(handle_command(command))  # Await the async query handler
        response = await handle_command(command)  # Await the async query handler

        logging.info(f"Bot response: {response}")

        # Optionally, speak the response (voice)
        speak_text(f"Processing your command: {response}") # Ensure speak_text is awaited
        
        # Display the response in the Streamlit app (chat)
        st.write(f"Bot: {response}")
        
        # Speak the response (run in a separate thread)
        speak_text(response)


        # Store the command and response for chat history
        if "history" not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append(f"User: {command}")
        st.session_state.history.append(f"Bot: {response}")

    else:
        st.write("Sorry, I couldn't hear your command. Please try again.")

# Streamlit UI setup
def main():
    # Streamlit UI
    st.title("Voice Assistant Bot")

    # Display instructions or information
    st.write("Ask me any query and I will try to respond!")

    # Add a reset button to clear the state
    if st.button("Reset"):
        st.session_state.history = []
        st.write("History cleared. You can start fresh.")
    
    # Button to start the bot and listen to the command
    if st.button("🎤 Speak"):
        st.write("Listening...")
        #start_bot()
        asyncio.run(start_bot())  # Run the async function in the event loop

if __name__ == "__main__":
    # Start the async loop
    main()

# Display chat history in the sidebar
st.sidebar.title("Voice History")
if "history" in st.session_state and st.session_state.history:
    for chat in st.session_state.history:
        st.sidebar.write(chat)


