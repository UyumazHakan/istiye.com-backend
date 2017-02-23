_author__ = 'Hakan Uyumaz'

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.utils import timezone

from ..forms import UserCreationForm
from ..utils import generate_token, send_activation_mail, custom_redirect

def login_user(request):
    if request.user.is_authenticated():
        return redirect("index")
    else:
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        if email and password:
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
        return redirect("index")

def register_user(request):
    if request.user.is_authenticated():
        return redirect("index")
    else:
        if request.method == "POST":
            if request.POST["password"] != request.POST["password2"]:
                print("asdadasd")
                return custom_redirect('index', type=4, head = "Hata", body= "Girdiginiz sifreler uyusmuyor.")
            form = UserCreationForm(request.POST)
            print("1")
            if form.errors:
                print(form.errors)
                custom_redirect("index", type = 4, head = "Hata", body = "Formu eksiksiz doldurunuz.")
            user = form.save()
            print("2")
            user.save()
            print("3")
            return custom_redirect("index", type = 1, head = "Basarili", body = "Kullanici kaydiniz basariyla olusturuldu.")
        else:
            return custom_redirect('index', type = 3, head = "Uyari", body = "Uye olmak icin lutfen sitedeki formu kullaniniz.")

def edit_profile(request):
    user = request.user
    if request.user.is_authenticated():
        if request.method == "POST":
            password = request.POST.get('password', None)
            password2 = request.POST.get('password2', None)
            if (password and not password2) or (not password and password2):
                print("aaa", request.POST["password"],request.POST["password2"])
                return custom_redirect('index', type=4, head="Hata", body="Girdiginiz sifreler uyusmuyor.")
            elif password and password2 and password == password2:
                print("ccc", request.POST["password"], request.POST["password2"])
                user.set_password(request.POST["password"])
            user.name = request.POST["name"]
            user.surname = request.POST["surname"]
            user.address = request.POST["address"]
            user.email = request.POST["email"]
            user.save()

        return redirect("index")
    else:
        return redirect("index")

def logout_user(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect("index")