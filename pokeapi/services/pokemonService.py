import pokeapi

POKEMON_COLORS = {
    11: "light_green"
}

POKEMONS_TYPES_COLOR = {
    "grass": "green",
    "poison": "purple",
    "bug": "light_green"
}

class PokemonServices(object):
    def __init__(self):
        pass

    def sprites(self, id):
        result = pokeapi.pokemons(id)["sprites"]
        for field in dict(result):
            if result[field] is None:
                del result[field]
        return result

    def essentials(self, id):
        result = pokeapi.pokemons(id)
        return self.extract_essentials(result)

    def essentials_range(self, _from, _to):
        result = []
        start_id = _from
        end_id = _to + 1
        for id in range(start_id, end_id):
            result.append(self.essentials(id))
        return result

    def default_image(self, id):
        return self.sprites(id)["front_default"]

    def extract_essentials(self, _input):
        return {
            "abilities": self.extract_habilities(_input),
            "base_experience": _input["base_experience"],
            "height": _input["height"],
            "id": _input["id"],
            "name": _input["name"],
            "order": _input["order"],           
            # "color": self.find_pokemon_color(_input["id"]),
            # "image": self.default_image(_input["id"]),
        }

    def extract_habilities(self, _input):
        abilities = _input["abilities"]
        result = []
        for item in abilities:
            print(f"hability: {item}")
            result.append({"name": item["ability"]["name"]})
        return result

    def build_type(self, item):
        type_name = item["type"]["name"]
        return {"name": type_name, "color": self.define_color_type(type_name)}

    def define_color_type(self, type_name):
        return POKEMONS_TYPES_COLOR.get(type_name, "black")

    def find_pokemon_color(self, id):
        try:
            return pokeapi.pokemons_color(id)["name"]
        except Exception as e:
            return self.define_pokemon_color(id)

    def define_pokemon_color(self, id):
        return POKEMON_COLORS.get(id, "black")