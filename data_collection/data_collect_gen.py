import argparse
import sys
import pokebase as pb
import ssl

def get_gen_pokemon():
    gen2 = pb.generation(2)
    return [p.name for p in gen2.pokemon_species]

parser = argparse.ArgumentParser()
parser.add_argument("gen", help="Choose which generation of pokemon to collect", type=int)
args = parser.parse_args()

if args.gen > 9 or args.gen < 1:
    print("Error: There's no existing generation")
    sys.exit(1)

list_pokemon = get_gen_pokemon()


