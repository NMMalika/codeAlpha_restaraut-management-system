from django.db import models
from django.utils import timezone

created_at = models.DateTimeField(default=timezone.now)





# Create your models here.
class ItemList(models.Model):
    category_name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, default="fa-solid fa-utensils")
    category_description = models.TextField(max_length=255, default="Default description")
    category_image = models.ImageField(upload_to='category_images/', default='default.jpg')
    
    def __str__(self):
        return self.category_name
    
class Items(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_description = models.TextField()
    item_image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(ItemList, related_name="Name", on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        
        
class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    
    def __str__(self):    
        return self.user_name
    
class Aboutus(models.Model):
    description = models.TextField()
    
    def __str__(self):
        return self.description[:50]
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        
class Booktable(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Booktable"
        verbose_name_plural = "Booktables"
        