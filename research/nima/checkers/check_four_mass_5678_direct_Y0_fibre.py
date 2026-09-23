"""Independently solve the Y0 four-pair fibre on the same external wall family."""
import contextlib,functools,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_four_mass_complete_component_companion_trace as sourced
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
prior=json.loads((OUT/'four-mass-5678-local-Laurent-trace.json').read_text());assert prior['passed']
e,x=s.symbols('eps x');z=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],
 [10+e,16,25,39],[2,3,5,7],[3,5,7,11],[5,8,13,21]])
H=z[4:8,:];assert s.factor(H.det())==-10*e
# Row-one incidence C_1 z=0 uniquely determines the four source
# weights from one free coordinate x=w2. The first TWO coordinates
# of C_2 z=0 then impose one quadratic, not an auxiliary psi chart.
w=H.T.inv()*s.Matrix([1,x,0,0]);V=(w[0]*z[4,:]+w[1]*z[5,:]).T;W=(w[2]*z[6,:]+w[3]*z[7,:]).T
P=s.Poly(s.cancel(V[0]*W[1]-V[1]*W[0]),x)
assert P.degree()==2
# Clear common scalar denominators before evaluating a boundary.
poly=s.Poly(s.together(P.as_expr()).as_numer_denom()[0],x)
coeff=[s.factor(c) for c in poly.all_coeffs()];a,b,c=coeff
disc=s.factor(b*b-4*a*c)
assert disc!=0
# At a fixed rational eps with rational roots, reconstruct both source
# weights and verify the 8x8 bosonic incidence Jacobian directly.
w2,w4,w5,w6,w7,w8,t,u=s.symbols('w2 w4 w5 w6 w7 w8 t u')
variables=(w2,w4,w5,w6,w7,w8,t,u)
C=s.Matrix([[1,w2,0,0,-w5,-w6,-w7,-w8],[0,0,1,w4,w5*t,w6*t,w7*u,w8*u]])
def at(value):
 zv=z.subs(e,value);wv=w.subs(e,value);Vv=V.subs(e,value);Wv=W.subs(e,value)
 pv=s.Poly(P.as_expr().subs(e,value),x);roots=s.solve(pv.as_expr(),x)
 assert len(roots)==2 and all(r.is_Rational for r in roots)
 terms=[]
 for root in roots:
  weights=wv.subs(x,root);vv=Vv.subs(x,root);ww=Wv.subs(x,root)
  denom=s.factor(vv[2]*ww[0]-ww[2]*vv[0]);assert denom!=0
  tv=s.factor(-ww[0]/denom);uv=s.factor(vv[0]/denom)
  w4v=s.factor(-tv*vv[3]-uv*ww[3])
  point=dict(zip(variables,(root,w4v,*weights,tv,uv)))
  assert C.subs(point)*zv==s.zeros(2,4)
  cols=[]
  for v in variables:
   derivative=C.diff(v).subs(point)*zv
   cols.append(s.Matrix([derivative[i,j] for i in range(2) for j in range(4)]))
  J=s.Matrix.hstack(*cols).det(method='domain-ge');assert J!=0
  dV=Vv.diff(x).subs(x,root);dW=Wv.diff(x).subs(x,root)
  eff=s.Matrix.hstack(tv*dV+uv*dW,s.eye(4)[:,3],vv,ww)
  assert J==H.det().subs(e,value)*eff.det(method='domain-ge')
  src=-s.S.One/(s.prod(point[v] for v in (w2,w4,w5,w6,w7,w8))*uv*(tv-uv))
  terms.append(s.factor(src*(weights[0]*tv)**4/J))
 @functools.lru_cache(None)
 def br(i,j,k,l):return zv[[i-1,j-1,k-1,l-1],:].det(method='domain-ge')
 traced,_=sourced.complete_component(br)
 assert s.factor(sum(terms)-traced)==0
 return {'eps':str(value),'two_rational_source_roots':[str(r) for r in roots],
         'direct_Y0_component':str(sum(terms)),'independent_sourced_psi_component':str(traced),
         'both_sheet_direct_Jacobian_factorization':True}
# Select two rational eps with square discriminant directly; no
# numerical interpolation of the residue is used as a proof.
assert disc==121*e**2-108*e+196
choices=[s.Rational(28*m+108,121-m*m) for m in (0,-3)]
assert all(s.sqrt(disc.subs(e,value)).is_Rational for value in choices)
rows=[at(value) for value in choices]
report={'schema':'marici.nima.four-mass-5678-direct-Y0-fibre.v1','passed':True,
 'explicit_bosonic_incidence_quadratic_coefficients':[str(v) for v in coeff],
 'bosonic_incidence_discriminant':str(disc),
 'jacobian_factorization':'J_z=det(H) det[d(C_2 z)/d(w2,w4,t,u)] after eliminating C_1 z=0; verified against direct 8x8 determinant on both sheets.',
 'offwall_witnesses':rows,
 'scope':'Independent direct Y0-bosonic-fibre/source-Jacobian calculation on two rational points of the same sourced <5678> wall family, comparing the complete eta1^4 eta5^4 component to independently constructed psi. Not yet a direct eps-Laurent expansion at the wall nor arbitrary-Y global target form.'}
(OUT/'four-mass-5678-direct-Y0-fibre.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'independent_offwall_Y0_fibre_samples':len(rows),
 'quadratic_coefficients':report['explicit_bosonic_incidence_quadratic_coefficients']},indent=2))
