"""Does a positive triple-vertical neighbor cancel the source w5=0 zero-column pole?"""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_loop_canonical_residue as top
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
neighbor=D.copy();neighbor[0,4]=0;neighbor[1,4]=w5 # physical 6 vertical, not the sourced slope t
assert neighbor.subs(w5,0)==D.subs(w5,0)
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
# Compute its sixfold cyclic residue directly in a common 14-chart.
a,b,c,h,g,f=s.symbols('a b c h g f')
T=s.Matrix([[1,w2,b,0,-h,-g,-w6,-w7,-w8],
            [0,a,c,1,w4,w5,w6*t,w7*u,w8*(u-f)]])
source=(w2,w4,w5,w6,w7,w8,t,u);normals=(a,b,c,h,g,f)
free=(1,2,4,5,6,7,8)
ambient=s.Matrix([T[r,j] for j in free for r in range(2)])
J=s.factor(ambient.jacobian(source+normals).det(method='domain-ge'))
assert J!=0

def minor(i,j):return s.factor(s.det(s.Matrix.hstack(T[:,i],T[:,j])))
cyclic=[minor(i,(i+1)%9) for i in range(9)]
assert all(s.factor(x-y)==0 for x,y in zip(cyclic,[a,w2*c-a*b,b,h,g*w4-h*w5,
 w6*(w5-g*t),w6*w7*(t-u),w7*w8*f,-w8*(u-f)]))
leading=w2*w4*w7*w8
remaining=(w5*w6)*(w6*w7*(t-u))*(-w8*u)
rho=s.factor(J/(leading*remaining))
assert s.factor(rho+top.source_density)==0
rhonormB=s.factor((rho*w5).subs(w5,0))
external=loop.Z8six*loop.Z8six[:6,:].inv()
samples=[('first',('1','1','0','1','1','1','3','2')),
         ('second',('2','3','0','4','2','5','7/2','3/2')),
         ('third',('3','2','0','1','4','2','5','1'))]
checks=[]
for name,raw in samples:
 point=dict(zip(vars,[s.Rational(x) for x in raw]))
 assert point[w5]==0 and all(point[x]>0 for x in (w2,w4,w6,w7,w8,u)) and point[t]>point[u]
 C=D.subs(point);assert C==neighbor.subs(point)
 Y=C*external
 frames=[pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0]
 assert frames
 fixed=frames[0];other=tuple(i for i in range(6) if i not in fixed)
 H=Y[:,list(fixed)];B=H.inv()*Y[:,list(other)]
 def jac(cell):
  cols=[]
  for x in vars:
   dY=cell.diff(x).subs(point)*external
   cols.append(s.Matrix(list(H.inv()*(dY[:,list(other)]-dY[:,list(fixed)]*B))))
  return s.Matrix.hstack(*cols)
 JA,JB=jac(D),jac(neighbor)
 assert all(JA[:,j]==JB[:,j] for j in range(8) if j!=2)
 detA,detB=JA.det(method='domain-ge'),JB.det(method='domain-ge')
 assert detA!=0 and detB!=0
 for direction in (JA[:,2],JA[:,2]+JA[:,0]/7+JA[:,5]/11):
  speedA,speedB=s.factor((JA.inv()*direction)[2]),s.factor((JB.inv()*direction)[2])
  assert speedA!=0 and speedB!=0
  otherprod=s.prod(point[x] for x in (w2,w4,w6,w7,w8))*point[u]*(point[t]-point[u])
  rA=s.factor(-s.S.One/(otherprod*detA*speedA))
  rB=s.factor(rhonormB.subs(point)/(detB*speedB))
  assert rA!=0 and rA+rB==0
  checks.append({'source_data':name,'regular_target_frame':list(fixed),
                 'cofactor_denominators_equal':s.factor(detA*speedA-detB*speedB)==0,
                 'local_scalar_and_all_flavor_pole_residues_cancel':True})
report={'schema':'marici.nima.nine-point-zero-column-neighbor-cancellation.v1','passed':True,
 'neighbor_source_minors':{'positive':positive,'zero':zero},
 'top_residue_density':str(rho),'relative_top_residue_sign':int(s.factor(rho/top.source_density)),
 'regular_boundary_controls':checks,
 'boundary':'A fourth generic-open local cancellation along a positive source zero-column facet. Neither cell covers the full n9 image, and remaining polar faces and global form are unresolved.'}
(OUT/'nine-point-zero-column-neighbor-cancellation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_boundary_controls':len(samples),
 'relative_source_orientation':report['relative_top_residue_sign']},indent=2))
