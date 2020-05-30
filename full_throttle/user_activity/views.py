import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse

from user_activity.models import *

# Create your views here.
@csrf_exempt
def get_activity_periods_view(request):
    members = []
    response_json = {"ok": False, "members": members}

    all_activity_periods = ActivityPeriod.objects.all()
    for activity_period in all_activity_periods:
        
        user = activity_period.user
        members.append({'id': user.user_id, 'real_name': user.user_name, 
            "tz": activity_period.tz, 
            'activity_periods' : json.loads(activity_period.activity_period)})

    return HttpResponse(json.dumps(response_json), status=200, content_type='application/json; charset=utf8')

