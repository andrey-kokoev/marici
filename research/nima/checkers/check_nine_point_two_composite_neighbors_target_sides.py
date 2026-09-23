"""Classify target-normal sides of two distinct positive w2-neighbors of sourced cell A."""
import contextlib,io,json,itertools
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
A=s.Matrix.hstack(D[:,:2],s.zeros(2,1),D[:,2:])
V=A.copy();V[0,1]=0;V[1,1]=w2 # old vertical column2 composite neighbor
E=A.copy();E[:,1]=s.zeros(2,1);E[:,2]=s.Matrix([w2,0]) # label3-sensitive neighbor
assert A.subs(w2,0)==V.subs(w2,0)==E.subs(w2,0)
Z=s.Matrix([[j**d for d in range(6)] for j in range(1,10)])
points=[('first',('0','1','1','1','1','1','3','2')),
        ('second',('0','3','1','4','2','5','7/2','3/2')),
        ('third',('0','2','2','1','4','2','5','1'))]
checks=[]
for name,raw in points:
 p=dict(zip(vars,[s.Rational(z) for z in raw]));Y=A.subs(p)*Z
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(i for i in range(6) if i not in fixed)
 H=Y[:,list(fixed)];target=H.inv()*Y[:,list(free)]
 def jac(cell):
  cols=[]
  for parameter in vars:
   delta=cell.diff(parameter).subs(p)*Z
   cols.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-
                    delta[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 JA,JV,JE=map(jac,(A,V,E))
 assert JA[:,1:]==JV[:,1:]==JE[:,1:]
 tangent=JA[:,1:];assert tangent.rank()==7
 annihilator=tangent.T.nullspace();assert len(annihilator)==1
 l=annihilator[0]
 normals={label:s.factor((l.T*J[:,0])[0]) for label,J in
          [('A',JA),('V',JV),('E',JE)]}
 assert all(v!=0 for v in normals.values())
 dets={label:J.det(method='domain-ge') for label,J in [('A',JA),('V',JV),('E',JE)]}
 assert all(d!=0 for d in dets.values())
 assert all(s.factor(normals[label]/normals['A']-dets[label]/dets['A'])==0
            for label in ('V','E'))
 checks.append({'point':name,'target_normal_quotient_scalars':{z:str(v) for z,v in normals.items()},
  'V_relative_target_normal_side_to_A':int(s.sign(normals['V']/normals['A'])),
  'E_relative_target_normal_side_to_A':int(s.sign(normals['E']/normals['A'])),
  'E_relative_target_normal_side_to_V':int(s.sign(normals['E']/normals['V'])),
  'three_target_jacobian_ranks':{'A':8,'V':8,'E':8}})
assert len({(z['V_relative_target_normal_side_to_A'],
             z['E_relative_target_normal_side_to_A']) for z in checks})==1
report={'schema':'marici.nima.nine-point-two-composite-neighbors-target-sides.v1','passed':True,
 'regular_positive_boundary_controls':checks,
 'source_orientations':{'A':'negative','vertical_phys2_V':'positive',
                        'label3_phys3_E':'positive'},
 'scope':'Exact local target-normal side classification at three positive shared source-boundary points. It informs contour ambiguity but cannot select global cell multiplicities, prove image coverage or the full n9 form.'}
(OUT/'nine-point-two-composite-neighbors-target-sides.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_controls':len(checks),
 'relative_target_normal_signs':{k:checks[0][k] for k in
 ('V_relative_target_normal_side_to_A','E_relative_target_normal_side_to_A',
 'E_relative_target_normal_side_to_V')}},indent=2))
