#Alban de Chasteigner 2018
#twitter : @geniusloci_bim
#geniusloci.bim@gmail.com
#https://github.com/albandechasteigner/GeniusLociForDynamo

import clr
import math
clr.AddReference("RevitServices")
import RevitServices 
from RevitServices.Persistence import DocumentManager
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
version=int(app.VersionNumber)

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

inputdoc = UnwrapElement(IN[0]) if isinstance(IN[0],list) else [UnwrapElement(IN[0])]
sw = IN[1]

#Inputdoc : Part of script by Andreas Dieckmann
if inputdoc[0] == None:
    doc = DocumentManager.Instance.CurrentDBDocument
elif isinstance(inputdoc[0],Document):
    doc = inputdoc[0]
elif isinstance(inputdoc[0],RevitLinkInstance):
    doc = inputdoc[0].GetLinkDocument()
else: doc = DocumentManager.Instance.CurrentDBDocument

if version < 2021:
	angleUnit = doc.GetUnits().GetFormatOptions(UnitType.UT_Angle).DisplayUnits
else:
	angleUnit = doc.GetUnits().GetFormatOptions(SpecTypeId.Angle).GetUnitTypeId()

outProjBasePt, outProjSurvPt, outProjLoc = [],[],[]

pbp = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_ProjectBasePoint).ToElements()
sbp = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_SharedBasePoint).ToElements()

projPos = doc.ActiveProjectLocation.GetProjectPosition(XYZ(0,0,0))

outProjBasePt = [pbp[0].SharedPosition.ToPoint(),abs(360-(round(Autodesk.Revit.DB.UnitUtils.ConvertFromInternalUnits(projPos.Angle,angleUnit),6)))]
outProjSurvPt = sbp[0].SharedPosition.ToPoint()
    	
if projPos == None:
	outProjLoc.append("No Project Position at origin point")
else:
	outProjLoc = XYZ(projPos.EastWest,projPos.NorthSouth,0).ToPoint()
	
OUT = outProjLoc, outProjBasePt, outProjSurvPt, doc.ActiveProjectLocation.Name
