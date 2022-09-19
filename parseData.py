import json, os

bigData = {}

courseCount = 0
trueCount = 0
with open("bigData.json", "a") as outfile:
    outfile.write("{")

    for file in os.listdir("outs"):
        print(file)
        fileDict = []
        f = open('outs/'+file, 'r')
        data = json.load(f)
        f.close()
        trueCount += data['totalCount']

        data = data["data"]
        for x in data:
            courseCount += 1
            subject = x['subjectDescription']
            courseNum = x['courseNumber']
            courseTitle = x['courseTitle']
            building = x['meetingsFaculty'][0]['meetingTime']['building']
            room = x['meetingsFaculty'][0]['meetingTime']['room']
            beginTime = x['meetingsFaculty'][0]['meetingTime']['beginTime']
            endTime = x['meetingsFaculty'][0]['meetingTime']['endTime']
            days = [x['meetingsFaculty'][0]['meetingTime']['sunday'], x['meetingsFaculty'][0]['meetingTime']['monday'], x['meetingsFaculty'][0]['meetingTime']['tuesday'], x['meetingsFaculty'][0]['meetingTime']['wednesday'], x['meetingsFaculty'][0]['meetingTime']['thursday'], x['meetingsFaculty'][0]['meetingTime']['friday'], x['meetingsFaculty'][0]['meetingTime']['saturday']]
            seats = x['seatsAvailable']
            if len(x['faculty']) > 0:
                teacher = x['faculty'][0]['displayName']
                teacherEmail = x['faculty'][0]['emailAddress']
            
            fileDict.append({"subject":subject, "courseNum":courseNum, "courseTitle":courseTitle, "building":building, "room":room, "beginTime":beginTime, "endTime":endTime, "days":days, "seats":seats, "teacher":teacher, "teacherEmail":teacherEmail})
        
        json_object = json.dumps(fileDict)
        outfile.write('"' + file[0:-4] + '":')
        outfile.write(json_object)
        if file != os.listdir("outs")[-1]:
            outfile.write(",\n")
    outfile.write("}")

print(trueCount, courseCount)
