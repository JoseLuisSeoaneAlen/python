# delaracion de 2 Routers
import json
jsonvar = json.dumps({
      "Routers": [
                   {
                     "Hostname": "R1",
                     "Vendor": "Cisco",
                     "Id": "1"
                   },
                   {
                     "Hostname": "R2",
                     "Vendor": "Huawei",
                     "Id": "2"
                   }
                ]
}, indent=4, sort_keys=True)
fo = open("fichero.txt", "w")
fo.write(jsonvar)
# Cerramos el archivo fichero.txt
fo.close()
