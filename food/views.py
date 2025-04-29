from django.shortcuts import render,redirect
from food.models import Contact, Items, ItemList, Booktable
from django.http import HttpResponse
from .forms import Booktableform

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
    
        obj= Contact(name=name, email=email, subject=subject, message=message)
        obj.save()
        # Here you can add code to send the message via email or save it to the database
        context ["message"]=f"Thank {name} for your message!"
    return render(request, 'contact.html', context)

def about(request):
    return render(request, 'about.html')



def menu(request):
    items = Items.objects.all()
    categories = ItemList.objects.all()
    
    return render(request, 'menu.html', {'items': items, 'categories': categories})

def feature(request):
    return render(request, 'feature.html')

def booking(request):
  forms=Booktableform()
  if request.method=='POST':
      print(request.POST)
  context={"form":forms}
  return render(request,'booking.html',context)