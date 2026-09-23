"""Exact quotient and scaling constraints on a putative Y0 bosonized form."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_four_mass_rank_six_Y0_regular_witness as basecheck
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
prior=json.loads((OUT/'four-mass-rank-six-Y0-regular-witness.json').read_text());assert prior['passed']
Z,K,D,variables=basecheck.Z,basecheck.K,basecheck.D,basecheck.variables
I4,I2=s.eye(4),s.eye(2)
M=s.Matrix([[1,2],[0,3],[-1,1],[2,0]])
shift=I4.row_join(M).col_join(s.zeros(2,4).row_join(I2))
bottom=s.diag(1,1,1,1,2,2);top=s.diag(2,2,2,2,1,1)
variants={'shift':shift,'bottom_times_2':bottom,'top_times_2':top}
expected={'shift':s.S.One,'bottom_times_2':s.S(2)**8,'top_times_2':s.S(2)**(-8)}
def quotient(E,indices):
 z,h=E[:,0:4],E[:,4:6]
 picked=z[list(indices),:];assert picked.det()!=0
 rest=[i for i in range(8) if i not in indices]
 return h[rest,:]-z[rest,:]*picked.inv()*h[list(indices),:]
def density(point,E):
 mapped=D.subs(point)*E
 assert mapped[:,0:4]==s.zeros(2,4)
 pivot=mapped[:,4:6];assert pivot.det()!=0
 cols=[]
 for x in variables:
  deriv=pivot.inv()*(D.diff(x).subs(point)*E)[:,0:4]
  cols.append(s.Matrix([deriv[i,j] for i in range(2) for j in range(4)]))
 J=s.Matrix.hstack(*cols).det(method='domain-ge');assert J!=0
 src=-s.S.One/(s.prod(point[x] for x in variables[:6])*point[variables[7]]*(point[variables[6]]-point[variables[7]]))
 return src/J
rows=[]
for row,record in zip(json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows'],prior['witnesses']):
 initial=dict(zip(variables,[s.Rational(x) for x in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(initial);Y=C*Z
 null=Y.nullspace();right=Y.T*(Y*Y.T).inv()
 G=s.Matrix.hstack(*null,*[right[:,j] for j in range(2)])
 G[:,0]=G[:,0]/G.det()
 assert G.det()==1 and Y*G==s.Matrix([[0,0,0,0,1,0],[0,0,0,0,0,1]])
 E=Z*G
 idx=next(indices for indices in itertools.combinations(range(8),4) if E[list(indices),0:4].det()!=0)
 Q=quotient(E,idx);assert Q.shape==(4,2)
 points=[p for _,p in basecheck.fibre(C)]
 original=[density(p,E) for p in points]
 assert sum(original)==s.Rational(record['Y0_chart_two_sheet_coefficient'])
 for name,W in variants.items():
  Enew=E*W
  assert Enew[:6,:].det()==E[:6,:].det()*W.det() and W.det()>0
  Qnew=quotient(Enew,idx)
  if name=='shift':assert Qnew==Q
  if name=='bottom_times_2':assert Qnew==2*Q
  if name=='top_times_2':assert Qnew==Q
  for p,c in zip(points,original):assert density(p,Enew)==expected[name]*c
 rows.append({'first_invertible_four_row_indices_one_based':[i+1 for i in idx],
  'base_full_two_sheet_coefficient':str(sum(original)),
  'unipotent_bottom_translation_invariance':True,
  'bottom_scaling_degree':8,'top_scaling_degree':-8})
# Homogeneity does NOT imply regularity at the zero quotient: x^9/y
# has total degree eight but an essential rational denominator there.
x,y,t=s.symbols('x y t');toy=x**9/y
assert s.cancel(toy.subs({x:t*x,y:t*y})-t**8*toy)==0
assert s.denom(s.cancel(toy))==y
report={'schema':'marici.nima.four-mass-bosonization-quotient-weights.v1','passed':True,
 'general_parabolic_GL6_jacobian':'For W=[[L,M],[0,R]] invertible, d^8Uprime/d^8U=det(W)^2/det(UM+R)^6.',
 'Y0_weight':'omega_U(Y0;Z W)=det(R)^6/det(W)^2 omega_U(Y0;Z).',
 'quotient_coordinates':'If z_rows_I (4x4) is invertible, Q=h_rest-z_rest*z_I^-1*h_I (4x2); invariant under h -> h+z M.',
 'two_positive_rank_six_witnesses':rows,
 'regularity_boundary':'Uniform h scaling has degree +8 and uniform z scaling degree -8. A homogeneous degree-eight rational function may nevertheless have poles at Q=0 (e.g. x^9/y). Nilpotent substitution requires canceled denominators in a local ring; this test does not prove it.'}
(OUT/'four-mass-bosonization-quotient-weights.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'witnesses':len(rows),'bottom_degree':8,'nilpotent_regularity_proved':False},indent=2))
