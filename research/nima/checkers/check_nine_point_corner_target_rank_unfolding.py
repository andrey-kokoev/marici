"""Probe rank-seven corner ramification of two cells in positive source square."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
A,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
B=A.copy();B[0,3]=-w4/t
C=A.copy();C[1,5]=w6*u
D=B.copy();D[1,5]=w6*u
cells={'A':A,'B':B,'C':C,'D':D}
external=loop.Z8six*loop.Z8six[:6,:].inv()
points=[('first',('1','0','1','1','1','1','2','2')),
        ('second',('2','0','3','2','1','4','3','3'))]
checks=[]
for name,raw in points:
 p=dict(zip(vars,[s.Rational(q) for q in raw]))
 Y=A.subs(p)*external
 fixed=(0,1);free=(2,3,4,5)
 assert Y[:,list(fixed)].det()!=0
 def jac(cell,point):
  Y0=cell.subs(point)*external
  H=Y0[:,list(fixed)];target=H.inv()*Y0[:,list(free)]
  cols=[]
  for parameter in vars:
   dY=cell.diff(parameter).subs(point)*external
   cols.append(s.Matrix(list(H.inv()*(dY[:,list(free)]-dY[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 ranks={};kernels={};unfold={}
 eps=s.symbols('eps')
 for label,cell in cells.items():
  J=jac(cell,p);ranks[label]=J.rank()
  if label not in ('B','D'):
   assert ranks[label]==8
   continue
  assert ranks[label]==7
  right=J.nullspace();left=J.T.nullspace()
  assert len(right)==len(left)==1
  r,l=right[0],left[0]
  # Jacobian along six tangent coordinates to the corner: w2,w5,w6,w7,w8,
  # simultaneous shift of t and u. Confirm these six are independent.
  tangent=s.Matrix.hstack(*(J[:,i] for i in (0,2,3,4,5)),J[:,6]+J[:,7])
  assert tangent.rank()==6
  kernels[label]={'right_kernel':[str(s.factor(z)) for z in r],
                  'has_w4_component':r[1]!=0,
                  'has_slope_gap_component':s.factor(r[6]-r[7])!=0,
                  'left_kernel':[str(s.factor(z)) for z in l]}
  unfold[label]={}
  for coordinate,perturb in [('slope_gap', {t:p[u]+eps}),
                              ('w4_weight',{w4:eps})]:
   moving=dict(p);moving.update(perturb)
   movingJ=jac(cell,moving)
   J1=movingJ.diff(eps).subs(eps,0)
   assert movingJ.subs(eps,0)==J
   pairing=s.factor((l.T*J1*r)[0])
   unfold[label][coordinate]={'left_first_jacobian_variation_right':str(pairing),
                              'simple_determinant_zero_along_path':pairing!=0}
 checks.append({'corner_point':name,'ranks':ranks,'kernel_data':kernels,'first_order_unfolding':unfold})
report={'schema':'marici.nima.nine-point-corner-target-rank-unfolding.v1','passed':True,
 'exact_corner_controls':checks,
 'scope':'Two exact positive controls characterize rank-seven B,D corner singularity and first-order unfolding. These pointwise checks do not establish generic/global fold classification or the singular pushed-form corner residue.'}
(OUT/'nine-point-corner-target-rank-unfolding.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'controls':[{'point':p['corner_point'],'ranks':p['ranks'],
 'unfold':{z:{v:y['simple_determinant_zero_along_path'] for v,y in d.items()}
           for z,d in p['first_order_unfolding'].items()}} for p in checks]},indent=2))
