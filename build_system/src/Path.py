import os


class Path():
    def __init__(self, name, parent = None, *children):
        self.name = name
        self.parent = parent
        self.children = list(children)

    def __str__(self):
        prefix = "Path"

        if self.is_folder():
            prefix = "Folder"
        elif self.is_file():
            prefix = "File"

        return f"{prefix}: {self.name}"

    def __repr__(self):
        return str(self)
    
    def is_folder(self):
        return os.path.isdir(self.full_path())
    
    def is_file(self):
        return os.path.isfile(self.full_path())

    def full_path(self):
        if self.parent != None:
            return self.parent.full_path() + "/" + self.name
        
        return self.name

    def exists(self):
        return os.path.exists(self.full_path())
    
    def root(self):
        if self.parent is not None:
            return self.parent.root()
        else:
            return self

    def print(self, indent = "", is_last = True):
        marker = "└──" if is_last else "├──"
        print(indent + marker + str(self))

        indent += "    " if is_last else "│   "
        for i, child in enumerate(self.children):
            child.print(indent, i == len(self.children) - 1)
    
    @staticmethod
    def parse(path: str):
        path_split = path.split("/")

        if len(path_split) == 0:
            return None
        
        root = Path("")
        last = root

        for i in path_split:
            if len(i) != 0:
                child = Path(i, last if len(last.name) != 0 else None)
                last.children.append(child)
                last = child

        return last
    
    @staticmethod
    def read(path, recursive = False):
        if len(path.children) != 0:
            return None

        if path.exists():
            for i in os.scandir(path.full_path()):
                child = Path(i.name, path)
                path.children.append(child)

                if recursive:
                    child = Path.read(child)

            return path

        else:
            return None