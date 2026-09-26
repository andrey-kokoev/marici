"""Exact finite contour sieve for chi3-blind unit-weight subsets of the four label3 cells."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_square_full_chi3_target_trace as trace
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
labels=('E','E_B','E_C','E_D')
rows=[]
for row in trace.rows:
 values={'E':s.Rational(row['E_two_sheet_chi3_power4_chi5_power4'])}
 values.update({name:s.Rational(v) for name,v in row['three_one_sheet_terms'].items()})
 assert set(values)==set(labels)
 binary_cancel=[];signed_cancel=[]
 for weights in itertools.product((0,1),repeat=4):
  if not any(weights):continue
  if sum(values[z]*w for z,w in zip(labels,weights))==0:
   binary_cancel.append(dict(zip(labels,weights)))
 for weights in itertools.product((-1,0,1),repeat=4):
  if not any(weights):continue
  if sum(values[z]*w for z,w in zip(labels,weights))==0:
   signed_cancel.append(dict(zip(labels,weights)))
 assert not binary_cancel and not signed_cancel
 rows.append({'target':row['target'],'nonempty_binary_subsets_tested':15,
              'nonzero_signed_unit_combinations_tested':80,
              'chi3_blind_binary_subsets':binary_cancel,
              'chi3_blind_signed_unit_combinations':signed_cancel})
# Relabelling the zero-phys3 square yields the label3 square exactly.
# Relative to original A-oriented density each relabelled cell changes
# its overall source sign; source-to-target fibre and fermion numerator
# are identical after deletion of the dormant physical row.
square=trace.bir.square
for original,new in zip('ABCD',labels):
 source=square.source[new]
 assert square.cells[new][:,1]==s.zeros(2,1)
 assert square.cells[new][:,[0,2,3,4,5,6,7,8]]==source
 assert square.sign[new]=={'A':1,'B':-1,'C':-1,'D':1}[original]
report={'schema':'marici.nima.nine-point-label3-square-unit-contour-support-sieve.v1',
 'passed':True,'exact_common_target_controls':rows,
 'unit_contour_obstruction':'At EACH exact common first-pivot rank-six positive target, every nonempty subset of the four complete oriented label3 cell traces has nonzero chi3^4 chi5^4 coefficient; even allowing each cell coefficient from {-1,0,+1}, all 80 nonzero combinations remain nonzero. Therefore NO constant unit-weight selection/reversal within the explicit label3 square can produce a generically chi3-blind rational superform. The zero-phys3 four-cell square and vertical F are chi3^4 chi5^4-blind, so including them cannot alter this component.',
 'scope':'Only chi3-BLIND candidate forms and bounded integer coefficients are constrained. The actual full nine-point amplitude may be chi3-sensitive; additional label3 cells or non-unit/bosonic weights could change the comparison. No global contour or canonical form is established.'}
(OUT/'nine-point-label3-square-unit-contour-support-sieve.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'controls':len(rows),'nonempty_unit_subsets_checked':15,
 'nonzero_signed_unit_combinations_checked':80,'cancellations_found':0},indent=2))
