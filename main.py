import json

f = open('out.txt', 'r')
data = json.load(f)
f.close()

data = data["data"]
for x in data:
    print(x['subjectDescription'], x['courseNumber'],
          x['meetingsFaculty'][0]['meetingTime']['building'])
