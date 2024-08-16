import streamlit as st
from yt_dlp import YoutubeDL
from moviepy.editor import *
import os

def extract_word_timestamps(video_url):
    # Download the YouTube video as an audio file using yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'videos/audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Since the output is directly a WAV file, we return the path
    return "videos/audio.wav"

def main():
    st.title("YouTube to Audio Converter")

    # Input URL
    youtube_url = st.text_input("Enter YouTube URL:")

    if youtube_url:
        if st.button("Convert to Audio"):
            with st.spinner("Processing..."):
                audio_file_path = extract_word_timestamps(youtube_url)
                st.success("Conversion Successful!")

                # Display the audio player
                st.audio(audio_file_path)

                # Provide a download link for the audio file
                with open(audio_file_path, "rb") as file:
                    btn = st.download_button(
                        label="Download Audio",
                        data=file,
                        file_name="audio.wav",
                        mime="audio/wav"
                    )

if __name__ == "__main__":
    main()
