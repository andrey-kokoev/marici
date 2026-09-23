"""Local sixfold Grothendieck fibre contour returns the complete two-sheet four-mass psi."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_loop_canonical_residue as local_residue
 import check_nine_point_loop_fibre_transverse_factorization as transverse
 import check_nine_point_four_mass_loop_embedding as embedded
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars,D9,Z8,Z9=embedded.D,embedded.variables,embedded.D9,embedded.Z8six,embedded.Z9six
rank_six=embedded.rank_six
assert local_residue.report['top_to_source_orientation_sign_in_declared_coordinate_order']==1
assert transverse.report['passed'] and len(transverse.report['source_sheet_tests'])==4
prior=json.loads((OUT/'four-mass-rank-six-Y0-regular-witness.json').read_text());assert prior['passed']
source_rows=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']
reports=[]
for index,row in enumerate(source_rows):
 initial=dict(zip(vars,[s.Rational(v) for v in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(initial);Y=C*Z8
 kernel=Y.nullspace();right=Y.T*(Y*Y.T).inv()
 G=s.Matrix.hstack(*kernel,*[right[:,j] for j in range(2)])
 G[:,0]=G[:,0]/G.det();assert G.det()==1
 ext=Z9*G;assert D9.subs(initial)*ext==D.subs(initial)*(Z8*G)
 fibre=list(rank_six.fibre(C));assert len(fibre)==2
 sheets=[]
 for root,point in fibre:
  source=s.factor(local_residue.residue.subs(point))
  direct=-s.S.One/(s.prod(point[v] for v in vars[:6])*point[vars[7]]*(point[vars[6]]-point[vars[7]]))
  assert source==direct
  Ci=D9.subs(point);image=Ci*ext
  assert image[:,:4]==s.zeros(2,4)
  H=image[:,4:6];assert H.det()!=0
  deriv=[]
  for v in vars:
   result=H.inv()*(D9.diff(v).subs(point)*ext)[:,0:4]
   deriv.append(s.Matrix(list(result)))
  J=s.Matrix.hstack(*deriv).det(method='domain-ge');assert J!=0
  coefficient=s.factor(source/J)
  px=s.det(s.Matrix.hstack(Ci[:,0],Ci[:,4]))
  py=s.det(s.Matrix.hstack(Ci[:,1],Ci[:,5]))
  assert px!=0 and py!=0
  sheets.append({'positive_source_sheet':root==0,'source_kernel_area':str(root),
                 'localized_fibre_residue':str(coefficient),
                 'fermionic_pair_ratio':str(s.factor(py/px)),
                 'coefficient_exact':coefficient,'pair_x_exact':px,'pair_y_exact':py})
 total=s.factor(sum(r['coefficient_exact'] for r in sheets))
 positive_only=next(r['coefficient_exact'] for r in sheets if r['positive_source_sheet'])
 assert total!=positive_only and all(r['coefficient_exact']!=0 for r in sheets)
 assert total==s.Rational(prior['witnesses'][index]['Y0_chart_two_sheet_coefficient'])
 moments=[s.factor(sum(r['coefficient_exact']*r['pair_x_exact']**(4-j)*r['pair_y_exact']**j for r in sheets)) for j in range(5)]
 hankel=s.Matrix(3,3,lambda i,j:moments[i+j]);assert hankel.rank()==2 and hankel.det()==0
 assert sheets[0]['fermionic_pair_ratio']!=sheets[1]['fermionic_pair_ratio']
 reports.append({'source_weights':row['weights'],'localized_sheet_count':2,
  'nonpositive_continuation_sheet_required':sum(r['positive_source_sheet'] for r in sheets)==1,
  'two_sheet_trace_matches_independently_checked_Y0_source_form':True,
  'two_sheet_trace_differs_from_positive_local_residue':True,
  'rank_two_fourth_order_flavor_hankel':True,
  'complete_four_mass_two_sheet_trace_coefficient':str(total),
  'sheets':[{k:r[k] for k in ('positive_source_sheet','source_kernel_area','localized_fibre_residue','fermionic_pair_ratio')} for r in sheets]})
report={'schema':'marici.nima.nine-point-sixfold-fibre-contour-two-sheet-trace.v1','passed':True,
 'local_contour_definition':'At fixed regular Y0, take the sum of the two small complex six-tori around the fibre intersections with cyclic source poles (12),(23),(34),(45),(67),(89) in the normal order a,b,c,h,e,f. The top cyclic G(2,9) source form has oriented residue equal to the eight-point fourmass source form; the exact 14x14 transverse Jacobian splits into target J8 and fibre M6, so each fixed-Y sixfold residue is source_density/J8 times the full fermionic delta product.',
 'witnesses':reports,
 'boundary':'This is a SPECIFIED complexified local fibre contour summing both source sheets, one not positive. It is NOT an identification with the canonical positive six-dimensional fibre contour, full nine-point image form, or full nine-point scattering amplitude. Fermionic four-flavor coefficients inherit the symbolic D9*chi9=D8*chi8 identity.'}
(OUT/'nine-point-sixfold-fibre-contour-two-sheet-trace.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_rank_six_targets':len(reports),
 'local_complex_sixfold_residues_per_target':2,'complete_two_sheet_hankel_rank':2},indent=2))
