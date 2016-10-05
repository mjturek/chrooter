import os
import shutil

class Environment:
    def __init__(self, root_path):
        self.root_path = root_path
        if not os.path.exists(self.root_path):
            os.makedirs(root_path)

    def add_command(self, command):
        deps = command.get_deps()
        for dep in deps:
            self.duplicate_into(dep)

    def duplicate_into(self, file_to_dup):
        # If dir doesn't exist in environment, create it
        dest_dir = os.path.join(self.root_path,
                                os.path.dirname(file_to_dup)[1:])
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Then copy it over
        shutil.copy(file_to_dup, dest_dir)
