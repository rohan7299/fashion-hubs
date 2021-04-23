from django.db import models
from django import forms
# Create your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
import random
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

class CategoryModel(models.Model):
    categoryName = models.CharField(max_length=30)
    class Meta:
        db_table="categories"
    def edit(self):
        return f'{self.id}/edit/'
    def deleteURL(self):
        return f'{self.id}/delete/'
    def __str__(self):
        return self.categoryName
class CategoryFormModel(forms.ModelForm):
    categoryName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = CategoryModel
        fields = '__all__'

class SubCategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel,default=None,on_delete=models.CASCADE)
    subCategoryName = models.CharField(max_length=50)
    subCategoryType = models.CharField(max_length=200,default=None)
    class Meta:
        db_table="subcategories"
    def edit(self):
        return f'{self.id}/edit/'
    def deleteURL(self):
        return f'{self.id}/delete/'
    def __str__(self):
        return self.subCategoryName
class SubCategoryModelForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=CategoryModel.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    subCategoryName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    subCategoryType = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = SubCategoryModel
        fields = '__all__'

class BrandModel(models.Model):
    brandName = models.CharField(max_length=30)
    class Meta:
        db_table="brands"
    def edit(self):
        return f'{self.id}/edit/'
    def deleteURL(self):
        return f'delete/'
    def __str__(self):
        return self.brandName
class BrandModelForm(forms.ModelForm):
    brandName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = BrandModel
        fields = '__all__'

class SuplierModel(models.Model):
    suplierName = models.CharField(max_length=100)
    suplierContact = models.BigIntegerField()
    suplierAddress = models.TextField()
    class Meta:
        db_table="supliers"
    def edit(self):
        return f'{self.id}/edit/'
    def __str__(self):
        return self.suplierName
class SuplierModelForm(forms.ModelForm):
    suplierName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    suplierContact = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    suplierAddress = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = SuplierModel
        fields = '__all__'

def uploadFile(instance,filename):
    print(filename)

class ProductModel(models.Model):
    subCategory =  models.ForeignKey(SubCategoryModel,default=None,on_delete=models.CASCADE)
    productName = models.CharField(max_length=300)
    productDescription = models.TextField()
    suplier =  models.ForeignKey(SuplierModel,default=None,on_delete=models.CASCADE)
    barcodeNumber = models.BigIntegerField(default=None,null=True)
    barcodeImage = models.CharField(max_length=200,default=None,null=True)
    wholesalePrice = models.IntegerField()
    salesPrice = models.IntegerField()
    brand =  models.ForeignKey(BrandModel,default=None,on_delete=models.CASCADE)
    created_at = models.CharField(max_length=30)
    active = models.BooleanField()
    class Meta:
        db_table="products"
    def edit(self):
        return f'{self.id}/edit/'
    def stock(self):
        return f'{self.id}/stock/'
    def __str__(self):
        return self.productName
class ProductModelImages(models.Model):
    productImages = models.FileField(max_length=2000,upload_to="images/products/%Y%m",null=True,blank=True,default='')
    product =  models.ForeignKey(ProductModel,default=None,on_delete=models.CASCADE)
    class Meta:
        db_table="productImages"
class ProductModelForm(forms.ModelForm):
    subCategory =  forms.ModelChoiceField(queryset=SubCategoryModel.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    productName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    productDescription = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    productImages = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'class':'form-control'}),required=False)
    suplier = forms.ModelChoiceField(queryset=SuplierModel.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    wholesalePrice = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    salesPrice = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    brand = forms.ModelChoiceField(queryset=BrandModel.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = ProductModel
        fields = '__all__'
        exclude = ['barcodeNumber','barcodeImage','created_at','active']

#stock
class StockModel(models.Model):
    product = models.ForeignKey(ProductModel,default=None,on_delete=models.RESTRICT)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=10)
    stock = models.IntegerField()
    class Meta:
        db_table="stocks"
    def edit(self):
        return f'{self.id}/edit'
class StockModelForm(forms.ModelForm):
    product =  forms.ModelChoiceField(queryset=ProductModel.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    color = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    size = forms.MultipleChoiceField(widget = forms.TextInput(attrs={'class':'form-control'}))
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = StockModel
        fields= '__all__'