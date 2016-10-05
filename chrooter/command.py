import subprocess
import os

class Command:
    def __init__(self, cmd):
        self.command_string = cmd

    def get_deps(self):
        dependencies = []
        out_stream = subprocess.Popen(['ldd', self.command_string],
                                      stdout=subprocess.PIPE)
        for line in out_stream.stdout:
            try:
                file_path = line.split('/', 1)[1].rsplit(' ',1)[0]
                file_path = os.path.join('/', file_path)
                dependencies.append(file_path)
            except IndexError as exception:
                continue
        return dependencies
