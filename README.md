 Nama    : Azka Nydia Estiningtyas <br>
 NPM     : 2206028970 <br>
 Kelas   : PBP E <br>

tautan repositori: https://gi-foodinventory.adaptable.app/main/

---

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 - [x] Membuat sebuah proyek Django baru.
    Pertama, saya membuat direktori lokal dan diberi nama ```food_inventory``` dan membuat virtual environment dengan menjalankan perintah ```python -m venv env```. Lalu, saya mengaktifkan virtual environment dengan ```source env/bin/activate```.

    Setelah itu, saya membuat ```requirements.txt``` untuk menambahkan dependencies dengan isi berikut:
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
    dan menginstall semuanya dengan perintah ```python -m pip install -r requirements.txt```.

    saya menggunakan perintah ```django-admin startproject food_inventory``` untuk mulai membuat proyek Django baru dan menambahkan ```*``` pada ```ALLOWED_HOSTS``` di ```settings.py``` supaya semua host mendapatkan akses.

 - [x] Membuat aplikasi dengan nama main pada proyek tersebut.
    Seperti langkah sebelumnya, saya menggunakan perintah ```python manage.py startapp main``` untuk membuat aplikasi ```main``` dan mendaftarkan aplikasi tersebut dengan menambahkan ```"main",``` pada list  ```INSTALLED_APPS``` yang terdapat dalam ```settings.py```.

    Setelah itu, saya membuat direktori ```template``` dalam direktori ```main``` dan membuat file baru yang diberi nama ```main.htlm```. Pada file tersebut, saya membuat header, nama, tabel, dan elemen lainnya menggunakan referensi koding yang didapatkan dari laman "https://www.w3schools.com/html/". 

 - [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    Dalam ```urls.py``` yang terletak didalam direktori main, Saya impor fungsi ```include``` dan menambah rute url menggunakan perintah ```path('main/', include('main.urls')),``` pada variabel ```urlpatterns```.

 - [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    - name sebagai nama item dengan tipe CharField.
    - amount sebagai jumlah item dengan tipe IntegerField.
    - description sebagai deskripsi item dengan tipe TextField.
    Saya menambahkan beberapa atribut pada ```models.py``` menggunakan kode berikut:
    ```
    from django.db import models

    class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    quality = models.TextField()
    type = models.CharField(max_length=255)
    ```
    Lalu, melakukan migrasi model menggunakan ```python manage.py makemigrations``` dan ```python manage.py migrate```.

 - [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    Pada file ```views.py```, saya menambahkan kode berikut:
    ```
    from django.shortcuts import render

    # Create your views here.
    def show_main(request):
        context = {
            'name': 'Azka Nydia Estiningtyas',
            'class': 'PBP E',
            'item_name1': 'Adeptus Temptation',
            'quality1': '5-Star',
            'type1': 'ATK-Boosting Dishes',
            'description1': 'Increases all party members ATK by 260~372 and CRIT Rate by 8~12 for 300s.',
            'amount1': '2',
            'item_name2': 'Cream of Mushroom Soup',
            'quality2': '2-Star',
            'type2': 'Recovery Dishes',
            'description2': 'Revives a character and restores 250~550 HP.',
            'amount2': '1'
        }
    return render(request, "main.html", context)
    ```

 - [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    Saya akan membuat file ```urls.py``` didalam direktori ```main``` dan menambahkan kode berikut:
    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

 - [x] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    Setelah semua isi direktorat dan proyek sudah lengkap, saya akan menggunakan git add, commit, dan push untuk memperbarui isi repositori pada github. Lalu, saya menggunakan adaptable untuk membuat app baru dengan memilih ```create new app```,  klik ```Connect an Existing Repository```, dan memilih repositori proyek ```food_inventory```. Setelah itu, saya memilih ```Python App Template``` sebagai template dan ```PostgreSQL``` sebagai tipe basis data. Spesifikasi dari aplikasi akan saya sesuaikan dengan versi python yang dipakai dan memasukkan ```ython manage.py migrate && gunicorn food_inventory.wsgi``` pada ```Start Command```. Aplikasi yang dibuat saya namai ```gi-foodinventory```, lalu saya deploy app.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    ![Bagan Django Azka](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/790b53a8-5659-4eeb-96e4-d917e755991a)

    Client akan mengeluarkan permintaan menggunakan browser. Lalu, ```Web Server``` akan melayani permintaan tersebut dan meneruskan permintaan ke ```WSGI```. ```Request``` yang masuk akan dikirimkan ke server Django melalui URL. Django akan menyocokan URL yang diterima dengan daftar URL pada ```urls.py``` dan meneruskan permintaan ke ```views.py```. Views akan berinteraksi dengan model melalui ```models.py``` dan mengambil atau menyimpan data dari atau ke ```Database```. Data akan ditampilkan dengan ```template``` yang sesuai dan akan dubah kedalam bentuk ```html```. Setelah itu, view mengembalikan ```respons``` dalam bentuk yang sesuai ke ```WSGI``` yang akan meneruskan ke ```server web``` dan mengirimkannya kembali ke client. 


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Kita menggunakan virtual environment karena virtual environment merupakan tempat virtual terisolasi yang dapat dipakai untuk mengelola proyek django sehingga satu proyek tidak akan berada di tempat yang sama dengan proyek lain dan masing-masing memiliki dependensi sendiri. Penggunaannya memungkinkan virtual environment menyesuaikan dengan ketergantungan dan spesifikasi dari masing-masing proyek. Membuat aplikasi web berbasis Django juga masih bisa dilakukan tanpa virtual environment, tetapi tidak disarankan karena akan ada kemungkinan terjadi konflik dependensi antar proyek jika memiliki banyak proyek.


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    MVC, MVT, dan MVVM merupakan tiga pola arsitektur perangkat lunak yang dikebangkan untuk membuat web atau perangkat lunak lainnya. Berikut penjelasannya dan perbedaannya: <br>
    a. MVC (Model-View-Controller) merupakan pola arsitektur yang memisahkan kode menjadi 3 bagian utama, diantaranya:<br>
        - Model: Berperan mengatur, memanipulasi, dan mengorganisasi data pada database.<br>
        - View: Bertugas menampilkan data dan melakukan interaksi dengan User.<br>
        - Controller: Bertugas menjadi perantara antara model dan view. Controller mengatur alur aplikasi dan memberi respons sesuai perintah User.<br>
        Perbedaan utama dari MVC adalah MVC merupakan pola yang lebih sederhana/umum dan menjadi pendekatan umum dalam pengembangan perangkat lunak tradisional. Umumnya dipakai pada Ruby on Rails, Laravel (PHP).<br>
    b. MVT (Model-View-Template) terdiri dari 3 bagian utama:<br>
        - Model: Berperan mengatur, memanipulasi, dan mengorganisasi data pada database.<br>
        - View: Bertugas menampilkan data dan melakukan interaksi dengan User.<br>
        - Template: Menggantikan peran controller dan berperan dalam mengatur bagaimana data akan tampil dari model ke dalam view menggunakan elemen-elemen HTML.<br>
        Perbedaan utama dari MVT adalah Template menggantikan controller dan digunakan dalam kerangka kerja Django untuk pengembangan aplikasi web berbasis Python. Template memungkinkan untuk memisahkan tampilan sehingga tampilan dalam dikembangkan menjadi lebih kompleks.<br>
    c. MVVM (Model-View-ViewModel)<br>
        - Model: Berperan mengatur, memanipulasi, dan mengorganisasi data pada database.<br>
        - View: Bertugas menampilkan data dan melakukan interaksi dengan User.<br>
        - ViewModel: Bertugas menjadi perantara antara model dan view, serta mengelola data yang ada dimodel dengan bentuk yang sesuai sebelum ditampilkan di View.<br>
        Perbedaan utama dari MVVM adalah ViewModel berperan dalam mengelola logika antara model dan view dan umumnya digunakan dalam pengembangan aplikasi berbasis web dengan framework JavaScript.<br>

