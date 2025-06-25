from django.shortcuts import render,redirect , Http404
from .models import User, Teacher,Student
from .forms import Teacher_user, Teacher_profile, Student_user, Student_profile, Teacher_loing_Form, Student_loing_Form
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'home.html')

def Teacher_register(request):
    tuf= Teacher_user(request.POST or None)
    tup = Teacher_profile(request.POST or None)
    if tuf.is_valid() or tup.is_valid():
        new_tuser = tuf.save(commit=False)
        new_tuser.set_password(tuf.cleaned_data['password'])
        new_tuser.is_teacher = True
        new_tuser.save()
        instance = tup.save(commit=False)
        instance.tu = new_tuser
        instance.save()
        return redirect('home')
    return render(request, 'teacher_register.html', {'tuf':tuf, 'tup':tup})

def Student_register(request):
    suf= Student_user(request.POST or None)
    sup = Student_profile(request.POST or None)
    if suf.is_valid() or sup.is_valid():
        new_suser = suf.save(commit=False)
        new_suser.set_password(suf.cleaned_data['password'])
        new_suser.is_student = True
        new_suser.save()
        instance = sup.save(commit=False)
        instance.su = new_suser
        instance.save()
        return redirect('home')
    return render(request, 'student_register.html', {'suf':suf, 'sup':sup})

def Teacher_loing(request):
    l_form = Teacher_loing_Form(request.POST or None)
    if l_form.is_valid():
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user.is_active and user.is_teacher:
            login(request, user)
            return redirect('Teacher_details')

    context = {
        "l_form": l_form,
    }
    return render(request, 'teacher_login.html', context)

def Teacher_details(request):
    if request.user.is_authenticated and request.user.is_teacher:
        return render(request, 'teacher_details.html')
    else:
        raise Http404

def Teacher_logout(request):
    logout(request)
    return redirect('home')

def Student_loing(request):
    s_form = Student_loing_Form(request.POST or None)
    if s_form.is_valid():
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user.is_active and user.is_student:
            login(request, user)
            return redirect('Student_details')

    context = {
        "s_form": s_form,
    }
    return render(request, 'student_login.html', context)

def Student_details(request):
    if request.user.is_authenticated and request.user.is_student:
        return render(request, 'student_details.html')
    else:
        raise Http404

def Student_logout(request):
    logout(request)
    return redirect('home')