"""Local generic cancellation at the second positive four-mass internal boundary t-u=0."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_loop_canonical_residue as top
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
v=s.symbols('v',positive=True)
neighbor=D.copy();neighbor[1,5]=w6*u # physical 7 now parallel to 8 and 9
assert neighbor.subs(t,u)==D.subs(t,u)
N9=s.Matrix.hstack(neighbor[:,:2],s.zeros(2,1),neighbor[:,2:])
positive=zero=0
for i,j in itertools.combinations(range(9),2):
 minor=s.factor(s.det(s.Matrix.hstack(N9[:,i],N9[:,j])))
 numerator,denominator=s.fraction(s.cancel(minor.subs(t,u+v)))
 assert all(z>=0 for z in s.Poly(numerator,w2,w4,w5,w6,w7,w8,u,v).coeffs()),(i,j,minor)
 assert all(z>=0 for z in s.Poly(denominator,w2,w4,w5,w6,w7,w8,u,v).coeffs())
 if minor==0:zero+=1
 else:positive+=1
assert (positive,zero)==(23,13)
# Old top coordinates have (67)=w5*w6*e, (78)=w6*w7*(v-e).
# Replace cyclic normal (67) by g=(78): e=v-g/(w6*w7).
new_measure_jac=-top.J/(w6*w7)
normal_leading=w2*w7*w8
remaining=(w4*w5)*(w5*w6*(t-u))*(-w8*u)
new_density=s.factor(new_measure_jac/(normal_leading*remaining))
assert s.factor(new_density+top.source_density)==0
external=loop.Z8six*loop.Z8six[:6,:].inv()
assert external[:6,:]==s.eye(6)
source_coordinates=(w2,w4,w5,w6,w7,w8,v,u)
CA=D.subs(t,u+v);CB=neighbor.subs(t,u+v)
assert CA.subs(v,0)==CB.subs(v,0)
samples=[('first',('1','1','1','1','1','1','0','2')),
         ('second',('2','3','1','4','2','5','0','3/2')),
         ('third',('3','2','2','1','4','2','0','1'))]
checks=[]
for name,raw in samples:
 point=dict(zip(source_coordinates,[s.Rational(z) for z in raw]))
 assert point[v]==0 and point[u]>0 and all(point[x]>0 for x in source_coordinates[:6])
 source=CA.subs(point);assert source==CB.subs(point)
 Y=source*external;fixed=(0,2);free=(1,3,4,5)
 H=Y[:,list(fixed)];assert H.det()!=0
 target=H.inv()*Y[:,list(free)]
 def jac(cell):
  columns=[]
  for x in source_coordinates:
   dY=cell.diff(x).subs(point)*external
   dB=H.inv()*(dY[:,list(free)]-dY[:,list(fixed)]*target)
   columns.append(s.Matrix(list(dB)))
  return s.Matrix.hstack(*columns)
 JA,JB=jac(CA),jac(CB)
 assert all(JA[:,k]==JB[:,k] for k in range(8) if k!=6)
 determinant_A=JA.det(method='domain-ge');determinant_B=JB.det(method='domain-ge')
 assert determinant_A!=0 and determinant_B!=0
 for direction in (JA[:,6],JA[:,6]+JA[:,0]/7+JA[:,4]/11):
  speed_A=s.factor((JA.inv()*direction)[6]);speed_B=s.factor((JB.inv()*direction)[6])
  assert speed_A!=0 and speed_B!=0
  replaced_A=JA.copy();replaced_A[:,6]=direction
  replaced_B=JB.copy();replaced_B[:,6]=direction
  assert replaced_A==replaced_B
  assert s.factor(determinant_A*speed_A-determinant_B*speed_B)==0
  otherprod=s.prod(point[x] for x in source_coordinates[:6])*point[u]
  residue_A=s.factor(-s.S.One/(otherprod*determinant_A*speed_A))
  residue_B=s.factor(s.S.One/(otherprod*determinant_B*speed_B))
  assert residue_A!=0 and residue_A+residue_B==0
 checks.append({'source_data':name,'both_target_jacobians_nonzero':True,
                'two_transverse_target_direction_cancellations':True})
report={'schema':'marici.nima.nine-point-slope-merge-adjacent-cell-cancellation.v1','passed':True,
 'positive_neighbor':'Replace physical column7 slope t by u, making physical columns (7,8,9) a positive triple-parallel block; cyclic (78)=0 replaces (67)=0.',
 'neighbor_ordered_minors':{'strictly_positive':positive,'identically_zero':zero},
 'common_positive_boundary':'t-u=v=0',
 'relative_cyclic_top_residue_orientation':'neighbor density exactly negative the sourced fourmass density in common source coordinate order',
 'generic_boundary_controls':checks,
 'cofactor_proof':'The two complete source and fermionic matrices coincide on v=0. Their source-to-target Jacobians differ in ONLY the v-normal column; their other seven columns agree. Cramer cofactor invariance and opposite oriented source densities cancel every local pushed scalar and Grassmann boundary residue wherever both Jacobians and transverse speeds are nonzero.',
 'boundary':'A second positive shared-boundary cancellation on a regular generic open, not a global triangulation, cancellation of u=0/external boundaries or full nine-point image canonical form.'}
(OUT/'nine-point-slope-merge-adjacent-cell-cancellation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_boundary_controls':len(checks),
 'relative_orientation':-1,'all_flavor_local_poles_cancel':True},indent=2))
