import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

data = load_data("animals_data.json")

output = ''  # Initialize empty output string

for animal_data in data:
    # Skip animals without a name
    if 'name' not in animal_data:
        continue

    # Start building the list item
    li_content = []
    li_content.append('<li class="cards__item">')
    li_content.append(f'  <div class="card__title">{animal_data["name"]}</div>')

    # Collect details for the paragraph
    details = []

    # Check and add diet
    if 'characteristics' in animal_data and 'diet' in animal_data['characteristics']:
        diet = animal_data['characteristics']['diet']
        details.append(f'<strong>Diet:</strong> {diet}')

    # Check and add location
    if 'locations' in animal_data and len(animal_data['locations']) > 0:
        location = animal_data['locations'][0]
        details.append(f'<strong>Location:</strong> {location}')

    # Check and add type
    if 'characteristics' in animal_data and 'type' in animal_data['characteristics']:
        animal_type = animal_data['characteristics']['type']
        details.append(f'<strong>Type:</strong> {animal_type}')

    # Add details paragraph if any details exist
    if details:
        li_content.append('  <p class="card__text">')
        li_content.append('<br/>\n    '.join(details))
        li_content.append('  </p>')

    li_content.append('</li>')

    # Add to main output
    output += '\n'.join(li_content) + '\n'

print(output)