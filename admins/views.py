from django.shortcuts import render,redirect,get_object_or_404

from .models import CategoryModel,CategoryFormModel,SubCategoryModel,SubCategoryModelForm,BrandModel,BrandModelForm,SuplierModel,SuplierModelForm,ProductModel,ProductModelForm,ProductModelImages,StockModel,StockModelForm
from django.conf import settings
import os
import random
import barcode
from datetime import datetime
import cv2
from pyzbar import pyzbar
import numpy as np
# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html',{'title':'Dashboard'})

def profile(request):
    if request.method=="POST":
        print(request.POST['firstname'])
    return render(request,'admin/profile.html',{'title':'Profile'})

def categoryView(request):
    allCategory = CategoryModel.objects.all()
    return render(request,'admin/category/categoryView.html',{'title':'Category','categories':allCategory})

def categoryCreate(request):
    form = CategoryFormModel(request.POST or None)
    if request.method == "POST":
        if form.is_valid:
            obj = form.save(commit=False)
            obj.save()
            return redirect("/admin/category/")
    return render(request,'admin/category/categoryCreate.html',{'title':'Create Category','form':form})

def categoryEdit(request,categoryId):
    oneCategory = get_object_or_404(CategoryModel,id=categoryId)
    form = CategoryFormModel(request.POST or None,instance=oneCategory)
    if request.method=="POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('/admin/category/')
    return render(request,'admin/category/categoryCreate.html',{'title':'Update Category','form':form})

def categoryDelete(request,categoryId):
    obj=get_object_or_404(CategoryModel,id=categoryId)
    obj.delete()
    return redirect('/admin/category/')

# sub category
def subCategoryView(request):
    allSubCategory = SubCategoryModel.objects.all()
    return render(request,'admin/subcategory/subCategoryView.html',{'title':'Sub Category','subCategories':allSubCategory})

def subCategoryCreate(request):
    form = SubCategoryModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid:
            obj = form.save(commit=False)
            obj.save()
            return redirect("/admin/subcategory/")
    return render(request,'admin/subcategory/subCategoryCreate.html',{'title':'Create Sub Category','form':form})

def subCategoryEdit(request,subCategoryId):
    oneSubCategory = get_object_or_404(SubCategoryModel,id=subCategoryId)
    form = SubCategoryModelForm(request.POST or None,instance=oneSubCategory)
    if request.method=="POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('/admin/subcategory/')
    return render(request,'admin/subcategory/subCategoryCreate.html',{'title':'Update Category','form':form})

def subCategoryDelete(request,subCategoryId):
    obj=get_object_or_404(SubCategoryModel,id=subCategoryId)
    obj.delete()
    return redirect('/admin/subcategory/')

#brands
def brandView(request):
    allbrands = BrandModel.objects.all()
    return render(request,'admin/brand/brandView.html',{'title':'Brands','brands':allbrands})

def brandCreate(request):
    form = BrandModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid:
            obj = form.save(commit=False)
            obj.save()
            return redirect("/admin/brand/")
    return render(request,'admin/brand/brandCreate.html',{'title':'Create Sub Category','form':form})

def brandEdit(request,brandId):
    obj = get_object_or_404(BrandModel,id=brandId)
    form = BrandModelForm(request.POST or None,instance=obj)
    if request.method=="POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('/admin/brand/')
    return render(request,'admin/brand/brandCreate.html',{'title':'Update Category','form':form})

def brandDelete(request):
    if request.method=="POST":
        obj=get_object_or_404(BrandModel,id=request.POST['brandId'])
        obj.delete()
    return redirect('/admin/brand/')

#Suppliers
def suplierView(request):
    obj = SuplierModel.objects.all()
    return render(request,'admin/suplier/suplierView.html',{'title':'Supplier','supliers':obj})

def suplierCreate(request):
    form = SuplierModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid:
            obj = form.save(commit=False)
            obj.save()
            return redirect("/admin/suplier/")
    return render(request,'admin/suplier/suplierCreate.html',{'title':'Create Suplier','form':form})

def suplierEdit(request,suplierId):
    obj = get_object_or_404(SuplierModel,id=suplierId)
    form = SuplierModelForm(request.POST or None,instance=obj)
    if request.method=="POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('/admin/suplier/')
    return render(request,'admin/suplier/suplierCreate.html',{'title':'Update Suplier','form':form})

def suplierDelete(request):
    if request.method=="POST":
        obj=get_object_or_404(SuplierModel,id=request.POST['brandId'])
        obj.delete()
    return redirect('/admin/suplier/')

#products
def productView(request):
    return render(request,'admin/product/productView.html',{'title':'Products'})

def productCreate(request):
    form = ProductModelForm(request.POST,request.FILES)
    if request.method == "POST":
        startingPoint = 1000000000000
        endingpoint = 9999999999999
        barcodeCode = random.randint(startingPoint,endingpoint)
        print(barcodeCode)
        EAN= barcode.get_barcode_class('ean13')
        ean = EAN(''+str(barcodeCode))
        barcode_Path = 'static/images/barcode/'+str(barcodeCode)
        fn = ean.save(os.path.join(settings.BASE_DIR,barcode_Path))
        barcode_Path='images/barcode/'+str(barcodeCode)+".svg"
        if form.is_valid:
            form.instance.barcodeNumber = barcodeCode
            form.instance.barcodeImage = barcode_Path
            now = datetime.now()
            form.instance.created_at = now.strftime("%Y-%m-%d %H:%M:%S")
            form.instance.active = True
            obj = form.save(commit=False)
            obj.save()
            for f in  request.FILES.getlist('productImages'):
                im = ProductModelImages(product_id=obj.id,productImages=f)
                im.save()
        return redirect("/admin/product/")
    return render(request,'admin/product/productCreate.html',{'title':'Create Product','form':form})

def stockView(request,productId):
    return render(request,'admin/stock/stockView.html',{'title':"Stock"})
def stockCreate(request,productId):
    form = StockModelForm(request.POST or None)
    product_obj = get_object_or_404(ProductModel,id=productId)
    # print(product_obj.subCategory_id)
    subCategory_obj = get_object_or_404(SubCategoryModel,id=product_obj.subCategory_id)
    arr = subCategory_obj.subCategoryType.split(',')
    if request.method == "POST":
        for obj in request.POST.getlist('size'):
            smobj = StockModel(product=product_obj,color=request.POST['color'],size=obj,stock=request.POST[obj])
            print(smobj)
            smobj.save()
    return render(request,'admin/stock/stockCreate.html',{'title':'Create Stock','form':form,'checkbox':arr})
def cameraOpen(request):
    # camera=cv2.VideoCapture(0)
    # ret, frame = camera.read()
    # while ret:
    #     ret,frame = camera.read()
    #     cv2.imshow('Barcode reader', frame)
    #     if cv2.waitKey(1) & 0xFF == 27:
    #         break
    #     else :
    #         print("si kbr")
    # camera.release()
    # cv2.destroyAllWindows()
    image = cv2.imread('D:/django/project/static/images/barcode/2727434759915.svg')
    _, image_thr = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
    # Count non-zero pixels along the rows; get indices, where count exceeds certain threshold (here: 100)
    row_nz = np.count_nonzero(image_thr, axis=0)
    idx = np.argwhere(row_nz > 100)
    # Generate new image, draw lines at found indices
    image_new = int(np.ones_like(image_thr) * 255)
    image_new[35:175, idx] = 0
    cv2.imshow('image_thr', image_thr)
    cv2.imshow('image_new', image_new)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # print(os.path.join(settings.BASE_DIR,'static\images\barcode\\2727434759915.svg'))
    # img = cv2.imread('D:/django/project/static/images/barcode/2727434759915.svg')
    # detectedBarcodes =pyzbar.decode(img)
    # if not detectedBarcodes:
    #     print("Barcode Not Detected or your barcode is blank/corrupted!")
    # else:
    #       # Traveres through all the detected barcodes in image
    #     for barcode in detectedBarcodes:
    #         # Locate the barcode position in image
    #         (x, y, w, h) = barcode.rect
    #         # Put the rectangle in image using 
    #         # cv2 to heighlight the barcode
    #         cv2.rectangle(img, (x-10, y-10),
    #                       (x + w+10, y + h+10), 
    #                       (255, 0, 0), 2)
    #         if barcode.data!="":
    #         # Print the barcode data
    #             print(barcode.data)
    #             print(barcode.type)
    # #Display the image
    # cv2.imshow("Image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # decodeObjects=decode(img)
    # print(pixels)
    # for bar in decodeObjects:
    #     print(bar)
    # while True:
    #     _,frame = cap.read()
    return render(request,'admin/camera/open.html')