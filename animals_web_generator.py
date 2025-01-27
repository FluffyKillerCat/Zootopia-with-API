import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animal_data = load_data("animals_data.json")

output = ''  # Define empty string to build HTML

for animal in animal_data:
    fields = []

    # Name field
    if 'name' in animal:
        fields.append(f"Name: {animal['name']}")

    # Characteristics - Diet
    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        fields.append(f"Diet: {animal['characteristics']['diet']}")

    if 'characteristics' in animal and 'type' in animal['characteristics']:
        fields.append(f"Type: {animal['characteristics']['type']}")

    # Location
    if 'locations' in animal and len(animal['locations']) > 0:
        fields.append(f"Location: {animal['locations'][0]}")

    if fields:
        output += '<li class="cards__item">\n'
        output += '<br/>\n'.join(fields)
        output += '\n</li>\n'

print(output)