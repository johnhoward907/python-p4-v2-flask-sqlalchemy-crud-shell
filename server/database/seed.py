# server/database/seed.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models import db, Plant

with app.app_context():
    print("🌱 Seeding database...")

    Plant.query.delete()

    plants = [
        Plant(name="Aloe", image="./images/aloe.jpg", price=11.50, is_in_stock=True),
        Plant(name="Cactus", image="./images/cactus.jpg", price=8.99, is_in_stock=True),
        Plant(name="Peace Lily", image="./images/peace-lily.jpg", price=14.25, is_in_stock=False)
    ]

    db.session.add_all(plants)
    db.session.commit()

    print("✅ Done seeding!")
