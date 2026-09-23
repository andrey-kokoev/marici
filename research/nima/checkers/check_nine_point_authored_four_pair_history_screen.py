"""Screen sourced n=9 nested-R histories against the four-pair label envelope."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima'))
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
source=(ROOT/'research/sources/nima/papers/n2mhv-tree/0808.2475/newrecursionv6.tex').read_text()
for token in (r'\label{PNNMHVnew}',r'\label{Lrep}',r'\label{Urep}',r'\label{generalR}'):
 assert token in source
histories=compile_nnmhv_histories(9)
target=set((1,2,4,5,6,7,8,9))
def envelope(h):
 a,b=h.outer_pair;c,d=h.inner_pair
 # Explicit momentum-twistor endpoint footprint of the two R factors;
 # terminal context/superscript vertices add only authored ancestors.
 endpoints={h.n,a-1,a,b-1,b,c-1,c,d-1,d}
 state=terminal_r_state(h)
 for spinor in (state.xi,state.lower_spinor,state.upper_spinor):endpoints.update(spinor.vertices)
 return endpoints
rows=[]
for index,h in enumerate(histories):
 footprint=envelope(h)
 rows.append({'history_index':index,'outer_pair':list(h.outer_pair),'inner_pair':list(h.inner_pair),
  'branch':h.branch,'boundary_updates':[{'side':u.side,'replacement_path':list(u.replacement_path)} for u in h.boundary_updates],
  'terminal_xi_path':list(terminal_r_state(h).xi.vertices),
  'explicit_endpoint_envelope':sorted(footprint),
  'has_no_explicit_label_three':3 not in footprint,
  'exact_eight_label_endpoint_match':footprint==target})
matched=[r for r in rows if r['exact_eight_label_endpoint_match']]
missing=[r for r in rows if r['has_no_explicit_label_three']]
assert len(histories)>20 and len(histories)==len(rows)
assert all((r['outer_pair'][0]==2) for r in matched)
assert all(r['explicit_endpoint_envelope']==sorted(target) for r in matched)
assert all(not r['exact_eight_label_endpoint_match'] for r in rows if 3 in r['explicit_endpoint_envelope'])
report={'schema':'marici.nima.nine-point-authored-four-pair-history-screen.v1','passed':True,
 'source':'research/sources/nima/papers/n2mhv-tree/0808.2475/newrecursionv6.tex, equations PNNMHVnew, generalR, Lrep, Urep',
 'n9_authored_history_count':len(rows),
 'no_explicit_label_three_count':len(missing),
 'exact_eight_label_endpoint_candidate_count':len(matched),
 'exact_eight_label_endpoint_candidates':matched,
 'all_history_records':rows,
 'claim_boundary':'An exact AUTHORED INDEX and endpoint-path screening, not a momentum-twistor generalized-R formula, fermionic-support proof, positroid matching or equality to the four-pair psi cell. Superscript boundary transport has been recorded but not algebraically reduced to an on-shell matrix. Any candidate requires a true source-to-positroid chart and orientation comparison.'}
path=ROOT/'research/nima/results/nine-point-authored-four-pair-history-screen.json'
path.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'n9_histories':len(rows),'no_label_three':len(missing),
 'exact_endpoint_candidates':len(matched),'candidate_indices':[r['history_index'] for r in matched]},indent=2))
