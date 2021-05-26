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
    
class TestPruebaJson(unittest.TestCase):
  def test_method(self):
    client = {}
