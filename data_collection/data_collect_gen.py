import argparse
import sys
import pokebase as pb

def get_flavor_text(pokemon_name, language="en"):
    """Fetches the flavor text of a Pokémon and removes line breaks and excessive spaces."""
    pokemon_species = pb.pokemon_species(pokemon_name)

    for entry in pokemon_species.flavor_text_entries:
        if entry.language.name == language:
            # Remove line breaks and extra spaces
            flavor_text = entry.flavor_text.replace("\n", " ").strip()
            # Remove extra spaces
            flavor_text = ' '.join(flavor_text.split())
            return flavor_text

    return "No flavor text found."


def get_gen_pokemon(gen):
    """Fetch Pokémon details from a given generation."""
    gen_data = pb.generation(gen)
    pokemon_list = []

    for species in gen_data.pokemon_species:
        pokemon_entry = pb.pokemon(species.name)  # Get detailed Pokémon info
        species_data = pb.pokemon_species(species.name)  # Get species-related info
        id = 1

        # Extract relevant data
        pokemon_info = {
            "id": id,
            "name": pokemon_entry.name.capitalize(),
            "image": pokemon_entry.sprites.front_default if pokemon_entry.sprites else None,
            "types": [t.type.name.capitalize() for t in pokemon_entry.types],
            "habitat": species_data.habitat.name.capitalize() if species_data.habitat else "Unknown",
            "color": species_data.color.name.capitalize(),
            "evolution_stage": species_data.evolves_from_species.name.capitalize() if species_data.evolves_from_species else "1",
            "height": pokemon_entry.height / 10,  # Convert to meters
            "weight": pokemon_entry.weight / 10,  # Convert to kg
            "abilities": [a.ability.name.capitalize() for a in pokemon_entry.abilities],
            "cries": pokemon_entry.cries.latest if hasattr(pokemon_entry, 'cries') else "No cry available",
            "flavor_text": get_flavor_text(pokemon_entry.name)
        }

        # Print for debugging
        print(f"ID: {pokemon_info['id']}")
        print(f"Name: {pokemon_info['name']}")
        print(f"Image URL: {pokemon_info['image']}")
        print(f"Types: {pokemon_info['types']}")
        print(f"Habitat: {pokemon_info['habitat']}")
        print(f"Color: {pokemon_info['color']}")
        print(f"Evolution Stage: {pokemon_info['evolution_stage']}")
        print(f"Height: {pokemon_info['height']}m")
        print(f"Weight: {pokemon_info['weight']}kg")
        print(f"Abilities: {pokemon_info['abilities']}")
        print(f"Cries: {pokemon_info['cries']}")
        print(f"Flavor Text: {pokemon_info['flavor_text']}\n")
        
        id += 1
        pokemon_list.append(pokemon_info)
    
    return pokemon_list

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("gen", help="Choose which generation of Pokémon to collect", type=int)
args = parser.parse_args()

if args.gen > 9 or args.gen < 1:
    print("Error: There's no existing generation")
    sys.exit(1)

# Fetch Pokémon details
list_pokemon = get_gen_pokemon(args.gen)

# Print the first Pokémon's type (✅ No more TypeError)
print(list_pokemon[0])  


