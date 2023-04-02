import os
import moviepy.editor

# get the directory and file name from user input
directory = input("Enter the directory where the video file is located: ")
filename = input("Enter the name of the video file (including extension): ")

# create the full file path
file_path = os.path.join(directory, filename)

# remove the extension from the file name
file_name_without_extension = os.path.splitext(filename)[0]

# create a folder to save the audio file
save_folder = "./audio"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# create the path for the output audio file
output_path = os.path.join(save_folder, file_name_without_extension + ".mp3")

# extract the audio from the video file
video = moviepy.editor.VideoFileClip(file_path)
audio = video.audio

# write the audio to a file
audio.write_audiofile(output_path)
