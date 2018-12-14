import json

people_string = '''
{
    "people": [
        {
            "name": "Kartikey Hebbar",
            "phone": "968-605-5388",
            "email": ["kvh@gmail.com"],
            "has_license": true
        },
        {
            "name": "Rajat Sahay",
            "phone": "968-605-6795",
            "email": ["Sahay@gmail.com"],
            "has_license": false
        }
    ]
}
'''

data = json.loads(people_string)
# print(data)
# print(type(data['people']))

# for person in data['people']:
#     print(person)
for person in data['people']:
    del person['phone']

with open('json_file.json','w') as f:
    json.dump(data, f, indent=2)
# new_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_string)
