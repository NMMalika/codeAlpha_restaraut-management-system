from django.contrib import admin
from food.models import Contact
from django.contrib.auth.models import User
from django.db import models
# Register your models here.
admin.site.site_header = "FoodResturantAdmin"
admin.site.site_title = "FoodResturantAdmin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email","subject", "message", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "subject")
    ordering = ("-created_at",)

admin.site.register(Contact, ContactAdmin)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['-created_at']
  