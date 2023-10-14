from django.shortcuts import render
import time
now_time = {'now_time':time.time()}
def home(request):
    return render(request,'Home/home_page.html',now_time)
