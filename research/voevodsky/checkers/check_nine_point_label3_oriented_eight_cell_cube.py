"""Complete horizontal/vertical x w4 x slope positive label3 source-cell cube."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_relabelled_four_cell_square as square
 import check_nine_point_vertical_label3_B_neighbor_cancels_lower_EB_pole as neighbor
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
vars=square.vars;w2,w4,w5,w6,w7,w8,t,u=vars
E=square.cells
F={name.replace('E','F',1):cell.copy() for name,cell in E.items()}
for cell in F.values():cell[0,2]=0;cell[1,2]=w2
assert F['F_B']==neighbor.FB
v=s.symbols('v',positive=True)
for name,cell in F.items():
 assert cell[:,1]==s.zeros(2,1) and cell[:,2]==s.Matrix([0,w2])
 for i,j in itertools.combinations(range(9),2):
  expression=s.factor(cell[:,[i,j]].det().subs(t,u+v))
  numerator,denominator=s.fraction(s.cancel(expression))
  assert all(c>=0 for c in s.Poly(numerator,w2,w4,w5,w6,w7,w8,u,v).coeffs())
  assert all(c>=0 for c in s.Poly(denominator,w2,w4,w5,w6,w7,w8,u,v).coeffs())
assert F['F'].subs(w4,0)==F['F_B'].subs(w4,0)
assert F['F_C'].subs(w4,0)==F['F_D'].subs(w4,0)
assert F['F'].subs(t,u)==F['F_C'].subs(t,u)
assert F['F_B'].subs(t,u)==F['F_D'].subs(t,u)
for suffix in ('','_B','_C','_D'):
 assert E['E'+suffix].subs(w2,0)==F['F'+suffix].subs(w2,0)
orient={**square.sign,**{'F'+name[1:]:-sign for name,sign in square.sign.items()}}
assert sum(orient.values())==0
assert all(orient['E'+suffix]+orient['F'+suffix]==0 for suffix in ('','_B','_C','_D'))
minors={name:str(s.factor(cell[:,[2,4]].det())) for name,cell in {**E,**F}.items()}
assert all(minors[name]=='w2*w4' for name in E)
assert minors['F']==minors['F_C']=='0'
assert all(s.factor(F[name][:,[2,4]].det()-w2*w4/t)==0 for name in ('F_B','F_D'))
Z=square.Z
p=dict(zip(vars,map(s.Rational,(0,1,1,1,1,1,3,2))))
checks=[]
for suffix in ('','_B','_C','_D'):
 CE,CF=E['E'+suffix],F['F'+suffix]
 Y=CE.subs(p)*Z;assert Y==CF.subs(p)*Z
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(k for k in range(6) if k not in fixed)
 H=Y[:,list(fixed)];B=H.inv()*Y[:,list(free)]
 def jac(cell):
  return s.Matrix.hstack(*[s.Matrix(list(H.inv()*(delta[:,list(free)]-delta[:,list(fixed)]*B)))
    for delta in (cell.diff(param).subs(p)*Z for param in vars)])
 JE,JF=jac(CE),jac(CF)
 assert all(JE[:,j]==JF[:,j] for j in range(1,8))
 checks.append({'vertical_edge':'E'+suffix+'/F'+suffix,
                'target_jacobian_ranks':{'horizontal':JE.rank(),'vertical':JF.rank()},
                'opposite_source_orientations':True})
report={'schema':'marici.nima.nine-point-label3-oriented-eight-cell-cube.v1','passed':True,
 'positive_eight_cell_labels':list(E)+list(F),
 'calibrated_intrinsic_density_signs_relative_E':orient,
 'chi3_power4_chi5_power4_source_minors':minors,
 'four_vertical_direction_w2_boundary_rank_controls':checks,
 'scope':'An eight-positive-cell source incidence cube (horizontal/vertical phys3 x w4 pole shift x slope pole shift), not a target triangulation. Edge target ranks and full pushed-pole behavior must be checked separately before promoting any contour.'}
(OUT/'nine-point-label3-oriented-eight-cell-cube.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_cells':len(E)+len(F),
 'vertical_w2_edge_target_ranks':checks},indent=2))
