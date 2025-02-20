import json
import random

def transform_laptop_data(json_file_path, output_json_path):
    """
    Transforms laptop data from a JSON file to a specific format and writes
    the transformed data to a new JSON file.

    Args:
        json_file_path (str): The path to the JSON file containing laptop data.
        output_json_path (str): The path to the output JSON file.

    Returns:
        bool: True if the transformation and writing were successful, False otherwise.
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading or parsing JSON file: {e}")
        return False

    transformed_data = []
    for item in data:
        # Skip items that are not laptop products
        if not isinstance(item, dict) or item.get('type') in ('SponsoredVideoAd', 'TileTakeOverProduct'):
            continue

        # Extract relevant information
        title = item.get('name')
        price = item.get('price')
        image_url = item.get('image')
        short_description = item.get('shortDescription')

        # Handle missing or invalid data
        if title is None or price is None or image_url is None:
            continue

        # Extract characteristics from the short description and other fields
        characteristics = []
        if short_description:
            characteristics.append(short_description)

        # Add other relevant characteristics from the item dictionary
        if 'RAM' in title:
            characteristics.append(title.split('RAM')[0].split()[-1] + " RAM")
        if 'SSD' in title:
            characteristics.append(title.split('SSD')[0].split()[-1] + " SSD")
        if 'Processor' in title:
            characteristics.append(title.split('Processor')[0].split()[-1] + " Processor")

        # Create the transformed data structure
        transformed_item = {
            "title": title,
            "price": price,
            "quantity": random.randint(50, 350),
            "imageUrl": image_url,
            "characteristics": characteristics,
            "category": "laptop"
        }
        transformed_data.append(transformed_item)

    try:
        with open(output_json_path, 'w', encoding='utf-8') as outfile:
            json.dump(transformed_data, outfile, indent=2)
        return True
    except IOError as e:
        print(f"Error writing to JSON file: {e}")
        return False

# Example usage:
json_file_path = "search_results_laptop_page_1.json"
output_json_path = "transformed_laptops1.json"
if transform_laptop_data(json_file_path, output_json_path):
    print(f"Transformed data written to {output_json_path}")
else:
    print("Transformation and writing failed.")