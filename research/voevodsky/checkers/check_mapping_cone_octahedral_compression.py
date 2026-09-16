"""Exact finite model of path compression by mapping cones.

For X-f->Y-g->Z, verifies the two cone comparison maps and the canonical
nullhomotopy of their composite, the basic octahedral compression cell.
"""
import json,sys
from pathlib import Path
try:
 import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
f=s.Matrix([[1,2],[0,1],[1,-1]])       # Y(3) <- X(2)
g=s.Matrix([[2,0,1],[-1,1,0]])        # Z(2) <- Y(3)
gf=g*f
# Cone(f): d=f; Cone(gf): d=gf; Cone(g): d=g.
# a=(a1=I_X,a0=g), b=(b1=f,b0=I_Z).
a1=s.eye(2);a0=g;b1=f;b0=s.eye(2)
chain_a=(gf*a1==a0*f)
chain_b=(g*b1==b0*gf)
# ba is canonically chain-nullhomotopic by h=I_Y: degree-zero Y -> degree-one Y.
h=s.eye(3)
null_deg0=(b0*a0==g*h)
null_deg1=(b1*a1==h*f)
tolist=lambda M:[[int(x) for x in row] for row in M.tolist()]
out={'schema':'marici.voevodsky.mapping-cone-octahedral-compression.v1','f':tolist(f),'g':tolist(g),'gf':tolist(gf),'cone_comparison_a_is_chain_map':chain_a,'cone_comparison_b_is_chain_map':chain_b,'composite_ba_nullhomotopy_degree_0':null_deg0,'composite_ba_nullhomotopy_degree_1':null_deg1,'all_exact':all([chain_a,chain_b,null_deg0,null_deg1]),'meaning':'The lower path X->Y->Z compresses to X->Z while Cone(f), Cone(gf), Cone(g) retain the residual and form the canonical octahedral triangle.','rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'mapping-cone-octahedral-compression.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
