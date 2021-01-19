from UnitAlg import Plane
#from OCC
from OCC.Core.TopoDS import TopoDS_Face, TopoDS_Shape
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeFace
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Common
from OCC.Core.TopAbs import TopAbs_FACE
from OCC.Core.TopExp import TopExp_Explorer


class Slicer():
    def slice(self, geometry:TopoDS_Shape, plane:Plane) -> TopoDS_Face:
        slicePlane = BRepBuilderAPI_MakeFace(plane).Shape()
        section = BRepAlgoAPI_Common(geometry, slicePlane).Shape()
        faceExplorer = TopExp_Explorer(section, TopAbs_FACE)
        faces = []
        while faceExplorer.More():
            faces.append(faceExplorer.Current())
            faceExplorer.Next()
        return faces