# Otomatis Membuat Video Surah Al Quran
Project ini bertujuan untuk mengetahui isi semua surah di dalam Al-Quran beserta suara tanpa mengedit video, ini menggunakan MoviePy dan ImageMagick

# Contoh Video:
<video autosize="true" controls>
    <source src="./hasil/1.mp4" type="video/mp4">
</video>

# Installation
1. Clone projectnya
`
git clone https://github.com/rafiathallah/AutoGeneratedSurah
`
2. install requirement package di console `pip install -r requirements.txt` dan install ImageMagick di [sini](https://imagemagick.org/script/download.php)
3. yang terakhir, jalankan programnya dengan menulis ini di console `python utama.py`

# Note
Kalau ingin mengganti surah, ganti `surah` variable di `utama.py` berdasarkan urutan surah di `source/surah`

Isi semua data surah, audio dan translasi ada di sini https://github.com/semarketir/quranjson