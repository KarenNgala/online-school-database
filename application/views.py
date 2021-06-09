from application.forms import *
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    user_profile = Profile.objects.get(user=current_user.id)
    course = Course.objects.get(name=user_profile.course)
    uni = University.objects.get(name=user_profile.uni)

    allUnits =  Unit.objects.filter(course=course.id, uni=uni.id)

    context = {
        'allUnits':allUnits
    }

    if request.method == 'GET':
        if 'unit' in request.GET:
            unit_id = request.GET.get('unit')
            files = File.objects.filter(unit=int(unit_id)).all()
            return render(request, 'pages/results.html', {'files':files})

    return render(request, 'index.html', context)


@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    user_profile = Profile.objects.get(user=current_user.id)
    course = Course.objects.get(name=user_profile.course)
    uni = University.objects.get(name=user_profile.uni)

    uploaded_files = File.objects.filter(uploaded_by=current_user.id).all()
    info = Profile.objects.get(user=current_user.id)
    all_files = File.objects.all()
    
    units =  Unit.objects.filter(course=course.id, uni=uni.id)
    context = {
        'units': units,
        'uploaded_files':uploaded_files,
        'info':info,
        'current_user':current_user
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        chosen_unit = request.POST.get('unit')
        file = request.POST.get('file')
        unit = Unit.objects.get(id=chosen_unit)
        upload = File(name=name, unit=unit, file=file)
        upload.uploaded_by = user
        upload.save()
        return redirect('profile')
    else:
        return render(request, 'pages/upload.html', context)


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    uploaded_files = File.objects.filter(uploaded_by=current_user.id).all()

    info = Profile.objects.get(user=current_user.id)

    context = {
        'uploaded_files':uploaded_files,
        'info':info,
        'current_user':current_user
    }
    return render(request, 'pages/profile.html', context)


@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user = request.user
    user = User.objects.get(id = current_user.id)
    user_profile = Profile.objects.get(user=current_user.id)

    allUnis =  University.objects.all()
    allCourses =  Course.objects.all()
    allYears =  Year_Of_Study.objects.all()

    context = {
        'allUnis':allUnis,
        'allCourses': allCourses,
        'allYears':allYears
    }

    if request.method == 'POST':
        selected_uni = request.POST.get('uni')
        selected_course = request.POST.get('course')
        selected_year = request.POST.get('year')
        uni = University.objects.get(id=selected_uni)
        course = Course.objects.get(id=selected_course)
        year = Year_Of_Study.objects.get(id=selected_year)

        profile = Profile(uni=uni, course=course, year=year)
        profile.id = user_profile.id
        profile.user = user
        profile.save()
        return redirect('profile')
    else:
        return render(request, 'pages/profile_edit.html', context)



@login_required(login_url='/accounts/login/')
def create_unit(request):
    current_user = request.user
    user_profile = Profile.objects.get(user=current_user.id)
    course = Course.objects.get(name=user_profile.course)
    uni = University.objects.get(name=user_profile.uni)
    year = Year_Of_Study.objects.get(name=user_profile.year)

    if request.method == 'POST':
        name = request.POST.get('name')
        new_unit = Unit(name=name)
        new_unit.course = course
        new_unit.uni = uni
        new_unit.year = year
        new_unit.save()
        return redirect('home')
    else:
        return render(request, 'pages/create_unit.html')