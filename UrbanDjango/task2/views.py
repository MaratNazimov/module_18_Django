from django.shortcuts import render
from django.views.generic import TemplateView


def func_temp(request):
    return render(request, 'second_task/func_temp.html')

class class_temp(TemplateView):
    template_name = 'second_task/class_temp.html'
