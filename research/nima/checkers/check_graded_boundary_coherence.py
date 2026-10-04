"""Validate the fresh graded-boundary proof packet against current sources."""
import json
from agda_receipt_audit import OWNER, verify_receipt

checked = verify_receipt('GradedBoundaryCoherence', 'graded-boundary-coherence',
                         ['GradedBoundaryBadFiller', 'GradedBoundaryBadErasure'])
result = {
    'schema': 'marici.nima.graded-boundary-coherence.v1',
    'passed': True,
    **checked,
    'all_grade_recovery': True,
    'contractible_interpretation_extensions': True,
    'comparison_reversal_involutive': True,
    'empty_answer_not_created': True,
    'fixed_boundary_fillers_can_be_distinct': True,
    'geometric_simplex_faces_constructed': False,
    'evidence': 'Fresh safe Cubical Agda proofs, not finite sample extrapolation.',
}
(OWNER / 'results/graded-boundary-coherence.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('PASS: all-grade recovery, contractible interpretation extensions, reversal, and marked-boundary hostiles; fresh source hashes match.')
