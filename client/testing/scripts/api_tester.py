#!/usr/local/bin/python

import client.location_client_api as api
print "Starting Locality API Testing"

print "----------"
print "Create API instance"
api_inst = api.locationapi('client/testing/scripts/location_service_cfg.yaml')

print "Insert new Entry into the Locality Service lat,lng,height"
ids = api_inst.insert(-48.9,142.3,99,'RigiLab')
print "Entry identifier (ids) returned is %s"%ids

print "----------"
print "Now Update Objects Location ids,lat,lng,height"
result = api_inst.update(ids,47.9,141.2,55,'RigiLab2')
print "Update was %s"%result

print "----------"
print "Now Search the Service lat,lng,height,lat_range,lng_range,height_range"
points = api_inst.search(lat=47.0,lng=141.0,height=50,lat_rng=1,lng_rng=1,height_rng=10)
print "Found Points %s"%points

print "----------"
print "Now Search the Service using Name"
points = api_inst.search(name='RigiLab2')
print "Found Points %s"%points

print "----------"
print "Now Get id info %s"%ids
result1 = api_inst.get(ids)
print "Info was %s"%result1

print "----------"
print "Now Remove ids %s"%ids
result = api_inst.delete(ids)
print "Remove was %s"%result




