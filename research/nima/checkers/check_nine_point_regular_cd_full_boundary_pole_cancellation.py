"""Full nonlinear generic-open C/D pushed pole cancellation at w4=0,t>u."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_loop_canonical_residue as top
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
A,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
C=A.copy();C[1,5]=w6*u
D=C.copy();D[0,3]=-w4/t
assert D.subs(w4,0)==C.subs(w4,0)
rho_C=-top.source_density;rho_D=top.source_density
assert s.factor(rho_C+rho_D)==0
chi=s.Matrix(8,4,lambda i,j:s.Symbol(f'chi{i+1}_{j+1}'))
assert C.subs(w4,0)*chi==D.subs(w4,0)*chi
external=loop.Z8six*loop.Z8six[:6,:].inv()
samples=[('first',('1','0','1','1','1','1','3','2')),
         ('second',('2','0','3','2','1','4','5/2','3/2')),
         ('third',('3','0','2','4','3','2','5','1'))]
checks=[]
for name,raw in samples:
 p=dict(zip(vars,[s.Rational(z) for z in raw]))
 assert p[w4]==0 and p[t]>p[u]>0 and all(p[z]>0 for z in (w2,w5,w6,w7,w8))
 assert C.subs(p)==D.subs(p)
 Y=C.subs(p)*external
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(j for j in range(6) if j not in fixed)
 H=Y[:,list(fixed)];target=H.inv()*Y[:,list(free)]
 def jac(cell):
  cols=[]
  for parameter in vars:
   delta=cell.diff(parameter).subs(p)*external
   cols.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-
                    delta[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 JC,JD=jac(C),jac(D)
 assert all(JC[:,j]==JD[:,j] for j in range(8) if j!=1)
 detC,detD=JC.det(method='domain-ge'),JD.det(method='domain-ge')
 assert detC!=0 and detD!=0
 poleprod=s.prod(p[z] for z in (w2,w5,w6,w7,w8))*p[u]*(p[t]-p[u])
 assert s.factor((rho_C*w4).subs(p)-1/poleprod)==0
 assert s.factor((rho_D*w4).subs(p)+1/poleprod)==0
 for direction in (JC[:,1],JC[:,1]+JC[:,0]/7+JC[:,6]/11):
  speedC,speedD=s.factor((JC.inv()*direction)[1]),s.factor((JD.inv()*direction)[1])
  assert speedC!=0 and speedD!=0
  replC=JC.copy();replC[:,1]=direction
  replD=JD.copy();replD[:,1]=direction
  assert replC==replD and s.factor(detC*speedC-detD*speedD)==0
  residueC=s.factor(1/(poleprod*detC*speedC))
  residueD=s.factor(-1/(poleprod*detD*speedD))
  assert residueC!=0 and residueC+residueD==0
 checks.append({'positive_boundary_point':name,'target_frame':list(fixed),
  'rank_C':8,'rank_D':8,'two_transverse_target_directions_cancel':True,
  'all_fermionic_components_cancel':True})
report={'schema':'marici.nima.nine-point-regular-cd-full-boundary-pole-cancellation.v1',
 'passed':True,'generic_source_boundary':'w4=0 with t>u>0 and other weights positive',
 'oriented_source_eightforms_C_D_opposite':True,
 'full_source_matrices_and_fermionic_numerators_identical_on_boundary':True,
 'seven_target_tangent_columns_identical_on_boundary':True,
 'exact_positive_boundary_controls':checks,
 'consequence':'The full NONLINEAR C/D pushed eight-form local simple-pole residues cancel at the shared w4=0 target facet wherever the maps are regular, for arbitrary transverse target directions and all fermionic components. Three exact regular positive controls certify a nonempty generic open.',
 'scope':'Does not establish regularity at the further t=u corner (D rank drops there), nonlinear form equality away from the common target facet, other cells or full n9 form.'}
(OUT/'nine-point-regular-cd-full-boundary-pole-cancellation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_regular_boundary_controls':len(checks),
 'full_nonlinear_pushed_pole_cancellation':True},indent=2))
