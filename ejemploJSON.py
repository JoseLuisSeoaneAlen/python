# un objeto diccionarios al que se agregan los datos de tres clientes entre los que se encuentra 
#el nombre los apellidos, la edad y la cantidad gastada por cada uno
import json
data = {}
data['clients'] = []
data['clients'].append({
    'first_name': 'Eva',
    'last_name': 'Duarte',
    'age': 27,
    'amount': 17.17})
data['clients'].append({
    'first_name': 'Jose',
    'last_name': 'Lopez',
    'age': 31,
    'amount': [10.90, 55.50]})
data['clients'].append({
    'first_name': 'Marc',
    'last_name': 'Gomez',
    'age': 36,
    'amount': 111.11})
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
