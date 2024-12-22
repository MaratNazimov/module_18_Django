from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ["Oleg", "Tanya", "Alexander", "Sergei", "Natalya", "Vladimir"]

def sign_up_by_html(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        subscribe = request.POST.get("subscribe")

        for i in users:
            if i == username:
                error = "Пользователь уже существует"
                return render(request, "fifth_task/registration_page.html",
                              {"error": error})
        if int(age) < 18:
            error = "Вы должны быть старше 18"
            return render(request, "fifth_task/registration_page.html",
                          {"error": error})
        if password != repeat_password:
            error = "Пароли не совпадают"
            return render(request, "fifth_task/registration_page.html",
                          {"error": error})
        if subscribe != 'on':
            error = "Вы не подтвердили согласие на обработку персональных данных"
            return render(request, "fifth_task/registration_page.html",
                          {"error": error})
        else:
            return HttpResponse(f"Приветствуем, {username}!")
    return render(request, "fifth_task/registration_page.html")


def sign_up_by_django(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]
            subscribe = form.cleaned_data["subscribe"]

            for i in users:
                if i == username:
                    error = "Пользователь уже существует"
                    return render(request, "fifth_task/registration_page.html",
                                  {"error": error})
            if int(age) < 18:
                error = "Вы должны быть старше 18"
                return render(request, "fifth_task/registration_page.html",
                              {"error": error})
            if password != repeat_password:
                error = "Пароли не совпадают"
                return render(request, "fifth_task/registration_page.html",
                              {"error": error})
            if subscribe == False:
                error = "Вы не подтвердили согласие на обработку персональных данных"
                return render(request, "fifth_task/registration_page.html",
                              {"error": error})
            else:
                return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = UserRegister()
    return render(request, "fifth_task/registration_page.html", {'form': form})


