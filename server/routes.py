from flask import jsonify, request
from app import app, db
from models import Hero, Power, HeroPower

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify({"heroes": [hero.serialize() for hero in heroes]})

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify({"powers": [power.serialize() for power in powers]})

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.serialize())
    return jsonify({"error": "Hero not found"}), 404

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.serialize())
    return jsonify({"error": "Power not found"}), 404

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    new_hero_power = HeroPower(
        strength=data['strength'],
        hero_id=data['hero_id'],
        power_id=data['power_id']
    )
    db.session.add(new_hero_power)
    db.session.commit()
    return jsonify({"message": "Hero Power relationship created!"}), 201
