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
        
        # Display available resolutions
        print("\nAvailable Resolutions:")
        resolutions = []
        for stream in video_streams:
            res = stream.resolution
            if res not in resolutions:
                resolutions.append(res)
                print(res)
        
        # Prompt user to select a resolution
        selected_res = input("\nEnter the desired resolution (e.g., 1080p): ")
        
        # Filter video streams based on the selected resolution
        selected_video_streams = yt.streams.filter(adaptive=True, mime_type="video/mp4", only_video=True, res=selected_res)
        
        # Filter audio streams
        audio_streams = yt.streams.filter(adaptive=True, mime_type="audio/mp4", only_audio=True)

        # Print selected video streams with their file sizes
        print("\nSelected Video Streams:")
        for stream in selected_video_streams:
            print(f"{stream} - Size: {stream.filesize / (1024 * 1024):.2f} MB")

        # Print audio streams with their file sizes
        print("\nAudio Streams:")
        for stream in audio_streams:
            print(f"{stream} - Size: {stream.filesize / (1024 * 1024):.2f} MB")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter the YouTube video URL: ")
    get_streams(url)
