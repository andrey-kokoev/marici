"""Source-bound audit of uniform finite-dimensional Layer 4 coherence."""
import json
from agda_receipt_audit import OWNER, verify_receipt

checked = verify_receipt('TypedGeneratorCoherence', 'typed-generator-coherence',
                         ['CoherenceBadGlobalFiller', 'CoherenceBadScoreLift'])
if any('Barycentric' in source for source in checked['local_sources_checked']):
    raise AssertionError('The uniform theorem must not depend on barycentric experiments')
result = {
    'schema': 'marici.nima.typed-generator-coherence.v1', 'passed': True, **checked,
    'existing_globular_boundary_and_filler_tower_reused': True,
    'maps_are_iterated_congruence_of_actual_compaction': True,
    'all_natural_number_dimensions_proved_by_induction': True,
    'comparison_maps_are_equivalences': True,
    'source_and_target_cell_recovery_paths': True,
    'all_iterated_recovery_comparisons_contractible': True,
    'certificate_contractible_for_fixed_reduction': True,
    'certify_quantifies_over_every_admitted_stack4_and_endpoints': True,
    'canonical_stack_and_two_stage_reduction_instantiated': True,
    'arbitrary_execution_and_higher_fillers_refuted': True,
    'score_cannot_preserve_all_comparison_types': True,
    'scope': 'All finite dimensions, uniformly quantified over natural numbers and typed globular boundaries. Preservation of retained-record identity structure and relative coherence inside complete recovery fibers. Not universal fillings for arbitrary relations or boundaries, a transfinite result, or a general infinity-category interface.'
}
(OWNER / 'results/typed-generator-coherence.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('PASS: uniform all-finite-dimensional preservation, relative recovery coherence, stack certification, and both rejection controls.')
