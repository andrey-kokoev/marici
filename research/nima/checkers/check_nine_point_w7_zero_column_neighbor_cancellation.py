"""Fifth positive neighboring cell cancels w7=0 zero-column facet."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_loop_canonical_residue as top
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
neighbor=D.copy();neighbor[1,6]=w7*t # physical 8 joins triple (6,7,8)
assert neighbor.subs(w7,0)==D.subs(w7,0)
N9=s.Matrix.hstack(neighbor[:,:2],s.zeros(2,1),neighbor[:,2:])
v=s.symbols('v',positive=True);positive=zero=0
for i,j in itertools.combinations(range(9),2):
 minor=s.factor(s.det(s.Matrix.hstack(N9[:,i],N9[:,j])))
 numerator,denominator=s.fraction(s.cancel(minor.subs(t,u+v)))
 assert all(z>=0 for z in s.Poly(numerator,w2,w4,w5,w6,w7,w8,u,v).coeffs()),(i,j,minor)
 assert all(z>=0 for z in s.Poly(denominator,w2,w4,w5,w6,w7,w8,u,v).coeffs())
 if minor==0:zero+=1
 else:positive+=1
assert (positive,zero)==(23,13)
# Six cyclic poles: (12),(23),(34),(45),(67),(78) in place of (89).
a,b,c,h,e,g=s.symbols('a b c h e g')
T=s.Matrix([[1,w2,b,0,-h,-w5,-w6,-w7,-w8],
            [0,a,c,1,w4,w5*t,w6*(t-e),w7*(t-e-g),w8*u]])
sources=(w2,w4,w5,w6,w7,w8,t,u);normals=(a,b,c,h,e,g)
ambient=s.Matrix([T[r,j] for j in (1,2,4,5,6,7,8) for r in range(2)])
J=s.factor(ambient.jacobian(sources+normals).det(method='domain-ge'));assert J!=0

def minor(i,j):return s.factor(s.det(s.Matrix.hstack(T[:,i],T[:,j])))
cyclic=[minor(i,(i+1)%9) for i in range(9)]
expected=[a,w2*c-a*b,b,h,w5*(w4-h*t),w5*w6*e,
          w6*w7*g,w7*w8*(t-e-g-u),-w8*u]
assert all(s.factor(x-y)==0 for x,y in zip(cyclic,expected))
leading=w2*w5*w6**2*w7
remaining=(w4*w5)*(w7*w8*(t-u))*(-w8*u)
rho=s.factor(J/(leading*remaining))
assert s.factor(rho+top.source_density)==0
external=loop.Z8six*loop.Z8six[:6,:].inv()
samples=[('first',('1','1','1','1','0','1','3','2')),
         ('second',('2','3','1','4','0','5','7/2','3/2')),
         ('third',('3','2','2','1','0','2','5','1'))]
checks=[]
for name,raw in samples:
 point=dict(zip(vars,[s.Rational(x) for x in raw]))
 assert point[w7]==0 and point[t]>point[u]>0 and all(point[x]>0 for x in vars[:6] if x!=w7)
 CA=D.subs(point);CB=neighbor.subs(point);assert CA==CB
 Y=CA*external
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(i for i in range(6) if i not in fixed)
 H=Y[:,list(fixed)];target=H.inv()*Y[:,list(free)]
 def jac(cell):
  cols=[]
  for variable in vars:
   dY=cell.diff(variable).subs(point)*external
   cols.append(s.Matrix(list(H.inv()*(dY[:,list(free)]-dY[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 JA,JB=jac(D),jac(neighbor)
 assert all(JA[:,i]==JB[:,i] for i in range(8) if i!=4)
 detA,detB=JA.det(method='domain-ge'),JB.det(method='domain-ge')
 assert detA!=0 and detB!=0
 for direction in (JA[:,4],JA[:,4]+JA[:,0]/7+JA[:,6]/11):
  speedA,speedB=s.factor((JA.inv()*direction)[4]),s.factor((JB.inv()*direction)[4])
  assert speedA!=0 and speedB!=0
  replacedA=JA.copy();replacedA[:,4]=direction
  replacedB=JB.copy();replacedB[:,4]=direction
  assert replacedA==replacedB and s.factor(detA*speedA-detB*speedB)==0
  otherprod=s.prod(point[x] for x in vars[:6] if x!=w7)*point[u]*(point[t]-point[u])
  residueA=s.factor(-s.S.One/(otherprod*detA*speedA))
  residueB=s.factor(s.S.One/(otherprod*detB*speedB))
  assert residueA!=0 and residueA+residueB==0
 checks.append({'source_data':name,'regular_target_frame':list(fixed),
                'two_transverse_direction_cancellations':True})
report={'schema':'marici.nima.nine-point-w7-zero-column-neighbor-cancellation.v1','passed':True,
 'positive_neighbor':'Physical column8=(-w7,w7*t) joins positive triple-parallel block (6,7,8); cyclic pole (78)=0 replaces (89)=0.',
 'neighbor_ordered_minors':{'strictly_positive':positive,'identically_zero':zero},
 'common_positive_source_boundary':'w7=0, where physical column8 vanishes',
 'cyclic_top_measure_coordinate_jacobian':str(J),
 'neighbor_intrinsic_density':str(rho),
 'relative_orientation':-1,
 'generic_positive_boundary_controls':checks,
 'all_flavor_local_poles_cancel_on_regular_boundary':True,
 'boundary':'Seventh source polar facet screened locally, not a global positive-image canonical form or complete n9 triangulation. w2 remains unscreened.'}
(OUT/'nine-point-w7-zero-column-neighbor-cancellation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'source_facet':'w7=0','positive_controls':len(checks),
 'relative_orientation':-1},indent=2))
