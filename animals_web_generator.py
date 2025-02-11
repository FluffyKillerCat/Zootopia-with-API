import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_skin_types(data):
    """Extracts all unique skin types from the dataset."""
    skin_types = set()
    for animal in data:
        if 'characteristics' in animal and 'skin_type' in animal['characteristics']:
            skin_types.add(animal['characteristics']['skin_type'])
    return list(skin_types)


def serialize_animal(animal_data):
    """Transforms an animal's data into an HTML list item."""
    if 'name' not in animal_data:
        return ""

    li_content = [f'<li class="cards__item">']
    li_content.append(f'  <div class="card__title">{animal_data["name"]}</div>')
    details = []

    if 'characteristics' in animal_data:
        if 'diet' in animal_data['characteristics']:
            details.append(f'<strong>Diet:</strong> {animal_data["characteristics"]["diet"]}')
        if 'type' in animal_data['characteristics']:
            details.append(f'<strong>Type:</strong> {animal_data["characteristics"]["type"]}')

    if 'locations' in animal_data and animal_data['locations']:
        details.append(f'<strong>Location:</strong> {animal_data["locations"][0]}')

    if details:
        li_content.append('  <p class="card__text">')
        li_content.append('<br/>'.join(details))
        li_content.append('  </p>')

    li_content.append('</li>')
    return '\n'.join(li_content)


def generate_html(data, template_path, output_path):
    """Generates a new HTML file from a template with injected animal data."""
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    animals_html = '\n'.join(serialize_animal(animal) for animal in data)
    updated_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open(output_path, "w") as output_file:
        output_file.write(updated_html)


def main():
    """Main function to execute the program."""
    data = load_data("animals_data.json")
    generate_html(data, "animals_template.html", "animals_output.html")
    print("HTML file generated successfully as animals_output.html")


if __name__ == "__main__":
    main()
