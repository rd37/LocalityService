#!/usr/local/bin/python

import client.location_client_api as api
print "Starting Locality API Testing"

print "----------"
print "Create API instance"
api_inst = api.locationapi('client/testing/scripts/location_service_cfg.yaml')

print "Insert new Entry into the Locality Service lat,lng,height"
id = api_inst.insert(-48.9,142.3,99)
print "Entry identifier (id) returned is %s"%id

print "----------"
print "Now Update Objects Location id,lat,lng,height"
result = api_inst.update(id,47.9,141.2,55)
print "Update was %s"%result

print "----------"
print "Now Search the Service lat,lng,height,lat_range,lng_range,height_range"
points = api_inst.search(47.0,141.0,50,1,1,10)
print "Found Points %s"%points


print "----------"
print "Now Remove id %s"%id
result = api_inst.delete(id)
print "Remove was %s"%result
