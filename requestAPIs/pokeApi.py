

#TODO: MiniProject PokeAPI

import requests 

class pokemonAPI:
    def __init__(self, url="https://pokeapi.co/api/v2/" ):
        self.__url = url
    def pokemonDetails(self,endpoint='pokemon'):
        args = {'limit': int(input("How many pokemon name want to see ? ")), 'offset': int(input('In which page do you want to be ? (0-60) '))}
        while args['limit'] != 'N':
            response = requests.get(self.__url+'%s'%endpoint, params=args)
            if response.status_code == 200:
                newView = response.json()['results']
                viewPokemon = input("Want to see the pokemons name? [Y/N]: ")
                if viewPokemon.lower() == 'y':
                    for pokemonNames in newView:
                        print(pokemonNames['name'])
                pokemonInfo = input('What"s the name of the pokemon you want to see the information? ')
                pokemonExist =any(True if  pokemonInfo==pokemonName['name'] else False for pokemonName in newView)
                if pokemonExist:
                    response = requests.get(self.__url+'%s/%s'%(endpoint,pokemonInfo))
                    if response.status_code ==  200:
                        infoPokemon = response.json()
                        print(f"""
                                \nThe pokemon name is {infoPokemon['name']}, the base experience are {infoPokemon['base_experience']}, the weight are {infoPokemon['weight']} and the height {infoPokemon['height']}
                                """.strip())
                        pokemonBool = input('Want to see the pokemon abilities [Y/N]')
                        if pokemonBool.lower() == 'y':
                            abilitiesInfo = infoPokemon['abilities']
                            pokemonListAbility = [] 
                            for abilityDetails in abilitiesInfo:
                                pokemonListAbility.append(''.join(list(map(str,abilityDetails['ability']['name'])))) 
                            pokemonListAbility[-1] = f"and {pokemonListAbility[-1]}"
                            print(f"{infoPokemon['name']} has {' '.join(map(str, pokemonListAbility))} abilities")
                           # self.pokemonAbilities(abilitie)
                else:
                    print('That pokemon name doesn"t exist, please enter a valid pokemon name')
                    continue
    
                args.update({'limit':int(input("How many pokemon name want to see ?: ")),'offset': int(input('In which page do you want to be ? (0-60)'))})
                continue
    def pokemonAbilities(self,endpoint):
        response = requests.get(url=endpoint)
        print(response.url)
start = pokemonAPI()
start.pokemonDetails()

