"""Exact rational rank-six targets with irreducible two-sheet four-mass inverse."""
import contextlib,io,json,math
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_sixfold_contour_generic_target_chart as previous
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
emb=previous.emb;D,variables,Z=emb.D,emb.variables,emb.Z8six
# SL(6) frame with first six retained twistors equal I6. The same
# positive orientation is inherited from moment-curve external data.
frame=Z[:6,:].inv();assert frame.det()>0
Z=Z*frame;assert Z[:6,:]==s.eye(6)
K=s.Matrix.vstack(*(v.T for v in Z.T.nullspace()))
assert K.shape==(2,8) and K*Z==s.zeros(2,6)
R=s.Matrix.hstack(s.eye(6),s.zeros(6,2));assert R*Z==s.eye(6)
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
rows=[]
for source_row in json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']:
 point=dict(zip(variables,[s.Rational(v) for v in source_row['weights']]+[s.Rational(source_row['t']),s.Rational(source_row['u'])]))
 C0=D.subs(point);Y0=C0*Z
 for exponent in range(3,9):
  perturb=s.Rational(1,10**exponent)
  deltaY=s.zeros(2,6);deltaY[0,4]=perturb
  Y=Y0+deltaY
  Cbar=C0+deltaY*R
  assert Cbar*Z==Y and Y!=Y0
  F=Cbar+T*K
  def lifted(i,j):
   polynomial=s.Poly(s.det(s.Matrix.hstack(F[:,i],F[:,j])),a,b,c,d)
   assert polynomial.coeff_monomial(a*d)==-polynomial.coeff_monomial(b*c)
   return s.factor(polynomial.coeff_monomial(1)+
     sum(polynomial.coeff_monomial(x)*x for x in (a,b,c,d))+
     polynomial.coeff_monomial(a*d)*q)
  equations=[lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))]
  M,rhs=s.linear_eq_to_matrix(equations,(a,b,c,d))
  if M.det()==0:continue
  solution=M.inv()*rhs
  P=s.Poly(s.factor(q-solution[0]*solution[3]+solution[1]*solution[2]),q)
  if P.degree()!=2:continue
  disc=s.factor(s.discriminant(P.as_expr(),q))
  if disc<=0:continue
  numer,denom=map(int,s.fraction(disc))
  if math.isqrt(numer)**2==numer and math.isqrt(denom)**2==denom:continue
  break
 else:raise AssertionError('no_positive_irreducible_discriminant_perturbation')
 Ft=(Cbar+T*K).subs(dict(zip((a,b,c,d),solution)))
 gauge_minor=s.Poly(s.det(s.Matrix.hstack(Ft[:,0],Ft[:,2])),q)
 assert s.gcd(gauge_minor,P).degree()==0
 def minor(i,j):return s.factor(s.det(s.Matrix.hstack(Ft[:,i],Ft[:,j])))
 px=minor(0,4);py=minor(1,5)
 assert px!=0
 num=s.Poly(py,q);den=s.Poly(px,q)
 rem_num=s.rem(num,P);rem_den=s.rem(den,P)
 inverse=s.invert(rem_den,P)
 reduced=s.rem(rem_num*inverse,P)
 assert reduced.degree()==1 and reduced.coeff_monomial(q)!=0
 trace=s.factor(2*reduced.coeff_monomial(1)-reduced.coeff_monomial(q)*P.all_coeffs()[1]/P.all_coeffs()[0])
 assert trace.is_Rational
 # Check that the two algebraic roots indeed reconstruct source matrices
 # with correct four parallel pairs and the perturbed generic target.
 radicals=s.solve(P.as_expr(),q);assert len(radicals)==2
 for root in radicals:
  assert s.simplify(P.eval(root))==0
  mapped=Ft.subs(q,root)
  assert mapped*Z==Y
  for i,j in ((0,1),(2,3),(4,5),(6,7)):
   assert s.simplify(s.det(s.Matrix.hstack(mapped[:,i],mapped[:,j])))==0
 rows.append({'source_weights':source_row['weights'],'rational_target_perturbation':str(perturb),
  'inverse_quadratic_coefficients':[str(v) for v in P.all_coeffs()],
  'discriminant':str(disc),'positive_nonsquare_discriminant':True,
  'fermionic_pair_ratio_in_quadratic_quotient':[str(reduced.coeff_monomial(1)),str(reduced.coeff_monomial(q))],
  'pair_ratio_genuinely_irrational_on_each_sheet':True,
  'two_sheet_pair_ratio_trace_is_rational':str(trace),
  'both_algebraic_sheets_satisfy_source_pairs_and_target':True})
report={'schema':'marici.nima.nine-point-genuinely-quadratic-four-mass-fibre.v1','passed':True,
 'witnesses':rows,
 'result':'Two exact non-source-selected rational rank-six targets have irreducible real quadratic inverse fibres. Their sheet fermionic pair ratios are nonconstant elements of Q[q]/P and thus individually irrational, but their algebraic trace is exactly rational. Since the oriented complete fourmass coefficient on each sheet is a rational function of q using source parameters and Jacobian, the two-sheet complete invariant is invariant under quadratic Galois exchange and has rational bosonic coefficients wherever regular.',
 'boundary':'External n9 data are strictly positive (oriented moment curve with positive-determinant SL6 frame). The target perturbations are rational and lie in a real open neighborhood of regular source targets; a separate certified positivity witness for each perturbed target is not claimed. Rationality of full weighted trace follows algebraically from Galois invariance, not from an explicit expanded arbitrary-Y closed formula or any full image canonical contour.'}
(OUT/'nine-point-genuinely-quadratic-four-mass-fibre.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'irreducible_real_rank_six_targets':len(rows),'individual_pair_ratios_rational':False},indent=2))
