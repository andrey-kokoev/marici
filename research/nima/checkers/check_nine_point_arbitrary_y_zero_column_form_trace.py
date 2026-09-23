"""Transport compact arbitrary-Y two-sheet four-pair trace to n=9 zero-column history."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_four_mass_global_target_trace_by_recentring as global_trace
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=global_trace.D,global_trace.variables
C9=s.Matrix.hstack(D[:,:2],s.zeros(2,1),D[:,2:])
Z8=s.Matrix(8,6,lambda i,j:s.Symbol(f'Z{i+1}_{j+1}'))
z3=s.Matrix(1,6,lambda _,j:s.Symbol(f'Z3_{j+1}'))
Z9=s.Matrix.vstack(Z8[:2,:],z3,Z8[2:,:])
chi8=s.Matrix(8,4,lambda i,j:s.Symbol(f'chi{i+1}_{j+1}'))
chi3=s.Matrix(1,4,lambda _,j:s.Symbol(f'chi3_{j+1}'))
chi9=s.Matrix.vstack(chi8[:2,:],chi3,chi8[2:,:])
assert C9*Z9==D*Z8 and C9*chi9==D*chi8
for parameter in vars:
 assert C9.diff(parameter)*Z9==D.diff(parameter)*Z8
# For arbitrary FIRST-PIVOT TARGET B, the SAME SL(6) recentering
# applies to all nine Z rows. The physical third row drops out of
# both the fibre ideal C9*z9=0 and the weight det(C9*h9)^4.
B=global_trace.B;G=global_trace.G
z8=Z8[:,2:]-Z8[:,:2]*B;h8=Z8[:,:2]
z9=Z9[:,2:]-Z9[:,:2]*B;h9=Z9[:,:2]
assert Z9*G==z9.row_join(h9)
assert C9*z9==D*z8 and C9*h9==D*h8
assert s.Matrix(list(C9*z9)).jacobian(vars)==s.Matrix(list(D*z8)).jacobian(vars)
assert (C9*h9).det()==(D*h8).det()
# No symbolic evaluation of the huge generic determinant is needed:
# the two determinant MATRICES, numerators and fibre ideals agree
# identically before their quadratic field traces are taken.
controls=[]
for index in range(3):
 if index<2:
  sample=global_trace.prior['rows'][index]
  weights=[s.Rational(v) for v in sample['weights']]+[s.Rational(sample['t']),s.Rational(sample['u'])]
  ext=global_trace.old.Z
 else:
  weights=[s.Rational(x) for x in (2,3,1,4,2,5)]+[s.Rational(7,2),s.Rational(3,2)]
  ext=s.Matrix([[j**degree for degree in range(6)] for j in range(1,9)])
 point=dict(zip(vars,weights))
 for row3 in (s.Matrix([[3**d for d in range(6)]]),
              s.Matrix([[2,7,11,17,23,31]])):
  nine=s.Matrix.vstack(ext[:2,:],row3,ext[2:,:])
  Y9=C9.subs(point)*nine;Y8=D.subs(point)*ext
  assert Y9==Y8
  H=Y8[:,:2];assert H.det()!=0
  target=H.inv()*Y8[:,2:]
  assert C9.subs(point)*nine*G.subs(dict(zip(list(B),list(target))))==Y8*G.subs(dict(zip(list(B),list(target))))
  for parameter in vars:
   delta9=C9.diff(parameter).subs(point)*nine
   delta8=D.diff(parameter).subs(point)*ext
   assert delta9==delta8
  controls.append({'target_sample':index,'inserted_row3':[str(z) for z in row3],
    'full_target_and_all_eight_source_derivatives_independent_of_row3':True,
    'same_both_sheet_trace_as_eight_point':global_trace.rows[index]['complete_target_eight_form_coefficient']})
report={'schema':'marici.nima.nine-point-arbitrary-y-zero-column-form-trace.v1','passed':True,
 'universal_arbitrary_Y_nine_point_source_coefficient':
 'For Y=[I2|B] and nine external rows Z9, write z9=Z9_last4-Z9_first2*B, h9=Z9_first2. Tr_{two solutions C9(v)*z9=0}[-det(C9(v)*h9)^4/{w2*w4*w5*w6*w7*w8*u*(t-u)*det(d(C9(v)*z9)/dv)}] equals identically the sourced eight-point four-pair trace after deleting physical label3, on the simple-fibre open set. The full fermionic numerator C9*chi9 is also independent of chi3.',
 'symbolic_all_Y_fibre_ideal_and_jacobian_independent_of_Z3':True,
 'symbolic_fermionic_numerator_independent_of_chi3':True,
 'exact_target_and_arbitrary_inserted_row_controls':controls,
 'scope':'An exact arbitrary-Y rational two-sheet trace for ONE zero-column n9 sourced four-pair contribution, not the COMPLETE nine-point NNMHV amplitude or positive-image canonical form. Inserting arbitrary row3 does not prove that this cell covers the n9 positive image.'}
(OUT/'nine-point-arbitrary-y-zero-column-form-trace.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'universal_arbitrary_Y_column3_decoupling':True,
 'target_controls':len(controls),'full_nine_point_form_open':True},indent=2))
