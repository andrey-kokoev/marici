"""Generic on-shell Ward basis: reduce a single-flavor four-form to three entries.

Independent SL(2)/GL(2) frame choices set lambda columns1,2 and tilde
columns6,7 to identity, on the corresponding regular open. Momentum
conservation determines tilde columns1,2. All remaining spinors are symbolic.
"""
from pathlib import Path
import itertools,json
import sympy as s
root=Path(__file__).resolve().parents[1]
l=s.symbols('l13:18')+s.symbols('l23:28');r=s.symbols('r13:16')+s.symbols('r23:26')
L=s.eye(2).row_join(s.Matrix(2,5,l))
Rtail=s.Matrix(2,3,r).row_join(s.eye(2))
R=(-Rtail*L[:,2:].T).row_join(Rtail)
assert L*R.T==s.zeros(2)
# U_i has zero entries1,2 and solves the two anti-supercharge constraints.
U=s.zeros(3,7)
for i in range(3):
 U[i,i+2]=1;U[i,5]=-R[0,i+2];U[i,6]=-R[1,i+2]
assert U*R.T==s.zeros(3,2)
K=L.col_join(U)
assert K[:,:5].det()==1
choices=list(itertools.combinations(range(7),4));pairs=list(itertools.combinations(range(3),2));columns=[]
for i,j in pairs:
 M=L.col_join(U[[i,j],:])
 columns.append(s.Matrix([s.expand(M[:,list(subset)].det(method='domain-ge')) for subset in choices]))
B=s.Matrix.hstack(*columns)
pivots=[choices.index((0,1,2,3)),choices.index((0,1,2,4)),choices.index((0,1,3,4))]
assert B[pivots,:]==s.eye(3)
# Check Q multiplication (exterior wedge) and anti-Q contraction identically.
for c in range(3):
 for spin in range(2):
  for subset in itertools.combinations(range(7),5):
   value=sum((-1)**j*L[spin,i]*B[choices.index(tuple(k for k in subset if k!=i)),c] for j,i in enumerate(subset))
   assert s.expand(value)==0
  for subset in itertools.combinations(range(7),3):
   value=0
   for i in range(7):
    if i in subset:continue
    larger=tuple(sorted((*subset,i)));value+=(-1)**larger.index(i)*R[spin,i]*B[choices.index(larger),c]
   assert s.expand(value)==0
report={'passed':True,'generic_spinor_parameters':list(map(str,(*l,*r))),'lambda':[[str(v) for v in row] for row in L.tolist()],'tilde_lambda':[[str(v) for v in row] for row in R.tolist()],'kernel_basis':[[str(v) for v in row] for row in K.tolist()],'four_form_basis':[[str(v) for v in row] for row in B.tolist()],'pivot_subsets_1_based':[[i+1 for i in choices[p]] for p in pivots],'pivot_matrix':'identity3','symbolic_Ward_checks':3*2*(21+35),'scope':'Generic on-shell single-flavor Ward space on the frame open <12> [67] !=0. Exterior-algebra dimension argument reduces all four-form tensors obeying both Ward constraints to this3-dimensional basis. Not yet a generic amplitude parity identity.'}
(root/'results/seven-point-universal-ward-basis.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'symbolic_parameters':16,'basis_dimension':3,'symbolic_Ward_checks':report['symbolic_Ward_checks'],'pivot_subsets':report['pivot_subsets_1_based']}))
