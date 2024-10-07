# Superheroes API

This API tracks superheroes and their superpowers. Built with Flask and SQLAlchemy.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
Run the application:
bash
Copy code
python app.py
Seed the database:
bash
Copy code
python seed.py
Endpoints
Heroes
GET /heroes: Returns a list of all heroes.
GET /heroes/<id>: Returns details of a hero by ID.
Powers
GET /powers: Returns a list of all powers.
GET /powers/<id>: Returns details of a power by ID.
PATCH /powers/<id>: Updates a power by ID.
Hero Powers
POST /hero_powers: Creates a new hero-power association.
Validation
The strength of a HeroPower must be one of: Strong, Weak, Average.
The description of a Power must be at least 20 characters long.
Testing
You can use Postman to import the provided collection and test the API endpoints.

vbnet
Copy code

### Final Steps
1. Make sure to initialize a Git repository and push your code to GitHub.
2. Test your API using Postman with the provided collection.