from django.shortcuts import render
from .models import *
# Create your views here.
def indexx(request):
    var="image"
    int=1
    import random
    thisdict =    [
  "protein",
  "juice",
  "red_phone",
  "apple",
  "camera",
  "clock",
  "headphone",
  "juice_pack",
  "printer"
]
    random.shuffle(thisdict)
    return render(request,'user_end/home.html',{'img_name':var,'star':int,'names':thisdict})
    return render(request,'user_end/home.html',{'img_name':var,'star':int,'names':thisdict})



def product_page(request):
    prod_d = Products.objects.all()
    pikName=[
         "apple",
         "headphone",
         "juice_pack",
         "printer"
        ]
    print(prod_d)
    return render(request,'user_end/product.html',{'pikuName':pikName,})
    # return render(request,'user_end/product.html',{'pikuName':pikName})
