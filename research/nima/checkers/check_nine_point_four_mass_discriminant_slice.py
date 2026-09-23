"""Exact one-parameter discriminant and critical-point test for four-mass inverse."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_genuinely_quadratic_four_mass_fibre as previous
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars,Z,K,R=previous.D,previous.variables,previous.Z,previous.K,previous.R
source=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows'][0]
point=dict(zip(vars,[s.Rational(v) for v in source['weights']]+[s.Rational(source['t']),s.Rational(source['u'])]))
C0=D.subs(point);epsilon,q,a,b,c,d=s.symbols('epsilon q a b c d')
delta=s.zeros(2,6);delta[0,4]=epsilon
Y=C0*Z+delta;Cbar=C0+delta*R
T=s.Matrix([[a,b],[c,d]]);F=Cbar+T*K

def lifted(i,j):
 polynomial=s.Poly(s.det(s.Matrix.hstack(F[:,i],F[:,j])),a,b,c,d)
 assert polynomial.coeff_monomial(a*d)==-polynomial.coeff_monomial(b*c)
 return s.factor(polynomial.coeff_monomial(1)+sum(polynomial.coeff_monomial(x)*x for x in (a,b,c,d))+polynomial.coeff_monomial(a*d)*q)
M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))],(a,b,c,d))
detM=s.factor(M.det(method='domain-ge'));assert detM!=0
solution=M.inv()*rhs
P=s.Poly(s.factor(q-solution[0]*solution[3]+solution[1]*solution[2]),q)
assert P.degree()==2
A,B,C=[s.factor(v) for v in P.all_coeffs()]
discriminant=s.factor(B*B-4*A*C)
assert s.factor(discriminant.subs(epsilon,s.Rational(1,1000))-
 s.Rational(previous.rows[0]['discriminant']))==0
disc_num=s.factor(s.together(discriminant).as_numer_denom()[0]);branch=s.Poly(disc_num,epsilon)
assert branch.degree()==2 and s.gcd(branch,branch.diff()).degree()==0
assert branch.all_coeffs()==[81471625,27031090,346921]
branch_roots=s.solve(branch.as_expr(),epsilon)
assert len(branch_roots)==2 and all(v.is_real and v<0 for v in branch_roots)
critical=s.factor(-B/(2*A))
Ft=(Cbar+T*K).subs(dict(zip((a,b,c,d),solution)))
gauge_pair=Ft[:,[0,2]]
gauge_det=s.factor(gauge_pair.det())
gauge=gauge_pair.inv()*Ft
w=(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],-gauge[0,6],-gauge[0,7])
t=-gauge[1,4]/gauge[0,4];u=-gauge[1,6]/gauge[0,6]
source_factors=(gauge_det,*w,u,t-u)
critical_nonzero=[]
for name,expr in zip(('gauge12','w2','w4','w5','w6','w7','w8','u','t_minus_u'),source_factors):
 value=s.cancel(expr.subs(q,critical))
 numerator,denominator=s.fraction(value)
 assert s.gcd(s.Poly(numerator,epsilon),branch).degree()==0,name
 assert s.gcd(s.Poly(denominator,epsilon),branch).degree()==0,name
 critical_nonzero.append(name)
assert s.gcd(s.Poly(s.together(A).as_numer_denom()[0],epsilon),branch).degree()==0
assert s.gcd(s.Poly(s.together(detM).as_numer_denom()[0],epsilon),branch).degree()==0
assert all(v>0 for v in branch.all_coeffs())
report={'schema':'marici.nima.nine-point-four-mass-discriminant-slice.v1','passed':True,
 'slice':'With strictly positive rank-six external data, perturb the rational target Y by Y[0,4] -> Y[0,4]+epsilon. Reconstruct the sourced four-pair inverse by Cbar+T*K and four pair-minor constraints.',
 'inverse_quadratic_coefficients':[str(v) for v in (A,B,C)],
 'discriminant':str(discriminant),'branch_polynomial':str(branch.as_expr()),
 'linear_solver_determinant':str(detM),
 'simple_finite_branch_points':True,'exact_negative_real_branch_points':[str(v) for v in branch_roots],
 'no_real_branch_for_epsilon_nonnegative':True,
 'source_factors_nonzero_at_both_branch_points':critical_nonzero,
 'fold_statement':'Both simple discriminant zeros avoid the source gauge pole, all six dlog weight poles, u=0, t-u=0, inverse quadratic leading coefficient zero, and the four-pair linear solver determinant zero. Hence they are regular simple inverse-map ramification points (source density regular) on this one-dimensional target slice. Locally epsilon-epsilon_star~z^2, the conjugate residues of a regular source differential have canceling 1/z terms; no square-root discriminant pole survives their two-sheet trace on this slice.',
 'boundary':'This is an exact one-parameter complex target slice, not a global discriminant classification in arbitrary Gr(2,6) or proof of the complete positive-image canonical form.'}
(OUT/'nine-point-four-mass-discriminant-slice.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'simple_branch_points':2,'source_poles_at_branch':0,'positive_epsilon_branch_points':0},indent=2))
