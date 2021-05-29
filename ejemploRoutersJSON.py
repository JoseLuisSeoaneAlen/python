# delaracion de 2 Routers
{
      “Routers”: [ 
                   { 
                     “Hostname”: “R1”,
                     “Vendor”: “Cisco”, 
                     “Id”: “1” 
                   }, 
                   { 
                     “Hostname”: “R2”,
                     “Vendor”: “Huawei”,
                     “Id”: “2” 
                   }
                ]
}

# guardamos los routers declarados en json_routers.txt
import json
 
with open('json_routers.txt') as json_data:
    json_parsed = json.loads(json_routers.read())
 
print(json.dumps(json_parsed, indent=4, sort_keys=True))
