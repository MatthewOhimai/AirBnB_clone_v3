#!/usr/bin/python3
"""
route for handling Place objects and operations
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models.place import Place


@app_views.route("/cities/<city_id>/places", methods=["GET"],
                 strict_slashes=False)
def places_by_city(city_id):
    """
    retrieves all Places objects by city
    :return the json of all Places
    """
    place_l = []
    city_obj = storage.get("City", str(city_id))
    for obj in city_obj.places:
        place_l.append(obj.to_json())

    return jsonify(place_list)


@app_views.route("/cities/<city_id>/places", methods=["POST"],
                 strict_slashes=False)
def place_create(city_id):
    """
    create a place route
    :return: newly created Place obj
    """
    place_j = request.get_json(silent=True)
    if place_j is None:
        abort(400, 'Not a JSON')
    if not storage.get("User", place_j["user_id"]):
        abort(404)
    if not storage.get("City", city_id):
        abort(404)
    if "user_id" not in place_j:
        abort(400, 'Missing user_id')
    if "name" not in place_j:
        abort(400, 'Missing name')

    place_j["city_id"] = city_id

    new_place = Place(**place_j)
    new_place.save()
    resp = jsonify(new_place.to_json())
    resp.status_code = 201

    return resp


@app_views.route("/places/<place_id>",  methods=["GET"],
                 strict_slashes=False)
def place_by_id(place_id):
    """
    gets a specific Place object by ID
    :param place_id: place object id
    :return: place obj with the specified id or error
    """

    fetched_obj = storage.get("Place", str(place_id))

    if fetched_obj is None:
        abort(404)

    return jsonify(fetched_obj.to_json())


@app_views.route("/places/<place_id>",  methods=["PUT"],
                 strict_slashes=False)
def place_put(place_id):
    """
    updates specific Place object by ID
    :param place_id: Place object ID
    :return: Place object and 200 on success, or 400 or 404 on failure
    """
    place_j = request.get_json(silent=True)

    if place_j is None:
        abort(400, 'Not a JSON')

    fetched_obj = storage.get("Place", str(place_id))

    if fetched_obj is None:
        abort(404)

    for key, val in place_j.items():
        if key not in ["id", "created_at", "updated_at", "user_id", "city_id"]:
            setattr(fetched_obj, key, val)

    fetched_obj.save()

    return jsonify(fetched_obj.to_json())


@app_views.route("/places/<place_id>",  methods=["DELETE"],
                 strict_slashes=False)
def place_delete_by_id(place_id):
    """
    deletes the Place by id
    :param place_id: Place object id
    :return: empty dict with 200 or 404 if not found
    """

    fetched_obj = storage.get("Place", str(place_id))

    if fetched_obj is None:
        abort(404)

    storage.delete(fetched_obj)
    storage.save()

    return jsonify({})
