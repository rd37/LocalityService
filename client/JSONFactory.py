'''
Created on Jun 21, 2014

@author: ronaldjosephdesmarais
'''
import json


    
#'{"request":"add_billboard","name":"RONS_test_bb","lat":-142.1111,"lng":48.7777}'
def createInsert(lat,lng,height,name):
    return '{"lat":%s,"lng":%s,"height":%s,"name":"%s"}'%(lat,lng,height,name)

def createDelete(ids):
    return '{"id":%s}'%(ids)

def createGet(ids):
    return '{"id":%s}'%(ids)

def createUpdate(ids,lat,lng,height,name):
    return '{"id":%s,"lat":%s,"lng":%s,"height":%s,"name":"%s"}'%(ids,lat,lng,height,name)

def createSearch(lat=None,lng=None,height=None,lat_rng=None,lng_rng=None,height_rng=None,name=None):
    if name is None:
        return '{"lat":%s,"lng":%s,"height":%s,"lat_rng":%s,"lng_rng":%s,"height_rng":%s}'%(lat,lng,height,lat_rng,lng_rng,height_rng)
    else:
        return '{"name":"%s"}'%name