"""Universal TP separation of A/C and B/D positive slope-face interiors; exact corner limits."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_slope_face_exact_fibre_normal_match as prior
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
A,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
B=A.copy();B[0,3]=-w4/t
C=A.copy();C[1,5]=w6*u
D=B.copy();D[1,5]=w6*u
assert A.subs(t,u)==C.subs(t,u) and B.subs(t,u)==D.subs(t,u)
Z=loop.Z8six
minors5=[Z[list(rows),:5].det() for rows in itertools.combinations(range(8),5)]
assert len(minors5)==56 and all(value>0 for value in minors5)
# P4=span(Z1,Z2,Z4,Z5). The B/D face target Y contains
# Q_B=Z4+u*(Z1+w2*Z2) in P4 and S_B=Z1+w2*Z2-T outside P4:
# det[Z1,Z2,Z4,Z5,S_B] on the first five coordinates is
#  -(w5*Delta12456 + w6*Delta12457 + w7*Delta12458 + w8*Delta12459),
#  strictly negative for TP Z and strictly positive weights.
# In contrast A/C face Q_A=Z4+u*(Z1+w2*Z2)+w4*Z5 has NONZERO
# Z5 coefficient, and cannot lie in Y_B cap P4=span(Q_B).
checks=[]
for name,raw,old in zip(('first','second'),
 [('1','1','1','1','1','1','2','2'),('2','3','3','2','1','4','3','3')],prior.checks):
 p=dict(zip(vars,[s.Rational(z) for z in raw]));YB=B.subs(p)*Z
 Q=Z[2,:]+p[u]*(Z[0,:]+p[w2]*Z[1,:])
 assert s.Matrix.vstack(YB,Q).rank()==2
 P4=s.Matrix.vstack(*(Z[i,:] for i in (0,1,2,3)))
 assert P4.rank()==4 and s.Matrix.vstack(P4,YB).rank()==5
 first5=s.Matrix.vstack(P4[:,:5],YB[0,:5]).det()
 expected=-sum((p[x]*s.Matrix.vstack(P4[:,:5],Z[i,:5]).det()
                for x,i in ((w5,4),(w6,5),(w7,6),(w8,7))),s.S.Zero)
 assert first5==expected and first5<0
 r=[s.Rational(z) for z in old['source_fibre_direction']]
 endpoint=-p[w4]/r[1]
 corner={var:p[var]+endpoint*r[j] for j,var in enumerate(vars)}
 assert corner[w4]==0 and corner[t]==corner[u]>0
 assert all(corner[var]>0 for var in (w2,w5,w6,w7,w8))
 assert A.subs(corner)==B.subs(corner)==C.subs(corner)==D.subs(corner)
 # This endpoint of the B/D fibre has EXACTLY the same target as p.
 Ycorner=A.subs(corner)*Z
 frame=(YB[:,0:2]);assert frame.det()!=0
 def target_chart(Y):return Y[:,0:2].inv()*Y[:,2:]
 assert target_chart(YB)==target_chart(Ycorner)
 checks.append({'point':name,'strictly_negative_B_S_outside_P4_minor':str(first5),
  'positive_B_D_face_fibre_corner_lambda':str(endpoint),
  'corner_source_weights':[str(corner[x]) for x in vars],
  'same_target_as_positive_B_D_face_source':True})
report={'schema':'marici.nima.nine-point-slope-face-strata-separation.v1','passed':True,
 'strictly_total_positive_external_proof':{
  'P4':'span(Z1,Z2,Z4,Z5)',
  'B_D_face_Y_intersection_P4':'span(Z4+u*(Z1+w2*Z2))',
  'strict_nonmembership':'det[Z1,Z2,Z4,Z5,S_B] is negative weighted sum of four positive ordered five-minors times w5,w6,w7,w8',
  'A_C_face_Q':'Z4+u*(Z1+w2*Z2)+w4*Z5',
  'consequence':'No strictly positive w4>0 A/C slope-face source shares a target plane with any strictly positive B/D slope-face source, for arbitrary strictly TP rank-six external data.'},
 'exact_positive_face_targets_with_shared_source_corner_limits':checks,
 'scope':'Strictly positive slope-face interiors are disjoint as images between A/C and B/D; their closures can meet at w4=0 as certified. Other off-face source cells and global image-form residues remain open.'}
(OUT/'nine-point-slope-face-strata-separation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'universal_strict_positive_slope_face_interiors_disjoint':True,
 'exact_shared_corner_target_controls':len(checks)},indent=2))
