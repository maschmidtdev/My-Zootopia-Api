import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

HEADERS = {
    "X-Api-Key": API_KEY
}


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """

    res = requests.get(f"https://api.api-ninjas.com/v1/animals?name={animal_name}", headers=HEADERS)
    return res.json()


def main():
    print(fetch_data("fox"))


if __name__ == '__main__':
    main()