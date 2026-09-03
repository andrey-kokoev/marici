"""Revised eight-field geometrization contract after source-word recovery."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research'/'voevodsky'/'results';OUT=V/'cosmology_source_geometrization_contract.json'
FIELDS=('canonical_generator_ids','algebraic_source_words','geometric_supports','source_differential','DNC_filtration','exceptional_specialization','transport_coherence','provenance_refs')
def admissible(population):return all(population[k]['populated'] for k in FIELDS)
def main():
 files=['cosmology_IBP_exact_source_certificates_a12.json','cosmology_nonmarked_K_exact_seeds_a12.json','cosmology_q_exact_source_certificates_a12.json'];certs=[]
 for name in files:certs.extend(r['source_certificate'] for r in json.loads((V/name).read_text())['records'])
 assert len(certs)==1224 and len({c['canonical_target_id'] for c in certs})==1224
 assert all(c['source_basis_digest'] and c['sparse_word'] is not None for c in certs)
 assert all(c['generator']['path'].startswith('research/voevodsky/') and len(c['generator']['source_digest'])==64 for c in certs)
 transport=json.loads((V/'cosmology_all_even_linear_transport_induction.json').read_text());composition=json.loads((V/'cosmology_repaired_transport_composition_a16.json').read_text());matrix=json.loads((V/'cosmology_linear_generator_transport_matrix.json').read_text())
 assert transport['passed'] and composition['nonzero_equation_residuals']==0 and matrix['nonzero_residuals']==0
 population={
  'canonical_generator_ids':{'populated':True,'evidence':'A12 labelled (T|S_K|Q,index) bases bound to generator digests; descriptor shift matrix supplies typed all-even images'},
  'algebraic_source_words':{'populated':True,'evidence':'1,224 normalized sparse rational certificates with exact replay'},
  'geometric_supports':{'populated':False,'missing':'map from every labelled algebraic generator to a source-derived support locus'},
  'source_differential':{'populated':False,'missing':'differential on the proposed geometric source object and d^2 residual'},
  'DNC_filtration':{'populated':False,'missing':'filtration degree and Rees/DNC map for each supported generator'},
  'exceptional_specialization':{'populated':False,'missing':'specialization map to a named exceptional-supported target complex'},
  'transport_coherence':{'populated':True,'evidence':'524,224 generator-row tests, 2,448 A14 certificate squares, 4,896 A16 paths, and symbolic all-even induction'},
  'provenance_refs':{'populated':True,'evidence':'certificate generator paths/source digests plus checker/result chain'} }
 assert not admissible(population)
 fabricated=json.loads(json.dumps(population));fabricated['geometric_supports']={'populated':True,'evidence':'arbitrary label'};assert not admissible(fabricated)
 out={'schema':'marici.voevodsky.cosmology-source-geometrization-contract.v2','status':'four_algebraic_fields_populated_four_geometric_fields_missing','original_conjecture':'Parity, pole, level, exponent, and transport descriptors determine geometric rank26 source generators.','evidence_revision':'Exact certificates and repaired transport now populate canonical algebraic IDs, source words, coherence, and provenance. They do not create geometric realization.','population':population,'populated_count':sum(v['populated'] for v in population.values()),'missing_count':sum(not v['populated'] for v in population.values()),'strongest_falsification':'Assigning an arbitrary support label leaves source differential, DNC filtration, and exceptional specialization absent; the full contract remains inadmissible.','surviving_scope':'A coherent all-even algebraic source presentation with replayable exact words.','first_missing_typed_object':'A source-derived map from each labelled T/S_K/Q generator descriptor to a geometric support locus.','acceptance_test':'For every generator family, derive the support from the denominator/relation constructor, verify transport preserves it under squared-axis multiplication, and reject fabricated or descriptor-only supports.','disposition':'Retain four populated algebraic fields; withhold geometrization and supported comparison until the four geometric fields are constructed.','next_gate':'construct-generator-support-map-from-denominator-loci','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
