# brew tap bramstein/webfonttools
# brew install sfnt2woff-zopfli

from hellbox import Chute, Hellbox


class GenerateWoff(Chute):
    def run(self, files):
        return [self._generate(file) for file in files]

    def _generate(self, file):
        Hellbox.info(f"Generating WOFF: {file.basename}")

        return file.transform("sfnt2woff-zopfli \"{input}\"", extension="woff")
