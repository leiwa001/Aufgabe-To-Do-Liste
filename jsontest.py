import json

dog_data = {
   "name": "Frieda"
     }

dog_data_json = json.dumps(dog_data)
print(dog_data_json)

new_dog_data = json.loads(dog_data_json)
print(new_dog_data)
