"""Constructive generic selector for a rank-four paired-fibre elimination."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_paired_trace_samples as earlier
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
Z,K,D,variables=earlier.Z,earlier.K,earlier.D,earlier.variables
prior=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text());assert prior['passed']
a,b,c,d=s.symbols('a b c d');T=s.Matrix([[a,b],[c,d]])
p,r,v,t=s.symbols('p r v t');S=s.Matrix([[p,r],[v,t]])
l=s.Matrix([[t,-v,-r,p]])
pairs=((0,1),(2,3),(4,5),(6,7))
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
kappa=s.Matrix([minor(K,i,j) for i,j in pairs]);assert kappa[3]!=0
# An arbitrary three-by-four linear coefficient block certifies the
# determinant identity without relying on the numerical moment-curve Z.
entries=s.symbols('m0:12');L=s.Matrix(3,4,entries)
shift=L.col_join(s.zeros(1,4))+kappa*l
assert s.expand(shift.det()-kappa[3]*L.col_join(l).det())==0
selectors=(s.Matrix([[1,0],[0,0]]),s.Matrix([[0,1],[0,0]]),
           s.Matrix([[0,0],[1,0]]),s.Matrix([[0,0],[0,1]]))
def matrix_of_linear_terms(base):
 rows=[]
 for i,j in pairs:
  poly=s.Poly(minor(base+T*K,i,j),a,b,c,d)
  rows.append([poly.coeff_monomial(x) for x in (a,b,c,d)])
 return s.Matrix(rows)
rows=[]
for idx,row in enumerate(prior['rows']):
 point=dict(zip(variables,[s.Rational(x) for x in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 Y=D.subs(point)*Z
 canonical=s.Matrix.hstack(Y*Z[:6,:].inv(),s.zeros(2,2))
 Ldata=matrix_of_linear_terms(canonical)
 assert Ldata[3,:]==s.zeros(1,4) and Ldata[:3,:].rank()==3
 determinants=[]
 for shiftS in selectors:
  adjrow=s.Matrix([[shiftS[1,1],-shiftS[1,0],-shiftS[0,1],shiftS[0,0]]])
  direct=matrix_of_linear_terms(canonical+shiftS*K)
  assert direct==Ldata+kappa*adjrow
  assert direct.det()==kappa[3]*Ldata[:3,:].col_join(adjrow).det()
  determinants.append(direct.det())
 assert any(x!=0 for x in determinants)
 selected=next(i for i,x in enumerate(determinants) if x!=0)
 # A determinant-changing coordinate shift never changes the target Y.
 assert (canonical+selectors[selected]*K)*Z==Y
 rows.append({'target_index':idx,'unshifted_linear_rank':Ldata.rank(),
  'elementary_shift_determinants':[str(x) for x in determinants],
  'first_admissible_shift_index':selected})
report={'schema':'marici.nima.four-pair-transversal-section-selector.v1','passed':True,
 'symbolic_det_identity':'det(Mshift)=det(K78)*det([L1;L2;L3;ell(S)]), ell(S)=(S22,-S21,-S12,S11); valid for any generic Z,Y in first-six observation chart',
 'selector':'If rank([L1;L2;L3])=3, one of the four fixed elementary shifts E11,E12,E21,E22 necessarily gives invertible Mshift; select first nonzero determinant.',
 'witnesses':rows,
 'scope':'Constructive nonempty Zariski-open transversal-section selection for the four-pair fibre using a symbolic determinant identity and two exact target witnesses. No expanded bosonic rational eight-form, Y0 nilpotent regularity, or nine-point history equality is claimed.'}
(OUT/'four-pair-transversal-section-selector.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'universal_symbolic_determinant_identity':True,'witnesses':len(rows),'constructive_selector':True},indent=2))
