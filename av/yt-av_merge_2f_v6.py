from moviepy.editor import *

# Load your video and audio files
video = VideoFileClip("/home/pen/Videos/Arcane: Season 2 | Official Trailer | Netflix.mp4")
audio = AudioFileClip("/home/pen/Videos/Arcane: Season 2 | Official Trailer | Netflix.m4a")

# Set the audio of the video to the loaded audio
final_video = video.set_audio(audio)

# Save the final video
final_video.write_videofile("/home/pen/Videos/Arcane_Season_2_Trailer_with_Audio.mp4")