import re

def camel_to_snake_case(name: str) -> str:
    # Find positions of uppercase letters, add underscore before them, and convert to lowercase
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return snake_case

def convert_dict_keys_to_snake_case(dictionary: dict) -> dict:
    """Convert dictionary keys from `camelCase` to `snake_case` recursively."""
    new_dict = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            value = convert_dict_keys_to_snake_case(value)
        new_dict[camel_to_snake_case(key)] = value
    return new_dict

def convert_shipping_info_v2_data(data: dict) -> dict:
    """Convert shipping info v2 data into the proper format."""
    new_dict = convert_dict_keys_to_snake_case(data)
    handling_time = new_dict.get('handling_time', {})
    if handling_time:
        new_handling_time = {
            "min": handling_time["from"],
            "max": handling_time["to"],
        }
        new_dict["handling_time"] = new_handling_time
    return new_dict