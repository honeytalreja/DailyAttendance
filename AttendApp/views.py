import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
    admin = False
    if request.user.is_superuser:
        admin = True

    title = Home.objects.get(key='title').data
    info = Home.objects.get(key='info').data
    sites = Site.objects.all()
    zones = Zone.objects.all()
    shifts = Shift.objects.all()
    args = {
        'title': title,
        'info': info,
        'zones': zones,
        'sites': sites,
        'shifts': shifts,
        'admin': admin,
    }
    return render(request, 'home/index.html', args)


def user_login(request):
    if request.method == 'GET':
        args = {
            'title': Home.objects.get(key='title').data,
            'errors': '',
        }
        return render(request, 'home/login.html', args)
    else:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            if user.is_superuser:
                login(request, user)

                title = Home.objects.get(key='title').data
                info = Home.objects.get(key='info').data
                sites = Site.objects.all()
                zones = Zone.objects.all()
                shifts = Shift.objects.all()
                args = {
                    'title': title,
                    'info': info,
                    'zones': zones,
                    'sites': sites,
                    'shifts': shifts,
                    'admin': True,
                }
                return redirect('/', args)
            else:
                args = {
                    'title': Home.objects.get(key='title').data,
                    'errors': 'Not enough permissions',
                }
                return render(request, 'home/login.html', args)
        else:
            args = {
                'title': Home.objects.get(key='title').data,
                'errors': 'Invalid Credentials',
            }
            return render(request, 'home/login.html', args)


def user_logout(request):
    logout(request)
    title = Home.objects.get(key='title').data
    info = Home.objects.get(key='info').data
    sites = Site.objects.all()
    zones = Zone.objects.all()
    shifts = Shift.objects.all()
    args = {
        'title': title,
        'info': info,
        'zones': zones,
        'sites': sites,
        'shifts': shifts,
        'admin': False,
    }
    return redirect('/', args)


def mark_attendance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        zone = Zone.objects.get(pk=request.POST.get('zone'))
        site = Site.objects.get(pk=request.POST.get('site'))
        shift = Shift.objects.get(pk=request.POST.get('shift'))
        print(name)
        print(zone)
        print(site)
        print(shift.in_time)
        print(shift.out_time)
        attendance_record = AttendanceRecord(employee_name=name,
                                             zone=zone,
                                             site=site,
                                             zonal_manager=zone.manager,
                                             shift=shift,
                                             timestamp=datetime.datetime.now())
        attendance_record.save()
        return None


@user_passes_test(lambda u: u.is_superuser)
def admin_data(request):
    if request.method == "GET":
        return render(request, 'home/data.html')
    else:
        date = request.POST.get("datepicker")
        if date == "":
            return render(request, 'home/data.html', {"error": "Please select a valid date !!"})
        date_split = date.split("-")
        data = AttendanceRecord.objects.all().filter(timestamp__year=date_split[0]) \
            .filter(timestamp__month=date_split[1]).filter(timestamp__day=date_split[2])
        return render(request, 'home/data.html', {"data": data})
