

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
     return render(request,'emanticc.html')

# def eggs(request):
#     return HttpResponse('Eggs are Great!!!')

def count(request):
     full=request.GET['fulltext']
     list=full.split()
     print(full)
     return render(request,'count.html',{'puratay':full,'count':len(list)})

def index(request):
    return render(request,'hi.html')
def new(request):
    return render(request,'base_layout.html')

def prod(request):
    return render(request,'product.html')
