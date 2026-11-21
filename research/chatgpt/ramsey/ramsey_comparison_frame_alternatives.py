"""Distinguish a fixed vertex permutation from a genuine row relabeling of the new incidence chart; compare conjugated-frame and fixed-R outputs."""
from pathlib import Path
import json
from ramsey_center_transfer_seed_binding import A,row,R,switched,hub
from ramsey_row_center_calculus import relabel
D=Path(__file__).parent;B=switched;v=1+hub;U=B[v];W=[w for w in range(22) if w!=v and not U>>w&1];fixed=relabel(B,R)
def chart_changes(C):
 assert C[v]==U
 return [w for w in W if C[w]&U!=B[w]&U]
def diff(C,D):return sum((a^b).bit_count() for a,b in zip(C,D))//4
rows=[]
for item in json.loads((D/'ramsey_row_center_calculus.json').read_text())['mark_transports']:
 K=item['permutation'];RK=[K[R[K[i]]] for i in range(22)];conjugated=relabel(B,RK);assert conjugated==relabel(row,K);entry=K[7];exit={K[w] for w in (11,14,16)};assert RK[entry]==entry and {RK[w] for w in exit}==exit
 rows.append({'phase':item['phase'],'fixed_vs_conjugated_outputs_equal':fixed==conjugated,'chart_changes_under_conjugated':chart_changes(conjugated),'edges_replaced_from_transferred_graph':diff(B,conjugated),'edges_different_between_comparisons':diff(fixed,conjugated),'comparison_permutation':RK})
label_vertices=[u for u in range(22) if U>>u&1];pair_to_vertex={frozenset(u for u in label_vertices if B[w]>>u&1):w for w in W};lift=list(range(22))
for u in label_vertices:lift[u]=R[u]
for pair,w in pair_to_vertex.items():lift[w]=pair_to_vertex[frozenset(R[u] for u in pair)]
matching_phases=[r['phase'] for r in rows if r['comparison_permutation']==lift];assert len(matching_phases)==1
result={'canonical_relift':lift,'canonical_relift_transport_phase':matching_phases[0],'fixed_R_chart_changes':chart_changes(fixed),'fixed_R_edges_replaced':diff(B,fixed),'conjugated_options':rows};(D/'ramsey_comparison_frame_alternatives.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
