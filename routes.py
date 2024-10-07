from flask import Flask, request, jsonify
from models import db, Hero, Power, HeroPower

def create_routes(app):
    @app.route('/heroes', methods=['GET'])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([hero.to_dict() for hero in heroes]), 200

    @app.route('/heroes/<int:id>', methods=['GET'])
    def get_hero(id):
        hero = Hero.query.get(id)
        if hero is None:
            return jsonify({'error': 'Hero not found'}), 404
        return jsonify(hero.to_dict()), 200

    @app.route('/powers', methods=['GET'])
    def get_powers():
        powers = Power.query.all()
        return jsonify([power.to_dict() for power in powers]), 200

    @app.route('/powers/<int:id>', methods=['GET'])
    def get_power(id):
        power = Power.query.get(id)
        if power is None:
            return jsonify({'error': 'Power not found'}), 404
        return jsonify(power.to_dict()), 200

    @app.route('/powers/<int:id>', methods=['PATCH'])
    def update_power(id):
        power = Power.query.get(id)
        if power is None:
            return jsonify({'error': 'Power not found'}), 404
        data = request.get_json()
        if 'description' in data:
            power.description = data['description']
        db.session.commit()
        return jsonify(power.to_dict()), 200

    @app.route('/hero_powers', methods=['POST'])
    def create_hero_power():
        data = request.get_json()
        new_hero_power = HeroPower(
            strength=data['strength'],
            power_id=data['power_id'],
            hero_id=data['hero_id']
        )
        db.session.add(new_hero_power)
        db.session.commit()
        return jsonify(new_hero_power.to_dict()), 201
