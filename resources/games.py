# All the routes for our games
import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
import requests
import json

games = Blueprint('games', 'games')


#Main Home Paige
@games.route('/', methods=['GET'])
def games_index():
    result = models.Game.select()
    print('result')
    game_dicts = [model_to_dict(game) for game in result]

    return jsonify({
        'data': game_dicts,
        'message': f"Successfully found {len(game_dicts)} games",
        'status': 200
    }), 200

#
# Search route
# user submits a form on a frontend. It will fetch to this route
# In this route you want to take what you want from the user and do a GET request to the API (/Search)
# Send back the response from the API to the front end
# Front end loop through and parse through the data you want # Console.log the data in the front end
@games.route('/search/<search_term>', methods=['GET'])
def games_search(search_term):
    print(search_term)
    req = requests.get('https://api.rawg.io/api/games?key=cc7a20c2a9db45bc8a0eb2994afda720&search=' + search_term)
    print(req.json())


    return jsonify(
        data = req.json(),
        message = "Searched game correctly",
        status = 201
    ),200



# @games.route('/<id>' methods=['GET'])
# def games_search():
#     req = requests.get('https://api.rawg.io/api/games?key=cc7a20c2a9db45bc8a0eb2994afda720&dates=2019-09-01,2019-09-30&platforms=18,1,7')
#     print(req.json())
#     print(req.status_code)





# @games.route('/<id>' methods=['GET'])
# def games_search():
#     req = requests.get('https://api.rawg.io/api/games?key=cc7a20c2a9db45bc8a0eb2994afda720&dates=2019-09-01,2019-09-30&platforms=18,1,7')
#     print(req.json())
#     print(req.status_code)


# create route
@games.route('/', methods=['POST'])
def create_game():
    payload = request.get_json()
    print(payload)
    new_game = models.Game.create(name=payload['name'], background_image=payload['background_image'], ratings=payload['ratings'], platforms=payload['platforms'])
    #ratings=payload[], getting error
    print(new_game)
    print(dir(new_game))
    game_dict = model_to_dict(new_game)
    return jsonify(
        data=game_dict,
        message='Uploaded New Game Successfully to your Favorite List',
        status=201
    ),201



#Show route
@games.route('/<id>', methods=['GET'])
def get_one_game(id):
    game = models.Game.get_by_id(id)
    print(game)
    return jsonify(
        data = model_to_dict(game),
        message = 'Success!!',
        status = 200
    ), 200

#Update Route
@games.route('/<id>', methods=['PUT'])
def update_game(id):
    payload = request.get_json()
    models.Game.update(name=payload['name'], background_image=payload['background_image'], ratings=payload['ratings'], platforms=payload['platforms']).where(models.Game.id == id).execute()
    updated_game = models.Game.get_by_id(id)
    updated_dog_dict = model_to_dict(update_game)

    return jsonify(
        data = updated_dog_dict,
        message = 'updated Successfully',
        status = 200
    ),200

# @games.route('/games/rent', methods=['PUT'])
# def update_game(id):
#
#     return "Rent Route is Working"


# Delete Route
@games.route('/<id>', methods=['DELETE'])
def delete_games(id):
    delete_query = models.Game.delete().where(models.Dog.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)

    return jsonify(
        data={},
        message = f"Successfully deleted {nums_of_rows_deleted} dog with id {id}",
        status=200
    ), 200
