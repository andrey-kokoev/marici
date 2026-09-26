"""All-component nonlinear local pushed pole cancellation on three regular E-square edges."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_relabelled_four_cell_square as square
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
vars=square.vars
w2,w4,w5,w6,w7,w8,t,u=vars
cells,Z=square.cells,square.Z
chi=s.Matrix(9,4,lambda i,j:s.Symbol(f'chi{i+1}_{j+1}'))
edge_specs=[('E','E_B',w4,[(1,0,1,1,1,1,3,2),
                              (2,0,3,2,1,4,4,3),
                              (3,0,2,3,4,1,5,2)]),
            ('E','E_C',t,[(1,1,1,1,1,1,2,2),
                           (2,3,2,1,4,1,3,3),
                           (3,2,1,4,2,3,4,4)]),
            ('E_C','E_D',w4,[(1,0,1,1,1,1,3,2),
                                (2,0,3,2,1,4,4,3),
                                (3,0,2,3,4,1,5,2)])]
rows=[]
for left,right,normal,raws in edge_specs:
 for index,raw in enumerate(raws):
  slope=s.symbols('slope')
  if normal==t:
   parameters=vars[:6]+(slope,u)
   p=dict(zip(parameters,list(map(s.Rational,raw[:6]))+
              [s.Rational(raw[6])-s.Rational(raw[7]),s.Rational(raw[7])]))
   CA,CB=(cells[name].subs(t,u+slope) for name in (left,right))
   n=parameters.index(slope)
  else:
   parameters=vars
   p=dict(zip(parameters,map(s.Rational,raw)))
   CA,CB=cells[left],cells[right]
   n=parameters.index(normal)
  assert CA.subs(p)==CB.subs(p)
  assert CA.subs(p)*chi==CB.subs(p)*chi
  # All seven common tangent-Jacobian columns agree.
  Y=CA.subs(p)*Z
  fixed=next(pair for pair in __import__('itertools').combinations(range(6),2) if Y[:,list(pair)].det()!=0)
  free=tuple(j for j in range(6) if j not in fixed)
  H=Y[:,list(fixed)];B=H.inv()*Y[:,list(free)]
  def jac(C):
   columns=[]
   for param in parameters:
    delta=C.diff(param).subs(p)*Z
    columns.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-
                           delta[:,list(fixed)]*B))))
   return s.Matrix.hstack(*columns)
  JA,JB=jac(CA),jac(CB)
  assert all(JA[:,j]==JB[:,j] for j in range(8) if j!=n)
  da,db=JA.det(method='domain-ge'),JB.det(method='domain-ge')
  assert da!=0 and db!=0
  other=s.prod(p[v] for v in vars[:6] if v!=normal)*p[u]
  if normal!=t:other*=p[t]-p[u]
  assert other!=0
  for direction in (JA[:,n],JA[:,n]+JA[:,(n+1)%8]/7+JA[:,(n+3)%8]/11):
   speedA=s.factor((JA.inv()*direction)[n]);speedB=s.factor((JB.inv()*direction)[n])
   assert speedA!=0 and speedB!=0
   swapA=JA.copy();swapB=JB.copy();swapA[:,n]=direction;swapB[:,n]=direction
   assert swapA==swapB
   assert s.factor(da*speedA-db*speedB)==0
   signA=square.sign[left];signB=square.sign[right]
   assert signA==-signB
   resA=s.factor(signA/(other*da*speedA))
   resB=s.factor(signB/(other*db*speedB))
   assert resA!=0 and s.factor(resA+resB)==0
  rows.append({'edge':left+'/'+right,'positive_control':index,
               'both_rank_eight':True,
               'complete_fermionic_boundary_numerator_identical':True,
               'two_transverse_target_direction_full_pushed_pole_cancellations':True})
assert len(rows)==9
report={'schema':'marici.nima.nine-point-label3-square-three-regular-pushed-pole-cancellations.v1',
 'passed':True,'positive_boundary_controls':rows,
 'regular_edges':3,'controls_per_edge':3,'transverse_directions_per_control':2,
 'scope':'Complete local nonlinear fermionic pushed simple-pole cancellations on the three REGULAR E square edges for rank-six positive moment-curve data. The E_B/E_D t-u edge is rank-collapsed and excluded. Global four-cell trace cancellation, full n9 contour and image form remain open.'}
(OUT/'nine-point-label3-square-three-regular-pushed-pole-cancellations.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'regular_edges':3,'exact_positive_controls':len(rows),
 'complete_superform_boundary_cancellation':True},indent=2))
