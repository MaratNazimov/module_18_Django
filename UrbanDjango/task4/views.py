from django.shortcuts import render

def main_page(request):
    title = 'Главная страница'
    context  = {
        'title': title,
        'content': ["Тут что-то есть :-)"]
    }
    return render(request, 'fourth_task/main_page.html', context)

def shop(request):
    title = 'Магазин'
    context = {
        'title': title,
        'content': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]}
    return render(request, 'fourth_task/shop.html', context)

def basket(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/basket.html', context)

def menu(request):
    title = 'Administrator Menu'
    context = {
        'title': title
    }
    return render(request, 'fourth_task/menu.html', context)
