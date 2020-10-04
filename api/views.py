from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from .models import Hit

from django.template import loader
import datetime
# Create your views here.

def lyricsPage(request):
	template = loader.get_template('api/index.html')
	return HttpResponse(template.render({},request))

def index(request):
	return HttpResponse("Hello, World! You're AwSSome.hahha.")

def get(request):
	try:
		ret = Hit.objects.all()
		data = {}
		allItems = []
		for obj in ret:
			item = {}
			item['click'] = obj.times
			item['at'] = obj.at
			allItems.append(item)

		data['history'] = allItems

	except Exception as e:
		return JsonResponse({'status':'false', 'message':" {}".format(e)})

	return JsonResponse(data)

def save(request):
	try:

		now = datetime.datetime.now()
		index = Hit.objects.count()
		index = index+1

		hit = Hit()
		hit.times = index
		hit.at = now
		hit.save()

	except Exception as e:
		return JsonResponse({'status':'false', 'message':" {}".format(e)})

	return HttpResponse("Caught you!")
