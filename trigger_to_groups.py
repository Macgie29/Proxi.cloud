import json
import requests

base_url = "https://panel.proxi.cloud/api/v2"
triggers_api_url = base_url+"/triggers.json"


#Wpisujemy swój ACCESS_TOKEN - można go dostać od Pawła
headers = {'Content-type': 'application/json',
           'ACCESS_TOKEN': ''}

#Zmienić wartość trigger_group_id na id grupy skąd pobieramy triggery, które potem dopasujemy do grup
#Type zmieniamy jeśli jest taka potrzeba
req = requests.get(triggers_api_url, {
    'trigger_group_id': '',
    'type': 'Geofence'
}, headers=headers)

json_data = req.json()

print(json_data)

strefaD_60m = []
other_triggers = []

#W polu "find" zmieniamy wartość na tą, którą skrypt ma nam znalezc!
for trigger in json_data:
    if trigger['name'].find("") != -1:
        strefaD_60m.append(trigger)
    else:
        other_triggers.append(trigger)

#Zmieniamy wartość trigger_group_ids.append na ID grupy DO KTÓREJ WYSYŁAMY TRIGGERY
for trigger in strefaD_60m:
    trigger_id = trigger['id']
    trigger_group_ids = [group['id'] for group in trigger['trigger_groups']]
    trigger_group_ids.append("")
    postman_message = {
        "trigger_group_ids": trigger_group_ids
    }
    url = base_url+f"/triggers/{trigger_id}.json"
    r = requests.patch(url, data=json.dumps(postman_message), headers=headers)
    print(r.status_code)
    #W Panelu jaki wyskoczy po uruchomieniu modułu powinny wyskakiwać trzycyfrowe liczby. Jeśli wyskakuje "204" to jest okej, jak coś innego to mamy problem i pytamy ładnie mnie, albo programistów :)

print("================")
print(strefaD_60m)

