import json
import pytz
from datetime import datetime
import calendar
zone = pytz.timezone('US/Central')


f = open('bigData.json', 'r')
data = json.load(f)
f.close()


def sortData(subject=None, courseNum=None, courseTitle=None, building=None, room=None, current=False, today=False, beginTime=None, endTime=None, days=None, seats=None, teacher=None, teacherEmail=None):
    if (beginTime != None and endTime != None) or today or current or days != None:
        sorted = []
        timeBypass = 0

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
        if beginTime == None and endTime == None:
            timeBypass = 1
        
        for i in data:
            for j in data.get(i):
                if j['beginTime'] != None and j['endTime'] != None and beginTime != None and endTime != None:
                    if int(j['beginTime']) < endTime and int(j['endTime']) > beginTime and list(j['days']) == dayClas and not timeBypass:
                        sorted.append(j)
                elif timeBypass and list(j['days']) == dayClas:
                    sorted.append(j)
    
    return sorted

print(sortData(today=True))
        
