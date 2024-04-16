import json


def save_to_file(data, filename):
    """
    Save data to a file.

    Args:
        data: Data to save.
        filename (str): Name of the file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_from_file(filename):
    """
    Load data from a file.

    Args:
        filename (str): Name of the file.

    Returns:
        Data loaded from the file.
    """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
