from django.contrib import admin
from food.models import Contact

# Register your models here.
admin.site.site_header = "FoodResturantAdmin"
admin.site.site_title = "FoodResturantAdmin"

admin.site.register(Contact)
