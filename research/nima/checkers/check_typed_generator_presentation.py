"""Source-bound audit of Layer 4 certified presentation reduction."""
import json
from agda_receipt_audit import OWNER, verify_receipt

checked = verify_receipt('TypedGeneratorPresentation', 'typed-generator-presentation',
                         ['PresentationBadCompletion', 'PresentationBadHistory'])
if any('Barycentric' in source for source in checked['local_sources_checked']):
    raise AssertionError('Layer 4 must not depend on the barycentric experiments')
result = {
    'schema': 'marici.nima.typed-generator-presentation.v1', 'passed': True, **checked,
    'layer4_over_fixed_layer3': True,
    'previous_three_layers_recovered': True,
    'declared_boundary_and_contractible_remainder_required': True,
    'source_and_boundary_recovery_paths': True,
    'equivalence_and_observation_preservation': True,
    'contractible_complete_recovery_packages_and_comparisons': True,
    'identity_and_composition_of_reductions': True,
    'successive_layer4_views_supported': True,
    'associative_compaction_and_recovery_package_agreement': True,
    'canonical_view_retains_history_and_input': True,
    'canonical_output_and_correctness_recomputed': True,
    'two_stage_circle_machine_example': True,
    'equal_scores_keep_distinct_histories_and_views': True,
    'score_based_reversible_reduction_refuted': True,
    'arbitrary_boolean_remainder_contraction_refuted': True,
    'no_barycentric_experiment_dependency': True,
    'scope': 'Declared, reversible presentation changes over Layer 3 retained execution records. Arbitrary higher payload types are allowed. No automatic certificate discovery, general rewrite strategy, cost bound, or permission to erase histories from equal scores.'
}
(OWNER / 'results/typed-generator-presentation.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('PASS: Layer 4 certified reduction, stack recovery, coherent composition, canonical execution view, and both erasure controls.')
