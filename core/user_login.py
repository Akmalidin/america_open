from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .EmailBackEnd import EmailBackEnd
from apps.settings.models import UserProfile
from django.shortcuts import get_object_or_404
from apps.settings.models import Settings
from django.contrib.auth.decorators import login_required
def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        school = request.POST.get('school')
        profile_photo = request.FILES.get('profile_photo')
        place_learn = request.POST.get('place_learn')
        region = request.POST.get('region')
        city = request.POST.get('city')
        clas = request.POST.get('clas')
        birthday = request.POST.get('birthday')
        
    # check email
        if User.objects.filter(email=email).exists():
           messages.warning(request,'Данный Email уже существует !')
           return redirect('register')

        # check username
        if User.objects.filter(username=username).exists():
           messages.warning(request,'Имя пользователя уже существует ! Выберите другой.')
           return redirect('register')
        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user_profile = UserProfile(
            user=user,
            phone_number=phone_number,
            school=school,
            place_learn=place_learn,
            region=region,
            city=city,
            clas=clas,
            birthday=birthday,
        )
        user.set_password(password)
        user.save()
        user_profile.save()
        if profile_photo:
            user_profile.profile_photo.save(profile_photo.name, profile_photo)
        
        user_profile.user = user
        
        return redirect('login')
       
    return render(request, 'registration/register.html')
def DO_LOGIN(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
		
        user = EmailBackEnd.authenticate(request,
                                     username=email,
                                     password=password)
        if user!=None:
           login(request,user)
           return redirect('index')
        else:
           messages.error(request,'Email / пароль введены неверно !')
    return redirect('login')
    
@login_required
def PROFILE(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    settings = Settings.objects.latest("id")
    return render(request, 'registration/profile.html', locals())
@login_required
def PROFILE_UPDATE(request):
    if request.method == "POST":
        user = request.user
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        school = request.POST.get('school')
        profile_photo = request.FILES.get('profile_photo')
        place_learn = request.POST.get('place_learn')
        region = request.POST.get('region')
        city = request.POST.get('city')
        clas = request.POST.get('clas')
        birthday = request.POST.get('birthday')
        user_id = request.user.id
        user_profile, created = UserProfile.objects.get_or_create(user = user)
        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user_profile.phone_number = phone_number
        user_profile.school = school
        user_profile.profile_photo = profile_photo
        user_profile.place_learn = place_learn
        user_profile.region = region
        user_profile.city = city
        user_profile.clas = clas
        user_profile.birthday = birthday

        if password != None and password != "":
            user.set_password(password)
        if not created:
            user_profile.phone_number = phone_number
            user_profile.school = school
            user_profile.profile_photo = profile_photo
            user_profile.place_learn = place_learn
            user_profile.region = region
            user_profile.city = city
            user_profile.clas = clas
            user_profile.birthday = birthday
        user.save()
        user_profile.save()
        messages.success(request,'Профиль успешно обновлен. ')
        return redirect('view_profile')
@login_required
def VIEW_PROFILE(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    settings = Settings.objects.latest("id")
    return render(request, 'registration/view_profile.html', locals())