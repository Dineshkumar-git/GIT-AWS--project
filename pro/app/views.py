from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ContactSerializer

# Api views ---------

@api_view(['GET'])
def apioverview(request):
    api_urls = {
    'list' : '/list/',
    'detail view' : '/detail/',
    'create' : '/create/',
    'update' : '/update/',
    'delete' : '/delete/',
    }
    return Response(api_urls)

@api_view(['GET'])
def list(request):
    tasks = Contact.objects.all()
    serializer = ContactSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    tasks = Contact.objects.get(id=pk)
    serializers  = ContactSerializer(tasks, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def create(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def update(request, pk):
    tasks = Contact.objects.get(id=pk)
    serializer = ContactSerializer(instance=tasks, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return JsonResponse(serializer.data)

@api_view(['DELETE'])
def delete(request, pk):
    tasks = Contact.objects.get(id=pk)
    tasks.delete()

    return Response(f'Item {pk} got deleted')




# Create your views here.

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent!')
    return render(request, 'contact.html')

def display_contact(request):
    data = Contact.objects.all()

    stu = {
        "student_number": data
    }
    return render(request, "display.html", stu)

def services(request):
    return render(request, 'services.html')
