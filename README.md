# Superheroes API

This is a Flask API for tracking superheroes and their superpowers. The API allows users to manage superhero data, including details about heroes and their associated powers.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing the API](#testing-the-api)
- [License](#license)

## Features

- Retrieve a list of all heroes and their details.
- Get details of a specific hero by ID.
- Retrieve a list of all powers and their details.
- Get details of a specific power by ID.
- Update a power's description.
- Create associations between heroes and powers with specific strengths.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/superheroes-code-challenge.git
   cd superheroes-code-challenge
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python -m app.app
The application will be running on http://127.0.0.1:5000.

Usage
You can access the API using any REST client, such as Postman or curl. The base URL for the API is:

arduino
Copy code
http://127.0.0.1:5000/api
API Endpoints
Heroes
Get all heroes

Method: GET
Endpoint: /heroes
Response: A JSON array of hero objects.
Get a specific hero

Method: GET
Endpoint: /heroes/<id>
Response: A JSON object of the hero with the specified ID.
Powers
Get all powers

Method: GET
Endpoint: /powers
Response: A JSON array of power objects.
Get a specific power

Method: GET
Endpoint: /powers/<id>
Response: A JSON object of the power with the specified ID.
Update a power

Method: PATCH
Endpoint: /powers/<id>
Request Body:
json
Copy code
{
  "description": "New description for the power."
}
Response: The updated power object.
Hero Powers
Create a hero power association
Method: POST
Endpoint: /hero_powers
Request Body:
json
Copy code
{
  "strength": 10,
  "hero_id": 1,
  "power_id": 2
}
Response: The created hero power association object.
Testing the API
To test the API, you can use tools like Postman or curl. Here are some examples using curl:

Get all heroes:

bash
Copy code
curl -X GET http://127.0.0.1:5000/api/heroes
Get a specific hero:

bash
Copy code
curl -X GET http://127.0.0.1:5000/api/heroes/1
Get all powers:

bash
Copy code
curl -X GET http://127.0.0.1:5000/api/powers
Get a specific power:

bash
Copy code
curl -X GET http://127.0.0.1:5000/api/powers/1
Update a power:

bash
Copy code
curl -X PATCH http://127.0.0.1:5000/api/powers/1 -H "Content-Type: application/json" -d '{"description": "New power description."}'
Create a hero power association:

bash
Copy code
curl -X POST http://127.0.0.1:5000/api/hero_powers -H "Content-Type: application/json" -d