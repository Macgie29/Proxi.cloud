import json
import requests

#Tutaj wrzucamy nazwy grup
trigger_groups_names = ['']
url = "https://panel.proxi.cloud/api/v2/trigger_groups.json"
data = {
  "name": "string",
  #Zmieniamy pole projekt_id zgodne z ID projektu, do którego chcemy pododawać grupy
  "project_id": ""
}
headers = {'Content-type': 'application/json',
    #Wpisujemy swój Access_Token - piszemy do Pawła
           'ACCESS_TOKEN': ''}



for group_name in trigger_groups_names:
  data["name"] = group_name
  r = requests.post(url, data=json.dumps(data), headers=headers)
  print(r.status_code)
#Jeśli wyskakuje wartość trzycifrowa "200" to jest okej, w przeciwnym wypadku pytamy mnie, albo programistów.



