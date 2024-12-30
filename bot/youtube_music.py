import vlc
import pafy

def play_music_from_youtube(video_url):
    try:
        # Get YouTube video details
        video = pafy.new(video_url)
        best_audio = video.getbestaudio()

        # Print song details
        print(f"Playing: {video.title}")
        print(f"Duration: {video.duration}")
        print(f"Author: {video.author}")

        # Play the audio stream
        player = vlc.MediaPlayer(best_audio.url)
        player.play()

        # Keep the script running while the audio plays
        while True:
            state = player.get_state()
            if state in (vlc.State.Ended, vlc.State.Error):
                break

    except Exception as e:
        print(f"An error occurred: {e}")
