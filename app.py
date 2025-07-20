import streamlit as st
import os
from dotenv import load_dotenv

# --- Import your refactored functions from the 'src' directory ---
# This keeps your app.py clean and focused on the UI.
from src.media_utils import download_audio, transcribe_audio
from src.llm_logic import create_summarization_chain, create_translation_chain

# --- Load Environment Variables ---
# Best practice to load secrets at the very start of your app.
# This will load the HUGGINGFACEHUB_API_TOKEN from your .env file.
load_dotenv() 

# --- Page Configuration ---
# All UI setup and configuration belongs in the main app file.
st.set_page_config(page_title="YouTube Summarizer", page_icon="📽️")
st.title("📽️ Multilingual YouTube Video Summarizer")

# --- Initialize Session State ---
# This is crucial for keeping data (like the summary) between button clicks.
if 'summary' not in st.session_state:
    st.session_state.summary = ""
if 'transcript' not in st.session_state:
    st.session_state.transcript = ""

# --- Create LLM Chains ---
# The app creates the tools it needs by calling your setup functions from llm_logic.py.
# This happens once when the script runs, making it efficient.
chain_summarize = create_summarization_chain()
chain_translate = create_translation_chain()

# --- Sidebar and User Input ---
# All code that creates UI elements for the user to interact with stays here.
st.sidebar.header("📥 Input")
youtube_url = st.sidebar.text_input("Enter YouTube Video URL")
model_type = st.sidebar.selectbox(
    label="Choose the Whisper model type",
    options=['tiny', 'base', 'small', 'medium', 'large']
)

# --- Main Application Flow ---
# This is the core logic that runs when the user clicks the main button.
if st.sidebar.button("🎬 Process Video"):
    if not youtube_url:
        st.sidebar.warning("⚠️ Please enter a valid YouTube URL.")
        st.stop()

    # The 'with st.status(...)' block orchestrates the process, showing UI updates.
    with st.status("🔄 Processing Video...", expanded=True) as status:
        try:
            st.write("📥 Downloading audio...")
            audio_path = download_audio(youtube_url) 
            st.success("✅ Audio downloaded.")

            st.write("🧠 Transcribing audio...")
            transcript, language = transcribe_audio(model_type, audio_path)
            st.success(f"✅ Transcription complete")

            st.write("🤖 Generating summary...")
            summary = chain_summarize.invoke({'text': transcript})
            st.success("✅ Summary generated.")
            
            # Update the session state to persist the results across reruns
            st.session_state.summary = summary
            st.session_state.transcript = transcript

            # Clean up temporary files
            os.remove(audio_path)
            status.update(label="✅ Video processed successfully!", state="complete")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            import traceback
            traceback.print_exc()
            st.stop()

# --- Display Results ---
# This logic checks the session state and displays results accordingly.
# It's separate from the button click, so results stay on screen.
if st.session_state.summary:
    st.subheader("📄 Video Summary")
    st.text_area("📝", st.session_state.summary, height=200)
    st.download_button("💾 Download Summary", st.session_state.summary, file_name="summary.txt")

    with st.expander("📃 Full Transcript"):
        st.text_area("🎧 Transcript", st.session_state.transcript, height=200)

    st.subheader("🌐 Translate Summary")
    language_to_translate_into = st.selectbox(
        label="Choose a language",
        options=['Mandarin Chinese', 'Spanish', 'English', 'Arabic', 'Hindi', 'Bengali', 'Portuguese', 'Russian', 'Japanese']
    )

    if st.button("Translate"):
        with st.spinner("Translating..."):
            translation_input = {
                "language": language_to_translate_into,
                "text_to_translate": st.session_state.summary
            }
            translation = chain_translate.invoke(translation_input)
            st.text_area("🌍 Translated Summary", translation, height=200)
else:
    # The initial message to the user before any processing.
    st.info("👈 Enter a YouTube URL and click **Process Video** from the sidebar.")
