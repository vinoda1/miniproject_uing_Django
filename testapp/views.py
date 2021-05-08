from django.shortcuts import render,HttpResponse,redirect
from testapp.models import Prodcuts ,User_details
from testapp.form import Products_Form,Detail_Form
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
def home(request):
    return render(request,'home.html')


def index(request):
    item=Prodcuts.objects.all() 

    return render(request,'index.html',{'product_item':item})

def detail_view(request):
    form_class=Detail_Form()
    if request.method == 'POST':
        form_class = Detail_Form(request.POST)
        if form_class.is_valid():
            form_class.save()
            return redirect('index')
        else:
            HttpResponse("something wrong,reload <a href='{{url:'display'}}'>reload</a>")
    
    else:
        my_dict={'form':form_class}
        return render(request,"detail.html",my_dict)
    

def upload(request):
    obj=Products_Form()

    if request.method=='POST':
        obj=Products_Form(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            return redirect('index')

        else:
            return HttpResponse("something wrong,reload <a href='{{url:'index'}}'>reload</a>")
    
    else:

        return render(request,'upload.html',{'upload_form':obj})

@login_required
def update(request,product_id):
    product_id=int(product_id)

    try:

        product_select=Prodcuts.objects.get(id=product_id)

    except Prodcuts.DoesNotExist:
        return redirect('index')

    else:
    
        product_form=Products_Form(request.POST or None,instance=product_select)

        if product_form.is_valid():
            old_image = ""
            if product_select.picture:
                old_image = product_select.picture.path
                #data/fields are updated 
                form = Products_Form(request.POST,request.FILES,instance = product_select)
                if form.is_valid():
                    #if you found image at specified location , remove it
                    if os.path.exists(old_image):
                        os.remove(old_image)
                        #updated fields will be saved
                        form.save()
        
            return redirect('index')
        return render(request,'upload.html',{'upload_form':product_form})  

def delete(request,product_id):
    
    product_id=int(product_id)
    
    try:
        product_select=Prodcuts.objects.get(id=product_id)

    except Prodcuts.DoesNotExist:
        return redirect('index')

    product_select.delete()
    return redirect('index')
    
def subscribe(request):
    return render(request,"subscribe.html")  

def success(request):
    return render(request,"success.html")

def contact(request):
    return render(request,'contact.html')

def About_us(request):
    return render(request,'Aboutus.html')

def logout(request):
    return render(request,'logout.html')
