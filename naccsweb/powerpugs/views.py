from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.utils import timezone

from .forms import PowerPugPlayerApp, PowerPugIGLApp
from .models import PowerPugsPlayerApplication, PowerPugsIGLApplication

def powerpugs(request):
    app = True
    try:
        applicant = PowerPugsPlayerApplication.objects.get(name=request.user.username)
    except:
        app = False
    return render(request, 'applications/powerpugs.html', {'app': app})

@login_required
def application(request):

    form = PowerPugPlayerApp(request.POST, request.FILES)
    try:
        user = User.objects.get(username=request.user.username)
    except:
        return redirect('not_found')
    
    try:
        application = PowerPugsPlayerApplication.objects.get(name = request.user.username)
        if application:
            player_app = application
    except:
        player_app = None

    

    if request.method == 'POST':
        if form.is_valid():
            success_message = "Your application has been successfully submitted. Accepted applicants will receive an acceptance email containing the following information: payment instructions; permittance into Power Pugs Season 3; and fully signed and finalized version of your STANDARD ESPORTS PLAYER CONTRACT within 48 hours."
            email = form.cleaned_data['email']
            college = form.cleaned_data['college']
            esea = form.cleaned_data['esea']
            faceit = form.cleaned_data['faceit']
            curr = form.cleaned_data['curr_team']
            igl = form.cleaned_data['igl']
            lan = form.cleaned_data['lan']
            other = form.cleaned_data['other']
            app = PowerPugsPlayerApplication()
            app.user = User.objects.get(username=request.user.username)
            app.name = request.user.username
            app.email = email
            app.college = college
            app.esea_link = esea
            app.igl = igl
            app.faceit_link = faceit
            app.curr_team = curr
            app.lan = lan
            app.other = other
            if request.FILES:
                app.application = request.FILES['contract']
            app.save()
            return render(request, 'applications/player_application.html', {'form': form, 'success': success_message})

    
    return render(request, 'applications/player_application.html', {'form': form, 'app': player_app})

def userAccepted(user):
    if user == False:
        return False
    else: 
        return True

@login_required
def iglapplication(request):
    form = PowerPugIGLApp(request.POST, request.FILES)
    try:
        applicant = PowerPugsPlayerApplication.objects.get(name=request.user.username)
    except:
        return redirect('power_pugs')
    
    if not userAccepted(applicant):
        return redirect('power_pugs')

    try:
        application = PowerPugsIGLApplication.objects.get(name = request.user.username)
        if application:
            player_app = application
    except:
        player_app = None

    if request.method == 'POST':
            if form.is_valid():
                success_message = "Your application has been successfully submitted. Accepted applicants will receive an acceptance email containing the following information: payment instructions; permittance into Power Pugs Season 3; and fully signed and finalized version of your STANDARD ESPORTS PLAYER CONTRACT within 48 hours."
                email = form.cleaned_data['email']
                esea = form.cleaned_data['esea']
                faceit = form.cleaned_data['faceit']
                curr = form.cleaned_data['curr_team']
                lan = form.cleaned_data['lan']
                other = form.cleaned_data['other']
                app = PowerPugsIGLApplication()
                app.user = User.objects.get(username=request.user.username)
                app.name = request.user.username
                app.email = email
                app.esea_link = esea
                app.faceit_link = faceit
                app.curr_team = curr
                app.lan = lan
                app.other = other
                print(app)
                if request.FILES:
                    app.application = request.FILES['contract']
                app.save()
                return render(request, 'applications/player_application.html', {'form': form, 'success': success_message})
    
    return render(request, 'applications/igl_application.html', {'form': form, 'app': player_app})