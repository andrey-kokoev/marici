"""Source-bound audit for marked triangle horns and witness-preserving rotation."""
import json
from agda_receipt_audit import OWNER, verify_receipt

checked = verify_receipt('MarkedTriangleCoherence', 'marked-triangle-coherence',
                         ['MarkedTriangleBadErasure'])
result = {
    'schema': 'marici.nima.marked-triangle-coherence.v1',
    'passed': True,
    **checked,
    'three_marked_horn_completion_spaces_contractible': True,
    'cyclic_rotation_is_filler_space_equivalence': True,
    'recovery_fixes_supplied_horn': True,
    'interpretation_extensions_contractible': True,
    'dependent_interpretations_preserve_marked_horn': True,
    'globular_comparison_preserves_filler_with_factorization_parameters': True,
    'equal_diagonals_can_have_distinct_factorizations': True,
    'full_marked_boundary_can_be_unfillable': True,
    'triple_forward_rotation_coherence_proved': False,
    'tetrahedron_faces_constructed': False,
}
(OWNER / 'results/marked-triangle-coherence.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('PASS: three horn completions, marked rotation equivalence, relative recovery, universal extension, and retained-factorization hostile.')
