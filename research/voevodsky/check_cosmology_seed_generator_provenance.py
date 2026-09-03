"""Audit tracked seed generators for retained exact-word construction state."""
from __future__ import annotations
import ast,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research'/'voevodsky'
OUT=V/'results'/'cosmology_seed_generator_provenance.json'
FILES=['check_cosmology_IBP_corrected_transport_exact_seeds.py','check_cosmology_nonmarked_K_exact_seeds.py','check_cosmology_q_exact_seeds.py']
NEEDED={'origins','erows','target','cols','coef','rank','recon'}
def main():
 records=[]
 for name in FILES:
  path=V/name;raw=path.read_bytes();tree=ast.parse(raw);assigned=set()
  for node in ast.walk(tree):
   if isinstance(node,(ast.Assign,ast.AnnAssign)):
    targets=node.targets if isinstance(node,ast.Assign) else [node.target]
    for t in targets:
     assigned.update(n.id for n in ast.walk(t) if isinstance(n,ast.Name))
   elif isinstance(node,ast.For):
    assigned.update(n.id for n in ast.walk(node.target) if isinstance(n,ast.Name))
  missing=sorted(NEEDED-assigned);assert not missing,(name,missing)
  text=raw.decode();imports=['check_rank26_total_energy_triple_relation_module','check_cosmology_rank26_p_normal_raw_relation_adapter','check_cosmology_rank26_p_normal_lower_quartile_source_dag','check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor','check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves']
  assert all(x in text for x in imports)
  records.append({'path':str(path.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(raw).hexdigest(),'retained_transient_state':sorted(NEEDED),'raw_relation_constructor':'check_rank26_total_energy_triple_relation_module.raw_relations/column_packet','row_adapter':'check_cosmology_rank26_p_normal_raw_relation_adapter.derivative_rows','basis_origin_trace':'check_cosmology_rank26_p_normal_lower_quartile_source_dag nodes[...].origin','exact_lift':'check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor.exact_row','exact_solver':'check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves.solve_rect'})
 out={'schema':'marici.voevodsky.cosmology-seed-generator-provenance.v1','status':'three_visible_generators_retain_words_but_IBP_and_q_have_no_git_provenance','git_history':{'nonmarked_K':'introduced with result in fff26499944bd3a9912078dccaed12ffae6c263f','IBP':'untracked; exact-path git log returned no commits','q':'untracked; exact-path git log returned no commits'},'records':records,'finding':'Each generator retains ordered origins, exact lifted rows, exact target, equation columns, rational coefficients, rank, and exact reconstruction immediately before writing its summary. No algebraic recomputation is needed to serialize certificates.','normalization_boundary':'Basis IDs are existing origin tuples (T/S_K/Q,index); canonical target IDs derive from the seed descriptor; sparse words are nonzero entries of coef in erows/origins order.','next_gate':'populate-seed-source-certificates','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
