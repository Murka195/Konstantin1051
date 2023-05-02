
import os 

from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, AudioClip, CompositeVideoClip

clip1 =  VideoFileClip("Weather Report Project/videos/1test/IMG_6832.MOV")#,audio=True)#.fx(v)


#clip1 = clip1.fx(vfx.resize,width=1080, height=1920)
#clip1.set_position((1080,1920))

clip2 =  VideoFileClip("Weather Report Project/videos/1test/IMG_6833.MOV")#, audio=True)



combined = concatenate_videoclips([clip1, clip2]) #, audio=True)

#combined.resize( (1080 ,1920) )

#combined.video.fx.all.resize(clip1, newsize=None, height=None, width=None, apply_to_mask=True)
combined.write_videofile("Weather Report Project/output/combined1.mp4")#.fx(vfx.resize, width=1080, height=1920)


