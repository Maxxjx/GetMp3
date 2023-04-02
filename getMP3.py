import os
import moviepy
import moviepy.editor
#---------/////input///////-------------------
#file location
FileAdderess=   "C:/Users/Maxx/Pictures/AnyDesk/"
#File Name
FileName=     "video_2022-02-16_19-02-47.mp4"

#------------output(do not change)---------------

video=moviepy.editor.VideoFileClip(FileAdderess+FileName)
audio=video.audio
#savefile path
savepath = "./audio"
FileName=os.path.splitext(FileName)[0]
audio.write_audiofile(savepath+"/"+FileName+".mp3")