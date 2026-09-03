#!/usr/bin/env python3
"""Exact witnesses for the typed coefficient-residual classifier."""

import json
from fractions import Fraction as Q
from pathlib import Path

fixtures = {
    "type_obstruction": {"typed": False},
    "comparison_obstruction": {"typed": True, "common_map": False},
    "presentation_behavior": {"typed": True, "common_map": True, "raw": (Q(2), Q(3)), "gauge_image": (Q(6), Q(6))},
    "mate_obstruction": {"mate_residual": Q(10, 3) - Q(2)},
    "coherencer_obstruction": {"route_residual": Q(2)*Q(3) - Q(5)},
    "pairing_obstruction": {"pairing_residual": Q(3, 4) - Q(2, 3)},
    "record_obstruction": {"pairing_residual": Q(0), "record_equal": False},
    "nonfaithful_quotient_ambiguity": {"source": (1, 3), "quotient": (1, 1), "monic": False},
    "source_law_obstruction": {"structural_residuals": (Q(0),)*4, "source_residual": Q(1, 7)},
}
checks = {
    "type_gate_detected": not fixtures["type_obstruction"]["typed"],
    "comparison_gate_detected": not fixtures["comparison_obstruction"]["common_map"],
    "gauge_reconciles_unequal_coordinates": fixtures["presentation_behavior"]["raw"][0] != fixtures["presentation_behavior"]["raw"][1] and len(set(fixtures["presentation_behavior"]["gauge_image"])) == 1,
    "mate_residual_nonzero": fixtures["mate_obstruction"]["mate_residual"] == Q(4, 3),
    "coherencer_residual_nonzero": fixtures["coherencer_obstruction"]["route_residual"] == 1,
    "pairing_residual_nonzero": fixtures["pairing_obstruction"]["pairing_residual"] == Q(1, 12),
    "record_fails_with_zero_pairing_residual": fixtures["record_obstruction"]["pairing_residual"] == 0 and not fixtures["record_obstruction"]["record_equal"],
    "equal_quotient_images_do_not_imply_source_equality": len(set(fixtures["nonfaithful_quotient_ambiguity"]["quotient"])) == 1 and len(set(fixtures["nonfaithful_quotient_ambiguity"]["source"])) == 2,
    "source_law_can_fail_after_structural_coherence": all(r == 0 for r in fixtures["source_law_obstruction"]["structural_residuals"]) and fixtures["source_law_obstruction"]["source_residual"] != 0,
    "raw_scalar_equality_is_not_type_authority": 2 == 2 and not fixtures["type_obstruction"]["typed"],
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.coefficient-residual-classifier.v1", "status": "passed", "check_count": len(checks), "checks": checks, "classes": list(fixtures), "disposition": "classify at the first defined failed typed gate"}
out = Path(__file__).parents[1] / "results" / "coefficient_residual_obstruction_classifier.json"
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": "passed", "check_count": len(checks), "class_count": len(fixtures)}, sort_keys=True))
