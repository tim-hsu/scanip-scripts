from scanip_api import *
import os
import glob

############################################################################

# dims4ph = [364,364,400]
# dims3ph = [364,364,280]
# voxDims = [27.5,27.5,25.0]
# vdims   = [x / 1000.0 for x in voxDims]
path    = "E:\\Tim\\projects\\first-moose-paper\\data\\mesh\\"
searchStr3ph = "*4ph*.sip"

############################################################################

allFiles = glob.glob(os.path.join(path, searchStr3ph))
for eachFile in allFiles:
    app = App.GetInstance()
    app.OpenDocument(eachFile)
    App.GetDocument().GenerateMesh()

    # template_name = "General statistics (perimeters)"
    # export_path =   eachFile.replace('.sip','-perimeters.csv')
    template_name = "General statistics (volumes)"
    export_path =   eachFile.replace('.sip','-volumes.csv')

    # doc, the document open in ScanIP, is an instance of the Doc class
    doc = App.GetDocument()
    doc.SetModelStatisticsTemplate(template_name, False)
    doc.UpdateModelStatisticsData()
    doc.ExportModelStatisticsData(export_path)

    App.GetDocument().Close()
