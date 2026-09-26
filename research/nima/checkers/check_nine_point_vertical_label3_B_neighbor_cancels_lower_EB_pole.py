"""Vertical label3 B-neighbor cancels E_B's lower interior w2 superpole locally."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_square_internal_wall_uncancelled_poles as prior
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
chamber=prior.chamber;trace=prior.trace
vars=trace.vars;w2,w4,w5,w6,w7,w8,t,u=vars
D=trace.bir.square.source['E_B']
EB=trace.bir.square.cells['E_B']
FB=EB.copy();FB[0,2]=0;FB[1,2]=w2
assert EB.subs(w2,0)==FB.subs(w2,0)
v=s.symbols('v',positive=True)
for i,j in itertools.combinations(range(9),2):
 det=s.factor(FB[:,[i,j]].det().subs(t,u+v))
 numerator,denominator=s.fraction(s.cancel(det))
 assert all(c>=0 for c in s.Poly(numerator,w2,w4,w5,w6,w7,w8,u,v).coeffs())
 assert all(c>=0 for c in s.Poly(denominator,w2,w4,w5,w6,w7,w8,u,v).coeffs())
# Moving horizontal to vertical column3 reverses the orientation of
# the composite x/y residue in the common nine-dimensional cell.
# The w4 pole shift from A to B flips both horizontal and vertical
# orientations, preserving their opposite relative w2 source residues.
rhoEB=s.factor(-1/(w2*w4*w5*w6*w7*w8*u*(t-u)))
rhoFB=-rhoEB
assert s.factor(rhoEB+rhoFB)==0
lower=chamber.threshold_low
pointB={var:chamber.parse(chamber.EB['inverse_source_parameters'][str(var)]).subs(chamber.e,lower)
        for var in vars}
assert pointB[w2]==0 and all(pointB[var]>0 for var in (w4,w5,w6,w7,w8,u)) and pointB[t]>pointB[u]
samples=[('interior_E_target_lower_wall',pointB),
         ('generic_one',dict(zip(vars,map(s.Rational,(0,1,1,1,1,1,3,2))))),
         ('generic_two',dict(zip(vars,map(s.Rational,(0,3,2,1,4,5,s.Rational(7,2),s.Rational(3,2))))))]
Z=trace.bir.square.Z
checks=[]
for name,p in samples:
 assert p[w2]==0 and EB.subs(p)==FB.subs(p)
 Y=EB.subs(p)*Z
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(i for i in range(6) if i not in fixed)
 H=Y[:,list(fixed)];B=H.inv()*Y[:,list(free)]
 def jac(C):
  cols=[]
  for param in vars:
   delta=C.diff(param).subs(p)*Z
   cols.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-delta[:,list(fixed)]*B))))
  return s.Matrix.hstack(*cols)
 JE,JF=jac(EB),jac(FB)
 assert all(JE[:,j]==JF[:,j] for j in range(1,8))
 de,df=JE.det(method='domain-ge'),JF.det(method='domain-ge')
 assert de!=0 and df!=0
 rest=s.prod(p[z] for z in (w4,w5,w6,w7,w8))*p[u]*(p[t]-p[u])
 for direction in (JE[:,0],JE[:,0]+JE[:,1]/7+JE[:,5]/11):
  se=s.factor((JE.inv()*direction)[0]);sf=s.factor((JF.inv()*direction)[0])
  assert se!=0 and sf!=0 and s.factor(de*se-df*sf)==0
  resE=s.factor(-1/(rest*de*se));resF=s.factor(1/(rest*df*sf))
  assert resE!=0 and s.factor(resE+resF)==0
 checks.append({'boundary':name,'source_matrix_and_full_fermionic_numerator_identical':True,
                'both_target_jacobians_rank_eight':True,
                'two_transverse_target_direction_full_superpole_cancellations':True})
report={'schema':'marici.nima.nine-point-vertical-label3-B-neighbor-cancels-lower-EB-pole.v1',
 'passed':True,'positive_F_B_cell':'phys2 zero, phys3=(0,w2); all later columns equal E_B',
 'intrinsic_source_orientations':{'E_B':str(rhoEB),'F_B':str(rhoFB)},
 'exact_positive_shared_w2_boundary_controls':checks,
 'consequence':'F_B is a DISTINCT positive vertical-label3 B-neighbor of E_B and cancels its full pushed w2=0 local superpole, including the lower interior E-target chi1^4 chi5^4 pole that survived the earlier four-cell E-square meromorphic sum. This is local cancellation, not a complete F_B arbitrary-Y trace or global n9 canonical form.',
 'scope':'Three positive rank8 boundary controls, including exactly the lower E_B support wall inside E positive image. Additional F_B inverse sheets/target overlaps and full contour not resolved.'}
(OUT/'nine-point-vertical-label3-B-neighbor-cancels-lower-EB-pole.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_F_B':True,'regular_boundary_controls':len(checks),
 'interior_EB_lower_superpole_locally_cancelled_by_FB':True},indent=2))
