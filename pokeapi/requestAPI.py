import requests

def resultResponse():
  r = requests.get('https://pokeapi.co/api/v2/pokemon/')

  print('Status = ', r.status_code)
  print('Data = ', requests.get('https://pokeapi.co/api/v2/pokemon/').json())
  print('Message = ', requests.get('https://pokeapi.co/api/v2/pokemon/', data={'key':'value'}))
  print('HTTP Code = ', requests.options('https://pokeapi.co/api/v2/pokemon/'))


# oficial site: https://pokeapi.co/

# return an JSON response with status, data, message and HTTP code.
