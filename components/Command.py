class Command:
    def createCompilerCommand(files, bootstrap):
        files = ' '.join(files)
        command = 'g++ ' + files + ' '

        if(bootstrap):
            command += bootstrap

        return command