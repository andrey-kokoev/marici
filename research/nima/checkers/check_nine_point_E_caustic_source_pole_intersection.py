"""Check whether E's algebraic caustic collides with a source pole or gauge singularity."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_E_complex_real_caustic_within_positive_V_family as caustic
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
e=caustic.e;D,vars=caustic.D,caustic.vars
w2,w4,w5,w6,w7,w8,t,u=vars
Q=s.Poly(s.factor(s.together(caustic.discriminant)).as_numer_denom()[0],e).sqf_part().monic()
dstar=s.factor(-caustic.P.nth(1)/(2*caustic.P.nth(2)))
coefficients=[s.factor(v.subs(caustic.free,dstar)) for v in caustic.linear]
source=caustic.start+caustic.T.subs(dict(zip((caustic.a,caustic.b,caustic.c,caustic.d),coefficients)))*caustic.K
pivot=s.factor(source[:,[0,2]].det())
assert pivot!=0
inverse=source[:,[0,2]].inv();gauge=inverse*source
point=dict(zip(vars,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
         -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
for i in range(2):
 for j in range(8):
  residual=s.cancel((gauge-D.subs(point))[i,j]);num,den=s.fraction(residual)
  assert s.rem(s.Poly(num,e),Q)==0 and s.gcd(s.Poly(den,e),Q).degree()==0
checks=[]
for label,expr in [('pivot',pivot)]+[(str(v),point[v]) for v in vars[:6]]+[
 ('u',point[u]),('t-u',point[t]-point[u]),
 ('target_pivot',caustic.H.det())]:
 num,den=map(lambda v:s.Poly(v,e),s.fraction(s.factor(expr)))
 num_gcd=s.gcd(Q,num).degree();den_gcd=s.gcd(Q,den).degree()
 checks.append({'quantity':label,'caustic_gcd_numerator_degree':num_gcd,
                'caustic_gcd_denominator_degree':den_gcd,
                'finite_nonzero_at_caustic':num_gcd==den_gcd==0})
assert all(z['finite_nonzero_at_caustic'] for z in checks)
report={'schema':'marici.nima.nine-point-E-caustic-source-pole-intersection.v1','passed':True,
 'quartic_caustic_polynomial':str(Q.as_expr()),
 'double_E_fibre_root':str(dstar),
 'exact_caustic_nonintersection_checks':checks,
 'consequence':'At the unique caustic parameter in (1/40,1/35), the coalesced E inverse source has finite nonzero pivot, six weights, u, t-u and target pivot. Hence its intrinsic logarithmic eight-form has no source pole there; the simple quadratic fold trace of the COMPLETE meromorphic E pushforward is regular by the paired-residue/local-trace identity. An individual inverse-Jacobian sheet diverges but the two-sheet sum cancels the fold singularity.',
 'scope':'Regularity of the full two-sheet E trace along this one-parameter target curve near the unique caustic, not an all-target physical canonical form or a statement about other cells.'}
(OUT/'nine-point-E-caustic-source-pole-intersection.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'source_pole_gauge_caustic_intersections':
 sum(not z['finite_nonzero_at_caustic'] for z in checks),'quantities':len(checks)},indent=2))
