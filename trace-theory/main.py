from foata_form_resolver import *
from graph import create_graph_vis_file
from utils import read_data
import subprocess
import argparse
import os
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Program uses trace theory to serialize threads, using foata classes and Diekerts's graph"
    )
    parser.add_argument('-f', '--file', '--input-file', 
                        help='file which stores input', 
                        required=True)
    parser.add_argument('-o', '--out', '--output-filename',
                        help='name for output files, default="graph"',
                        default='graph')
    args = parser.parse_args()

    input = read_data(args.file)

    print("alphabet: ", input.alphabet)
    print("word: ", input.word)

    I = resolve_identities(input.transactions)
    D = resolve_dependencies(input.transactions)

    print("I: ", I)
    print("D: ", D)

    foata_form = resolve_foata_GH_method(input.word, D, input.alphabet)
    print(pretty_foata_string(foata_form))

    create_graph_vis_file(foata_form, D, args.out)

    img_file = f"{args.out}.png"
     
    subprocess.run(["dot", "-Tpng", f"{args.out}.dot", "-o", img_file], check=True)
    print(f"Graph saved in {img_file} file")
    if os.name == 'nt':
        os.startfile(img_file)
    if os.name == 'posix':
        if sys.platform == 'darwin':
            subprocess.call(['open', img_file])
        else:
            subprocess.call(['xdg-open', img_file])
    
