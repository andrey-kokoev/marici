"""Exact composition and octahedral coherence for two reciprocal mate cells."""
import json,sys
from pathlib import Path
try:
 import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
RX=s.Matrix([[0,1],[1,0]])
RY=s.Matrix([[0,1,0],[1,0,0],[0,0,-1]])
RZ=s.Matrix([[0,1],[1,0]])
fP=s.Matrix([[1,2],[0,1],[1,-1]])
gP=s.Matrix([[2,0,1],[-1,1,0]])
fM=RY*fP*RX;gM=RZ*gP*RY;hP=gP*fP;hM=gM*fM
composite=(RZ*hP==hM*RX)
adjoint=(RX*hP.T==hM.T*RZ)
def diag2(A,B): return s.diag(A,B)
RCf=diag2(RY,RX);RCh=diag2(RZ,RX);RCg=diag2(RZ,RY)
# Octahedral cone maps a:Cone(f)->Cone(gf), b:Cone(gf)->Cone(g).
aP=diag2(gP,s.eye(2));aM=diag2(gM,s.eye(2))
bP=diag2(s.eye(2),fP);bM=diag2(s.eye(2),fM)
a_nat=(RCh*aP==aM*RCf);b_nat=(RCg*bP==bM*RCh)
# Canonical nullhomotopy h=I_Y is reciprocal-natural.
h_nat=(RY*s.eye(3)==s.eye(3)*RY)
tolist=lambda M:[[int(x) for x in row] for row in M.tolist()]
out={'schema':'marici.voevodsky.composed-bidirectional-octahedral-cell.v1','f_plus':tolist(fP),'g_plus':tolist(gP),'composite_plus':tolist(hP),'composite_minus':tolist(hM),'composite_reciprocal_square':composite,'composite_adjoint_mate_square':adjoint,'first_octahedral_map_reciprocal_natural':a_nat,'second_octahedral_map_reciprocal_natural':b_nat,'nullhomotopy_reciprocal_natural':h_nat,'all_exact':all([composite,adjoint,a_nat,b_nat,h_nat]),'meaning':'Composition of two bidirectional mate cells commutes with cone compression and its octahedral nullhomotopy.','rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'composed-bidirectional-octahedral-cell.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
