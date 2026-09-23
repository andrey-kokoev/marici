"""Falsify identification of the ordinary-product n=9 history with four-mass psi."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_four_mass_complete_component_companion_trace as psi
 import check_nine_point_four_mass_auxiliary_match as aux
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
screen=json.loads((OUT/'nine-point-authored-four-pair-history-screen.json').read_text())
assert screen['passed'] and [r['history_index'] for r in screen['exact_eight_label_endpoint_candidates']]==[9,27]
# The retained local labels (1..8) map to physical n=9 labels
# (1,2,4,5,6,7,8,9); history 9 is the ordinary R_{9;2,5} R_{9;6,8}
# product. Its momentum-twistor factors are [8,1,2,3,4] [8,4,5,6,7].
def five_component(br,sequence,label):
 assert len(sequence)==5 and label in sequence
 denominator=s.prod(br(*(sequence[(offset+i)%5] for i in range(4))) for offset in range(5))
 remainder=[x for x in sequence if x!=label]
 return br(*remainder)**4/denominator
def candidate9(br):return s.factor(five_component(br,(8,1,2,3,4),1)*five_component(br,(8,4,5,6,7),5))
zs=[('frozen_quotient',aux.bracket),('independent_moment_curve',psi.moment_br)]
rows=[]
for name,br in zs:
 source,_=psi.complete_component(br)
 ordinary=candidate9(br)
 assert source!=0 and ordinary!=0 and source!=ordinary
 rows.append({'data':name,'complete_sourced_psi_component':str(source),
  'history9_ordinary_five_bracket_product_component':str(ordinary),
  'ratio_history9_to_psi':str(s.factor(ordinary/source)),
  'not_equal':True})
assert rows[0]['ratio_history9_to_psi']!=rows[1]['ratio_history9_to_psi']
report={'schema':'marici.nima.nine-point-candidate9-vs-four-mass-psi.v1','passed':True,
 'published_nested_R_history_index':9,
 'history_label':'R_{9;2,5}^{0;0} R_{9;6,8}^{2,5;0} with no active lower boundary replacement; ordinary five-bracket product on the retained labels',
 'local_to_physical_label_map':[1,2,4,5,6,7,8,9],
 'independent_kinematic_witnesses':rows,
 'conclusion':'The authored ordinary-product history 9 is NOT IDENTICAL as a standalone term to the complete starred four-mass psi invariant: their eta1^4 eta5^4 ratios are nonconstant on two independent exact inputs. This does not exclude a sum of histories, another representation, or a role for candidate 27 with a transported xi spinor.',
 'remaining_candidate_27':'outer (2,8), left-nested inner (5,7), transported xi=(9,8,2), no boundary replacements; requires explicit generalized-R momentum-twistor/positroid translation.'}
(OUT/'nine-point-candidate9-vs-four-mass-psi.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'candidate9_standalone_equal':False,
 'independent_ratios':[r['ratio_history9_to_psi'] for r in rows],
 'remaining_endpoint_candidate':27},indent=2))
