from django.shortcuts import render

from admins.models import ProductModel,ProductModelImages
# Create your views here.
def homepage(request):
    products = ProductModel.objects.all()
    productImages =  ProductModelImages.objects.all()
    return render(request,'customer/index.html',{'products':products,'productImages':productImages})