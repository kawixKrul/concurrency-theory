import argparse
from utils import parse_input, write_result
from concurrent_gauss import ConcurrentGauss
from foata_form_resolver import *
from grapg_vis import visualize_diekerts_graph
import subprocess
import os 
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Program performs concurrent gaussian elimination on input matrix"
    )
    parser.add_argument('-f', '--file', '--input-file', 
                        type=str,
                        help='path to file which stores input, default="matrix_input.txt"',
                        default="matrix_input.txt")
    parser.add_argument('-o', '--out', '--output-filename',
                        type=str,
                        help='name for output files, default="graph"',
                        default='graph')
    parser.add_argument('-c', '--check',
                        action='store_true',
                        help='check results with java checker',
                        default=False)
    parser.add_argument('-t', '--threads', '--thread-pool-size',
                        type=int,
                        help='max size of available threads in a pool',
                        default=10)
    args = parser.parse_args()

    A, b = parse_input(args.file)

    CG = ConcurrentGauss(A, b, args.threads)
    T = transactions(CG.len)
    A = alphabet(T)
    D = resolve_dependencies(A)

    print(f'Transactions: {T}\n')
    print(f'Alphabet: {A}\n')
    print(f'Dependency set: {D} \n')
    
    FNF = resolve_foata_GH_method(A, D, A)
    print(f'Foata normal form: {pretty_foata_string(FNF)} \n')

    visualize_diekerts_graph(CG.len, args.out)
    
    result = CG.resolve()
    for row in result: 
        print(row)
    matrix_to_check = CG.to_diagonal()
    result_file = "matrix_output.txt"
    write_result(result_file, matrix_to_check)

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

    if args.check:
        log_file = 'output.log'
        maven_path = "Matrices-master/"
        working_dir = os.path.join(os.getcwd(), maven_path)
        command = [
            'mvn',
            'exec:java',
            '-Dexec.mainClass=pl.edu.agh.macwozni.matrixtw.Checker', 
            f'-Dexec.args=../{args.file} ../{result_file}'
            ]
        with open(log_file, "w") as log:
            with subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,  
                cwd=working_dir,
                bufsize=1, 
                universal_newlines=True) as proc:
                stdout, stderr = proc.communicate()

                log.write("STDOUT:\n")
                log.write(stdout)
                
                log.write("\nSTDERR:\n")
                log.write(stderr)

        if os.name == 'nt':
            os.startfile(log_file)
        if os.name == 'posix':
            if sys.platform == 'darwin':
                subprocess.call(['open', log_file])
            else:
                subprocess.call(['xdg-open', log_file])
                