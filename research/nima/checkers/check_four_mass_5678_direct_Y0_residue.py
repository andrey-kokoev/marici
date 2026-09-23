"""Independent direct Y0 fibre Laurent residue at the sourced <5678> wall."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_four_mass_5678_direct_Y0_fibre as fibre
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
prior=json.loads((OUT/'four-mass-5678-local-Laurent-trace.json').read_text());assert prior['passed']
e,x=fibre.e,fibre.x
w,V,W,H=fibre.w,fibre.V,fibre.W,fibre.H
a,b,c=fibre.coeff;disc=fibre.disc
D=s.cancel(V[2]*W[0]-W[2]*V[0])
t=s.cancel(-W[0]/D);u=s.cancel(V[0]/D)
w4=s.cancel(-t*V[3]-u*W[3])
assert s.cancel(fibre.P.as_expr()-(V[0]*W[1]-V[1]*W[0]))==0
# The direct 8x8 bosonic source-to-Cz Jacobian factors exactly; reduce
# the 4x4 effective determinant in the source w2 variable first.
eff=s.Matrix.hstack(t*V.diff(x)+u*W.diff(x),s.eye(4)[:,3],V,W)
J=s.cancel(H.det()*eff.det(method='domain-ge'))
source=-s.S.One/(x*w4*s.prod(w)*u*(t-u))
term=s.factor(s.cancel(source*(w[0]*t)**4/J))
roots=[s.factor((-b+sign*s.sqrt(disc))/(2*a)) for sign in (1,-1)]
branches=[]
for root in roots:
 expr=s.cancel(term.subs(x,root))
 branches.append(s.series(expr,e,0,2).removeO().expand())
trace=s.cancel(sum(branches))
residue=s.factor(s.limit(e*trace,e,0))
assert residue==s.Rational(2,325)
report={'schema':'marici.nima.four-mass-5678-direct-Y0-residue.v1','passed':True,
 'direct_bosonic_fibre_quadratic_coefficients':[str(v) for v in (a,b,c)],
 'direct_bosonic_residue_in_eps':str(residue),
 'independently_computed_sourced_psi_residue_in_eps':prior['simple_residue_in_eps'],
 'bracket_coordinate_residue':str(s.factor(-10*residue)),
 'method':'Solve C z=0 in the four-pair source chart by the independent w2 quadratic; compute source density and the FACTORED 8x8 Jacobian as rational functions of w2,eps; substitute both algebraic branches, expand their Laurent series and sum BEFORE taking eps0.',
 'scope':'Direct Y0 polynomial/Berezin component residue, distinct from the sourced psi companion-matrix engine. Generic z-open set away from the wall; global Y-dependent bosonic eight-form and nine-point history not computed.'}
(OUT/'four-mass-5678-direct-Y0-residue.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'independent_direct_Y0_residue':str(residue),'matches_source':True},indent=2))
