import os
import sys
from Directory.Folder import Folder

from Directory.Path import Path

class Builder:
    def __init__(self, args):
        if len(args) < 2:
            print("python build.py <FILE_NAME> <PLATFORM>")
            print("    PLATFORM: win / lin")

            self._init = False
            return

        self.args = args
        self.workspace_dir = self.args[0]
        self.home_dir = self.args[1]

        self._init = True
    
    def build_pixa_lib_win(self):
        includes = [f"{self.workspace_dir}inc"]
        src_files = [f"{self.workspace_dir}src/*.c"]

        build_cmd = "clang -fuse-ld=llvm-lib "

        # add source-files
        for i in src_files:
            build_cmd += f"{i} "

        # add includes
        for i in includes:
            build_cmd += f"-I{i} "

        
        build_cmd += f"-o{self.workspace_dir}/lib/windows/pixa32s.lib"
        
        print(f"Executing: {build_cmd}")
        ret = os.system(build_cmd)

def build_example():
    pass

def build_pixa_lib():
    includes = []

def main():
    includes = []
    src_files = []

    if len(sys.argv) < 2:
        print("python build.py <FILE_NAME> <PLATFORM>")
        print("    PLATFORM: win / lin")

        return False

    workspace_dir = sys.argv[0]
    home_dir = sys.argv[1]

    return True

if __name__ == "__main__":
    path = Path.read(Path.parse("./example_dir/"), True)

    if path:
        path.root().print()

    # f = Folder.read(path.root(), True)
    # f.print()

    # Path.parse("./example_dir/asdf").root().print()
    # print(Path.parse("./example_dir/asdf").exists())
    # Folder.from_path(Path.parse("./example_dir/"), True).print()