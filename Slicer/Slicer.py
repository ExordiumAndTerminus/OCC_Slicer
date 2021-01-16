from UnitAlg import Plane
#from OCC
import shapely
from .OCC_To_Shapely import *
from OCC.Core.TopoDS import topods, TopoDS_Face, TopoDS_Shape, TopoDS_Compound, TopoDS_Iterator
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeFace
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Section
from OCC.Core.TopOpeBRepTool import TopOpeBRepTool_ShapeExplorer
from OCC.Core.TopAbs import TopAbs_FACE, TopAbs_EDGE, TopAbs_SHAPE
from OCC.Core.TopExp import TopExp_Explorer

class Slicer():
    def slice(self, geometry:TopoDS_Shape, plane:Plane) -> Polygon:
        face = BRepBuilderAPI_MakeFace(plane).Shape()
        section = BRepAlgoAPI_Section(geometry, plane)
        section.Build()
        piece = section.Shape()
        #section.Shape creates a topoDSCompound
        print(piece)
        # for s in piece:
        #     print("tada")
        explorer = TopOpeBRepTool_ShapeExplorer(piece, TopAbs_FACE)
        faceExplorer = TopExp_Explorer(piece, TopAbs_SHAPE)
        print(faceExplorer.Current())
        iter = TopoDS_Iterator(piece)
        #returns it as an edge...=/
        print(iter.Value())
        # test = Convert(piece)
        # print(test)
        # print(explorer.Current())
        # explorer.Next()
        #TODO: return polygon instead of section
        return piece

#def Slice(geomety:TopoDS_Shape?, plane:Plane) -> Polygon:
    #Do thing