# home/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

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
    return render(request, 'index.html')

# def logout_view(request):
#     logout(request)
#     return render(request, 'logout.html')
