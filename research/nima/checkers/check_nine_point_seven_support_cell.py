"""A full-dimensional n=9 candidate cell retains a polyhedral rank-one kernel fibre."""
import json,itertools
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results'
prior=json.loads((N/'nine-point-determinantal-fibre.json').read_text());assert prior['passed']
K=s.Matrix([[int(x) for x in row] for row in prior['kernel_basis']]);Z=s.Matrix([[j**d for d in range(6)] for j in range(1,10)]);assert K*Z==s.zeros(3,6)
w=s.symbols('w2:8',positive=True);u,v=s.symbols('u v',positive=True)
weights=(s.Integer(1),)+w;slopes=(0,1,1,2,u,u,v)
C=s.zeros(2,9)
for j in range(7):C[:,j]=s.Matrix([weights[j],weights[j]*slopes[j]])
assert C[:,[7,8]]==s.zeros(2,2)
A=s.symbols('a0:3');B=s.symbols('b0:3');T=s.Matrix([A,B]);D=C+T*K
# Each zero column imposes two independent linear equations on T.
assert D[:,8]==s.Matrix([A[2],B[2]])
assert D[:,7]==s.Matrix([A[1]-6*A[2],B[1]-6*B[2]])
zero={A[1]:0,A[2]:0,B[1]:0,B[2]:0}
Drestricted=D.subs(zero);assert Drestricted==C+s.Matrix([[A[0]*K[0,j] for j in range(9)],[B[0]*K[0,j] for j in range(9)]])
def delta(M,i,j):return s.expand(M[0,i]*M[1,j]-M[0,j]*M[1,i])
assert all(not delta(Drestricted,i,j).has(A[0]*B[0]) for i,j in itertools.combinations(range(9),2))
point={**{wi:s.Integer(1) for wi in w},u:s.Integer(3),v:s.Integer(4)}
Cp=C.subs(point)
assert {p for p in itertools.combinations(range(9),2) if delta(Cp,*p)==0}=={p for p in itertools.combinations(range(9),2) if 7 in p or 8 in p or p in ((1,2),(4,5))}
assert all(delta(Cp,i,j)>0 for i,j in itertools.combinations(range(7),2) if (i,j) not in ((1,2),(4,5)))
Y=C*Z;P=Y[:,[0,1]].inv()*Y[:,2:]
J=s.factor(P.reshape(8,1).jacobian((*w,u,v)).subs(point).det());assert J==s.Rational(102400,194481)
# The two remaining parallel-pair constraints pin the affine 2D fibre.
eq=[delta(Drestricted,i,j) for i,j in ((1,2),(4,5))]
M=s.Matrix([[s.diff(f,z).subs(point) for z in (A[0],B[0])] for f in eq]);det=s.factor(M.det());assert det==-882
report={'schema':'marici.nima.nine-point-seven-support-cell.v1','passed':True,
 'zero_columns':[8,9],'surviving_seven_columns':[1,2,3,4,5,6,7],
 'surviving_pair_constraints':['Delta_(2,3)=0','Delta_(5,6)=0'],
 'source_dimension':8,'ambient_fixed_target_fibre_dimension':6,
 'zero_column_forced_kernel_coefficients':['a1=0','a2=0','b1=0','b2=0'],
 'restricted_fibre_dimension':2,'restricted_quadratic_coordinates':['q01=0','q02=0','q12=0'],
 'source_minors_affine_on_restricted_fibre':36,
 'sample_target_jacobian':str(J),'remaining_pair_constraint_determinant':str(det),
 'scope':'A full-dimensional positive n=9 source-cell image and locally unique source lift at one positive moment-curve Z. This is an unsourced candidate cell, not a nine-point generalized-R history/form identification or global coverage.'}
(N/'nine-point-seven-support-cell.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
