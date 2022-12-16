
#!/usr/bin/python3
"""Main file!"""
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", strict_slashes=False, methods=["GET"])
def status():
    """Defines the request status"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False, methods=["GET"])
def stats():
    """Retrieves the number of each objects by type"""

    return jsonify({"amenities": storage.count(Amenity),
                    "cities": storage.count(City),
                    "places": storage.count(Place),
                    "reviews": storage.count(Review),
                    "states": storage.count(State),
                    "users": storage.count(User)})
