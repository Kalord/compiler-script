import os
import sys
from components.Finder import Finder
from components.Command import Command

def main():
    if(len(sys.argv) == 1):
        print('ERROR')
        exit()

    pathToDirectory = sys.argv[1]
    bootstrap = None

    if(len(sys.argv) == 3):
        bootstrap = sys.argv[2]

    command = Command.createCompilerCommand(
        Finder.findFiles(pathToDirectory, r'^\w+\.cpp$'), 
        bootstrap
    )

    os.system(command)
    print(command)
    
if __name__ == '__main__':
    main()