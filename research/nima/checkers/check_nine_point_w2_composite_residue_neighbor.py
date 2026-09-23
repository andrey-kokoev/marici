"""Composite cyclic residue and adjacent positive cell cancel final w2 source facet."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_loop_canonical_residue as top
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
neighbor=D.copy();neighbor[0,1]=0;neighbor[1,1]=w2
assert neighbor.subs(w2,0)==D.subs(w2,0)
N9=s.Matrix.hstack(neighbor[:,:2],s.zeros(2,1),neighbor[:,2:])
v=s.symbols('v',positive=True);positive=zero=0
for i,j in itertools.combinations(range(9),2):
 minor=s.factor(s.det(s.Matrix.hstack(N9[:,i],N9[:,j])))
 numerator,denominator=s.fraction(s.cancel(minor.subs(t,u+v)))
 assert all(a>=0 for a in s.Poly(numerator,w2,w4,w5,w6,w7,w8,u,v).coeffs()),(i,j,minor)
 assert all(a>=0 for a in s.Poly(denominator,w2,w4,w5,w6,w7,w8,u,v).coeffs())
 if minor==0:zero+=1
 else:positive+=1
assert (positive,zero)==(23,13)
# The common NINE-dimensional loop-column cell has physical column2=(x,y).
# Its FIVE cyclic poles (23),(34),(45),(67),(89) produce an induced
# normal-crossing two-form dx^dy/(x*y). The two eight-cells are its
# opposite residues y=0 and the COMPOSITE induced pole x=0.
x,y,b,c,h,e,f=s.symbols('x y b c h e f')
C=s.Matrix([[1,x,b,0,-h,-w5,-w6,-w7,-w8],
            [0,y,c,1,w4,w5*t,w6*(t-e),w7*u,w8*(u-f)]])
sources=(x,y,w4,w5,w6,w7,w8,t,u);normals=(b,c,h,e,f)
ambient=s.Matrix([C[r,j] for j in (1,2,4,5,6,7,8) for r in range(2)])
J=s.factor(ambient.jacobian(sources+normals).det(method='domain-ge'))
assert J==-top.J

def minor(i,j):return s.factor(s.det(s.Matrix.hstack(C[:,i],C[:,j])))
cyclic=[minor(i,(i+1)%9) for i in range(9)]
assert s.factor(cyclic[0]-y)==0 and s.factor(cyclic[1]-(x*c-y*b))==0
assert cyclic[2]==b
# Take b=0 before c=0 at generic x!=0, yielding (23)=x*c.
leading=x*w5*w6*w7*w8
remaining=y*(w4*w5)*(w6*w7*(t-u))*(-w8*u)
base_density=s.factor(J/(leading*remaining))
assert s.factor(base_density-1/(x*y*w4*w5*w6*w7*w8*u*(t-u)))==0
# In ordered dx^dy^drest: Res_{y=0}=-dx^drest; Res_{x=0}=+dy^drest.
rhoA=s.factor(-s.cancel(base_density*y).subs({x:w2,y:0}))
rhoB=s.factor(s.cancel(base_density*x).subs({x:0,y:w2}))
assert s.factor(rhoA-top.source_density)==0 and s.factor(rhoA+rhoB)==0
external=loop.Z8six*loop.Z8six[:6,:].inv()
samples=[('first',('0','1','1','1','1','1','3','2')),
         ('second',('0','3','1','4','2','5','7/2','3/2')),
         ('third',('0','2','2','1','4','2','5','1'))]
checks=[]
for name,raw in samples:
 point=dict(zip(vars,[s.Rational(z) for z in raw]))
 assert point[w2]==0 and point[t]>point[u]>0 and all(point[z]>0 for z in vars[1:6])
 CA=D.subs(point);CB=neighbor.subs(point);assert CA==CB
 Y=CA*external
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(i for i in range(6) if i not in fixed)
 H=Y[:,list(fixed)];target=H.inv()*Y[:,list(free)]
 def jac(cell):
  cols=[]
  for parameter in vars:
   dY=cell.diff(parameter).subs(point)*external
   cols.append(s.Matrix(list(H.inv()*(dY[:,list(free)]-dY[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 JA,JB=jac(D),jac(neighbor)
 assert all(JA[:,j]==JB[:,j] for j in range(1,8))
 detA,detB=JA.det(method='domain-ge'),JB.det(method='domain-ge')
 assert detA!=0 and detB!=0
 for direction in (JA[:,0],JA[:,0]+JA[:,1]/7+JA[:,6]/11):
  speedA,speedB=s.factor((JA.inv()*direction)[0]),s.factor((JB.inv()*direction)[0])
  assert speedA!=0 and speedB!=0
  alternateA=JA.copy();alternateA[:,0]=direction
  alternateB=JB.copy();alternateB[:,0]=direction
  assert alternateA==alternateB and s.factor(detA*speedA-detB*speedB)==0
  otherprod=s.prod(point[z] for z in vars[1:6])*point[u]*(point[t]-point[u])
  residueA=s.factor(-s.S.One/(otherprod*detA*speedA))
  residueB=s.factor(s.S.One/(otherprod*detB*speedB))
  assert residueA!=0 and residueA+residueB==0
 checks.append({'source_data':name,'regular_target_frame':list(fixed),
                'two_transverse_target_direction_cancellations':True})
report={'schema':'marici.nima.nine-point-w2-composite-residue-neighbor.v1','passed':True,
 'positive_neighbor':'Physical column2=(0,w2) joins the positive vertical triple (2,4,5); loop physical column3 remains zero.',
 'neighbor_ordered_minors':{'strictly_positive':positive,'identically_zero':zero},
 'fivefold_loop_cell_intrinsic_density':str(base_density),
 'old_cell_as_y_zero_residue':str(rhoA),
 'neighbor_as_induced_x_zero_composite_residue':str(rhoB),
 'opposite_orientations':True,
 'generic_positive_shared_boundary_controls':checks,
 'all_flavor_local_poles_cancel_on_w2_zero':True,
 'scope':'The FINAL basic source dlog factor w2 now has an exact local adjacent positive-cell cancellation, requiring a composite induced x=0 pole after five cyclic residues rather than direct exchange of six cyclic poles. Eight of eight basic facets have local screens, not an exhaustive n9 triangulation, all intersection cancellations, or the full image canonical form.'}
(OUT/'nine-point-w2-composite-residue-neighbor.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'final_source_facet':'w2=0','composite_top_residue':True,
 'positive_boundary_controls':len(checks)},indent=2))
