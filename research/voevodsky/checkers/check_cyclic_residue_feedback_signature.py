from __future__ import annotations
import json
from pathlib import Path

SOURCE=Path('research/voevodsky/cyclic-residue-feedback-signature.json')
OUT=Path('research/voevodsky/results/cyclic_residue_feedback_signature.json')

def main():
 d=json.loads(SOURCE.read_text(encoding='utf-8'))
 vertices=d['vertices']; expected={'A','B','C'}
 complete_vertices=set(vertices)==expected and all(
  {'parameter_sort','object_sort','residue_sort','generator','coherencer'}<=set(vertices[v]) for v in expected)
 transports=set(d['residue_transports'])=={'T_A','T_B','T_C'}
 transitions=set(d['transition_candidates'])=={'Phi_A','Phi_B','Phi_C'}
 cells=set(d['edge_comparison_2_cells'])=={'alpha_A','alpha_B','alpha_C'}
 cyclic_typing=all([
  'R_A -> P_B' in d['residue_transports']['T_A'],
  'R_B -> P_C' in d['residue_transports']['T_B'],
  'R_C -> P_A' in d['residue_transports']['T_C'],
  'G_B o T_A o C_A' in d['edge_comparison_2_cells']['alpha_A'],
  'G_C o T_B o C_B' in d['edge_comparison_2_cells']['alpha_B'],
  'G_A o T_C o C_C' in d['edge_comparison_2_cells']['alpha_C']])
 realization=d['realization_state']; missing=sorted(k for k,v in realization.items() if v=='missing')
 result={
  'schema':'marici.voevodsky.cyclic-residue-feedback-signature-check.v1',
  'three_vertices_simultaneously_declared':complete_vertices,
  'three_transports_declared':transports,
  'three_transitions_declared':transitions,
  'three_edge_cells_declared':cells,
  'counterclockwise_typing_verified':cyclic_typing,
  'cycle_cell_declared':'Omega_ABC' in d['cycle_cell']['name'],
  'completion_obligation_declared':'omega-limit' in d['completion_interface']['obligation'],
  'missing_realizations':missing,
  'signature_complete':all([complete_vertices,transports,transitions,cells,cyclic_typing]),
  'realization_complete':not missing,
  'passed':all([complete_vertices,transports,transitions,cells,cyclic_typing])}
 text=json.dumps(result,indent=2,sort_keys=True);OUT.write_text(text+'\n',encoding='utf-8');print(text)
if __name__=='__main__':main()
