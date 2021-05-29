# tomamos los routers declarados anteriormente, pero lo hacemos como formato XML
<?xml version="1.0" encoding="UTF-8" ?>
<root>
  <Routers>
    <Hostname>R1</Hostname>
    <Vendor>Cisco</Vendor>
    <Id>1</Id>
  </Routers>
  <Routers>
    <Hostname>R2</Hostname>
    <Vendor>Huawei</Vendor>
    <Id>2</Id>
  </Routers>
</root>

# guardamos en un archivo llamado «xml_router.txt»
# importando el modulo de python «xmltodict», leemos los datos en xml e imprimimos en pantalla
import xmltodict
 
with open('xml_router.txt') as xml_data:
    xml_parsed = xmltodict.parse(xml_router.read())
 
print(xml_parsed)
print()
print(xml_parsed['root'])
print()
print(xml_parsed['root']['Routers'])
print()
print(xml_parsed['root']['Routers'][0])
