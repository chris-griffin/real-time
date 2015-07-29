from PIL import Image, ImageFont, ImageDraw
from google.transit import gtfs_realtime_pb2
import nyct_subway_pb2
import urllib
import datetime
from time import sleep
import math
import os
from config import *
import traceback

times = []
out = ''

while True:
	try:
		mtafeed = gtfs_realtime_pb2.FeedMessage()
		response = urllib.urlopen('http://datamine.mta.info/mta_esi.php?key=' + MTA_KEY + '&feed_id=1')
		mtafeed.ParseFromString(response.read())
		current_time = datetime.datetime.now()
		for stop in STOP_IDS:
			for entity in mtafeed.entity:
			                if entity.trip_update:
			                    for update in entity.trip_update.stop_time_update:
			                        if update.stop_id == stop:
							time = update.arrival.time
							if time <= 0:
								time = update.departure.time
							time = datetime.datetime.fromtimestamp(time)
							time = math.trunc(((time - current_time).total_seconds()) / 60)
							times.append(time)
			times.sort()
			for time in times:
				if time < 0:
					times.remove(time)
			for time in times[:NUM_TRAINS]:
				out+=str(time)
				out+=str(',')
			out = out[:-1]
			
			staticimg = Image.open('staticimages/' + stop[0] + stop[3] + '.ppm')
			draw = ImageDraw.Draw(staticimg)
			font = ImageFont.truetype('/usr/share/fonts/truetype/droid/DroidSans.ttf', 12)
			draw.text((16, 1), out,(200,200,200),font=font)
			staticimg.save('dynamicimages/dynamictime.ppm')
			times = []
			out = ''
		
			os.system('sudo ./rpi-rgb-led-matrix/led-matrix -r 16 -c 2 -t 5 -b 50 -D 1 -m 5000 dynamicimages/dynamictime.ppm')
	except Exception:
		print traceback.format_exc()



	




