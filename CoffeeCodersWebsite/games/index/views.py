from django.shortcuts import render
from django.templatetags.static import static
import json
from django.conf import settings

def index(request):
    with open(settings.STATICFILES_DIRS[3] + "/json/desc.json") as json_file:
        data = json.load(json_file)
    print(data)
    for i in data['live_projects']:
        i['img'] = static(i['img'])
    data['story']['image'] = static(data['story']['image'])
    for i in data['members']:
        i['img'] = static(i['img'])
    return render(request,'index/index.html',data)
