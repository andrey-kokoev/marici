"""Exact finite fixture for reciprocal forward/backward mate coherence."""
import json,sys
from pathlib import Path
try:
 import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
# Reciprocal involutions on state and output fibers.
RX=s.Matrix([[0,1,0],[1,0,0],[0,0,-1]])
RY=s.Matrix([[0,1],[1,0]])
Dp=s.Matrix([[1,2,0],[-1,0,3]])
Dm=RY*Dp*RX
forward=(RY*Dp==Dm*RX)
backward=(RX*Dp.T==Dm.T*RY)
# Cone(D)=Y degree 0 plus X degree 1. Reciprocal cone map is diag(RY,RX).
cone_plus=s.zeros(5);cone_plus[:2,2:]=Dp
cone_minus=s.zeros(5);cone_minus[:2,2:]=Dm
Rcone=s.diag(RY,RX)
cone_chain=(Rcone*cone_plus==cone_minus*Rcone)
cone_involution=(Rcone*Rcone==s.eye(5))
# Hodge operator on Y+X and its reciprocal covariance.
Qp=s.Matrix.vstack(s.Matrix.hstack(s.zeros(2),Dp),s.Matrix.hstack(Dp.T,s.zeros(3)))
Qm=s.Matrix.vstack(s.Matrix.hstack(s.zeros(2),Dm),s.Matrix.hstack(Dm.T,s.zeros(3)))
hodge=(Rcone*Qp==Qm*Rcone)
tolist=lambda M:[[int(x) for x in row] for row in M.tolist()]
out={'schema':'marici.voevodsky.bidirectional-adjoint-mate-cone-cell.v1','R_X':tolist(RX),'R_Y':tolist(RY),'D_plus':tolist(Dp),'D_minus':tolist(Dm),'forward_square_commutes':forward,'backward_adjoint_square_commutes':backward,'reciprocal_cone_map_is_chain_map':cone_chain,'reciprocal_cone_map_is_involution':cone_involution,'hodge_operator_is_reciprocal_covariant':hodge,'all_exact':all([forward,backward,cone_chain,cone_involution,hodge]),'meaning':'Fixed forward transport, compatible backward possibility, reciprocal exchange, cone compression, and Hodge enhancement form one coherent bidirectional cell.','rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'bidirectional-adjoint-mate-cone-cell.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
