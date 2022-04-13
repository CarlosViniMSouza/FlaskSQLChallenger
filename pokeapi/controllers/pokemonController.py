from http import HTTPStatus
from flask import Blueprint, jsonify
from ..services.pokemonService import PokemonServices

blueprint = Blueprint('pokemonController', __name__)
pokemon_service = PokemonServices


@blueprint.route("https://pokeapi.co/api/v2/pokemon/?offset=<id>", methods=["GET"])
def get_pokemon(id):
    result = pokemon_service.essentials(id)        
    return jsonify({"result": result}), HTTPStatus.OK
