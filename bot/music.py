import yt-dlp # type: ignore
import os

def play_music_from_youtube(video_url):
    try:
        # Create a 'downloads' folder if it doesn't exist
        if not os.path.exists('Downloads'):
            os.makedirs('Downloads')

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'Downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            audio_file = ydl.prepare_filename(info_dict).replace('.webm', '.mp3')

        # Play the audio file
        print(f"Playing: {info_dict['title']}")
        os.system(f"start {audio_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
