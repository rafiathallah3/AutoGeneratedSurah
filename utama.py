import moviepy.editor as mp
import json, os, random

surah = 1
# for surah in range(1, 115):
surah_json = json.load(open(f'./source/surah/surah_{surah}.json', encoding="utf-8"))
translasi_inggris = json.load(open(f'./source/translation/en/en_translation_{surah}.json'))

total_durasi = 6
semua_audio: list[mp.AudioFileClip] = []

for i in range(0, surah_json['count'] + 1):
    audio_clip = mp.AudioFileClip(f'./source/audio/{surah:03d}/{i:03d}.mp3')
    total_durasi += audio_clip.duration
    semua_audio.append(audio_clip)

total_durasi += 3
print(total_durasi, surah)

semua_background = []
nomor_background = [i for i in range(1, len(os.listdir('./source/background')) + 1)]
durasi_background = 0
random.shuffle(nomor_background)

for i in nomor_background:
    background: mp.VideoFileClip = mp.VideoFileClip(f'./source/background/{i}.mp4').fx(mp.vfx.colorx, .4).fx(mp.vfx.speedx, 0.85)
    semua_background.append(background)

    durasi_background += background.duration
    if(durasi_background > total_durasi):
        break

background = mp.CompositeVideoClip(semua_background)

nomor_belakang = int(str(surah)[-1])
nama_surah = mp.TextClip(f"Surat {surah_json['name']}".upper(), fontsize=70, color='white', font='Arial-Black').set_duration(6).set_start(2).crossfadein(2)
deskrips_surah = mp.TextClip(f"{f'{surah}st' if +nomor_belakang == 1 else f'{surah}nd' if nomor_belakang == 2 else f'{surah}rd' if nomor_belakang == 3 else f'{surah}th'} Chapter Of The Holy Quran", fontsize=60, color='white', font='Arial', stroke_width=.5).set_duration(6).set_start(2).crossfadein(2)
background_Clip = mp.ColorClip(size=background.size, color=[255,255,255]).set_opacity(0)
bgSize = background_Clip.size
tc1Size = nama_surah.size
tc2Size = deskrips_surah.size
awal_surah = mp.CompositeVideoClip([
    background_Clip,
    nama_surah.set_position((bgSize[0]/2-tc1Size[0]/2, bgSize[1]/2 - tc1Size[1]/2 - 50)).set_start(0).crossfadeout(1),
    deskrips_surah.set_position((bgSize[0]/2-tc2Size[0]/2, bgSize[1]/2 - tc2Size[1]/2 + 50)).set_start(0).crossfadeout(1)
]).set_duration(6)

clips = []

clips.append(awal_surah)

def TambahkanSurah(i: int):
    audio_surah = semua_audio[i]
    isi_surah = mp.TextClip(surah_json['verse'][f'verse_{i}'], fontsize=90, color='white', font='Calibri', size=background.size).set_duration(audio_surah.duration)
    translate_surah = mp.TextClip(translasi_inggris['verse'][f'verse_{i}'], fontsize=60, color='white', font='Arial', method='caption', size=(background.size[0] - 100, background.size[1])).set_duration(audio_surah.duration)

    background_surah = mp.ColorClip(size=background.size, color=[255,255,255]).set_opacity(0)
    
    bgSize = background_surah.size
    size_isi_surah = isi_surah.size
    size_translate = translate_surah.size

    hasil_ayat = mp.CompositeVideoClip([
        background_surah,
        isi_surah.set_position((bgSize[0]/2-size_isi_surah[0]/2, bgSize[1]/2 - size_isi_surah[1]/2 - 75)).crossfadein(1).set_start(0).crossfadeout(1),
        translate_surah.set_position((bgSize[0]/2-size_translate[0]/2, bgSize[1]/2 - size_translate[1]/2 + 50)).crossfadein(1).set_start(0).crossfadeout(1)
    ]).set_duration(audio_surah.duration)
    hasil_ayat = hasil_ayat.set_audio(audio_surah)
    
    return hasil_ayat

for i in range(0, surah_json['count'] + 1):
    hasil_ayat = TambahkanSurah(i)

    clips.append(hasil_ayat)
    print(surah_json['verse'][f'verse_{i}'])

hasil_semua_ayat = mp.concatenate_videoclips(clips)

final = mp.CompositeVideoClip([background, hasil_semua_ayat]).set_duration(total_durasi)
# final.save_frame('test.png')
final.write_videofile(f'hasil/{surah}.mp4')