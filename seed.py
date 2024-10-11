from app import app, db
from models import Hero, Power, HeroPower

with app.app_context():
    db.create_all()

    # Add heroes
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
    ]

    # Add powers
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly at supersonic speed"),
        Power(name="super senses", description="enhances the wielder's senses to super-human levels"),
    ]

    db.session.add_all(heroes + powers)
    db.session.commit()

    # Add hero powers relationships
    hero_powers = [
        HeroPower(strength="Strong", hero_id=1, power_id=1),
        HeroPower(strength="Average", hero_id=2, power_id=2),
        HeroPower(strength="Weak", hero_id=3, power_id=3),
        HeroPower(strength="Strong", hero_id=4, power_id=1),
    ]

    db.session.add_all(hero_powers)
    db.session.commit()

    print("Database seeded successfully!")
