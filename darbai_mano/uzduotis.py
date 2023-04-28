
from zoneinfo import available_timezones


amerikos_laiko_zonos = []

for tz in available_timezones():
    if 'America' in tz:
        amerikos_laiko_zonos.append(tz)

for laiko_zona in amerikos_laiko_zonos:
    print(laiko_zona)