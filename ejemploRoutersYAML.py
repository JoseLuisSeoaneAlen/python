#Declaramos los routers en formato YAML.

Routers:
- Hostname: R1
  Vendor: Cisco
  Id: '1'
- Hostname: R2
  Vendor: Huawei
  Id: '2'
    
# guardamos en fichero yaml_router.txt e imprimimos por pantalla
import yaml
 
with open('yaml_router.txt') as yaml_data:
    yaml_parsed = yaml.load(yaml_router, Loader=yaml.FullLoader)
 
print(yaml_parsed)
print(type(yaml_parsed))
