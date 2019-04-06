# brew install ttfautohint

from hellbox import Chute, Hellbox


class Autohint(Chute):
    def run(self, files):
        return [self._hint(file) for file in files]

    def _hint(self, file):
        Hellbox.info(f"Hinting: {file.basename}")

        if file.extension == "ttf":
            return file.transform("ttfautohint \"{input}\" \"{output}\"")
        elif file.extension == "otf":
            return file.transform("autohint -o \"{output}\" -nb -q \"{input}\"")
        else:
            Hellbox.warn(f"Skipping {file.basename} (not a hintable format)")
            return file
