# 📽️ AI-Powered Multilingual YouTube Video Summarizer
<img width="2222" height="1088" alt="image" src="https://github.com/user-attachments/assets/9d34aa43-1612-423c-b79e-34bc88a5dc99" />
<img width="2216" height="1014" alt="image" src="https://github.com/user-attachments/assets/15727042-0c73-4e17-976d-8743e1fa5291" />


## ✨ Features

- **YouTube Audio Downloader:** Ingests any public YouTube video URL and extracts the audio stream using `yt-dlp`.
- **Multilingual Transcription:** Utilizes OpenAI's Whisper model to accurately transcribe audio from a wide range of languages.
- **AI-Powered Summarization:** Leverages a Large Language Model (LLM) via Hugging Face to generate concise, abstractive summaries of the video's content.
- **On-Demand Translation:** Translates the generated summary into multiple languages.
- **Interactive UI:** A user-friendly interface built with Streamlit allowing users to select different Whisper model sizes and view results in real-time.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **AI Orchestration:** [LangChain](https://www.langchain.com/)
- **LLM Hosting:** [Hugging Face Endpoints](https://huggingface.co/inference-endpoints)
- **Transcription Model:** [OpenAI Whisper](https://openai.com/research/whisper)
- **Audio Processing:** [yt-dlp](https://github.com/yt-dlp/yt-dlp), [FFmpeg](https://ffmpeg.org/)
- **Language:** Python 3.9+

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.9 or higher
- [FFmpeg](https://ffmpeg.org/download.html) installed and added to your system's PATH. (This is crucial for audio conversion).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    - Create a file named `.env` in the root of the project directory.
    - Add your Hugging Face API token to this file:
      ```
      HUGGINGFACEHUB_API_TOKEN="hf_YourSecretTokenGoesHere"
      ```

### Running the Application

Once the setup is complete, you can run the Streamlit app with the following command:

```bash
streamlit run app.py
