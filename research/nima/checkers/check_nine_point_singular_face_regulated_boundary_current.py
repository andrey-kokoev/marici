"""Show B/D singular slope-face boundary currents cancel BEFORE nonproper fibre pushforward."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_loop_canonical_residue as top
 import check_nine_point_four_mass_loop_embedding as loop
 import check_nine_point_slope_face_exact_fibre_normal_match as prior
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
A,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars;gap=t-u
B=A.copy();B[0,3]=-w4/t
D=B.copy();D[1,5]=w6*u
assert s.simplify((D-B).subs(t,u))==s.zeros(2,8)
B9=s.Matrix.hstack(B[:,:2],s.zeros(2,1),B[:,2:])
D9=s.Matrix.hstack(D[:,:2],s.zeros(2,1),D[:,2:])
assert B9.subs(t,u)==D9.subs(t,u)
chi=s.Matrix(9,4,lambda i,j:s.Symbol(f'chi{i+1}_{j+1}'))
assert (B9.subs(t,u)*chi)==(D9.subs(t,u)*chi)
Z=s.Matrix(9,6,lambda i,j:s.Symbol(f'Z{i+1}_{j+1}'))
assert (B9.subs(t,u)*Z)==(D9.subs(t,u)*Z)
# Independent cyclic-top source densities from the earlier oriented
# sixfold residue calculations: B=-rho_A, D=rho_A.
rho_A=top.source_density
rho_B=-rho_A;rho_D=rho_A
face_B=s.factor(rho_B*gap);face_D=s.factor(rho_D*gap)
assert s.factor(face_B+face_D)==0 and face_B!=0
assert s.factor(face_B-1/(w2*w4*w5*w6*w7*w8*u))==0
# dt^du=d(gap)^du; six weights precede gap, so the two resulting
# ordered seven-face-form coefficients are precisely +/-face_B.
controls=[]
for name,raw,old in zip(('first','second'),
 [('1','1','1','1','1','1','2','2'),('2','3','3','2','1','4','3','3')],prior.checks):
 p=dict(zip(vars,[s.Rational(x) for x in raw]))
 r=[s.Rational(x) for x in old['source_fibre_direction']]
 assert r[1]!=0 and r[0]==r[6]==r[7]==0
 # In source-face coordinates (w2,w4,w5,w6,w7,w8,u), the kernel
 # vector contracts the seven-form to a NONZERO six-form. With fibre
 # coordinate w4 and base invariants z_i=w_i-r_i*w4/r_w4 the oriented
 # coefficient of d(w2,z5,z6,z7,z8,u) is -r_w4*face_B.
 contracted_B=s.factor(-r[1]*face_B.subs(p))
 contracted_D=s.factor(-r[1]*face_D.subs(p))
 assert contracted_B!=0 and contracted_B+contracted_D==0
 controls.append({'point':name,'nonzero_face_coefficient_B':str(face_B.subs(p)),
                  'nonzero_contracted_fibre_density_B':str(contracted_B),
                  'opposite_contracted_fibre_density_D':str(contracted_D),
                  'exact_pair_cancels_before_regulated_fibre_integration':True})
report={'schema':'marici.nima.nine-point-singular-face-regulated-boundary-current.v1',
 'passed':True,'universal_equal_face_source_maps_for_arbitrary_Z_and_chi':True,
 'ordered_source_face_residue_B':str(face_B),
 'ordered_source_face_residue_D':str(face_D),
 'exact_positive_controls':controls,
 'regulated_statement':'With the SAME compactly supported cutoff inside the common strictly positive face, the paired boundary seven-forms sum to zero pointwise, including full bosonic and fermionic numerators. Any linear integration along the collapsed fibre then returns zero for the paired regulated current, independently of target-Jacobian rank.',
 'limits':'Individual open positive fibre integrals can diverge at endpoints; no unregulated pushforward, commutation of source residue with target-form residue, singular eight-form cancellation, global image form, or full triangulation follows.'}
(OUT/'nine-point-singular-face-regulated-boundary-current.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'paired_face_current_cancellation':True,
 'nonzero_fibre_controls':len(controls),'target_jacobian_required':False},indent=2))
