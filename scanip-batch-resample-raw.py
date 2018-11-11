from scanip_api import *
import os
import glob

############################################################################

dims3ph         = [323,323,226]

currentVoxSize  = [30.9140,30.9140,30.9140] # (nm)
vd              = [x / 1000.0 for x in currentVoxSize]

targetVoxSize   = [40.0,40.0,40.0] # (nm)
vdt             = [x / 1000.0 for x in targetVoxSize]

path            = "E:\\Tim\\projects\\first-moose-paper\\data\\mesh\\"
searchStr3ph    = "syn015*3ph*.raw"

# fileBaseStr = "syn080-scaled-3phase-"
# allFiles = glob.glob(os.path.join(path, "syn080*.raw"))

############################################################################

allFiles = glob.glob(os.path.join(path, searchStr3ph))
for eachFile in allFiles:
    App.GetInstance().ImportRawImage(eachFile,
                                     ImportOptions.UnsignedCharPixel,
                                     dims3ph[0], dims3ph[1], dims3ph[2],
                                     vd[0], vd[1], vd[2], 0,
                                     ImportOptions.BinaryFile,
                                     ImportOptions.LittleEndian,
                                     CommonImportConstraints().SetWindowLevel(0, 0).SetCrop(0, 0, 0, dims3ph[0], dims3ph[1], dims3ph[2]))

    App.GetDocument().ResampleDataByPixelSpacing(vdt[0], vdt[1], vdt[2],
                                                 Doc.NearestNeighbourInterpolation,
                                                 Doc.NearestNeighbourInterpolation)

    App.GetDocument().GetBackgroundByName("Raw import  [W:0.00 L:0.00]").RawExport(eachFile.replace(".raw","-resample-" + str(targetVoxSize[0]) + "nm.raw"))
    App.GetDocument().SaveAs(eachFile.replace(".raw","-resample-" + str(targetVoxSize[0]) + "nm.sip"))
    App.GetDocument().Close()
