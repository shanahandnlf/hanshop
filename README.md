
- [Tugas 2](#tugas-2-pbp)
- [Tugas 3](#tugas-3-pbp)



# Tugas 2 PBP

Nama            : Shanahan Danualif Erwin

Kelas           : PBP F

Link Adaptable  : https://hanshop.adaptable.app/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat sebuah proyek Django baru.

Untuk membuat sebuah proyek Django baru, sebaiknya kita menjalankan sebuah _virtual environment_ terlebih dahulu untuk mencegah terjadi konfilk proyek Django dengan proyek yang lain. Kita bisa menjalankan perintah __"python -m venv env"__ di terminal untuk membuat virtual environment. Kemudian jalankan __"env\Scripts\activate.bat"__ untuk mengaktifkannya. Kita sebaiknya menggunakan Command Prompt saja sebagai terminal karena di PowerShell tidak bisa mengaktifkan _virtual environment_.

Selanjutnya kita akan meng-_install_ _dependencies_ __django, gunicorn, whitenoise, psycopg2-binary, requests, urllib3__ agar proyek dapat berfungsi dengan baik. Kita akan membuat file __requirements.txt__ dalam direktori yang sama dan kita isi dengan _dependencies_ yang dibutuhkan. Kemudian jalankan perintah  __"pip install -r requirements.txt"__ di terminal untuke meng-_install_. Setelah itu, kita dapat menjalankan perintah __"django-admin startproject hanshop .""__ untuk membuat proyek Django dengan nama hanshop. Perlu diingat "hanshop" adalah nama proyek Django saya dan dapat diganti sesuai keinginan kita.

Agar kita dapat _deploy_ proyek kita kepada _web hosting_, kita akan mengganti text yang ada pada __settings.py__. Kita akan menambahkan tanda * pada __ALLOWED_HOSTS__ agar proyek mengizinkan akses dari semua _host_. Nanti tampilan __ALLOWED_HOSTS__ pada setting.py akan menjadi 
__ALLOWED_HOSTS = ["*"]__. Dengan demikian, proyek Django berhasil dibuat. Sebagai catatan sebaiknya kita selalu memakai _virtual environment_ saat menggunakan Django. 
 
- Membuat aplikasi dengan nama main pada proyek tersebut.

Sebelum membuat aplikasi, pastikan virtual environment kita sudah menyala seperti yang sudah dijelaskan pada poin sebelumnya. Kemudian kita akan menjalankan perintah __"python manage.py startapp main"__ dalam direktori proyek django kita. Perintah ini akan membuat aplikasi dengan direktori baru yang bernama __main__ yang menjadi struktur awal aplikasi Django.

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

Setelah app __main__ sudah terbentuk, kita harus menghubungkan aplikasi ke dalam proyek Django kita. Kita dapat menghubungkannya dengan cara membuka berkas settings.py yang berada dalam direktori proyek Django. Kemudian kita akan menambahkan __"main"__ ke dalam variabel __INSTALLED_APPS__. Hasil akhir kodenya akan terlihat seperti ini 
__"INSTALLED_APPS = ['main']__"(jangan menghapus daftar aplikasi __INSTALLED_APPS__ yang sudah ada)

- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
  - name sebagai nama item dengan tipe CharField
  - amount sebagai jumlah item dengan tipe IntegerField
  - description sebagai deskripsi item dengan tipe TextField.

Untuk membuat model pada aplikasi __main__, kita akan membuka models.py dan mengisi kode seperti berikut:
````
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
````
Pada line 1 kita akan meng-_import_ module model dari django. Kemudian pada line 3-6 kkita membuat sebuah model bernama Product dengan field name, amount, description, dan price. Tiap field mempunyai tipe data yang sesuai dengan kebutuhan nama fieldnya. Untuk name kita memakai CharField yang cocok untuk menyimpan text dengan panjang 255 karakter. Untuk amount dan price kita memakai Integer Field untuk menyimpan angka apapun asalkan masih dalam range Integer. Untuk description kita memakai TextField yang cocok untuk menyimpan teks panjang seperti sebuah paragraf karena tidak ada panjang karakter maksimum.

Selanjutnya kita akan melakukan migrasi model dengan menjalankan perintah __"python manage.py makemigrations"__ diikuti __"python manage.py migrate"__ untuk melakukan migrasi model ke dalam basis data lokal. Tiap kali ada perubahan dalam model, kita harus melakukan migrasi ini agar perubahan tersebut tercatat.

- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

Pertama, buatlah direktori baru bernama __templates__ dalam direktori __main__. Kemudian kita buat berkas __main.html__ yang akan kita isi dengan koding sebagai berikut:
````
<h1>Inventory List Page</h1>

<h5>Nama aplikasi: </h5>
<p>{{app_name}}<p>
<h5>Nama: </h5>
<p>{{nama_mahasiswa}}</p><p>
<h5>Kelas: </h5>
<p>{{class_name}}<p>
````
Kode berikut adalah kode untuk menampilkan app_name, nama_mahasiswa, dan class_name untuk aplikasi kita. Kita memakai double curly braces seperti ini __{{ ... }}__ untuk menyimpan variabel yang valuenya kita masukkan di __views.py__. 

Bukalah views.py yang berada dalam direktori kemudian kita akan membuat fungsi seperti ini:
````
def show_main(request):
    context = {
        'app_name': 'Han Shop',
        'nama_mahasiswa': 'Shanahan Danualif Erwin',
        'class_name': 'PBP F',
    }
    return render(request, "main.html", context)
````
Dalam fungsi ini terdapat dictionary untuk menyimpan value app_name, nama_mahasiswa, dan class_name kita. Kita juga menggunakan __render__ yang berfungsi untuk me-_render_ tampilan __main.html__ kita.

Selanjutnya buatlah file __urls.py__ dalam direktori main. file __urls.py__ ini akan mengonfigurasi routing untuk aplikasi __main__ kita. Kita akan menambahkan koding seperti ini:
````
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
````
Disini kita meng-_import_ module __path__ untuk mendefinisikan pola URL kita dan __show_main__ dari __main.views__ yang sudah kita buat. Kemudian pada line 4 kita menetapkan namespace __main__ sebagai konfigurasi URL ini agar tidak ada konflik dengan aplikasi berbeda. Terlihat pada line 7 nanti fungsi __show_main__ akan dipanggil ketika URL diakses.

Setelah itu kita akan membuka file __urls.py__ dalam direktori proyek. Kita akan mengimpor fungsi __include__ seperti ini ````from django.urls import path, include```` untuk mengimpor URL dari aplikasi main ke urls.py dalam direktori proyek. Kemudian tambahkan rute URL seperti ini:
````
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
````
Kode ini membuat path __main/__ akan diarahkan ke urls.py yang berada dalam aplikasi __main__

Dengan demikian, akan terlihat tampilan HTML yang kita inginkan beserta value yang sdah kita atur di views setelah melakukan routing ini.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Alt text](image.png)

Alurnya pertama client akan meminta request yang diarahkan ke urls.py. Disini pola URL di urls.py akan dicocokkan dengan URL yang diterima kemudian urls.py akan memilih fungsi view sesuai request dari user. Selanjutnya View akan melakukan query ke model dimana model dapat melakukan transaksi data dengan database untuk mendapatkan data yang sesuai. Model kemudian akan mengirim _respond data_ ke view kembali yang dilanjutkan dengan view memilih template HTML yang sesuai dengan permintaan client. Terakhir, template yang telah dipilih akan ditampilkan ke pengguna dari halaman web

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita menggunakan virtual environment agar proyek Django yang sedang kita jalankan terisolasi dari proyek lain. Hal ini sangat penting agar _dependencies_ yang kita _install_ hanya digunakan untuk proyek itu saja. Hal ini juga bermanfaat agar tiap proyek bisa mempunyai _dependencies_ masing-masing. Selain itu, kita bisa mengatur versi dari python atau package yang kita gunakan agar sesuai dengan kebutuhan proyek kita. Selain itu, dengan virtual environment proyek kita bisa lebih portable sehingga jika ada orang lain yang ingin menggunakan proyek kita, mereka dapat membuat virtual environment saja kemudian meng-_install_ dependencies yang dibutuhkan tanpa khawatir terjadi konflik pada komputernya.

Kita tetap bisa menjalankan aplikasi berbasis Django tanpa menggunakan virtual environment. Namun banyak sekali masalah yang dapat terjadi jika kita tidak menggunakan virtual environment yang dapat menghambat pengembangan aplikasi kita. Contohnya seperti jika terjadi perbedaan versi antara python yang ada di lingkungan global dengan versi Python yang digunakan pada Django akan membuat masalah karena beda versinya. Tentu saja lebih mudah untuk mengaktifkan virtual environment dan mengunduh versi Django sesuai kebutuhan kita.



4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

- MVC (Model-View_Controller) 
    - Model: Model disini berfungsi untuk mengelola data dan berhubungan langsung dengan _database_
    - View: bagian yang bertanggung jawab untuk menampilkan informasi atau data kepada pengguna
    - Controller: sebagai perantara Model dan View dalam setiap proses request dari user.

- MVT (Model-View-Template)
    - Model: Bagian yang bertanggung jawab mengatur dan mengelola data dari aplikasi
    - View: Komponen yang mengatur bagaimana data yang dikelola akan ditampilkan kepada pengguna
    - Template: Komponen yang berperan sebagai tampilan yang dikembalikan kepada pengguna

- MVVM(Model-View-ViewModel)
    - Model: Bertanggung jawab untuk mengambil dan menyimpan data serta memproses data yang diperlukan
    - View: Mewakili representasi visual dari data yang ditampilkan ke pengguna
    - ViewModel: Berperan sebagai jembatan antara Model dan View, bertanggung jawab untuk menyimpan status tampilan dan menjalankan operasi yang diperlukan untuk mengubah data dalam Model ke format yang dapat ditampilkan.

 - Perbedaan yang dapat terlihat dari ketiga arsitektur ini adalah cara interaksi antara komponen-komponennya. Pada MVC kita menggunakan Controller untuk mengatur alur aplikasi. Sedangkan MVT merupakan turunan dari struktur MVC dimana View yang berperan sebagai jembatan antara Model, Template dan Template berfungsi sebagai tampilan untuk pengguna menggantikan peran View pada MVC, dan Model berfungsi mengolah data mengelola data pada aplikasi seperti pada MVT. Terakhir untuk MVVM yang berperan sebagai jembatan antara Model dan View adalah ViewModelnya, sedangkan Model dan Viewnya berfungsi seperti pada MVC.

# Tugas 3 PBP

1. Apa perbedaan antara form POST dan form GET dalam Django?
- GET
    - Biasa digunakan untuk mengirim data-data tidak penting
    - Untuk mengirim permintaan ke server tertentu guna mendapatkan data atau sumber daya tertentu.
    - Nilai variabel ditampilkan di URL sehingga user dapat memasukkan nilai variabel baru, tetapi tidak terlalu aman
- POST
    - Digunakan untuk mengirim data-data sensitif seperti password
    - Untuk mengirimkan data ke server guna membuat atau memperbarui data tertentu.
    - Nilai variabel tidak terekspos di URL jadi lebih aman


2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

- XML (eXtensible Markup Language)
    - Format file untuk menyimpan data dengan cara yang terstruktur, tetapi tidak efisien
    - Lebih kompleks dan ukuran filenya lebih besar dari JSON
    - Pilihan utama untuk mentransmisikan data terstruktur melalui web.


- JSON (JavaScript Object Notation)
    - Format file untuk menyimpan data secara efisien, tetapi tidak rapi untuk dilihat
    - Sintaks yang lebih ringan dan berukuran lebih kecil.
    - Cocok sebagai media penyimpanan untuk aplikasi web karena kesederhanaannya.

- HTML (Hypertext Markup Language)
    - Format file yang digunakan untuk menampilkan konten web


3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

Alasan utamanya adalah format JSON yang lebih sederhana dan ringkas. Hal ini menyebabkan JSON dapat ditransmisikan lebih cepat melalui jaringan serta pemrosesan data menjadi lebih cepat dibanding menggunakan XML. Oleh karena itu, JSON sangat cocok digunakan untuk pertukaran data antara aplikasi web modern



4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).


- Membuat input form untuk menambahkan objek model pada app sebelumnya.

Untuk membuat input form, pertama-tama kita harus membuat direktori yang bernama _templates_ pada direktori root kemudian kita isi dengan berkas base.html. FIle html ini akan menjadi template dasar projek kita dengan kodingan:
````
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
````

Selanjutnya, kita akan mengubah _settings.py_ yang berada dalam direktori hanshop. Carilah TEMPLATES kemudian tambahkan __'DIRS': [BASE_DIR / 'templates'],__ agar dapat terhubung dengan base.html yang telah dibuat. Kode akhir akan terlihat seperti ini:
````
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # perubahan disini
        'APP_DIRS': True,
        ...
    }
]
...
````
Bukalah file __main.html__ dalam folder main/templates dan ubahlah kode menjadi berikut:
````
{% extends 'base.html' %}

{% block content %}
    <h1>Trading Card Store</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>
{% endblock content %}
````
Kode diatas menggunakan __base.html__ sebagai template utama kita. Setelah kita melakukan setup skeleton sebagai kerangka views, kita akan memulai membuat form input data. Buatlah file __forms.py__ dalam direktori main untuk membuat struktur form yang dapat menerima data produk baru. Isi kodingannya:
````
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount" , "description", "price"]
````
Kemudian, kita membuka file _views.py_ dalam direktori main yang kita tambahkan import modulnya dan kita edit fungsi __create_item__ untuk menambahkan data produk secara otomatis ketika form di-submit. Kodingannya seperti ini:
````
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
````

Selanjutnya, kita menambahkan path URL dalam __urls.py__ dalam direktori main. Caranya dengan mengisi kode berikut:
````
from main.views import show_main, create_item
...
urlpatterns = [
    ...
    path('create-item', create_item, name='create_item'),
]
````
Selanjutnya kita akan mengedit file html yang ada di direktori main/templates. Pertama buatalah file baru bernama __create_item.html__ yang diisi dengan:
````
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
````
Kode ini digunakan agar pengguna dapat mengisi form dan di-submit sesuai fields yang sudah dibuat pada model. Setelah itu, bukalah main.html yang berada dalam direktori main/templates yang kita tambahkan dengan kode:
````
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
````
Kode ini akan menampilkan data produk dalam bentuk tabel serta tombol "Add New Item" yang kalau diklik akan redirect user ke halaman form.


- Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
Sebelum kita membuat fungsi views yang kita inginkan, importlah modul-modul ini terlebih dahulu karena dibutuhkan oleh fungsi views yang kita ingin buat dalam file views.py dalam folder main
````
from django.shortcuts import render
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
````
Selanjutnya kita akan memulai membuat fungsi views yang kita inginkan. Kita akan mengedit __views.py__ dalam direktori main untuk membuat fungsi-fungsinya. Untuk melihat objek yang sudah kita tambahkan, ubahlah kode show_main dengan menambahkan __items = Item.objects.all()__ yang dapat mengambil seluruh object Item yang tersimpan di database. Kode fungsinya akan seperti ini:
````
def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Shanahan Danualif Erwin', # Nama kamu
        'class': 'PBP F', # Kelas PBP kamu
        'items': items
    }

    return render(request, "main.html", context)
````
Untuk melihat objek yang kita inginkan dalam format XML, buatlah fungsi show_xml seperti berikut:
````
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
````
Jika ingin melihat data-data yang kita tambahkan berdasarkan id yang kita inginkan dalam format XML, tambahkan fungsi show_xml_by_id seperti ini:
````
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
````
Untuk melihat objek yang kita inginkan dalam format JSON, buatlah fungsi show_xml seperti berikut:
````
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
````

Jika ingin melihat data-data yang kita tambahkan berdasarkan id yang kita inginkan dalam format JSON, tambahkan fungsi show_json_by_id seperti ini:
````
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
````

- Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

Bukalah __urls.py__ yang berada dalam direktori main dan tambahkan pathing berikut:
````
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ....
]
````

- Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

![Alt text](image-1.png)
![Alt text](image-2.png)
![Alt text](image-3.png)
![Alt text](image-4.png)
![Alt text](image-5.png)
![Alt text](image-6.png)