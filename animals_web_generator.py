import json

import data_fetcher


def get_animal_from_user():
    """Get Animal name from user"""
    animal_name = input('Which Animal Would you like to display? ')
    return animal_name









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
        li_content.append('<br/>\n    '.join(details))
        li_content.append('  </p>')

    li_content.append('</li>')
    return '\n'.join(li_content)


def generate_html(data, switch, animal):
    """Generates a full HTML file with animal data."""
    if switch:
        animals_html = '\n'.join(serialize_animal(animal) for animal in data)
    else:
        animals_html = f"<h2>The animal {animal} doesn't exist.</h2>"


    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Animal Cards</title>
        <style>
            html {{ background-color: #ffe9e9; }}
            h1 {{ text-align: center; font-size: 40pt; font-weight: normal; }}
            body {{
                font-family: 'Roboto','Helvetica Neue', Helvetica, Arial, sans-serif;
                font-style: normal;
                font-weight: 400;
                letter-spacing: 0;
                padding: 1rem;
                text-rendering: optimizeLegibility;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
                -moz-font-feature-settings: "liga" on;
                width: 900px;
                margin: auto;
            }}
            .cards {{ list-style: none; margin: 0; padding: 0; }}
            .cards__item {{
                background-color: white;
                border-radius: 0.25rem;
                box-shadow: 0 20px 40px -14px rgba(0,0,0,0.25);
                overflow: hidden;
                padding: 1rem;
                margin: 50px;
            }}
            .card__title {{
                color: #696969;
                font-size: 1.25rem;
                font-weight: 300;
                letter-spacing: 2px;
                text-transform: uppercase;
            }}
            .card__text {{
                flex: 1 1 auto;
                font-size: 0.95rem;
                line-height: 2;
                margin-bottom: 1.25rem;
            }}
        </style>
    </head>
    <body>
        <h1>Animal Cards</h1>
        <ul class="cards">
            {animals_html}
        </ul>
    </body>
    </html>
    """
    return html_template


def main():
    """Main function to execute the program."""
    while True:
        animal = get_animal_from_user()

        data = data_fetcher.fetch_data(animal)
        if data:

            html_content = generate_html(data, True, animal)



        else:

            html_content = generate_html(data, False, animal)
        with open("animals_template.html", "w") as file:
            file.write(html_content)

        print("HTML file generated successfully.")


if __name__ == "__main__":
    main()
