import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:

    output_parts = []


    if 'name' in animal:
        output_parts.append(f"Name: {animal['name']}")

    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        output_parts.append(f"Diet: {animal['characteristics']['diet']}")
    if 'locations' in animal and len(animal['locations']) > 0:
        output_parts.append(f"Location: {animal['locations'][0]}")
    if 'type' in animal['characteristics']:
        output_parts.append(f"Type: {animal['characteristics']['type']}")



    if output_parts:
        print('\n'.join(output_parts))
