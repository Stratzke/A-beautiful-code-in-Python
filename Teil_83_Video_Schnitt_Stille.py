import moviepy.editor as mvpe


def lade_datei(datei):
  name, ext = datei.split('.')
  return mvpe.VideoFileClip(datei), name+'_stille.'+ext


ab, stille = 0.05, 0.03
video, ausgabedatei = lade_datei('Teil_83_Beispiel.mp4')
clips = [video.subclip(i*ab, (i+1)*ab) for i in range(int(video.end/ab))
         if video.subclip(i*ab, (i+1)*ab).audio.max_volume() >= stille]
video2 = mvpe.concatenate_videoclips(clips)
video2.write_videofile(ausgabedatei, fps=30, preset='ultrafast', codec='libx264',
                      temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac', threads=4)
print(f'Länge vorher/nachher in Sek.: {video.end:.2f} / {video2.end:.2f}')         