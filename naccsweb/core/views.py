from django.shortcuts import render
from .models import HubStats
import os
import requests
from .faceit import get_hub_size
from django.conf import settings
import mimetypes
from django.conf import settings
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
    player = get_hub_size()
    num_matches = HubStats.objects.get(id=1)
    return render(request, 'core/index.html', {'main': True, 'player_count': player, 'num_matches': num_matches.matches})

def riot(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "riot.txt")
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404