from app import db, app  # Import app along with db
from models import Hero, Power

def seed_database():
    # Use application context
    with app.app_context():
        # Check if the database is already populated
        if Hero.query.count() > 0 or Power.query.count() > 0:
            print("Database already seeded.")
            return

        # Create sample heroes
        hero1 = Hero(name='Superman')
        hero2 = Hero(name='Batman')

        # Create sample powers
        power1 = Power(description='Flight')
        power2 = Power(description='Strength')

        # Add heroes and powers to the session
        db.session.add(hero1)
        db.session.add(hero2)
        db.session.add(power1)
        db.session.add(power2)
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
