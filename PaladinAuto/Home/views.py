from django.shortcuts import render
import time

menu = [
{'title':'Главная', 'name':'home'},
{'title':'Рабочий процесс', 'name':'work_process'},
{'title':'Отзывы', 'name':'reviews'},
{'title':'Контакты', 'name':'contacts'},
]
def home(request):
    data = {
        'title':'Главная страница',
        'menu':menu,
    }
    return render(request,'Home/home_page.html', context=data)

def contacts(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request,'Home/contacts.html', context=data)

def reviews(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request,'Home/reviews.html', context=data)

def submit_application(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request,'Home/submit_application.html', context=data)

def work_process(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request,'Home/work_process.html', context=data)

