from scanip_api import *
import os
import glob

############################################################################

dims4ph = [364, 364, 400]
dims3ph = [364, 364, 280]
voxDims = [27.5, 27.5, 25.0]
vdims   = [x / 1000.0 for x in voxDims]
path    = "E:\\Tim\\projects\\nano-infiltrates\\mesh\\"
# fileBaseStr = "syn080-scaled-3phase-"
# allFiles = glob.glob(os.path.join(path, "syn080*.raw"))
searchStr3ph = "msri*res27.5*3ph*.raw"
searchStr4ph = "msri*res27.5*4ph*.raw"

############################################################################

allFiles = glob.glob(os.path.join(path, searchStr3ph))
for eachFile in allFiles:
    App.GetInstance().ImportRawImage(eachFile,
                                     ImportOptions.UnsignedCharPixel, dims3ph[0], dims3ph[1], dims3ph[2], vdims[0], vdims[1], vdims[2], 0,
                                     ImportOptions.BinaryFile, ImportOptions.LittleEndian,
                                     CommonImportConstraints().SetWindowLevel(0, 0).SetCrop(0, 0, 0, dims3ph[0], dims3ph[1], dims3ph[2]))

    App.GetDocument().Threshold(1, 1, Doc.CreateNewMask, App.GetDocument().GetSliceIndices(Doc.OrientationYZ), Doc.OrientationYZ)
    App.GetDocument().Threshold(2, 2, Doc.CreateNewMask, App.GetDocument().GetSliceIndices(Doc.OrientationYZ), Doc.OrientationYZ)
    App.GetDocument().Threshold(3, 3, Doc.CreateNewMask, App.GetDocument().GetSliceIndices(Doc.OrientationYZ), Doc.OrientationYZ)

    App.GetDocument().ApplyFillGaps(Doc.MostContactSurface,
        [App.GetDocument().GetMaskByName("Mask 1"),
        App.GetDocument().GetMaskByName("Mask 3"),
        App.GetDocument().GetMaskByName("Mask 2")],
        True, 100)

    # 2017-06-14 20:47:24 - FE model creation
    App.GetDocument().CreateFeModel("Model 1")

    # 2017-06-14 20:47:30 - Objects mode activation
    App.GetDocument().EnableObjectsMode()

    # 2017-06-14 20:47:32 - Part creation
    App.GetDocument().GetModelByName("Model 1").AddMasks(
        [App.GetDocument().GetGenericMaskByName("Mask 1"),
        App.GetDocument().GetGenericMaskByName("Mask 2"),
        App.GetDocument().GetGenericMaskByName("Mask 3")])

    # 2017-06-14 20:47:32 - Models mode activation
    App.GetDocument().EnableModelsMode()

    # 2017-06-14 20:47:51 - Model configuration modification
    App.GetDocument().GetActiveModel().SetEditAdvancedParametersManuallyOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), True)
    App.GetDocument().GetActiveModel().SetEditAdvancedParametersManuallyOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), True)
    App.GetDocument().GetActiveModel().SetEditAdvancedParametersManuallyOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), True)

    App.GetDocument().GetActiveModel().SetTargetMinimumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), 0.05)
    App.GetDocument().GetActiveModel().SetTargetMinimumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), 0.05)
    App.GetDocument().GetActiveModel().SetTargetMinimumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), 0.05)

    App.GetDocument().GetActiveModel().SetTargetMaximumErrorOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), 0.005)
    App.GetDocument().GetActiveModel().SetTargetMaximumErrorOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), 0.005)
    App.GetDocument().GetActiveModel().SetTargetMaximumErrorOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), 0.005)

    App.GetDocument().GetActiveModel().SetMaximumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), 0.25)
    App.GetDocument().GetActiveModel().SetMaximumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), 0.25)
    App.GetDocument().GetActiveModel().SetMaximumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), 0.25)

    App.GetDocument().GetActiveModel().SetInternalChangeRateOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), 50)
    App.GetDocument().GetActiveModel().SetInternalChangeRateOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), 50)
    App.GetDocument().GetActiveModel().SetInternalChangeRateOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), 50)

    App.GetDocument().GetActiveModel().SetSmoothAgainstBackground(True)
    App.GetDocument().GetActiveModel().SetRefineNearSlits(False)

    App.GetDocument().GenerateMesh()
    App.GetDocument().SaveAs(eachFile.replace(".raw",".sip"))
    ############################ Save triple line statistics into csv file #################################
    template_name = "General statistics (perimeters)"
    # doc, the document open in ScanIP, is an instance of the Doc class
    doc = App.GetDocument()
    doc.SetModelStatisticsTemplate(template_name, False)
    doc.UpdateModelStatisticsData()
    doc.ExportModelStatisticsData(eachFile.replace(".raw","-perimeters.csv"))
    ########################################################################################################
    App.GetDocument().Close()


######################################################################################################################################################################################

allFiles = glob.glob(os.path.join(path, searchStr4ph))
for eachFile in allFiles:
    App.GetInstance().ImportRawImage(eachFile,
                                     ImportOptions.UnsignedCharPixel, dims4ph[0], dims4ph[1], dims4ph[2], vdims[0], vdims[1], vdims[2], 0,
                                     ImportOptions.BinaryFile, ImportOptions.LittleEndian,
                                     CommonImportConstraints().SetWindowLevel(0, 0).SetCrop(0, 0, 0, dims4ph[0], dims4ph[1], dims4ph[2]))


    App.GetDocument().Threshold(1, 1, Doc.CreateNewMask, App.GetDocument().GetSliceIndices(Doc.OrientationYZ), Doc.OrientationYZ)
    App.GetDocument().Threshold(2, 2, Doc.CreateNewMask, App.GetDocument().GetSliceIndices(Doc.OrientationYZ), Doc.OrientationYZ)
    App.GetDocument().Threshold(3, 3, Doc.CreateNewMask, App.GetDocument().GetSliceIndices(Doc.OrientationYZ), Doc.OrientationYZ)
    App.GetDocument().Threshold(4, 4, Doc.CreateNewMask, App.GetDocument().GetSliceIndices(Doc.OrientationYZ), Doc.OrientationYZ)

    # App.GetDocument().GetMaskByName("Mask 4").Activate()
    # App.GetDocument().ApplyIslandRemovalFilter(64)

    App.GetDocument().ApplyFillGaps(Doc.MostContactSurface,
        [App.GetDocument().GetMaskByName("Mask 1"),
        App.GetDocument().GetMaskByName("Mask 3"),
        App.GetDocument().GetMaskByName("Mask 4"),
        App.GetDocument().GetMaskByName("Mask 2")],
        True, 100)

    # 2017-06-14 20:47:24 - FE model creation
    App.GetDocument().CreateFeModel("Model 1")

    # 2017-06-14 20:47:30 - Objects mode activation
    App.GetDocument().EnableObjectsMode()

    # 2017-06-14 20:47:32 - Part creation
    App.GetDocument().GetModelByName("Model 1").AddMasks(
        [App.GetDocument().GetGenericMaskByName("Mask 1"),
        App.GetDocument().GetGenericMaskByName("Mask 2"),
        App.GetDocument().GetGenericMaskByName("Mask 3"),
        App.GetDocument().GetGenericMaskByName("Mask 4")])

    # 2017-06-14 20:47:32 - Models mode activation
    App.GetDocument().EnableModelsMode()

    # 2017-06-14 20:47:51 - Model configuration modification
    App.GetDocument().GetActiveModel().SetCompoundCoarsenessOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), -15)

    App.GetDocument().GetActiveModel().SetEditAdvancedParametersManuallyOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), True)
    App.GetDocument().GetActiveModel().SetEditAdvancedParametersManuallyOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), True)
    App.GetDocument().GetActiveModel().SetEditAdvancedParametersManuallyOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), True)
    App.GetDocument().GetActiveModel().SetEditAdvancedParametersManuallyOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), True)

    App.GetDocument().GetActiveModel().SetTargetMinimumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), 0.05)
    App.GetDocument().GetActiveModel().SetTargetMinimumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), 0.05)
    App.GetDocument().GetActiveModel().SetTargetMinimumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), 0.05)

    App.GetDocument().GetActiveModel().SetTargetMaximumErrorOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), 0.005)
    App.GetDocument().GetActiveModel().SetTargetMaximumErrorOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), 0.005)
    App.GetDocument().GetActiveModel().SetTargetMaximumErrorOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), 0.005)

    App.GetDocument().GetActiveModel().SetMaximumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), 0.25)
    App.GetDocument().GetActiveModel().SetMaximumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), 0.25)
    App.GetDocument().GetActiveModel().SetMaximumEdgeLengthOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), 0.25)

    App.GetDocument().GetActiveModel().SetInternalChangeRateOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), 50)
    App.GetDocument().GetActiveModel().SetInternalChangeRateOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), 50)
    App.GetDocument().GetActiveModel().SetInternalChangeRateOnPart(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), 50)

    App.GetDocument().GetActiveModel().SetSmoothAgainstBackground(True)
    App.GetDocument().GetActiveModel().SetRefineNearSlits(False)

    # 2017-06-14 20:47:53 - Contact creation
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), App.GetDocument().GetActiveModel().GetPartByName("Mask 1"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), App.GetDocument().GetActiveModel().GetPartByName("Mask 2"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), App.GetDocument().GetActiveModel().GetPartByName("Mask 3"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), App.GetDocument().GetActiveModel().GetPartByName("Mask 4"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), Model.Xmin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), Model.Xmax)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), Model.Ymin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), Model.Ymax)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), Model.Zmin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), Model.Zmax)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), App.GetDocument().GetActiveModel().GetPartByName("Mask 1"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), App.GetDocument().GetActiveModel().GetPartByName("Mask 2"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), App.GetDocument().GetActiveModel().GetPartByName("Mask 3"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), App.GetDocument().GetActiveModel().GetPartByName("Mask 4"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), Model.Xmin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), Model.Xmax)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), Model.Ymin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), Model.Ymax)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), Model.Zmin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), Model.Zmax)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), App.GetDocument().GetActiveModel().GetPartByName("Mask 1"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), App.GetDocument().GetActiveModel().GetPartByName("Mask 2"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), App.GetDocument().GetActiveModel().GetPartByName("Mask 3"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), App.GetDocument().GetActiveModel().GetPartByName("Mask 4"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), Model.Xmin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), Model.Xmax)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), Model.Ymin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), Model.Ymax)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), Model.Zmin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), Model.Zmax)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), App.GetDocument().GetActiveModel().GetPartByName("Mask 1"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), App.GetDocument().GetActiveModel().GetPartByName("Mask 2"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), App.GetDocument().GetActiveModel().GetPartByName("Mask 3"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), App.GetDocument().GetActiveModel().GetPartByName("Mask 4"))
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), Model.Xmin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), Model.Xmax)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), Model.Ymin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), Model.Ymax)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), Model.Zmin)
    App.GetDocument().GetActiveModel().AddSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), Model.Zmax)

    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), App.GetDocument().GetActiveModel().GetPartByName("Mask 1"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), App.GetDocument().GetActiveModel().GetPartByName("Mask 1"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), App.GetDocument().GetActiveModel().GetPartByName("Mask 2"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), App.GetDocument().GetActiveModel().GetPartByName("Mask 1"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), App.GetDocument().GetActiveModel().GetPartByName("Mask 3"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), App.GetDocument().GetActiveModel().GetPartByName("Mask 1"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 1"), App.GetDocument().GetActiveModel().GetPartByName("Mask 4"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), App.GetDocument().GetActiveModel().GetPartByName("Mask 1"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), App.GetDocument().GetActiveModel().GetPartByName("Mask 2"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), App.GetDocument().GetActiveModel().GetPartByName("Mask 2"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), App.GetDocument().GetActiveModel().GetPartByName("Mask 3"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), App.GetDocument().GetActiveModel().GetPartByName("Mask 2"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 2"), App.GetDocument().GetActiveModel().GetPartByName("Mask 4"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), App.GetDocument().GetActiveModel().GetPartByName("Mask 2"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), App.GetDocument().GetActiveModel().GetPartByName("Mask 3"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), App.GetDocument().GetActiveModel().GetPartByName("Mask 3"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 3"), App.GetDocument().GetActiveModel().GetPartByName("Mask 4"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), App.GetDocument().GetActiveModel().GetPartByName("Mask 3"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), App.GetDocument().GetActiveModel().GetPartByName("Mask 4"))
    App.GetDocument().GetActiveModel().RemoveSurfaceContact(App.GetDocument().GetActiveModel().GetPartByName("Mask 4"), App.GetDocument().GetActiveModel().GetPartByName("Mask 4"))

    App.GetDocument().GenerateMesh()
    App.GetDocument().ExportAbaqusVolume(eachFile.replace(".raw",".inp"), False)
    App.GetDocument().SaveAs(eachFile.replace(".raw",".sip"))
    ############################ Save triple line statistics into csv file #################################
    template_name = "General statistics (volumes)"
    # doc, the document open in ScanIP, is an instance of the Doc class
    doc = App.GetDocument()
    doc.SetModelStatisticsTemplate(template_name, False)
    doc.UpdateModelStatisticsData()
    doc.ExportModelStatisticsData(eachFile.replace(".raw","-volumes.csv"))
    ########################################################################################################
    App.GetDocument().Close()
