from . import models

def get_categories(request):
    category = models.Category.objects.all()
    # print(categories)
    return dict(category=category)