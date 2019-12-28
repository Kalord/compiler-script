import os

class Directory:
    root = None
    listFiles = []

    def __init__(self, pathToDirectory):
        self.root = pathToDirectory
        self.listFiles = os.listdir(self.root)

    def getRoot(self):
        return self.root

    def getListFilest(self):
        return self.listFiles