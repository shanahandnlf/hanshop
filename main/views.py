from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'app_name': 'main',
        'nama_mahasiswa': 'Shanahan Danualif Erwin',
        'class_name': 'PBP F',

        # 'name': 'Holo Charizard Card',
        # 'amount': '100',
        # 'description': 'Authentic from 1999',
        # 'price': '$4200'
    }
    return render(request, "main.html", context)