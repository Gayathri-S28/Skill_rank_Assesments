import json
with open('ex5.json','r') as f:
    ex5 = json.load(f)
    # for i in ex5:
    #  if i['id'] == "0001":
    #   print(i["batters"])
    for i in ex5:
        if i["name"] == "Old Fashioned":
            i['batters']['batter'].append({'id': '1005', 'type': 'Tea'})
            break
with open('ex5.json','w') as f:
    json.dump(ex5,f,indent=4)
