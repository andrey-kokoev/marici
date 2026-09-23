"""Compute sixfold residue of cyclic top-cell G_+(2,9) form on four-mass loop cell."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
source=(ROOT/'research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex').read_text()
assert r'\frac{d^{2\times n} C}{\mathrm{vol}(GL(2))}' in source
assert r'(12)(23)\cdots(n1)' in source
w2,w4,w5,w6,w7,w8,t,u=s.symbols('w2 w4 w5 w6 w7 w8 t u')
a,b,c,h,e,f=s.symbols('a b c h e f')
sources=(w2,w4,w5,w6,w7,w8,t,u);normals=(a,b,c,h,e,f)
C=s.Matrix([[1,w2,b,0,-h,-w5,-w6,-w7,-w8],
            [0,a,c,1,w4,w5*t,w6*(t-e),w7*u,w8*(u-f)]])
D=s.Matrix([[1,w2,0,0,0,-w5,-w6,-w7,-w8],
            [0,0,0,1,w4,w5*t,w6*t,w7*u,w8*u]])
assert C.subs(dict.fromkeys(normals,0))==D
assert C[:,[0,3]]==s.eye(2)
free=(1,2,4,5,6,7,8)
ambient=s.Matrix([C[row,j] for j in free for row in range(2)])
J=s.factor(ambient.jacobian(sources+normals).det(method='domain-ge'))
assert J!=0

def minor(i,j):return s.factor(s.det(s.Matrix.hstack(C[:,i],C[:,j])))
cyclic=[minor(i,(i+1)%9) for i in range(9)]
expected=[a,w2*c-a*b,b,h,w5*(w4-h*t),w5*w6*e,
          w6*w7*(t-e-u),w7*w8*f,-w8*(u-f)]
assert all(s.factor(x-y)==0 for x,y in zip(cyclic,expected)),list(zip(cyclic,expected))
zero=dict.fromkeys(normals,0)
# The six pole factors in the chosen transverse coordinate order
# a,b,c,h,e,f have leading coefficients 1,1,w2,1,w5*w6,w7*w8.
leading=w2*w5*w6*w7*w8
remaining=s.prod(cyclic[i].subs(zero) for i in (4,6,8))
assert s.factor(remaining)==-w4*w5*w6*w7*w8*u*(t-u)
residue=s.factor(J.subs(zero)/(leading*remaining))
source_density=-s.S.One/(w2*w4*w5*w6*w7*w8*u*(t-u))
relative=s.factor(residue/source_density)
assert relative in (s.S.One,-s.S.One)
# Cross-check simultaneous multivariate local residue does not hide a
# nonnormal-crossing factor: (23)=w2*c-a*b, so the b,c residue at a=0
# is normal crossing for generic w2 != 0.
assert cyclic[1]==w2*c-a*b
assert s.factor(J/(w5*w6*w7*w8)) in (s.S.One,-s.S.One)
report={'schema':'marici.nima.nine-point-loop-canonical-residue.v1','passed':True,
 'source_formula':'d^(2xn)C/volGL2 divided by (12)(23)...(n1), gauge C[:,(phys1,phys4)]=I2, free columns phys(2,3,5,6,7,8,9) in column-major differential order.',
 'coordinate_order':{'source':['w2','w4','w5','w6','w7','w8','t','u'],
                     'normals':['a','b','c','h','e','f']},
 'cyclic_adjacent_minors':[str(v) for v in cyclic],
 'gauge_measure_coordinate_jacobian':str(J),
 'sixfold_residue_density':str(residue),
 'sourced_eight_point_fourmass_cell_density':str(source_density),
 'top_to_source_orientation_sign_in_declared_coordinate_order':int(relative),
 'interpretation':'The sixfold pole of the primary sourced cyclic top-cell G(2,9) measure on the positive loop/parallel-pair cell reproduces the intrinsic sourced fourmass cell dlog form up to the explicit orientation sign. This fixes a LOCAL source-contour residue of the top Grassmannian measure, NOT the positive image canonical form or its six-dimensional fibre pushforward.'}
(OUT/'nine-point-loop-canonical-residue.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'relative_orientation':int(relative),'cyclic_poles':6},indent=2))
