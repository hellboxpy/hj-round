# brew install woff2

import os
import subprocess
from hellbox import Chute, Hellbox


class GenerateWoff2(Chute):
    def run(self, files):
        return [self._generate(file) for file in files]

    def _generate(self, file):
        Hellbox.info(f"Generating WOFF2: {file.basename}")

        return file.transform("woff2_compress \"{input}\"", extension="woff2")
