**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    **Membuat Proyek Django baru**

    Membuat folder/ direktori baru dengan nama kedaii-ledy. Setelah itu saya membuka command prompt melalui W+R dan masuk ke direktori tersebut. Setelah itu saya membuat *virtual environtment* dengan menjalankan perintah *python -m venv env*. Setelah berhasil membuat *virtual environtment*, saya mengaktifkannya dengan perintah *env\Scripts\activate*. *Virtual environtment* saya pun aktif ditandai dengan (env) yang muncul.

    Setelah itu saya membuat berkas text (requirements.txt) yang berisikan *depedencies* yang akan digunakan untuk memaksimalkan pengembangan  dan menginstall *depedencies*  tersebut dengan perintah *pip install -r requirements.txt.* Kemudian saya membuat proyek Django bernama kedaii-ledy dengan perintah *django-admin startproject kedaii_ledy .* 

    Setelah berhasil membuat proyek kedaii_ledy, saya menambahkan [localhost](http://localhost) dan 127.0.0.1 pada ALLOWED_HOST di dalam [settings.py](http://settings.py) untuk mendaftarkan host yang diizinkan untuk mengakses web. Kemudian saya menjalankan server Django dengan perintah runserver. Setelah itu saya mengecek terlebih dahulu dengan membuka  [http://localhost:8000](http://localhost:8000/) untuk memastikan Django saya sudah berhasil dibuat. Setelah berhasil membuat Django, saya menggunggah proyek ke repositori github.

    Setelah berhasil mengunggah proyek ke github, saya membuat akun Pacil Web Service untuk melakukan deployment. Setelah berhasil login ke PWS, saya membuat project baru di PWS bernama kedaiiledy. Setelah mendapatkan URL deployment, saya menambahkan URL tersebut ke dalam list ALLOWED_HOST pada [settings.py](http://settings.py). Setelah itu saya melakukan git add, commit dan push untuk menyimpan perubahan ke repository Github. Tidak lupa juga saya melakukan push ke PWS. 

    **main**

    Setelah status di PWS berubah menjadi Running, langkah selanjutnya adalah membuat aplikasi ‘main’ di dalam proyek kedaii-ledy, lalu jalankan dengan perintah *python [manage.py](http://manage.py/) startapp main*. Setelah muncul direktori baru dengan nama kedaii-ledy, saya menambahkan ‘main’ kedalam variabel INSTALLED_APPS pada settings.py yang ada di direktori proyek untuk mendaftarkan aplikasi ‘main’ tersebut.

    **routing**

    Di dalam urls.py pada direktori proyek, saya menambahkan path baru agar halaman aplikasi main bisa diakses secara langsung. Setelah itu saya melakukan runserver.

    **membuat model** 

    pertama-tama saya membuat folder/ direktori baru bernama ‘templates’ di dalam direktori ‘main’. Setelah itu membuat berkas main.html yang kemudian di dalamnya saya masukkan kode yang saya salin dari tutorial yang detailnnya saya ganti sesuai dengan contoh. setelah itu saya melakukan pengecekan dengan membuka html tersebut di web, dan berhasil.

    saya membuka file [models.py](http://models.py) yang ada dalam direktori main. Didalamnya saya menambahkan class ProductEntry(models.Model) yang didalamnya saya masukkan detail-detailseperti name, price, dan description dengan tipe sesuai dengan yang ada di soal. Setelah mengubah models.py, saya membuat dan menerapkan migrasi model ke dalam data lokal.

    **membuat view yg berisi nama dan npm**

    saya membuka file [views.py](http://views.py) yang ada dalam direktori main, di dalam file tersebut, saya mengimpor fungsi render. Lalu saya menambahkan fungsi show_main dibawahnya yang berisi npm, nama, dan kelas saya. Lalu pada main.html, saya mengubah yang awalnya langsung berubah nama, npm, dan kelas, menjadi variabel name, npm, dan class yang ada pada views.py.

    **routing [urls.py](http://urls.py) pada main**

    saya membuat berkas [urls.py](http://urls.py) di direktori main, berkas tersebut saya isi dengan kode yang sama yang ada pada tutorial 1. Setelah itu saya mengkonfigurasinya dengan urls.py yang ada dalam direktori proyek. 

    **deploy ke pws**

    Setelah selesai melakukan routing dan berhasil membuka url web, saya melakukan push ke PWS dengan perintah git push pws main:master. Namun, karena terjadi error pada PWS, sehingga deploy saya ke PWS pada langkah terakhir ini failed.

    **Membuat README**

    Saya membuat [README.md](http://README.md) melalui visual studio.

**BAGAN REQUEST CLIENT KE WEB APLIKASI BERBASIS DJANGO**
    ![alt text](WebDjangoRute.png)

**FUNGSI GIT**
    Git digunakan untuk melacak dan mengontrol versi kode proyek yang dikerjakan. Git memudahkan progammer untuk memantau semua revisi yang telah dilakukan dengan proyek seiring waktu.

**Mengapa Menggunakan Framework Django**
    Karena framework Django mampu untuk membuat situs web dengan cepat dan mudah untuk mengembangkannya. Selain itu, Django menyediakan banyak fitur bawaan dan sangat aman dari berbagai ancaman.

**Mengapa model pada Django disebut sebagai ORM**
    ORM (Object Relation Mapping) adalah teknik pemograman yang memudahkan data dipetakan secara mulus antara aplikasi dengan basis data. Django menggunakan ORM untuk memetakan objek Python ke struktur basis data relasional, sehingga memudahkan pengembang untuk berinteraksi dengan basis data hanya menggunakan Python