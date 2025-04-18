from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        object = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        # Here you can add code to send the message via email or save it to the database
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')