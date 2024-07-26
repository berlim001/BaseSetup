import subprocess
import os
import argparse
import shutil

def create_build_folder(args):
    CURRENT_DIRECTORY = os.getcwd()
    build_folder = CURRENT_DIRECTORY + "\\build" 
    
    if args.rebuild == True and os.path.exists(build_folder):
        print("Clean rebuild, removing folder: " + build_folder)
        shutil.rmtree(build_folder)

    if not os.path.exists(build_folder):
        print("Creating build folder at: " + build_folder)
        os.makedirs(build_folder)

def compile(args):
    print("compiling with: " + args.compile)
    if args.compile == "g++":
        subprocess.run(["g++","-o","build/build", "src/main.cpp"])
        return
    
    print(args.compile + " not valid compilation typepython!")

def build():
    print("===================================BUILDING===================================")

    parser = argparse.ArgumentParser()
    parser.add_argument("-rb", "--rebuild", help='clean rebuild', action="store_true", default=False)
    parser.add_argument("-c", "--compile", help='compile type', type= str, default="g++")
    args = parser.parse_args()
    
    # create the build folder
    create_build_folder(args);

    # create the build
    compile(args);

    print("================================BUILD COMPLETE================================")

if __name__ == "__main__":
    build()