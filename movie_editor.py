#pip install moviepy

import moviepy.editor as mp
clip = mp.VideoFileClip("Housefull4.mp4")
clip_resized = clip.resize(height = 360)
clip_resized.write_videofile("Housefull4_Resized.mp4")