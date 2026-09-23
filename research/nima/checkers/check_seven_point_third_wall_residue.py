"""Cyclic source-form residues on the 34/71 versus zero-column-1 wall."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
wall=json.loads((N/'results/seven-point-third-repair-wall.json').read_text());assert wall['inward_side']=='OPPOSITE'
w3,w4,w5,w6,w7,u,v,h,e,f=s.symbols('w3 w4 w5 w6 w7 u v h e f');face=(w3,w4,w5,w6,w7,u,v)
C=s.Matrix([[-h,1,w3,w4,w5,w6,w7],[-h*(v+e),0,w3,w4*(1+f),2*w5,u*w6,v*w7]])
def gauged(M,pivots):
 D=M[:,list(pivots)].inv()*M
 assert D[:,list(pivots)]==s.eye(2)
 return D
def cyclic(M):return s.prod(s.det(M[:,[i,(i+1)%M.cols]]) for i in range(M.cols))
# 7-column top source form: residues at e=f=0 then h=0.
D=gauged(C,(1,4));coords=[D[i,j] for j in (0,2,3,5,6) for i in range(2)]
J=s.Matrix(coords).jacobian((*face,h,e,f))
P=cyclic(D);assert s.factor((P/(e*f)).subs({e:0,f:0}))!=0
L=s.factor((P/(e*f)).subs({e:0,f:0}))
# Computing the full ten-variable determinant is manageable after the
# transverse substitution; no numeric sampling enters the symbolic ratio.
J0=s.factor(J.subs({e:0,f:0}).det())
paired=s.factor((J0/L)*h).subs(h,0)
paired=s.factor(paired);assert paired!=0
# 6-column top form on surviving columns 2..7, residue f=0.
E=gauged(C[:,list(range(1,7))],(0,3))
coords6=[E[i,j] for j in (1,2,4,5) for i in range(2)]
J6=s.factor(s.Matrix(coords6).jacobian((*face,f)).subs({h:0,e:0,f:0}).det())
L6=s.factor((cyclic(E)/f).subs({h:0,e:0,f:0}));assert L6!=0
zero=s.factor(J6/L6)
ratio=s.factor(paired/zero)
assert ratio!=0
report={'schema':'marici.nima.seven-point-third-wall-residue.v1',
 'common_face_coordinates':list(map(str,face)),
 'paired_cell_residue_coefficient':str(paired),'zero_column_residue_coefficient':str(zero),
 'source_residue_ratio':str(ratio),
 'normalization':'Seven-column top cyclic form in gauge columns 2,5, residue order e then f then h, with parameters [face,h,e,f]. Six-column top cyclic form in same pivot gauge, residue f. Overall exterior signs are relative to those declared ordered parameters.',
 'scope':'Symbolic source forms only, not physical generalized-R history identification.'}
(N/'results/seven-point-third-wall-residue.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
