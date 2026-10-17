# My Zootopia API

A small Python project that generates an HTML website containing information about animals.

The application asks the user for an animal name, retrieves matching animal data from the [API Ninjas Animals API](https://api-ninjas.com/api/animals), and generates an HTML page displaying the results.

## Features

- Search for animals by name
- Fetch animal data from an external API
- Display information such as:
  - Animal name
  - Diet
  - Location
  - Type, if available
- Generate an `animals.html` website from an HTML template
- Display a message when no matching animal is found

## Project Structure

```text
My-Zootopia-Api/
│
├── animals_web_generator.py
├── data_fetcher.py
├── animals_template.html
├── animals.html
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/maschmidtdev/My-Zootopia-Api.git
cd My-Zootopia-Api
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## API Key

This project uses the API Ninjas Animals API.

1. Create an account at [API Ninjas](https://api-ninjas.com/).
2. Get your API key.
3. Create a `.env` file in the project directory:

```text
API_KEY=your_api_key_here
```

The `.env` file is ignored by Git and should not be committed.

## Usage

Run:

```bash
python animals_web_generator.py
```

You will be asked to enter an animal name:

```text
Enter a name of an animal: fox
```

The application retrieves matching animals and creates:

```text
animals.html
```

Open this file in a web browser to view the generated website.

If no animal is found, the generated page will display a corresponding message.

## Technologies

- Python
- Requests
- python-dotenv
- HTML / CSS
- API Ninjas Animals API