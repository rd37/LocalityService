'''
Created on Jun 21, 2014

@author: ronaldjosephdesmarais
'''
import json


    
#'{"request":"add_billboard","name":"RONS_test_bb","lat":-142.1111,"lng":48.7777}'
def createInsert(lat,lng,height):
    return '{"lat":%s,"lng":%s,"height":%s}'%(lat,lng,height)

def createDelete(id):
    return '{"id":%s}'%(id)

def createUpdate(id,lat,lng,height):
    return '{"id":%s,"lat":%s,"lng":%s,"height":%s}'%(id,lat,lng,height)

def createSearch(lat,lng,height,lat_rng,lng_rng,height_rng):
    return '{"lat":%s,"lng":%s,"height":%s,"lat_rng":%s,"lng_rng":%s,"height_rng":%s}'%(lat,lng,height,lat_rng,lng_rng,height_rng)