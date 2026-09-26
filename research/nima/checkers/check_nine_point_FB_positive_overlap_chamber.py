"""Exact rational F_B inverse and positivity chamber along a positive E target family."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_five_cell_lower_internal_full_trace_cancellation as five
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
chamber=five.chamber;trace=five.trace
vars=trace.vars;w2,w4,w5,w6,w7,w8,t,u=vars
e=chamber.e;Y=chamber.Y
Z,K,cell=five.Z,five.K,five.cell
T=five.T;a,b,c,d,q=five.a,five.b,five.c,five.d,five.q
start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def lifted(i,j):
 poly=s.Poly(minor(start+T*K,i,j),a,b,c,d)
 assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
 return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in five.bir.pairs],(a,b,c,d))
assert M.rank()==4
left=s.factor((M.T.nullspace()[0].T*rhs)[0]);assert s.diff(left,q)!=0
qvalue=s.factor(-left.subs(q,0)/s.diff(left,q))
sol=M.gauss_jordan_solve(rhs.subs(q,qvalue))[0]
assert s.factor(qvalue-sol[0]*sol[3]+sol[1]*sol[2])==0
source=start+T.subs(dict(zip((a,b,c,d),sol)))*K
gauge=source[:,[0,2]].inv()*source
point=dict(zip(vars,(gauge[1,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
         -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
assert all(s.cancel((gauge-cell.subs(point))[i,j])==0 for i in range(2) for j in range(8))
formulas={str(v):str(s.factor(point[v])) for v in vars}
boundary=s.factor(point[t]-point[u])
checks=[]
for value in (s.Rational(1,20),s.Rational(1,2),s.S.One,s.S(2),chamber.threshold_high,s.S(50),s.S(100)):
 signs={str(v):str(s.sign(s.factor(point[v].subs(e,value)))) for v in vars[:6]}
 signs['u']=str(s.sign(s.factor(point[u].subs(e,value))))
 signs['t-u']=str(s.sign(boundary.subs(e,value)))
 checks.append({'e':str(value),'F_B_positive':all(z=='1' for z in signs.values()),
                'exact_source_positivity_signs':signs})
threshold_F_w4=s.Rational(1691,21913)
threshold_F_w2=s.Rational(44,445)
assert 0<threshold_F_w4<threshold_F_w2
assert s.factor(point[w4]-895*(21913*e-1691)/(37*(3488*e+58879)))==0
assert s.factor(point[w2]-(445*e-44)/259)==0
for expr in [point[v] for v in (w5,w6,w7,w8,u)]+[boundary]:
 numerator,denominator=s.fraction(s.factor(expr))
 assert all(z>=0 for z in s.Poly(numerator,e).coeffs())
 assert all(z>=0 for z in s.Poly(denominator,e).coeffs())
 assert numerator.subs(e,0)>0 and denominator.subs(e,0)>0
assert point[w4].subs(e,threshold_F_w4)==0
assert point[w2].subs(e,threshold_F_w4)<0
assert chamber.J_E.subs(e,threshold_F_w4)!=0
assert chamber.J_E.subs(e,threshold_F_w2)!=0
P0,q0,J0=five.inverse_at(threshold_F_w4)
assert J0!=0 and P0[w4]==0 and P0[w2]<0
assert all(P0[v]!=0 for v in (w5,w6,w7,w8,u)) and P0[t]-P0[u]!=0
assert s.factor(cell[:,[0,1]].det()-w2)==0 # chi1^4 chi3^4 survives w4=0
report={'schema':'marici.nima.nine-point-FB-positive-overlap-chamber.v1','passed':True,
 'E_positive_target_family':'w2=e>0; other weights (1,1,1,1,1,3,2); positive moment-curve retained labels (1,3,4,5,6,7,8,9)',
 'complete_unique_F_B_inverse_source':formulas,
 'F_B_t_minus_u':str(boundary),
 'exact_positive_controls':checks,
 'complete_one_parameter_positive_chamber':'The F_B unique inverse has strictly positive source weights IFF e>44/445. Its w4 changes sign earlier at e=1691/21913<44/445, and all remaining six positivity factors are strictly positive for every e>0.',
 'additional_nonpositive_F_B_w4_wall_inside_E_image':{'E_source_e':'1691/21913',
  'F_B_w2_negative':True,'F_B_w4_zero':True,
  'E_and_F_B_target_jacobians_nonzero':True,
  'F_B_chi1_power4_chi3_power4_minor_nonzero':True},
 'scope':'Exact all-e>0 chamber classification on one fixed positive E target curve, plus a new F_B nonpositive-sheet w4=0 meromorphic wall inside regular E image. No full cell-contour cancellation or global n9 image canonical form.'}
(OUT/'nine-point-FB-positive-overlap-chamber.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'F_B_w2':formulas['w2'],
 'samples':[{k:p[k] for k in ('e','F_B_positive')} for p in checks]},indent=2))
