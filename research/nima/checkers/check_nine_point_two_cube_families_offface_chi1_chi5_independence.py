"""Test if two locally pole-cancelling EB/FB families give proportional off-face forms."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_four_cell_two_zero_column_facet_full_pole as face
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
wall=face.wall;first=wall.first;cube=wall.cube;trace=first.support.prior.trace
Z9=wall.old.Z9;vars=wall.vars;w2,w4,w5,w6,w7,w8,t,u=vars
rows=[]
for evalue in (s.Rational(1,2),s.S.One):
 p=dict(zip(vars,(evalue,1,1,1,1,1,3,2)))
 Y=cube.E['E'].subs(p)*Z9
 B=Y[:,:2].inv()*Y[:,2:]
 z=Z9[:,2:]-Z9[:,:2]*B;h=Z9[:,:2]
 oldEB=trace.inverse_one_sheet(Y,trace.bir.square.source['E_B'],trace.bir.zero_sets['E_B'])
 oldFB,_,_=first.support.five.inverse_at(evalue)
 points={'zero2_E_B':oldEB,'zero2_F_B':oldFB,
         'zero3_E_B':{v:s.factor(wall.points['E_B'][v].subs(wall.e,evalue)) for v in vars},
         'zero3_F_B':{v:s.factor(wall.points['F_B'][v].subs(wall.e,evalue)) for v in vars}}
 coeff={}
 for key,C in face.C.items():
  point=points[key]
  assert all(point[v]>0 for v in vars[:6]) and point[u]>0 and point[t]>point[u]
  target=C.subs(point)*Z9
  assert target[:,:2].det()!=0 and target[:,:2].inv()*target[:,2:]==B
  jac=s.Matrix.hstack(*[s.Matrix(list(C.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
  assert jac!=0
  minor15=s.factor(C[:,[0,4]].det().subs(point))
  assert minor15!=0
  coeff[key]=s.factor(cube.orient[key.split('_',1)[1]]*minor15**4*
                      (C.subs(point)*h).det()**4/
                      (s.prod(point[v] for v in vars[:6])*point[u]*(point[t]-point[u])*jac))
 sums={fam:s.factor(coeff[fam+'_E_B']+coeff[fam+'_F_B']) for fam in ('zero2','zero3')}
 assert sums['zero2']!=0 and sums['zero3']!=0
 rows.append({'E_source_e':str(evalue),'chi1_power4_chi5_power4_offface_pair_sums':
              {k:str(v) for k,v in sums.items()},
              'zero3_over_zero2_pair_sum_ratio':str(s.factor(sums['zero3']/sums['zero2']))})
assert rows[0]['zero3_over_zero2_pair_sum_ratio']!=rows[1]['zero3_over_zero2_pair_sum_ratio']
report={'schema':'marici.nima.nine-point-two-cube-families-offface-chi1-chi5-independence.v1',
 'passed':True,'exact_E_target_ray_controls':rows,
 'offface_two_pair_forms_not_constant_multiples_on_target_open':True,
 'consequence':'The two EB/FB pair sums individually cancel their common local pole, but their chi1^4 chi5^4 OFF-FACE rational coefficients are both nonzero and have different exact ratios at e=1/2 and e=1. Hence the two family pair-form contributions are not related by any target-INDEPENDENT relative scalar on the common rational simple-fibre open. Local residue cancellation cannot choose the cross-family global contour coefficient.',
 'scope':'Two exact common positive targets and one fermionic component; not a full target form, all-cell contour or physical nine-point history normalization.'}
(OUT/'nine-point-two-cube-families-offface-chi1-chi5-independence.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'two_nonzero_pair_sums':True,
 'ratios_differ':True,'controls':[r['E_source_e'] for r in rows]},indent=2))
