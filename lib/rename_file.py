from hellbox import Chute


class RenameFile(Chute):
    def __init__(self, *, prefix=None, suffix=None):
        self.prefix = prefix
        self.suffix = suffix

    def run(self, files):
        return [self._rename(file) for file in files]

    def _rename(self, file):
        name = ""
        if self.prefix:
            name += self.prefix
        name += file.root
        if self.suffix:
            name += self.suffix
        name += f".{file.extension}"

        return file.copy(basename=name)
