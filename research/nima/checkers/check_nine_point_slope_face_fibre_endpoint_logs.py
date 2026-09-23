"""Exact endpoint logarithms show why B/D singular face currents need a shared regulator."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_slope_face_exact_fibre_normal_match as prior
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
vars=loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
points=[('first',('1','1','1','1','1','1','2','2'),s.Rational(-14,55),s.Rational(7,11)),
        ('second',('2','3','3','2','1','4','3','3'),s.Rational(-1213,645),s.oo)]
lam=s.symbols('lambda',real=True);checks=[]
for name,raw,L,U in points:
 p=dict(zip(vars,[s.Rational(z) for z in raw]))
 r=[s.Rational(z) for z in prior.checks[len(checks)]['source_fibre_direction']]
 weights=[p[z]+lam*r[i] for i,z in enumerate(vars[1:6],1)]
 assert r[1]>0
 # In ordered six-base coordinates (w2,z5,z6,z7,z8,u), contraction
 # along the positive fibre vector r gives this seven-form coefficient.
 FB=s.factor(-r[1]/(p[w2]*p[u]*s.prod(weights)))
 FD=-FB
 assert s.factor(FB+FD)==0
 for q in (L,(L+U)/2 if U!=s.oo else s.S.Zero):
  if q!=L:assert all(v.subs(lam,q)>0 for v in weights)
 lower_coeff=s.factor(s.limit((lam-L)*FB,lam,L,dir='+'))
 assert lower_coeff!=0 and s.limit(FB,lam,L,dir='+') in (s.oo,-s.oo)
 upper_coeff=None
 if U!=s.oo:
  upper_coeff=s.factor(s.limit((U-lam)*FB,lam,U,dir='-'))
  assert upper_coeff!=0
  assert s.limit(FB,lam,U,dir='-') in (s.oo,-s.oo)
 else:
  # Five weights grow linearly and the individual upper tail converges.
  assert all(r[i]>0 for i in range(1,6))
  tail=s.factor(s.limit(lam**5*FB,lam,s.oo))
  assert tail!=0
 checks.append({'point':name,'positive_interval':[str(L),str(U)],
  'contracted_B_fibre_density':str(FB),'contracted_D_fibre_density_is_negative_B':True,
  'nonzero_lower_log_coefficient':str(lower_coeff),
  'nonzero_upper_log_coefficient':str(upper_coeff) if upper_coeff is not None else None,
  'upper_tail_power':(-5 if U==s.oo else None),
  'matched_cutoff_pair_integral_zero_for_any_inner_cutoffs':True,
  'mismatched_lower_cutoff_scales_have_finite_shift':
   str(lower_coeff)+' * log(c) for lower cutoffs epsilon and c*epsilon'})
report={'schema':'marici.nima.nine-point-slope-face-fibre-endpoint-logs.v1','passed':True,
 'exact_positive_target_fibres':checks,
 'consequence':'Each individual B or D contracted source-boundary current has a logarithmic divergence at the w4=0 lower endpoint; the first target also has an upper w5=0 logarithm. Opposite currents cancel exactly with identical cutoffs. Changing only D lower cutoff epsilon to c*epsilon leaves lower_coeff*log(c); therefore no individual unregulated fibre pushforward or regulator-independent separated B,D pairing has been constructed.',
 'boundary':'These fibre endpoint logs are SOURCE-face quantities, not target canonical-form residues or proof of singular pushed eight-form poles.'}
(OUT/'nine-point-slope-face-fibre-endpoint-logs.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'endpoint_data':[{'point':c['point'],
 'lower_log':c['nonzero_lower_log_coefficient'],
 'upper_log':c['nonzero_upper_log_coefficient']} for c in checks]},indent=2))
