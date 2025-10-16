from pytubefix import YouTube
from pytubefix.cli import on_progress
import sys

def get_streams(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Title: {yt.title}")
        print(f"Thumbnail URL: {yt.thumbnail_url}")

        # Get all available video streams
        video_streams = yt.streams.filter(adaptive=True, mime_type="video/mp4", only_video=True)
        
        # Display available video streams with resolutions and file sizes
        print("\nAvailable Video Streams:")
        for i, stream in enumerate(video_streams):
            print(f"{i + 1}. {stream.resolution} - Size: {stream.filesize / (1024 * 1024):.2f} MB")

        # Prompt user to select a video stream
        video_choice = int(input("\nEnter the number of the video stream you want to download: ")) - 1
        selected_video_stream = video_streams[video_choice]

        # Get all available audio streams
        audio_streams = yt.streams.filter(adaptive=True, mime_type="audio/mp4", only_audio=True)
        
        # Display available audio streams with bitrates and file sizes
        print("\nAvailable Audio Streams:")
        for i, stream in enumerate(audio_streams):
            print(f"{i + 1}. {stream.abr} - Size: {stream.filesize / (1024 * 1024):.2f} MB")

        # Prompt user to select an audio stream
        audio_choice = int(input("\nEnter the number of the audio stream you want to download: ")) - 1
        selected_audio_stream = audio_streams[audio_choice]

        # Print selected streams
        print(f"\nSelected Video Stream: {selected_video_stream.resolution} - Size: {selected_video_stream.filesize / (1024 * 1024):.2f} MB")
        print(f"Selected Audio Stream: {selected_audio_stream.abr} - Size: {selected_audio_stream.filesize / (1024 * 1024):.2f} MB")

        # Download the selected streams
        selected_video_stream.download(filename="video.mp4")
        selected_audio_stream.download(filename="audio.mp4")
        print("\nDownload completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter the YouTube video URL: ")
    get_streams(url)
