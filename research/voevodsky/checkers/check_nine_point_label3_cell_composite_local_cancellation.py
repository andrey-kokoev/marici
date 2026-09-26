"""Composite loop-shift residue and regular A/E local w2 boundary cancellation."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_loop_canonical_residue as top
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
D,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
A=s.Matrix.hstack(D[:,:2],s.zeros(2,1),D[:,2:])
E=A.copy();E[:,1]=s.zeros(2,1);E[:,2]=s.Matrix([w2,0])
assert E.subs(w2,0)==A.subs(w2,0)
# Common 9-dimensional positive cell col2=(x,0),col3=(y,0):
# five cyclic normal poles (12),(23),(45),(67),(89); after (12)
# and (23), the remaining (34)=y pole gives A, while the induced
# x=0 composite pole gives E. Calibrate their relative orientations
# against the already independently computed ORIGINAL sixfold residue.
x,y,a,b,h,e,f=s.symbols('x y a b h e f')
T=s.Matrix([[1,x,y,0,-h,-w5,-w6,-w7,-w8],
            [0,a,b,1,w4,w5*t,w6*(t-e),w7*u,w8*(u-f)]])
sources=(x,y,w4,w5,w6,w7,w8,t,u);normals=(a,b,h,e,f)
ambient=s.Matrix([T[row,j] for j in (1,2,4,5,6,7,8) for row in range(2)])
J=s.factor(ambient.jacobian(sources+normals).det(method='domain-ge'))
assert J!=0

def minor(i,j):return s.factor(s.det(s.Matrix.hstack(T[:,i],T[:,j])))
cyclic=[minor(i,(i+1)%9) for i in range(9)]
assert cyclic[0]==a and cyclic[1]==x*b-a*y and cyclic[2]==y
leading=x*w5*w6*w7*w8
remaining=y*(w4*w5)*(w6*w7*(t-u))*(-w8*u)
common=s.factor(J/(leading*remaining))
K=w4*w5*w6*w7*w8*u*(t-u)
assert s.factor(common* x*y*K) in (s.S.One,-s.S.One)
# Res_y dx^dy^drest = -dx^drest; Res_x = +dy^drest.
raw_A=s.factor(-s.cancel(common*y).subs({y:0,x:w2}))
raw_E=s.factor(s.cancel(common*x).subs({x:0,y:w2}))
assert raw_A==-raw_E
calibration=s.factor(top.source_density/raw_A)
assert calibration in (s.S.One,-s.S.One)
rho_E=s.factor(raw_E*calibration)
assert s.factor(rho_E+top.source_density)==0
Z=s.Matrix([[j**d for d in range(6)] for j in range(1,10)])
points=[('first',('0','1','1','1','1','1','3','2')),
        ('second',('0','3','1','4','2','5','7/2','3/2')),
        ('third',('0','2','2','1','4','2','5','1'))]
controls=[]
for name,raw in points:
 p=dict(zip(vars,[s.Rational(z) for z in raw]));assert p[w2]==0 and p[t]>p[u]>0
 assert A.subs(p)==E.subs(p)
 Y=A.subs(p)*Z
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(j for j in range(6) if j not in fixed)
 H=Y[:,list(fixed)];target=H.inv()*Y[:,list(free)]
 def jac(cell):
  cols=[]
  for parameter in vars:
   delta=cell.diff(parameter).subs(p)*Z
   cols.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-
                    delta[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 JA,JE=jac(A),jac(E)
 assert all(JA[:,i]==JE[:,i] for i in range(1,8))
 da,de=JA.det(method='domain-ge'),JE.det(method='domain-ge')
 assert da!=0 and de!=0
 W=s.prod(p[z] for z in (w4,w5,w6,w7,w8))*p[u]*(p[t]-p[u])
 for target_dir in (JA[:,0],JA[:,0]+JA[:,1]/7+JA[:,6]/11):
  speedA,speedE=s.factor((JA.inv()*target_dir)[0]),s.factor((JE.inv()*target_dir)[0])
  assert speedA!=0 and speedE!=0
  replA=JA.copy();replA[:,0]=target_dir
  replE=JE.copy();replE[:,0]=target_dir
  assert replA==replE and s.factor(da*speedA-de*speedE)==0
  residueA=s.factor(-1/(W*da*speedA));residueE=s.factor(1/(W*de*speedE))
  assert residueA!=0 and residueA+residueE==0
 controls.append({'positive_shared_source_boundary':name,'rank_A':8,'rank_E':8,
                  'two_transverse_target_directions_cancel':True})
report={'schema':'marici.nima.nine-point-label3-cell-composite-local-cancellation.v1','passed':True,
 'common_nine_dimensional_source_form_density':str(common),
 'calibration_to_original_sixfold_top_residue':str(calibration),
 'original_A_intrinsic_density':str(top.source_density),
 'label3_cell_E_composite_induced_x_zero_density':str(rho_E),
 'opposite_oriented_source_residues':True,
 'regular_exact_positive_boundary_controls':controls,
 'scope':'A distinct label3-sensitive positive E cell is an explicit composite-top-residue neighbor canceling A w2=0 pushed local pole on a regular generic open. Another independently found positive neighbor already cancels this same A source facet; these local pairs are alternative contour choices and NOT evidence that summing ALL positive cells yields a triangulation or global n9 form.'}
(OUT/'nine-point-label3-cell-composite-local-cancellation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'label3_neighbor_opposite_orientation':True,
 'regular_boundary_controls':len(controls)},indent=2))
