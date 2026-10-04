"""Source-bound audit for tetrahedral horns and the common completion criterion."""
import json
from agda_receipt_audit import OWNER, verify_receipt

checked = verify_receipt('MarkedTetrahedronCoherence', 'marked-tetrahedron-coherence',
                         ['MarkedTetrahedronBadErasure'])
result = {
    'schema': 'marici.nima.marked-tetrahedron-coherence.v1',
    'passed': True,
    **checked,
    'all_four_missing_face_completions_contractible': True,
    'six_edges_and_three_supplied_faces_fixed': True,
    'four_face_readings_are_witness_space_equivalences': True,
    'relative_dependent_interpretation_extensions_contractible': True,
    'coherent_completion_iff_forgetful_projection_equivalence': True,
    'triangle_operations_and_recovery_witness_preserved_definitionally': True,
    'tetrahedral_filler_matches_globular_grade_three': True,
    'equal_diagonal_distinct_complete_tetrahedra': True,
    'incompatible_fixed_face_obstruction_is_conditional': True,
    'concrete_incompatible_four_face_boundary_constructed': False,
    'grade_four_fixed_boundary_comparison_constructed': False,
}
(OWNER / 'results/marked-tetrahedron-coherence.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('PASS: four relative tetrahedral completions, shared completion criterion, exact triangle recovery, and retained-tetrahedron hostile.')
