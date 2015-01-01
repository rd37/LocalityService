'''
Created on Dec 6, 2014

@author: ronaldjosephdesmarais
'''
import JSONFactory as jfac
import requests,json,yaml
from httplib2 import Http
from urllib import urlencode
import urllib2,urllib,json

class locationapi(object):
    service_url='http://127.0.0.1:8000/locality'
    
    def __init__(self,cfgfile):
        #readin yaml conf file and and set location of the location service
        cfg_f = yaml.load( open(cfgfile,'r') )
        self.service_url = cfg_f['location-service-url']
        
        
    #returns the object identifier created for the insert
    def insert(self,lat,lng,height,name):
        json_msg = jfac.createInsert(lat,lng,height,name) 
        resp = requests.get("%s/insert/?jsonMsg=%s&sid=90908978"%(self.service_url,json_msg))
        json_obj = json.loads('%s'%resp.content)
        return json_obj['id']
        
    def delete(self,ids):
        json_msg = jfac.createDelete(ids)  
        resp = requests.get("%s/delete/?jsonMsg=%s&sid=90908978"%(self.service_url,json_msg))
        json_obj = json.loads('%s'%resp.content)
        if json_obj['Error']:
            return False
        else:
            return True
        
    def update(self,ids,lat,lng,height,name):
        json_msg = jfac.createUpdate(ids,lat,lng,height,name)   
        resp = requests.get("%s/update/?jsonMsg=%s&sid=90908978"%(self.service_url,json_msg))
        json_obj = json.loads('%s'%resp.content)
        if json_obj['Error']:
            return False
        else:
            return True
        
    #returns a json object
    def search(self,lat=None,lng=None,height=None,lat_rng=None,lng_rng=None,height_rng=None,name=None):
        json_msg = jfac.createSearch(lat,lng,height,lat_rng,lng_rng,height_rng,name)  
        resp = requests.get("%s/search/?jsonMsg=%s&sid=90908978"%(self.service_url,json_msg))
        json_obj = json.loads('%s'%resp.content)
        if 'Error' in json_obj:
            return None
        else:
            return json_obj
        return str(json_obj)
    
    def get(self,ids):
        json_msg = jfac.createGet(ids)   
        resp = requests.get("%s/get/?jsonMsg=%s&sid=90908978"%(self.service_url,json_msg))
        print "Get::%s"%resp.content
        json_obj = json.loads('%s'%resp.content)
        if json_obj['Error']:
            return None
        else:
            return json_obj['info']