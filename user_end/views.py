from django.shortcuts import render

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
    return render(request,'user_end/product.html',{'img_name':var,'star':int,'names':thisdict})
