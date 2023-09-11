from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'app_name': 'HanShop',
        'nama_mahasiswa': 'Shanahan Danualif Erwin',
        'class_name': 'PBP F',
    }
    return render(request, "main.html", context)