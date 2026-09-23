"""Exact parabolic SL6 covariance of the two-sheet Y0-chart eight-form."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_four_mass_rank_six_Y0_regular_witness as witness
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
previous=json.loads((OUT/'four-mass-rank-six-Y0-regular-witness.json').read_text());assert previous['passed']
Z,K,D,variables=witness.Z,witness.K,witness.D,witness.variables
L=s.diag(2,1,1,1);R=s.diag(s.Rational(1,2),1)
M=s.zeros(4,2);M[0,0]=3;M[2,1]=-1
W=L.row_join(M).col_join(s.zeros(2,4).row_join(R))
assert W.det()==1
# For U'=(UM+R)^-1 UL, dU'=H^-1 dU (L-MU').
# Eight row-major coordinates: det(dU'/dU)=det(H)^-4 det(L-MU')^2
# =det(W)^2 det(H)^-6. Test without expanding eight symbolic variables.
U=s.Matrix([[s.Rational(1,2),s.Rational(1,3),s.Rational(1,4),s.Rational(1,5)],
            [s.Rational(2,3),s.Rational(3,4),s.Rational(4,5),s.Rational(5,6)]])
H=U*M+R;Up=H.inv()*U*L
assert s.factor((L-M*Up).det()-W.det()*H.det()**(-1))==0
basis=[]
for i in range(2):
 for j in range(4):
  X=s.zeros(2,4);X[i,j]=1
  Y=H.inv()*X*(L-M*Up)
  basis.append(s.Matrix([Y[x,y] for x in range(2) for y in range(4)]))
J=s.Matrix.hstack(*basis).det(method='domain-ge')
assert J==H.det()**(-6)
rows=[]
for row,record in zip(json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows'],previous['witnesses']):
 point=dict(zip(variables,[s.Rational(v) for v in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(point);Y=C*Z
 kernel=Y.nullspace();right=Y.T*(Y*Y.T).inv()
 G=s.Matrix.hstack(*kernel,*[right[:,j] for j in range(2)])
 G[:,0]=G[:,0]/G.det()
 assert G.det()==1
 assert Y*G==s.Matrix([[0,0,0,0,1,0],[0,0,0,0,0,1]])
 base=Z*G;new=base*W
 assert new[:6,:].det()==Z[:6,:].det()>0
 contributions=[]
 for root,p in witness.fibre(C):
  dp=D.subs(p)
  baseY=dp*base;newY=dp*new
  assert baseY[:,0:4]==s.zeros(2,4) and newY[:,0:4]==s.zeros(2,4)
  def jac(external,representative):
   pivot=representative[:,4:6];assert pivot.det()!=0
   cols=[]
   for v in variables:
    deriv=pivot.inv()*(D.diff(v).subs(p)*external)[:,0:4]
    cols.append(s.Matrix([deriv[i,j] for i in range(2) for j in range(4)]))
   return s.Matrix.hstack(*cols).det(method='domain-ge')
  j0=jac(base,baseY);j1=jac(new,newY)
  assert j0!=0 and j1==j0*R.det()**(-6)
  source=-s.S.One/(s.prod(p[x] for x in variables[:6])*p[variables[7]]*(p[variables[6]]-p[variables[7]]))
  contributions.append((source/j0,source/j1))
 assert sum(x[0] for x in contributions)==s.Rational(record['Y0_chart_two_sheet_coefficient'])
 assert sum(x[1] for x in contributions)==s.Rational(record['Y0_chart_two_sheet_coefficient'])*R.det()**6
 rows.append({'base_trace':record['Y0_chart_two_sheet_coefficient'],
              'transformed_trace':str(sum(x[1] for x in contributions)),
              'sheetwise_jacobian_multiplier':str(R.det()**(-6))})
# A rank-four body cannot be reached by a constant invertible ambient GL6
# transformation: all 28 six-brackets of [z|0|0] vanish.
body=s.Matrix([[j**k for k in range(4)]+[0,0] for j in range(1,9)])
assert body.rank()==4 and all(body[list(ix),:].det()==0 for ix in itertools.combinations(range(8),6))
report={'schema':'marici.nima.four-mass-Y0-parabolic-covariance.v1','passed':True,
 'generic_chart_jacobian':'For W=[[L,M],[0,R]] in SL6, Uprime=(UM+R)^-1 UL and d^8Uprime=det(UM+R)^-6 d^8U.',
 'Y0_density_multiplier':'omega_U(Y0;Z W)=det(R)^6 omega_U(Y0;Z)',
 'two_full_trace_witnesses':rows,
 'nilpotent_body_boundary':'All 28 external six-brackets vanish at rank-four bosonized body, whereas all positive SL6 witness six-brackets remain nonzero; parabolic covariance cannot itself give the nilpotent continuation.'}
(OUT/'four-mass-Y0-parabolic-covariance.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'parabolic_jacobian_exponent':-6,'two_sheet_tests':len(rows),
                  'nilpotent_regularization_claimed':False},indent=2))
