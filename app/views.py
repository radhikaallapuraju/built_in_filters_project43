from django.shortcuts import render

# Create your views here.
import datetime
def built_in_filters(request):
    dt=datetime.datetime.now()
    d={'dt':'Hii HoW aRe You','dt':dt,'c':1}
    
    return render(request,'built_in_filters.html',d)
