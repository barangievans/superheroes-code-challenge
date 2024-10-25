markdown
Copy code
# Superheroes API

## Description
The Superheroes API allows you to manage superheroes and their powers. It includes endpoints to retrieve, create, and manage hero and power relationships.

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- Flask-SQLAlchemy

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/barangievans/superheroes-code-challenge.git
   cd superheroes_code_challenge
Create a virtual environment and activate it:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Running the Application
Set the environment variables:

bash
Copy code
export FLASK_APP=app.py
export FLASK_ENV=development  # For debug mode
On Windows, use:

bash
Copy code
set FLASK_APP=app.py
set FLASK_ENV=development
Run the Flask application:

bash
Copy code
flask run
The application will be running at http://localhost:5000.

Endpoints
GET /heroes
Description: Retrieve a list of all superheroes.
Response:
json
Copy code
{
    "heroes": [
        {
            "id": 1,
            "name": "Superman"
        },
        {
            "id": 2,
            "name": "Batman"
        }
    ]
}
GET /powers
Description: Retrieve a list of all powers.
Response:
json
Copy code
{
    "powers": [
        {
            "id": 1,
            "description": "Flight"
        },
        {
            "id": 2,
            "description": "Strength"
        }
    ]
}
GET /heroes/int:id
Description: Retrieve a specific superhero by ID.
Parameters:
id: The ID of the superhero.
Response:
json
Copy code
{
    "id": 1,
    "name": "Superman"
}
GET /powers/int:id
Description: Retrieve a specific power by ID.
Parameters:
id: The ID of the power.
Response:
json
Copy code
{
    "id": 1,
    "description": "Flight"
}
POST /hero_powers
Description: Create a relationship between a hero and a power.
Request Body:
json
Copy code
{
    "strength": 10,
    "hero_id": 1,  // ID of Superman
    "power_id": 1   // ID of Flight
}
Response:
json
Copy code
{
    "message": "Hero Power relationship created!"
}
Seeding the Database
To seed the database with sample data, create a new route in app.py:

python
Copy code
@app.route('/seed', methods=['GET'])
def seed():
    seed_database()
    return jsonify({"message": "Database seeded!"}), 200
Then visit http://localhost:5000/seed to populate the database with initial heroes and powers.

Testing
You can use tools like Postman or cURL to test the API endpoints.

Example cURL Requests
Get all heroes:

bash
Copy code
curl -X GET http://localhost:5000/heroes
Get all powers:

bash
Copy code
curl -X GET http://localhost:5000/powers
Get a specific hero:

bash
Copy code
curl -X GET http://localhost:5000/heroes/1
Get a specific power:

bash
Copy code
curl -X GET http://localhost:5000/powers/1
Create a hero power relationship:

bash
Copy code
curl -X POST http://localhost:5000/hero_powers -H "Content-Type: application/json" -d '{"strength": 10, "hero