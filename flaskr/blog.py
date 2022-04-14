from flask import Flask, render_template

import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    r = requests.get('https://pokeapi.co/api/v2/pokedex/2')
    pokemon = r.json()
    return render_template('index.html', pokemon=pokemon)

@app.route('/<pokemon_id>', methods=['GET'])
def pokemon(pokemon_id):
  r = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon_id))
  pokemon = r.json()
  return render_template('pokemon.html', pokemon=pokemon, pokemon_id=pokemon_id)

if __name__ == "__blog__":
  app.run(debug=True)