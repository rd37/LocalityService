from django.shortcuts import render

# Create your views here.
from django.shortcuts import RequestContext, loader, render
from django.template import loader

from locality3d.models import location

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):
    print "3DLocality::Index"
    jsonMsg = request.GET['jsonMsg']
    json_req = json.loads(jsonMsg)
    return HttpResponse("Index::3D Locality Service")
    
    
@csrf_exempt
def insert(request):
    print "Try Insert"
    jsonMsg = request.GET['jsonMsg']
    print "Got Message %s"%jsonMsg
    json_req = json.loads(jsonMsg)
    #print "Got message %s"%json_req
    loc_obj = location(lat=json_req['lat'],lng=json_req['lng'],name=json_req['name'],height=json_req['height'])
    loc_obj.save()
    #print "done insert save"
    return HttpResponse('{"id":%s,"lat":%s,"lng":%s,"name":"%s","height":%s}'%(str(loc_obj.pk),json_req['lat'],json_req['lng'],json_req['name'],json_req['height'] ))

@csrf_exempt
def delete(request):
    print "3DLocality::Delete"
    jsonMsg = request.GET['jsonMsg']
    json_req = json.loads(jsonMsg)
    print "Find Location Object id %s"%(json_req['id'])
    loc_obj = location.objects.filter(pk=json_req['id'])
    
    if len(loc_obj) == 0:
        return HttpResponse('{"Error":true,"Message":"Id %s not Found"}'%json_req['id'])
    else:
        loc_obj[0].delete()
        return HttpResponse('{"Error":false,"Message":"Id %s Found"}'%json_req['id'])

@csrf_exempt
def get(request):
    print "3DLocality::Get"
    jsonMsg = request.GET['jsonMsg']
    json_req = json.loads(jsonMsg)
    print "Find Location Object id %s"%(json_req['id'])
    loc_obj = location.objects.filter(pk=json_req['id'])
    
    if len(loc_obj) == 0:
        return HttpResponse('{"Error":true,"Message":"Id %s not Found"}'%json_req['id'])
    else:
        return HttpResponse('{"Error":false,"info": {"lat":%s,"lng":%s,"height":%s,"name":"%s"} }'%(loc_obj[0].lat,loc_obj[0].lng,loc_obj[0].height,loc_obj[0].name))

@csrf_exempt
def update(request):
    print "3DLocality::Update"
    jsonMsg = request.GET['jsonMsg']
    json_req = json.loads(jsonMsg)
    print "Find Location Object id %s"%(json_req['id'])
    loc_obj = location.objects.filter(pk=json_req['id'])
    
    if len(loc_obj) == 0:
        return HttpResponse('{"Error":true,"Message":"Id %s Found"}'%json_req['id'])
    else:
        if 'lat' in json_req:
            loc_obj[0].lat = json_req['lat']
        if 'lng' in json_req:
            loc_obj[0].lng = json_req['lng']
        if 'name' in json_req:
            loc_obj[0].name = json_req['name']
        if 'height' in json_req:
            loc_obj[0].height = json_req['height']
        loc_obj[0].save()
        return HttpResponse('{"Error":false,"Message":"Id %s Found"}'%json_req['id'])
    
@csrf_exempt
def search(request):
    print "3DLocality::Search"
    jsonMsg = request.GET['jsonMsg']
    json_req = json.loads(jsonMsg)
    if 'lat' in json_req and 'lng' in json_req and 'lat_rng' in json_req and 'lng_rng' in json_req and 'height' in json_req and 'height_rng' in json_req:
        sLat = json_req['lat']
        sLatRng = json_req['lat_rng']
        sLng = json_req['lng']
        sLngRng = json_req['lng_rng']
        sHeight = json_req['height']
        sHeightRng = json_req['height_rng']
        search_objs = location.objects.filter(lat__gt=(sLat-sLatRng),lat__lt=(sLat+sLatRng),lng__gt=(sLng-sLngRng),lng__lt=(sLng+sLngRng),height__gt=(sHeight-sHeightRng),height__lt=(sHeight+sHeightRng)).values('pk','lat','lng','height','name')
        location_context = RequestContext(request, {'objects': search_objs } )
        template = loader.get_template('LocalityService/jsons/location_search_results.json')
        return HttpResponse( template.render(location_context) )
    elif 'name' in json_req :
        name = json_req['name']
        search_objs = location.objects.filter(name=name)
        location_context = RequestContext(request, {'objects': search_objs } )
        template = loader.get_template('LocalityService/jsons/location_search_results.json')
        return HttpResponse( template.render(location_context) )
    else:
        return HttpResponse('{"Error":true,"Message":"Please Check your Parameters"}')
    
