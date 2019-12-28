import re
from fs.Directory import Directory

class Finder:
    def findDirectory(root, files):
        matches = []

        for file in files:
            if(re.match(r'^\w+$', file)):
                directory = Directory(root + '/' + file)
                matches.append(directory)
        
        return matches

    def findFiles(pathToDirectory, pattern):
        rootDirectory = Directory(pathToDirectory)
        stack = [rootDirectory]
        matches = []

        while(stack):
            currentDirectory = stack.pop()
            files = currentDirectory.getListFilest()

            for file in files:
                if(re.match(pattern, file)):
                    matches.append(currentDirectory.getRoot() + '/' + file)
            
            stack += Finder.findDirectory(currentDirectory.getRoot(), files)
        
        return matches
