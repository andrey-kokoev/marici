"""Prove entire positive t=u face target fibre is one affine weight line for TP Z."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_slope_face_exact_fibre_normal_match as prior
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
A,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
Z=loop.Z8six
# The physical rows are (Z1,Z2,Z4,Z5,Z6,Z7,Z8,Z9); strict total
# positivity follows from the distinct increasing moment-curve nodes.
minors6=[s.det(Z[list(rows),:]) for rows in itertools.combinations(range(8),6)]
assert len(minors6)==28 and all(m>0 for m in minors6)
minors4=[s.det(Z[list(rows),:4]) for rows in itertools.combinations(range(8),4)]
assert len(minors4)==70 and all(m>0 for m in minors4)
# For arbitrary strictly TP rank-six Z, at positive weights:
# P=span(Z1,Z2,Z4); Q=Z4+u Z1+u*w2 Z2 is in P; and
# S=Z1+w2 Z2-T is NOT in P because det[Z1,Z2,Z4,T] on any TP
# four-coordinate projection is a strictly positive weighted sum.
# Thus Y cap P=span(Q), and any other face preimage has Q'=Q,
# forcing u'=u, w2'=w2 from the fixed Z4 coefficient.
# W=span(Z5,...,Z9) has dim5; Q is NOT in W because
# det[Q,Z5,...,Z9]=det[Z4,W]+u*det[Z1,W]+u*w2*det[Z2,W]>0.
# Hence projection W->k6/Y has rank4, so the five-weight fibre
# is EXACTLY a one-dimensional affine line. No disconnected other
# face-preimage branch can evade this argument within B or D.
checks=[]
for name,raw,old in zip(('first','second'),
 [('1','1','1','1','1','1','2','2'),('2','3','3','2','1','4','3','3')],prior.checks):
 point=dict(zip(vars,[s.Rational(z) for z in raw]))
 T=point[w4]*Z[3,:]/point[u]+sum((point[var]*Z[i,:] for var,i in
                      ((w5,4),(w6,5),(w7,6),(w8,7))),s.zeros(1,6))
 Q=Z[2,:]+point[u]*(Z[0,:]+point[w2]*Z[1,:])
 witness4=s.det(s.Matrix.vstack(Z[0,:4],Z[1,:4],Z[2,:4],T[:,:4]))
 witness6=s.det(s.Matrix.vstack(Q,*[Z[i,:] for i in range(3,8)]))
 assert witness4>0 and witness6>0
 Y=s.Matrix.vstack(Z[0,:]+point[w2]*Z[1,:]-T,Q)
 assert Y.rank()==2
 assert s.Matrix.vstack(Z[0,:],Z[1,:],Z[2,:],Y).rank()==4
 assert s.Matrix.vstack(*[Z[i,:] for i in range(3,8)],Q).rank()==6
 r=[s.Rational(z) for z in old['source_fibre_direction']]
 assert r[0]==r[6]==r[7]==0
 lower=[];upper=[]
 for i in range(1,6):
  if r[i]>0:lower.append(-point[vars[i]]/r[i])
  elif r[i]<0:upper.append(-point[vars[i]]/r[i])
 assert lower
 L=max(lower);U=min(upper) if upper else s.oo
 assert L<0<U
 candidate=old['matching_candidates'];assert len(candidate)==1
 match=s.Rational(candidate[0]['lambda'])
 assert not (L<match<U)
 checks.append({'point':name,'positive_T_outside_P_minor':str(witness4),
  'Q_outside_W_minor':str(witness6),
  'complete_positive_face_fibre_lambda_interval':{'lower_open':str(L),'upper_open':str(U)},
  'unique_D_normal_jet_match_lambda':str(match),
  'matched_lambda_inside_positive_fibre':False})
report={'schema':'marici.nima.nine-point-slope-face-full-positive-fibre.v1','passed':True,
 'universal_total_positivity_proof':{
  'P':'span(Z1,Z2,Z4)','Q':'Z4+u*(Z1+w2*Z2)',
  'S':'Z1+w2*Z2-T, with T=(w4/u)*Z5+w5*Z6+w6*Z7+w7*Z8+w8*Z9',
  'Y_cap_P':'span(Q), since strictly positive four-minors give T outside P',
  'u_w2_uniqueness':'Any positive B/D slope-face preimage of Y has Q prime proportional Q; its fixed Z4 coefficient is 1, so u prime=u and w2 prime=w2.',
  'five_weight_projection_rank':'4, since Q lies outside W=span(Z5,...,Z9) by a strictly positive six-minor sum.',
  'entire_face_fibre':'One affine line in five weights; its positive part is an open interval.'},
 'exact_strictly_positive_moment_curve_controls':checks,
 'scope':'This excludes ALL positive B/D slope-face preimages matching B normal jet for the two tested target points, not only one fibre branch. Does not exclude other positive cells or targets, nonlinear off-face images, or certify global form.'}
(OUT/'nine-point-slope-face-full-positive-fibre.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'universal_full_face_fibre_dimension':1,
 'controls':[{'point':z['point'],'positive_interval':z['complete_positive_face_fibre_lambda_interval'],
 'normal_match':z['unique_D_normal_jet_match_lambda']} for z in checks]},indent=2))
