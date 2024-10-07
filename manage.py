from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Superheroes API!"

@app.route('/heroes')
def heroes():
    return jsonify([
        {"id": 1, "name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"id": 2, "name": "Doreen Green", "super_name": "Squirrel Girl"}
    ])

@app.route('/heroes/<int:id>')
def hero(id):
    heroes = [
        {"id": 1, "name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"id": 2, "name": "Doreen Green", "super_name": "Squirrel Girl"}
    ]
    for hero in heroes:
        if hero['id'] == id:
            return jsonify(hero)
    return jsonify({"error": "Hero not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
