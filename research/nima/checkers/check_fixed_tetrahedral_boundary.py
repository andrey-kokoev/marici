"""Source-bound audit of fixed-boundary comparison and path-indexed extension."""
import json
from agda_receipt_audit import OWNER, verify_receipt

checked = verify_receipt('FixedTetrahedralBoundary', 'fixed-tetrahedral-boundary',
                         ['FixedBoundaryBadErasure'])
result = {
    'schema': 'marici.nima.fixed-tetrahedral-boundary.v1',
    'passed': True,
    **checked,
    'all_four_faces_fixed_in_comparison': True,
    'inhabited_filler_space_equivalent_to_route_loop_space': True,
    'comparison_equivalent_to_residual_nullhomotopy': True,
    'grade_four_globular_comparison': True,
    'four_face_charts_lift_to_comparison_equivalences': True,
    'dependent_path_yoneda_and_unique_extension': True,
    'equivalence_fiber_yoneda_instantiated_at_tetrahedral_horn': True,
    'endpoint_only_extension_refuted_by_boolean_loop': True,
    'based_package_contractibility_does_not_imply_ambient_contractibility': True,
    'naive_transfer_to_original_retained_arrows_refuted': True,
    'native_object_paths_cannot_realize_all_retained_arrows': True,
    'concrete_distinct_fixed_boundary_tetrahedral_fillers_constructed': False,
    'equivariant_extension_for_original_E_constructed': False,
    'four_simplex_boundary_constructed': False,
}
(OWNER / 'results/fixed-tetrahedral-boundary.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('PASS: fixed-face loop classification, grade-four comparison, path/fiber Yoneda, retained-loop control, and original-E interface obstruction.')
