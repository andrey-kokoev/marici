from __future__ import annotations
import json
from pathlib import Path

BASE=Path('research/aspect/contracts/theta-rh-interaction-net-state.v1.json')
OUT=Path('research/voevodsky/contracts/theta-rh-cubical-scc-overlay.v1.json')
PACKET='research/voevodsky/cyclic-local-realizations-and-global-pasting-gate.md'

def node(i,status,deps,source=PACKET,authority='algebraic_derived_nonrealization'):
 return {'id':i,'status':status,'source_locator':source if status=='constructed' else None,'depends_on':deps,'authority_class':authority if status=='constructed' else 'formal_slot'}

def main():
 c=json.loads(BASE.read_text(encoding='utf-8'))
 additions=[
  node('cubical_level0_three_vertex_faces','constructed',[],'research/voevodsky/cyclic-residue-feedback-signature.json'),
  node('cubical_level1_three_edge_comparisons','constructed',['cubical_level0_three_vertex_faces']),
  node('cubical_level2_global_lax_filler','constructed',['cubical_level1_three_edge_comparisons'],'research/voevodsky/cyclic-filler-pasting-complex.md'),
  node('cubical_completion_preservation','constructed',['cubical_level2_global_lax_filler'],'research/voevodsky/cyclic-residue-feedback-categorical-completion.md'),
  node('cubical_residual_child_tower','constructed',['cubical_level2_global_lax_filler'],'research/voevodsky/cyclic-filler-pasting-complex.md'),
  node('cubical_residual_parent_promotion','open',['cubical_residual_child_tower'])]
 ids={x['id'] for x in c['constructors']};assert not ids.intersection(x['id'] for x in additions)
 c['constructors'].extend(additions)
 c['cubical_adapter']={
  'source':'research/voevodsky/cyclic-residue-feedback-signature.json',
  'projection':{'vertices':'level0','edge_cells':'level1','Omega_ABC':'level2','residual_feedback':'child_tower'},
  'promotion_policy':'residual re-entry cannot modify parent without cubical_residual_parent_promotion',
  'cubical_type_theory_implementation':False,
  'source_global_naturality':False,
  'canonical_scc_contract_mutated':False}
 OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(c,indent=2)+'\n',encoding='utf-8');print(OUT)
if __name__=='__main__':main()
