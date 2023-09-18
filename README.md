 Nama    : Azka Nydia Estiningtyas <br>
 NPM     : 2206028970 <br>
 Kelas   : PBP E <br>

---
# Genshin Food Inventory

https://gi-foodinventory.adaptable.app/main/

---
# Tugas 2 Checklist
Checklist untuk tugas ini adalah sebagai berikut.<br>
 - [x] Membuat sebuah proyek Django baru.<br>
 - [x] Membuat aplikasi dengan nama main pada proyek tersebut.<br>
 - [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.<br>
 - [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.<br>
        - name sebagai nama item dengan tipe CharField.<br>
        - amount sebagai jumlah item dengan tipe IntegerField.<br>
        - description sebagai deskripsi item dengan tipe TextField.<br>
 - [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.<br>
 - [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.<br>
 - [x] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.<br>
 - [x] Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.<br>

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
 - [x] Membuat sebuah proyek Django baru.<br>
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

    saya menggunakan perintah ```django-admin startproject food_inventory``` untuk mulai membuat proyek Django baru dan menambahkan ```*``` pada ```ALLOWED_HOSTS``` di ```settings.py``` supaya semua host mendapatkan akses. Lalu, saya juga membuat ```.gitignore```.

 - [x] Membuat aplikasi dengan nama ```main``` pada proyek tersebut.<br>
    Seperti langkah sebelumnya, saya menggunakan perintah ```python manage.py startapp main``` untuk membuat aplikasi ```main``` dan mendaftarkan aplikasi tersebut dengan menambahkan ```"main",``` pada list  ```INSTALLED_APPS``` yang terdapat dalam ```settings.py```.

    Setelah itu, saya membuat direktori ```template``` dalam direktori ```main``` dan membuat file baru yang diberi nama ```main.htlm```. Pada file tersebut, saya membuat header, nama, tabel, dan elemen lainnya menggunakan referensi koding yang didapatkan dari laman "https://www.w3schools.com/html/". 

 - [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.<br>
    Dalam ```urls.py``` yang terletak didalam direktori main, Saya impor fungsi ```include``` dan menambah rute url menggunakan perintah ```path('main/', include('main.urls')),``` pada variabel ```urlpatterns```.

 - [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.<br>
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

 - [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.<br>
    Pada file ```views.py```, saya menambahkan kode berikut:
    ```
    from django.shortcuts import render

    # Create your views here.
    def show_main(request):
        context = {
            'name': 'Azka Nydia Estiningtyas',
            'npm': '2206028970',
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

 - [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py. <br>
    Saya akan membuat file ```urls.py``` didalam direktori ```main``` dan menambahkan kode berikut:
    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

 - [x] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.<br>
    Setelah semua isi direktori dan proyek sudah lengkap, saya akan menggunakan git add, commit, dan push untuk memperbarui isi repositori pada github. Lalu, saya menggunakan adaptable untuk membuat app baru dengan memilih ```create new app```,  klik ```Connect an Existing Repository```, dan memilih repositori proyek ```food_inventory```. Setelah itu, saya memilih ```Python App Template``` sebagai template dan ```PostgreSQL``` sebagai tipe basis data. Spesifikasi dari aplikasi akan saya sesuaikan dengan versi python yang dipakai dan memasukkan ```ython manage.py migrate && gunicorn food_inventory.wsgi``` pada ```Start Command```. Aplikasi yang dibuat saya namai ```gi-foodinventory```, lalu saya deploy app.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.<br>

    ![Bagan Django Azka](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/790b53a8-5659-4eeb-96e4-d917e755991a)

    Client akan mengeluarkan permintaan HTTP menggunakan browser. Lalu, ```Web Server``` akan melayani permintaan tersebut dan meneruskan permintaan ke ```WSGI```. ```Request``` yang masuk akan dikirimkan ke server Django melalui URL. Django akan menyocokan URL yang diterima dengan daftar URL pada ```urls.py``` dan meneruskan permintaan ke ```views.py``` sesuai permintaan Client. Views akan berinteraksi dengan model melalui ```models.py``` dan model akan mengambil atau menyimpan data dari atau ke ```Database```. Data akan ditampilkan dengan ```template``` yang sesuai dan akan diubah kedalam bentuk ```html``` yang berfungsi menampilkan data-data sesuai permintaan. Setelah itu, view mengembalikan ```respons``` dalam bentuk yang sesuai ke ```WSGI``` yang akan meneruskan ke ```server web``` dan mengirimkannya kembali ke client. 


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>
    Kita menggunakan virtual environment karena virtual environment dipakai untuk mengisolasi dan mengelola suatu proyek django sehingga satu proyek tidak akan berada di tempat yang sama dengan proyek lain dan masing-masing memiliki dependensi sendiri. Penggunaannya memungkinkan virtual environment menyesuaikan dengan ketergantungan dan spesifikasi dari masing-masing proyek. Kita juga masih bisa membuat aplikasi web berbasis Django tanpa virtual environment, tetapi tidak disarankan karena akan ada kemungkinan terjadi konflik dependensi antar proyek jika terdapat banyak proyek.


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    MVC, MVT, dan MVVM merupakan tiga pola arsitektur perangkat lunak yang dikebangkan untuk membuat web atau perangkat lunak lainnya. Berikut penjelasannya dan perbedaannya: <br>
    a. MVC (Model-View-Controller) merupakan pola arsitektur yang memisahkan kode menjadi 3 bagian utama, diantaranya:<br>
        - Model: Berperan mengatur, memanipulasi, dan mengorganisasi data pada database.<br>
        - View: Bertugas menampilkan visualisasi dari data dan melakukan interaksi dengan User.<br>
        - Controller: Bertugas menjadi perantara antara model dan view. Controller mengatur alur aplikasi dan memberi respons sesuai perintah User.<br>
        ->> Perbedaan utama dari MVC adalah MVC merupakan pola yang lebih sederhana/umum dan menjadi pola yang umum dalam pengembangan perangkat lunak tradisional. Uniknya, walau controller menjadi jembatan antara model dan view, view tidak menyimpan informasi mengenai controller. MVC umumnya dipakai pada Ruby on Rails, Laravel (PHP).<br>
        <br>
    b. MVT (Model-View-Template) terdiri dari 3 bagian utama:<br>
        - Model: Berperan mengatur, memanipulasi, dan mengorganisasi data pada database.<br>
        - View: Bertugas menampilkan visualisasi dari data dan melakukan interaksi dengan User.<br>
        - Template: Menggantikan peran controller dan berperan dalam mengatur bagaimana data akan tampil dari model ke dalam view menggunakan 
        elemen-elemen HTML. Pada dasarnya, Template adalah kode HTML yang merender data.<br>
        ->> >Perbedaan utama dari MVT adalah Template menggantikan controller dan digunakan dalam kerangka kerja Django untuk pengembangan aplikasi web berbasis Python. Template memungkinkan untuk memisahkan tampilan sehingga tampilan dapat dikembangkan menjadi lebih kompleks. Pola ini dapat dipakai untuk aplikasi kecil atau besar dan contohnya adalah Django.<br>
        <br>
    c. MVVM (Model-View-ViewModel)<br>
        - Model: Berperan mengatur, memanipulasi, dan mengorganisasi data pada database.<br>
        - View: Bertugas menampilkan visualisasi dari data dan melakukan interaksi dengan User.<br>
        - ViewModel: Bertugas menjadi perantara antara model dan view, serta mengelola data yang ada dimodel dengan bentuk yang sesuai sebelum ditampilkan di View.<br>
        ->> Perbedaan utama dari MVVM adalah ViewModel berperan dalam mengelola logika antara model dan view dan umumnya digunakan dalam pengembangan aplikasi berbasis web dengan framework JavaScript. Pola arsitektur MVVM bersifat event-driven dan kurang idea untuk proyek kecil.<br>
<br>
<br>
Referensi:<br>
- https://www.w3schools.com/html/ <br>
- https://www.geeksforgeeks.org/difference-between-mvc-and-mvt-design-patterns/ <br> 
- https://www.geeksforgeeks.org/difference-between-mvc-mvp-and-mvvm-architecture-pattern-in-android/ <br>
- https://nitinnain.com/djangos-request-response-cycle/ <br>



# Tugas 3 Checklist

 - [x] Membuat input form untuk menambahkan objek model pada app sebelumnya. <br> 
 - [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID. <br> 
 - [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.<br> 
 - [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder.<br> 
    - Apa perbedaan antara form POST dan form GET dalam Django?<br> 
    - Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?<br> 
    - Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?<br> 
    - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).<br> 
 - [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.<br> 
 - [x] Melakukan add-commit-push ke GitHub.<br> 