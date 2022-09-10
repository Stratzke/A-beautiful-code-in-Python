import moviepy.editor as mvpe
import itertools as it


def lade_datei(datei):
  name, ext = datei.split('.')
  return mvpe.VideoFileClip(datei), name+'_stille.'+ext


def finde_sprache(audio, ab, stille):
  a = [audio.subclip(i*ab, (i+1)*ab).max_volume() >= stille for i in range(int(audio.end/ab))]
  b = [(k,len(list(g))*ab) for k,g in it.groupby(a)]
  schnittliste, start = [], 0
  for sprache, länge in b:
    if sprache: 
      schnittliste.append((start,start+länge))
    start += länge   
  return schnittliste        


video, ausgabedatei = lade_datei('Teil_83_Beispiel.mp4')
schnittliste = finde_sprache(video.audio, 0.05, 0.03)
clips = [video.subclip(s,e) for s,e in schnittliste]
video = mvpe.concatenate_videoclips(clips)
video.write_videofile(ausgabedatei, fps=30, preset='ultrafast', codec='libx264',
                      temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac', threads=4)
video.close()                      