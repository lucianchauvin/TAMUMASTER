import json
import pytz
from datetime import datetime
import calendar
zone = pytz.timezone('US/Central')


f = open('bigData.json', 'r')
data = json.load(f)
f.close()
data = [y for sub in [data.get(x) for x in data] for y in sub]


def sortData(data, subject=None, courseNum=None, courseTitle=None, building=None, room=None, current=False, today=False, beginTime=None, endTime=None, days=None, seats=None, teacher=None, teacherEmail=None):
    sorted = data
    if (beginTime != None and endTime != None) or today or current or days != None:
        sortedTemp = []

        dayDict = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2,
                   'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
        dayClas = [0,0,0,0,0,0,0]
        
        if current:
            endTime, beginTime = int(datetime.now(zone).strftime(
                "%H%M")), int(datetime.now(zone).strftime("%H%M"))
            day = calendar.day_name[datetime.now(zone).weekday()]
            dayClas[dayDict[day]] = True
            if datetime.now(zone).strftime("%p") == "PM":
                endTime += 1200
                beginTime += 1200
        elif today:
            day = calendar.day_name[datetime.now(zone).weekday()]
            dayClas[dayDict[day]] = True
        else:
            if days != None:
                dayClas = days
            else:
                dayClas = [1,1,1,1,1,1,1]
        
        for j in sorted:
            if j['beginTime'] != None and j['endTime'] != None and current:
                if int(j['beginTime']) < endTime and int(j['endTime']) > beginTime and list(j['days'])[dayDict[day]]:
                    sortedTemp.append(j)
            elif today:
                if list(j['days'])[dayDict[day]]:
                    sortedTemp.append(j)
            else:
                if list(j['days']) == dayClas:
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

    return sorted

print(sortData(data, teacher="Haydon"))

