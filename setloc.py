import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

locations = FilteredElementCollector(doc).OfClass(ProjectLocation).ToElements()
TransactionManager.Instance.EnsureInTransaction(doc)
for loc in locations:
	if loc.Name == IN[0]:
		doc.ActiveProjectLocation = loc
		break
	else:
		pass
TransactionManager.Instance.TransactionTaskDone()

OUT = loc
