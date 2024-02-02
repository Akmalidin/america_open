from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from admin_soft.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.

# Pages
def index(request):
  today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
  today_users_count = User.objects.filter(last_login__gte=today_start).count()
  new_clients_count = User.objects.filter(date_joined__gte=today_start).count()
  total_users_count = User.objects.all().count()
  return render(request, 'pages/index.html', locals())

def billing(request):
  return render(request, 'pages/billing.html', { 'segment': 'billing' })

def tables(request):
  return render(request, 'pages/tables.html', { 'segment': 'tables' })

def vr(request):
  return render(request, 'pages/virtual-reality.html', { 'segment': 'vr' })

def rtl(request):
  return render(request, 'pages/rtl.html', { 'segment': 'rtl' })

def profile(request):
  return render(request, 'pages/profile.html', { 'segment': 'profile' })


# Authentication
class UserLoginView(LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Register failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/register.html', context)

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')

class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm