import json
from unittest.util import sorted_list_difference
import pytz
from datetime import datetime
import calendar
zone = pytz.timezone('US/Central')


f = open('bigData.json', 'r')
data = json.load(f)
f.close()
data = [y for sub in [data.get(x) for x in data] for y in sub]


def sortData(data, subject=None, courseNum=None, courseTitle=None, building=None, room=None, current=False, today=False, beginTime=None, endTime=None, days=None, openSeats=False, teacher=None, teacherEmail=None):
    sorted = data
    if current:
        sortedTemp = []
        dayDict = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2,
                   'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
        dayClas = [0, 0, 0, 0, 0, 0, 0]
        time = int(datetime.now(zone).strftime("%H%M"))
        day = calendar.day_name[datetime.now(zone).weekday()]

        for j in sorted:
            if j['beginTime'] != None and j['endTime'] != None:
                if list(j['days'])[dayDict[day]] and int(j['beginTime']) <= time and int(j['endTime']) >= time:
                    sortedTemp.append(j)
        sorted = sortedTemp
    if subject != None:
        sortedTemp = [x for x in sorted if x['subject'] == subject]
        sorted = sortedTemp
    if courseNum != None:
        sortedTemp = [x for x in sorted if x['courseNum'] == courseNum]
        sorted = sortedTemp
    if building != None:
        sortedTemp = [x for x in sorted if x['building'] == building]
        sorted = sortedTemp
    if room != None:
        sortedTemp = [x for x in sorted if x['room'] == room]
        sorted = sortedTemp
    if teacher != None:
        sortedTemp = [x for x in sorted if teacher in x['teacher']]
        sorted = sortedTemp
    if openSeats:
        sortedTemp = [x for x in sorted if x['seats'] > 0]
        sorted = sortedTemp
    if beginTime != None and endTime != None:
        sortedTemp = []
        for j in sorted:
            if j['beginTime'] != None and j['endTime'] != None:
                if int(j['beginTime']) <= endTime and int(j['endTime']) >= beginTime:
                    sortedTemp.append(j)
        sorted = sortedTemp

    return sorted


sorted = sortData(data, building='VMS')
print(f"Courses Found: {len(sorted)}")
for x in sorted:
    print(x)
