 Nama    : Azka Nydia Estiningtyas <br>
 NPM     : 2206028970 <br>
 Kelas   : PBP E <br>

---
# Genshin Food Inventory

https://gi-foodinventory.adaptable.app/main/

---

# Direktori

- [Tugas 2](#tugas-2-checklist)
- [Tugas 3](#tugas-3-checklist)
- [Tugas 4](#tugas-4-checklist)

---

# Tugas 2 Checklist

--- 
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

---

# Tugas 3 Checklist

--- 

Checklist untuk tugas ini adalah sebagai berikut.<br>

 - [x] Membuat input form untuk menambahkan objek model pada app sebelumnya. <br> 
    Pertama, saya melakukan routing dari ```main/``` menjadi ```/``` sehingga saya tidak perlu menggunakan ```main/``` untuk membuka laman pada local host. Setelah itu, saya membuat file ```forms.py``` pada direktori main untuk membuat struktur form yang nantinya akan dipakai untuk menambah data baru saat input form. Berikut kodenya:
    ```
    from django.forms import ModelForm
    from main.models import Barang
    
    class ItemForm(ModelForm):
        class Meta:
            model = Barang
            fields = ["name", "quality", "type", "description", "amount"]
    ```

    Lalu, saya melakukan menambahkan import baru ke ```views.py``` supaya fungsi pada file tersebut dapat berjalan.
    ```
    from django.http import HttpResponseRedirect
    from main.forms import ItemForm
    from django.urls import reverse
    from main.models import Barang
    ```

    Setelah itu, saya menambahkan fungsi baru dengan nama ```create_product``` pada file yang sama yang akan menerima parameter ```request```. fungsi ini yang akan membuat supaya data yang saya masukkan pada input form akan tersimpan dan menambahkan data produk baru saat klik button submit.
    ```
    def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
    ```

    saya juga menambahkan ```products = Barang.objects.all()``` pada fungsi ```show_main``` dan menambahkan ```'products' : products,``` pada context supaya input data baru yang tersimpan muncul di ```main.html```.

    Karena saya menambah fungsi baru, maka pada saya melakukan routing URL didalam ```urls.py``` dengan menambah import dan path url fungsi 
    ```create_product``` pada ```urlpatterns```.

    ```from main.views import show_main, create_product```

    ```
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product', create_product, name='create_product'),
    ]
    ```

    Setelah itu, saya membuat file HTML baru dengan nama ```create_product.html``` pada satu direktori dengan ```main.html``` supaya dapat menginput form baru.

    ```
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```

    Lalu pada ```main.html```, saya menambahkan modifikasi supaya input yang dibuat sebelumnya dan button untuk menambah input dapat muncul. 
    
    ```
    <table 
    class="center" 
    style=
    "margin-top: 30px;
    width: 100%;
    margin-left:auto;
    margin-right:auto;
    border-spacing: 5px;
    text-align: center;"
    border: 3px solid cadetblue;">
    <tr 
    style="background-color: #455359;
    color: antiquewhite;">
        <th style="border: 1px solid black;">Name</th>
        <th style="border: 1px solid black;">Quality</th>
        <th style="border: 1px solid black;">Type</th>
        <th style="border: 1px solid black;">Description</th>
        <th style="border: 1px solid black;">Amount</th>
    </tr>
    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td style="border: 1px solid black;">{{product.name}}</td>
            <td style="border: 1px solid black;">{{product.quality}}</td>
            <td style="border: 1px solid black;">{{product.type}}</td>
            <td style="border: 1px solid black;">{{product.description}}</td>
            <td style="border: 1px solid black;">{{product.amount}}</td>
        </tr>
    {% endfor %}
    </table>

    <br />

    <a style=" display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;"
    href="{% url 'main:create_product' %}">
        <button>
            Add New Item
        </button>
    </a>
    ```
    

 - [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID. <br> 
    Pada ```views.py```, saya menampilan HTML (```main.html```) menggunakan fungsi ```show_main``` dan membuat fungsi-fungsi lain untuk menampilkan atau mengembalikan data dalam bentuk XML, JSON, XML by ID, dan JSON by ID dengan masing-masing fungsi bernama ```show_[format file]```. Semua fungsi hanya menerima parameter ```request``` kecuali  XML by ID dan JSON by ID yang juga menerima parameter ```id```.
    ```
    def show_main(request):
        products = Barang.objects.all()
        context = {
            'name': 'Azka Nydia Estiningtyas',
            'npm': '2206028970',
            'class': 'PBP E',
            'products' : products,
        }

        return render(request, "main.html", context)

    def show_xml(request):
        data = Barang.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Barang.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Barang.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Barang.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    <br> 

 - [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.<br> 
    Pada ```views.py```, sayang mengimport masing-masing fungsi yang telah dibuat dan menambahkan path URL ke ```urlpatterns```.
    ```
    from django.urls import path
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product', create_product, name='create_product'),
        path('xml/', show_xml, name='show_xml'), 
        path('json/', show_json, name='show_json'),
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ]
    ```
    <br> 

 - [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder.<br> 
    - Apa perbedaan antara form POST dan form GET dalam Django?<br> 
        POST dan GET merupakan metode request HTTP yang dipakai untuk menangani form. Terdapat beberapa perbedaan yang dimiliki POST dan GET. Pertama, perbedaan pada tujuan penggunaannya. POST umumnya digunakan saat sebuah permintaan akan melakukan perubahan pada database, sedangkan GET dipakai saat tidak ingin melakukan perubahan pada database, melainkan untuk permintaan yang hanya membaca data seperti browser request. Kedua, terdapat juga perbedaan pada aspek keamanan dimana POST lebih aman dibanding GET. Hal ini membuat GET tidak cocok digunakan untuk data sensitif seperti password form dan admin form karena informasi tersebut dapat terlihat di URL, tetapi pengiriman data sensitif akan lebih aman dengan POST karena data tersebut tidak terekspose secara terbuka. Terakhir, Kapasitas data dari POST dan GET juga berbeda. POST tidak memiliki batasan panjang URL dan dapat mengirim jumlah data dalam kuantitas yang banyak, tetapi terdapat batasan jumlah data yang dapat dikirim dengan GET.<br> 
    <br> 
    - Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?<br> 
        1. XML (eXtensible Markup Language) merupakan bahasa markup yang dipakai untuk menyimpan atau mengirim data antar aplikasi. XML memiliki fleksibilitas yang tinggi dalam mendefinisikan format data, tetapi memiliki peraturan yang ketat perihal sintaksis.<br> 
        2. JSON (JavaScript Object Notation) merupakan bahasa yang berfungsi mengirim data melalui internet antar server dan aplikasi, tetapi dengan format data yang lebih sederhana dan ringan. Bahasa ini mudah untuk di pahami dan lakukan sehingga populer digunakan sebagai format data dalam API.  <br> 
        3. HTML (HyperText Markup Language) merupakan bahasa markup yang berfungsi untuk menampilkan konten web atau visual yang akan muncul di browser. HTML menyusun tampilannya menggunakan elemen seperti tag dan atribut. HTML memiliki aturan sintaksis yang ketat, tetapi terdapat banyak elemen bawaan sehingga tampilan dari laman web fleksible untuk diubah sesuai keinginan.<br> 
        <br> 
    - Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?<br> 
        Karena terdapat beberapa keunggulan dari JSON ketimbang bahasa lain. Pertama, JSON lebih mudah untuk dibaca dan ditulis sehingga akan lebih mudah bagi manusia untuk membaca dan melakukan perubahan. Kedua, JSON juga lebih ringkas dan padat isinya sehingga pengiriman data menjadi lebih efisien dan ukuran data yang dipindahkan berkurang. Terakhir, JSON juga kompatibel dengan JavaScript sehingga mudah untuk dikembangkan dan diintegrasi dengan aplikasi lain.<br>
        <br> 
    - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).<br> 
        Telah dijelaskan pada checklist diatas<br> 

 - [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.<br>
    - HTML<br>
    ![HTML #1](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/81f76fac-f710-4d6e-ad5a-9bbb29ad4add)<br>
    ![HTML #2](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/69b3a57b-3c58-4771-a89f-8eac1675d69f)<br>
    - XML <br>
    ![XML](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/b8b56b5a-768a-43cf-acb4-fd18fd5a98b7)<br>
    - JSON <br>
    ![JSON](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/ad845a80-9052-4c9b-9541-5936f45d2fbb)<br>
    - XML by ID <br>
    ![XML by ID](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/7585dcf4-652a-41ff-a446-24b3f0002413)<br>
    - JSON by ID <br>
    ![JSON by ID](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/67d319b7-94fc-4766-bcc1-9908adbaefdf)<br>
    
 - [x] Melakukan add-commit-push ke GitHub.<br> 

 # Bonus tugas 3

 - [x] Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini" (dengan X adalah jumlah data item yang tersimpan pada aplikasi) dan menampilkannya di
 atas tabel data. Kalimat pesan boleh dikustomisasi sesuai dengan tema aplikasi, namun harus memiliki makna yang sama. <br>
    Pertama, saya menambahkan sebuah variabel ```jumlah_items``` yang berisi data jumlah data baru yang sudah di input pada ```views.py``` di fungsi ```show_main```. Lalu, saya menambahkan messagenya kedalam dictionary ```context``` sehingga koding terlihat seperti dibawah ini. Setelah itu, saya memperbarui isi html dengan memasukkan message yang telah dibuat kedalam ```main.html```.<br>
    
    ```# menambah di views.py
    def show_main(request):
    products = Barang.objects.all()
    jumlah_item = len(products)
    context = {
        'name': 'Azka Nydia Estiningtyas',
        'npm': '2206028970',
        'class': 'PBP E',
        'products' : products,
        'total_items' : f'You have {jumlah_item} types of food items in here',
    } 

    return render(request, "main.html", context)

    
    # menambah di main.html
    <p style="text-align: center;">{{ total_items }}</p>```

Referensi: <br>
- https://docs.djangoproject.com/en/4.2/topics/forms/
- https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/
- https://www.linkedin.com/advice/0/what-advantages-disadvantages-using-json-vs-xml.


---

# Tugas 4 Checklist

---

Checklist untuk tugas ini adalah sebagai berikut:

- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar. <br>
    <br>
    Pertama, saya menjalankan virtual enviorment dulu menggunakan ```env\Scripts\activate.bat```. Lalu, saya meng-import ```redirect```, ```UserCreationForm```, dan ```messages``` untuk memudahkan pembuatan formulir register dan menambahkan fungsi register pada ```views.py``` di main supaya User yang sudah registrasi akan dibuat dan tersimpan akunnya saat klik submit. Berikut cuplikan kode untuk fungsi ```register```.<br>
    ```
    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    ```
    
    Setelah itu, saya membuat file html bernama ```register.html``` untuk membuat laman register dimana terdapat formulir yang perlu diinput untuk membuat akun didalam folder ```templates``` di main. Setelah fungsi request selesai dibuat, saya import fungsi ```register``` dan menambahkan path urlnya kedalam ```urls.py``` supaya dapat diakses.<br>
    ```
    path('register/', register, name='register'),
    ```

    Kedua, saya mengimplementasikan login dengan meng-import ```authenticate``` dan ```login``` untuk memudahkan melakukan autentikasi akun User saat Login, serta membuat fungsi ```login_user``` di ```views.py```.<br>
    ```
    def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
    ```

    Setelah itu, saya membuat lagi file html dengan nama ```login.html``` untuk menampilkan laman login didalam folder ```template``` di main. Fungsi login yang selesai dibuat akan diimport di ```urls.py``` dan ditambahkan path urlnya supaya dapat diakses.<br>
    ```
    path('login/', login_user, name='login'),
    ```

    Ketiga, saya membuat juga laman logout supaya tidak hanya satu akun yang dapat login. Saya melakukannya dengan melakukan import ```logout``` dan menambahkan fungsi ```logout_user``` di ```views.py``` di main. <br>
    ```
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```
    
    Berbeda dengan kedua fungsi sebelumnya, yang hanya bisa logout adalah yang sudah login sehingga button untuk logout berada di ```main.html``` supaya hanya bisa diakses yang sedang login. Namun, seperti sebelumnya, fungsi ```logout_user``` akan diimport ke ```urls.py``` dan di tambahkan url pathnya supaya dapat diakses fungsinya.<br>
    ```
    path('logout/', logout_user, name='logout'),
    ```

    Walaupun ketiga dungsi sudah dibuat dan dapat diakses, aksesnya User masih sama, yaitu bisa mengakses laman utama tanpa login sehingga saya perlu import ```login_required``` dan menambahkan ```@login_required(login_url='/login')``` di atas fungsi ```show_main``` supaya akses lama utama hanya dapat dibuka untuk User yang sudah di autentikasi.<br>

    Lalu, saya import ```datetime``` dan membuat cookie bernama ```last_login``` didalam fungsi ```login_user``` untuk mencatat kapan User terakhir login. Berikut kode untuk menambahkan cookie ```response.set_cookie('last_login', str(datetime.datetime.now()))```. <br>
    
    Supaya last_login muncul di laman utama, maka saya menambahkannya di ```context``` dalam fungsi ```show_main``` menggunakan kode ```'last_login': request.COOKIES['last_login'],``` dan agar cookie User tidak dapat diakses User lain, saya menambahkan kode ``` response.delete_cookie('last_login')``` di fungsi ```logout``` agar cookie terhapus saat User logout. Lalu, ```last_login``` saya panggil kedalam html supaya dapat dilihat oleh User.<br>

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal. <br>
    Dibawah ini foto jika item dibuat oleh berbeda User tetapi tidak di filter sehingga semua item pada User berbeda akan muncul siapapun User yang login.
    ![akunori](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/94bde34e-937e-4fd1-8237-7d43bef6b9c0)
    <br>
    <br>
    Pada dua foto dibawah ini adalah 2 akun User yang saya buat setelah item sudah difilter sesuai User dengan masing-masing memiliki 3 jenis item berbeda sesuai add item yang masing-masing User lakukan.<br>
    ![akun #1](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/12a6d80e-5ac0-4c7d-8efb-c5a763df7647)<br>
    ![akun #2](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/c4c6938f-799a-47a4-abbd-e97f031d2357)<br>

- [x] Menghubungkan model ```Item``` dengan ```User```. <br>
    Pada langkah sebelumnya, saya sudah mengimplementasikan cookie, registrasi, login, dan logout. Namun, Item yang dimasukkan kedalam belum dikaitkan dengan User tertentu sehingga Item akan terlihat oleh semua User yang telah login. Supaya hanya User yang menambahkan Item yang bisa melihat item tersebut, saya membuat sebuah relationship antara User dan Item dengan import ```User``` dan menambah  variabel user di ```models.py``` menggunakan kode berikut:<br>
    ```
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```
    
    Setelah itu, saya menambah kode di fungsi ```add_item``` (Pada tugas sebelumnya, nama fungsinya ```create_product```) supaya Item yang ditambahkan ditandai bahwa itu milik User yang sedang login. <br>
    ```
    def add_item(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    ```

    Saya juga mengubah isi dari fungsi ```show_main``` di ```views.py``` dengan menggantikan isi variabel product dengan ``` products = Product.objects.filter(user=request.user)``` dan mengubah isi nama di context dengan ```'name': request.user.username,```. Hal ini dilakukan supaya item dan nama yang muncul didalam adalah punya User yang sedang login. Lalu, saya menyimpan perubahan menggunakan makemigrations dan migrate di cmd.<br>

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan ```cookies``` seperti ```last login``` pada halaman utama aplikasi. <br>
    Pada foto dibawah, Infomasi usernama saya taruh paling atas dan last login saya taruh dibawah button add item.
    ![akun #1](https://github.com/AzkaNydiaEsti/food_inventory/assets/124995308/12a6d80e-5ac0-4c7d-8efb-c5a763df7647)<br>

- [x] Menjawab beberapa pertanyaan berikut pada ```README.md``` pada root folder (silakan modifikasi ```README.md``` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas). <br>

    - Apa itu Django ```UserCreationForm```, dan jelaskan apa kelebihan dan kekurangannya? <br>
        UserCreationForm merupakan build-in module yang diturunkan dari ModelForm dan berguna untuk membuat User baru yang dapat mengakses web application. Pembuatan user baru memerluka 3 input, yaitu username, password, dan password confirmation. <br>
        - Kelebihannya: UserCreationForm django mudah untuk digunakan hanya dengan menggunakan beberapa baris kode, UserCreationForm juga mudah untuk mengintegrasi dengan authentication system sehingga akun User yang telah dibuat mudah untuk disimpan dan dikelola, UserCreationForm dapat di customized sesuai kebutuhan developer, dan kompatibel dengan berbagai aplikasi/extension. <bt>
        - Kekurangan: Walaupun mudah dipakai dan di customized, terdapat keterbatasan dalam melakukan autentifikasi dan vaidasi akun yang kompleks karena fitur yang ditawarkan masih dasar. Tampilan HTML dari registrasi user juga polos sehingga perlu diubah sendiri oleh developer. <br>
        <br>
    - Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? <br>
        Autentikasi dalam konteks Django adalah proses memverifikasi identitas dari User yang masuk aplikasi. Hal ini untuk memastika User yang dapat mengakses fitur aplikasi hanyalah User sah dan untuk menjaga keamanan aplikasi. Umumnya, autentikasi memerlukan username dan password User. <br>
        <br>
        Sedangkan, otorisasi adalah proses untuk menentukan fitur apa yang dapat User gunakan setelah terverifikasi dan dapat masuk aplikasi. Otorisasi berfungsi supaya User hanya dapat melakukan atau mengakses hal yang diizinikan saja dan tidak dapat mengakses data sensitif aplikasi yang bukan miliknya. Kedua hal tersebut krusial demi menjaga keamanan aplikasi dan melindungi data privasi yang tersimpan didalam aplikasi supaya tidak dapat diakses oleh orang yang tidak punya hak. <br>
        <br>
    - Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna? <br>
        Cookies adalah data yang disimpan dalam perangkat user selama periode tertentu setelah User melakukan login dalam aplikasi. Penggunaan cookies umumnya untuk otentikasi, personalisasi, dan managemen sesi. Saat User melakukan login, sebuah cookie session akan dibuat untuk User tersebut, dan Django akan menggunakan cookie ini untuk menyimpan informasi yang diinput oleh User dalam bentuk data sesi selama session tersebut. Informasi yang disimpan dalam sesi dapat bervariasi, termasuk nama User atau preferensi User. Data sesi ini dapat diakses oleh User dan dapat dihapus baik secara manual oleh User atau secara otomatis dalam periode tertentu. Penggunaan cookies untuk mengelola sesi User memungkinkan aplikasi Django untuk menjaga status User, mengidentifikasi User yang masuk, dan menyimpan informasi penting lainnya selama User sedang login<br>
        <br> 
    -  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? <br> 
        Penggunaan cookies aman jika dilindungi dengan baik, tetapi terdapat beberapa risiko saat menggunakan cookies, seperti berikut: <br>
            1. Kebocoran data: Karena cookies menyimpan informasi dari User dan kadang termasuk data sensitif seperti otentifikasi User sehingga terdapat potensi risiko privasi untuk data tersebut diambil saat cookies diakses oleh Penyerang atau hacker. <br>
            2. Cross-Site Scripting (XSS): Saat penyerang melakukan serangan XSS, mereka dapat menyisipkan script jahat kedalam aplikasi dan mengakses cookies User sehingga dapat masuk kedalam aplikasi sebagai User.<br>
            3. Cross-Site Request Forgery (CSRF): Penyerang dapat memaksa User yang sudah terautentikasi untuk melakukan request tanpa persetujuan User. <br>
            4. Session Hijacking: Cookies User yang berhasil dicuri dapat digunakan oleh penyerang untuk masuk aplikasi dan mengambil alih session user. <br>
            <br>
    - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
        Telah dijelaskan pada checklist diatas<br>

- [x] Melakukan ```add```-```commit```-```push``` ke GitHub. <br>
    Saya melakukan ```git add .``` , ```git commit -m "<>"```, dan ```git push -u origin main``` setelah semua koding selesai supaya di-update di github.<br>

Referensi
- https://www.javatpoint.com/django-usercreationform

# Bonus Tugas 4

- [x] Tambahkan tombol dan fungsi untuk menambahkan amount suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu.<br>
    Pertama, saya membuat fungsi ```dec_item``` dan ```inc_item``` untuk membuat button yang akan mengurangi dan menambah jumlah dari tiap item. <br>
    ```
    def dec_amount(request, id):
    item = Barang.objects.get(pk=id)
    if request.method == 'POST':
        if item.amount > 0:
            if item.amount > 0:
                item.amount -= 1
                item.save() 
            elif item.amount <= 0:
                item.delete()
    return redirect('main:show_main')

    def inc_amount(request, id):
        item = Barang.objects.get(pk=id)
        if request.method == 'POST':
            if item.amount > 0:
                item.amount += 1
                item.save() 
        return redirect('main:show_main')
    ```

    Setelah itu, saya import fungsi dan tambah urls pathnya didalam ```urls.py``` supaya dapat dipanggil di ```main.html```.<br>
    ```
    path('dec_amount/<int:id>/', views.dec_amount, name='dec_amount'),
    path('inc_amount/<int:id>/', views.inc_amount, name='inc_amount'),
    ```

    Lalu, saya memodifikasi main.html supaya tombol muncul dan bisa digunakan dengan kode berikut:<br>
    ```
    <td style="align-items: center; display: flex">
        <form method="post" action="{% url 'main:dec_amount' product.id %}">
            {% csrf_token %}
            <button type="submit">-</button>
        </form>
        <span style="margin: 0 10px;">{{ product.amount }}</span>
        <form method="post" action="{% url 'main:inc_amount' product.id %}">
            {% csrf_token %}
            <button type="submit">+</button>
        </form>
    </td>
    ```

- [x] Tambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori.<br>
     Pertama, saya membuat fungsi ```deelete_item``` untuk membuat button yang akan mengurangi dan menambah jumlah dari tiap item. <br>
    ```
    def delete_item(request, id):
    if request.method == 'POST':
        item = Barang.objects.get(id=id)
        item.delete()
    
    return redirect('main:show_main')
    ```

    Setelah itu, saya import fungsinya dan tambah urls pathnya didalam ```urls.py``` supaya dapat dipanggil di ```main.html```.<br>
    ```
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    ```

    Lalu, saya memodifikasi main.html supaya tulisan delete muncul dan bisa digunakan dengan kode berikut:<br>
    ```
    <td>
        <form action="{% url 'main:delete_item' product.id %}" method="POST">
            {% csrf_token %}
            <button style="background-color: antiquewhite; border: none; color: #91BEDC;" type="submit">
                <span>Delete</span>
            </button>
        </form>
    </td>
    ```
