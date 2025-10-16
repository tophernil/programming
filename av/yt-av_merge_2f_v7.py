from moviepy.editor import *

# Load your video and audio files
video = VideoFileClip("/home/pen/projects/python/av/video.mp4")
audio = AudioFileClip("/home/pen/projects/python/av/audio.mp4")

# Set the audio of the video to the loaded audio
final_video = video.set_audio(audio)

# Save the final video
final_video.write_videofile("/home/pen/projects/python/av/Beginner Classical Guitar Song - Calatayud Vals.mp4")