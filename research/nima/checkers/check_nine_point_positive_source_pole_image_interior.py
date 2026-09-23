"""Exact positive full n9 preimage of the positive four-mass w4=0 pole target."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_four_mass_positive_source_boundary_pole_slice as source_pole
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
C=loop.D9.subs(source_pole.point)
frame=loop.Z8six[:6,:].inv();assert frame.det()>0
external=loop.Z9six*frame
K=s.Matrix.vstack(*(v.T for v in external.T.nullspace()))
assert K.shape==(3,9) and K*external==s.zeros(3,6)
T=s.Matrix([[s.Rational('0.18780'),s.Rational('-0.17109'),s.Rational('0.04228')],
            [s.Rational('-0.55713'),s.Rational('0.37724'),s.Rational('-0.08275')]])
positive=C+T*K
minors=[]
for i,j in itertools.combinations(range(9),2):
 val=s.det(s.Matrix.hstack(positive[:,i],positive[:,j]))
 assert val>0,(i+1,j+1,val)
 minors.append(val)
assert positive*external==C*external
for chosen in itertools.combinations(range(9),6):
 expected=s.prod(b-a for a,b in itertools.combinations((i+1 for i in chosen),2))*frame.det()
 assert expected>0
 assert external[list(chosen),:].det(method='domain-ge')==expected
Y=positive*external;H=Y[:,4:6];assert H.det()!=0
B=H.inv()*Y[:,:4]
columns=[]
for variable in loop.variables:
 delta=loop.D9.diff(variable).subs(source_pole.point)*external
 dB=H.inv()*(delta[:,:4]-delta[:,4:6]*B)
 columns.append(s.Matrix(list(dB)))
J=s.Matrix.hstack(*columns).det(method='domain-ge');assert J!=0
report={'schema':'marici.nima.nine-point-positive-source-pole-image-interior.v1','passed':True,
 'positive_fourmass_boundary_pole_epsilon':str(source_pole.pole),
 'exact_left_kernel_displacement_T':[[str(T[i,j]) for j in range(3)] for i in range(2)],
 'same_two_by_six_target_matrix_exact':True,
 'all_36_ordered_two_minors_of_full_source_strictly_positive':True,
 'minimum_ordered_two_minor':str(min(minors)),
 'all_84_ordered_external_six_minors_strictly_positive':True,
 'eight_dimensional_target_chart_jacobian_nonzero_at_positive_full_source':True,
 'conclusion':'The exact target at which the positive fourmass source cell has a genuine w4=0 pushed-form pole ALSO has an explicitly certified strictly positive full n9 top-cell preimage with a surjective rank-eight local target map. Hence the target is INTERIOR to the n9 positive top-cell image at this external data, not an image-boundary face. The positive-cell contour pole therefore cannot be promoted to a canonical full-image boundary pole merely from its source-cell provenance.',
 'boundary':'One exact rank-six positive external witness and one target. Interior regularity of the FULL IMAGE canonical form is a standard positive-geometry expectation, not an explicitly computed full-image canonical form here. No global form equality or cancellation mechanism among all source cells is asserted.'}
(OUT/'nine-point-positive-source-pole-image-interior.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'exact_same_target_positive_preimage':True,
 'all_source_minors_positive':36,'all_external_six_minors_positive':84,
 'target_chart_rank':8},indent=2))
