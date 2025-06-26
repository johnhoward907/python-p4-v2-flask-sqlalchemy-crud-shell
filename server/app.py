# server/app.py

from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/plants/<int:id>', methods=['PATCH'])
def update_plant(id):
    plant = Plant.query.get_or_404(id)
    data = request.get_json()

    if "is_in_stock" in data:
        plant.is_in_stock = data["is_in_stock"]

    db.session.commit()

    return jsonify({
        "id": plant.id,
        "name": plant.name,
        "image": plant.image,
        "price": plant.price,
        "is_in_stock": plant.is_in_stock
    })

@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get_or_404(id)

    db.session.delete(plant)
    db.session.commit()

    return "", 204

if __name__ == '__main__':
    app.run(port=5555, debug=True)
