from http import HTTPStatus
from flask import Blueprint, jsonify
from ..services.pokemonService import PokemonServices

blueprint = Blueprint('pokemonController', __name__)
pokemon_service = PokemonServices

@blueprint.route("/v1/pokemons/<id>", methods=["GET"])
def find_essentials(id):
    result = pokemon_service.essentials(id)        
    return jsonify({"result": result}), HTTPStatus.OK

@blueprint.route("/v1/pokemons/<id>/sprites", methods=["GET"])
def find_assets(id):
    result = pokemon_service.sprites(id)        
    return jsonify({"result": result}), HTTPStatus.OK