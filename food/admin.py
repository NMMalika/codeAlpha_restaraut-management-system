from django.contrib import admin
from food.models import Contact

# Register your models here.
admin.site.site_header = "FoodResturantAdmin"
admin.site.site_title = "FoodResturantAdmin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email","subject", "message", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "subject")
    ordering = ("-created_at",)

admin.site.register(Contact, ContactAdmin)
  