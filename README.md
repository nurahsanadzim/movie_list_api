# movie_list_api
My college assignment, API for list of movie, created with [django-rest-framework](https://www.django-rest-framework.org), with token-based authentication and [TMDB](https://www.kaggle.com/tmdb/tmdb-movie-metadata) edited dataset.

### Requirements
* Python 3
* Django 3.0.7
* django-rest-framework 3.11.0

### Instalasi
* **(Opsional)** Jalankan instalasi di [virtual environment](https://docs.python.org/3/tutorial/venv.html) terlebih dahulu jika tidak ingin mencampuradukkan library Python base di desktop anda dengan library aplikasi ini, dengan memindahkan folder project ke dalam folder virtual environment.
1. Pastikan Python 3 sudah terinstall di desktop anda. 
2. Install Package yang diperlukan dengan command: `pip install Django==3.0.7 djangorestframework==3.11.0`.
3. Pindah pada posisi folder `movie_list_api`, yang terdapat file `manage.py`.
4. Jalankan server dengan command: `python manage.py runserver`.
5. Buka browser dengan membuka alamat: http://127.0.0.1:8000/ untuk menuju ke halaman dokumentasi API.
6. Untuk menggunakan API, daftarkan akun anda di http://127.0.0.1:8000/daftar/, otomatis anda akan mendapatkan token API.

### Demo Youtube
https://youtu.be/XDIuXBrM5CE

---

### Project UAS Mata Kuliah Rekayasa Web
Nama: Nur Ahsan Adzim<br>
NIM: 42517013<br>
Kelas: 3A TKJ

**Kelompok 7, anggota kelompok:**
1. Nur Ahsan Adzim (42517013)
2. Andi Fachrul Reza (42517005)
