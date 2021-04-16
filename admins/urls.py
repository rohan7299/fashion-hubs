from django.urls import path,include
from .views import dashboard,profile,categoryView,categoryCreate,categoryEdit,categoryDelete
from .views import subCategoryView,subCategoryCreate,subCategoryEdit,subCategoryDelete
from .views import brandView,brandCreate,brandEdit,brandDelete
from .views import suplierView,suplierCreate,suplierEdit,suplierDelete
from .views import productView,productCreate
from .views import stockView,stockCreate,cameraOpen
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('',login),
    path('dashboard/',dashboard),
    path('profile/',profile),

    path('category/',categoryView),
    path('category/create/',categoryCreate),
    path('category/<int:categoryId>/edit/',categoryEdit),
    path('category/<int:categoryId>/delete/',categoryDelete),

    path('subcategory/',subCategoryView),
    path('subcategory/create/',subCategoryCreate),
    path('subcategory/<int:subCategoryId>/edit/',subCategoryEdit),
    path('subcategory/<int:subCategoryId>/delete/',subCategoryDelete),

    path('brand/',brandView),
    path('brand/create/',brandCreate),
    path('brand/<int:brandId>/edit/',brandEdit),
    path('brand/delete/',brandDelete),

    path('suplier/',suplierView),
    path('suplier/create/',suplierCreate),
    path('suplier/<int:suplierId>/edit/',suplierEdit),
    path('suplier/delete/',suplierDelete),

    path('product/',productView),
    path('product/create/',productCreate),

    path('product/<int:productId>/stock/',stockView),
    path('product/<int:productId>/stock/create/',stockCreate),

    path('camera/',cameraOpen),
] + static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)