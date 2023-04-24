from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones
from pprint import pprint

america_time_zones = []

for tz in available_timezones():
    if 'America' in tz:
        america_time_zones.append(tz)

for time_zone in america_time_zones:
    print(time_zone)