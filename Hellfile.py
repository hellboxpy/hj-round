from hellbox import Hellbox
from hellbox.jobs.dsig import InsertDummyDsig
from hellbox.jobs.fontmake import GenerateOtf, GenerateTtf
from hellbox.jobs.ttfautohint import Autohint
from hellbox.jobs.woff2 import GenerateWoff2

Hellbox.default = "build"

with Hellbox("build") as task:
    task.describe("Builds font files from source")
    task.clean("build")

    source = task.read("source/*.ufo")
    source >> GenerateOtf() >> InsertDummyDsig() >> task.write("build/otf")

    ttf = source >> GenerateTtf() >> InsertDummyDsig() >> Autohint()
    ttf >> task.write("build/ttf")
    ttf >> GenerateWoff2() >> task.write("build/woff2")
