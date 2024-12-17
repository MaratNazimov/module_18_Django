from django.shortcuts import render

def page(request):
    title = 'Игровая платформа'
    text = 'Главная страница'
    shop_ing = 'Магазин'
    basket_ = 'Корзина'
    cont_dict = {
        'title': title,
        'text': text,
        'shop_ing': shop_ing,
        'basket_': basket_,
    }
    return render(request, 'third_task/main_page.html', cont_dict)

def shop(request):
    return render(request, 'third_task/shop.html')

def basket(request):
    return render(request, 'third_task/basket.html')
