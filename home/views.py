# home/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, TestimonialForm
from .models import Room, Testimonial
from django.db.models import Q

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect logged-in users to the homepage

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def homepage(request):
    room_type = request.GET.get('room_type')
    if room_type:
        featured_rooms = Room.objects.filter(room_type=room_type)
    else:
        featured_rooms = Room.objects.all()

    testimonials = Testimonial.objects.all()
    form = TestimonialForm()

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'index.html', {
        'featured_rooms': featured_rooms,
        'testimonials': testimonials,
        'form': form,
        'selected_type': room_type
    })

def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("home") 
    else:
        form = RegisterForm()

    return render(request, "signup.html", {"form": form})