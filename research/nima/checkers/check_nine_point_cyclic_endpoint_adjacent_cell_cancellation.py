"""Third adjacent positive eight-cell: cyclic endpoint u=0 pole exchange (89)<->(91)."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_loop_canonical_residue as top
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
neighbor=D.copy();neighbor[1,7]=0 # physical 9 lies on cyclic ray of physical 1,2
assert neighbor.subs(u,0)==D.subs(u,0)
N9=s.Matrix.hstack(neighbor[:,:2],s.zeros(2,1),neighbor[:,2:])
v=s.symbols('v',positive=True)
positive=zero=0
for i,j in itertools.combinations(range(9),2):
 minor=s.factor(s.det(s.Matrix.hstack(N9[:,i],N9[:,j])))
 numerator,denominator=s.fraction(s.cancel(minor.subs(t,u+v)))
 assert all(c>=0 for c in s.Poly(numerator,w2,w4,w5,w6,w7,w8,u,v).coeffs()),(i,j,minor)
 assert all(c>=0 for c in s.Poly(denominator,w2,w4,w5,w6,w7,w8,u,v).coeffs())
 if minor==0:zero+=1
 else:positive+=1
assert (positive,zero)==(23,13)
# Replace (89)=w7*w8*f with (91)=g=-w8*(u-f).
# Thus f=u+g/w8 and df/dg=+1/w8.
measure_jac=top.J/w8
normal_leading=w2*w5*w6
remaining=(w4*w5)*(w6*w7*(t-u))*(w7*w8*u)
neighbor_density=s.factor(measure_jac/(normal_leading*remaining))
assert s.factor(neighbor_density+top.source_density)==0
external=loop.Z8six*loop.Z8six[:6,:].inv()
assert external[:6,:]==s.eye(6)
samples=[('first',('1','1','1','1','1','1','3','0')),
         ('second',('2','3','1','4','2','5','7/2','0')),
         ('third',('3','2','2','1','4','2','5','0'))]
checks=[]
for name,raw in samples:
 point=dict(zip(vars,[s.Rational(x) for x in raw]))
 assert point[u]==0 and point[t]>0 and all(point[x]>0 for x in vars[:6])
 CA=D.subs(point);CB=neighbor.subs(point);assert CA==CB
 Y=CA*external
 frames=[pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0]
 assert frames
 fixed=frames[0];free=tuple(i for i in range(6) if i not in fixed)
 H=Y[:,list(fixed)];target=H.inv()*Y[:,list(free)]
 def jac(cell):
  cols=[]
  for variable in vars:
   derivative=cell.diff(variable).subs(point)*external
   dB=H.inv()*(derivative[:,list(free)]-derivative[:,list(fixed)]*target)
   cols.append(s.Matrix(list(dB)))
  return s.Matrix.hstack(*cols)
 JA,JB=jac(D),jac(neighbor)
 assert all(JA[:,j]==JB[:,j] for j in range(7))
 detA,detB=JA.det(method='domain-ge'),JB.det(method='domain-ge')
 assert detA!=0 and detB!=0
 for direction in (JA[:,7],JA[:,7]+JA[:,0]/7+JA[:,4]/11):
  speedA,speedB=s.factor((JA.inv()*direction)[7]),s.factor((JB.inv()*direction)[7])
  assert speedA!=0 and speedB!=0
  alternateA=JA.copy();alternateA[:,7]=direction
  alternateB=JB.copy();alternateB[:,7]=direction
  assert alternateA==alternateB
  assert s.factor(detA*speedA-detB*speedB)==0
  otherprod=s.prod(point[x] for x in vars[:6])*point[t]
  residueA=s.factor(-s.S.One/(otherprod*detA*speedA))
  residueB=s.factor(s.S.One/(otherprod*detB*speedB))
  assert residueA!=0 and residueA+residueB==0
 checks.append({'source_data':name,'regular_target_frame':list(fixed),
                'both_target_jacobians_nonzero':True,
                'two_transverse_target_direction_cancellations':True})
report={'schema':'marici.nima.nine-point-cyclic-endpoint-adjacent-cell-cancellation.v1','passed':True,
 'positive_neighbor':'Physical column9=(-w8,0), so cyclic (91)=0 replaces (89)=0; physical cyclic block (9,1,2) is parallel.',
 'neighbor_ordered_minors':{'strictly_positive':positive,'identically_zero':zero},
 'common_positive_boundary':'u=0',
 'relative_cyclic_top_residue_orientation':'neighbor intrinsic density exactly negative sourced fourmass density',
 'generic_boundary_controls':checks,
 'cofactor_proof':'Both full source and fermionic matrices coincide on u=0. Their target Jacobians share the seven u-boundary tangent columns, differing only in u-normal column; opposite oriented top residues and Cramer cofactor identity cancel every local pushed scalar and SU4 component residue wherever regular.',
 'boundary':'A third local adjacent-cell cancellation, including a cyclic endpoint source divisor. Does not establish the entire nine-point image contour or whether this facet represents a genuine full-image boundary.'}
(OUT/'nine-point-cyclic-endpoint-adjacent-cell-cancellation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_boundary_controls':len(checks),
 'relative_orientation':-1,'all_flavor_local_poles_cancel':True},indent=2))
