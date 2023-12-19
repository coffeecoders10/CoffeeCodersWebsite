from django.shortcuts import render
from django.templatetags.static import static
import json
from django.conf import settings

def ccadmin(request):
    with open(settings.STATICFILES_DIRS[-1] + "/json/desc.json") as json_file:
        data = json.load(json_file)

    # print(data)
    # data = json.dumps(data, indent=4)

    if request.method == 'POST':
        form_key = request.POST['button']
        form_value = json.loads(request.POST[form_key].replace("\'", "\""))

        data[form_key] = form_value
        json_object = json.dumps(data, indent = 4)

        file_name = settings.STATICFILES_DIRS[-1] + "/json/desc.json"
        with open(file_name, "w") as outfile:
            outfile.write(json_object)
            
    for key, value in data.items():
        data[key] = json.dumps(data[key], indent=4)
    # print(data)
    return render(request,'index/admin.html', {'data': data})

def index(request):
    with open(settings.STATICFILES_DIRS[-1] + "/json/desc.json") as json_file:
        data = json.load(json_file)
    # print(data)

    # for i in data['live_projects']:
    #     i['img'] = static(i['img'])

    data['story']['image'] = static(data['story']['image'])

    for i in data['members']:
        i['img'] = static(i['img'])

    return render(request,'index/index.html',data)
