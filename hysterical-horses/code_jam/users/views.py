from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .forms import AccountCreationForm


@login_required()
def profile(request):
    context = {"user_form": None, "profile_form": None}
    return render(request, "users/profile.html", context)


def signup_view(request):
    form = AccountCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)  # Immediately log the user in
        return redirect('dashboard-index')

    context = {'form': form}
    return render(request, 'users/signup.html', context)

# def login_user


def profile_view(request):
    context = {'user': None}

    return render(request, "users/profile.html", context)
