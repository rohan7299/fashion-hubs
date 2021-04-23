from admins .models import CategoryModel,SubCategoryModel
def categories_processor(request):
    categories = CategoryModel.objects.all()
    subcategories = SubCategoryModel.objects.all()
    return {'categories': categories,'subcategories':subcategories}