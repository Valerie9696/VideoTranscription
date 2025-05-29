import moviepy.editor as mp
import whisper
import os
import re


def extract_audio_from_video(video_path, audio_path):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)


def transcribe_audio(audio_path, output_text_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    transcription = result['text']
    processed_text = add_line_breaks(transcription)
    with open(output_text_file, 'w', encoding="utf-8") as f:
        f.write(processed_text)


def add_line_breaks(text):
    processed_text = re.sub(r'(?<=[.!?])\s+', '\n', text)
    return processed_text


def transcribe_video_to_text(video_file, output_text_file):
    temp_audio_file = "temp_audio.wav"
    try:
        extract_audio_from_video(video_file, temp_audio_file)
        transcribe_audio(temp_audio_file, output_text_file)
    finally:
        if os.path.exists(temp_audio_file):
            os.remove(temp_audio_file)


if __name__ == "__main__":
    # set the paths of the video files and the output text file here.
    video_file = ""
    output_text_file = ""
    transcribe_video_to_text(video_file, output_text_file)
    print(f"Transcription saved to {output_text_file}")