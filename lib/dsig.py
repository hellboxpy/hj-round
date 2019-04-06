from fontTools import ttLib
from hellbox import Chute, Hellbox


class DummyDsig(Chute):
    def run(self, files):
        return [self._insert_dummy(file) for file in files]

    def _insert_dummy(self, file):
        Hellbox.info(f"Updating DSIG: {file.basename}")

        copy = file.copy()

        font = ttLib.TTFont(copy.content_path)
        font.tables["DSIG"] = self._create_signature()
        font.save(copy.content_path)

        return copy

    def _create_signature(self):
        signature = ttLib.newTable("DSIG")
        signature.ulVersion = 1
        signature.usFlag = 0
        signature.usNumSigs = 0
        signature.signatureRecords = []
        return signature
