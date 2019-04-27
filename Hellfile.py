from hellbox import Hellbox
from hellbox.jobs.dsig import InsertDummyDsig
from hellbox.jobs.fontmake import GenerateOtf, GenerateTtf

from lib.autohint import Autohint
from lib.woff import GenerateWoff
from lib.woff2 import GenerateWoff2


PostProduction = Hellbox.compose(InsertDummyDsig(), Autohint())


Hellbox.default = "build"

with Hellbox("build") as task:
    task.describe("Builds font files from source")

    source = task.read("source/*.ufo")
    otf = source >> GenerateOtf() >> PostProduction()
    ttf = source >> GenerateTtf() >> PostProduction()
    woff = ttf >> GenerateWoff()
    woff2 = ttf >> GenerateWoff2()

    otf >> task.write("build/otf")
    ttf >> task.write("build/ttf")
    woff >> task.write("build/woff")
    woff2 >> task.write("build/woff2")
