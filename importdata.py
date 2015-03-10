from google.transit import gtfs_realtime_pb2
import nyct_subway_pb2
import urllib
import datetime
import math
import os
import config

times = []
out = ''
	
mtafeed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('http://datamine.mta.info/mta_esi.php?key=' + mtakey + '&feed_id=1')
mtafeed.ParseFromString(response.read())
current_time = datetime.datetime.now()
for entity in mtafeed.entity:
                if entity.trip_update:
                    for update in entity.trip_update.stop_time_update:
                        if update.stop_id == stopid:
				time = update.arrival.time
				if time == 0:
					time = update.departure.time
				time = datetime.datetime.fromtimestamp(time)
				time = math.trunc(((time - current_time).total_seconds()) / 60)
				times.append(time)
times.sort()
for time in times[:num_trains]:
	out+=str(time)
	if num_trains > 1:
		out+=str(', ')
		num_trains = num_trains - 1
print out






