from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # save data in database in form model
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'{username}, Your account has been created, now you can Add Projec!')
            return redirect('budget-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})