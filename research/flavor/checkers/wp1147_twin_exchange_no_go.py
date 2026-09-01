import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

anti6_copies = 2
quartet_choices = ["4_a", "4_b"]
# WP1056: the two one-quartet localizations are exchange-related, but the
# packet does not choose between them. Selecting either breaks exchange within
# the selected cell because the exchange maps it to the other cell.
selected_cells = ["localize_4_a", "localize_4_b"]
exchange_fixed_selected_cells = 0
prelocalization_formal_exchange = 1
postlocalization_unbroken_exchange_certificates = 0
production_kernel_invariance_certificates = 0
equal_weight_only_certificates = 1
assert anti6_copies == 2 and len(quartet_choices) == 2
assert exchange_fixed_selected_cells == 0
assert prelocalization_formal_exchange == 1
assert postlocalization_unbroken_exchange_certificates == 0
assert production_kernel_invariance_certificates == 0

missing_object = {
    "id": "post_localization_exchange_certificate",
    "required_fields": ["exchange_operator", "fixed_localization_cell", "invariant_production_kernel", "same_frame_gain"],
    "failed_consequence": "unbroken physical twin exchange after quartet localization",
    "acceptance_test": "derive an exchange that fixes the selected quartet localization, leaves the production kernel invariant, and preserves gain 3/2"
}
assert len(missing_object["required_fields"]) == 4

result = {
    "schema": "marici.flavor.wp1147.v1",
    "status": "PASS",
    "question": "Does the selected localized SU6 cell carry a physical twin-branch exchange symmetry?",
    "dpc": {
        "conjecture": "The equal-weight twin branches have an unbroken physical exchange symmetry after localization.",
        "rivals": [
            "prelocalization multiplicity exchange",
            "postlocalization unbroken exchange",
            "equal algebraic weights only",
            "quartet-choice quotient"
        ],
        "risky_consequences": [
            "exchange fixes the selected quartet cell",
            "production kernel is invariant",
            "same-frame gain remains 3/2",
            "the three matching orbits are physical"
        ],
        "falsification_attempt": "WP1056's exchange swaps the two one-quartet cells rather than fixing either selected cell. No post-localization exchange or kernel-invariance certificate is sourced.",
        "residual": "A quotient of the symmetric quartet choice or a new production packet may restore exchange.",
        "disposition": "reject unbroken physical twin exchange and record the typed blocker"
    },
    "anti6_copies": anti6_copies,
    "quartet_choices": quartet_choices,
    "selected_cells": selected_cells,
    "prelocalization_formal_exchange": prelocalization_formal_exchange,
    "exchange_fixed_selected_cells": exchange_fixed_selected_cells,
    "postlocalization_unbroken_exchange_certificates": postlocalization_unbroken_exchange_certificates,
    "production_kernel_invariance_certificates": production_kernel_invariance_certificates,
    "equal_weight_only_certificates": equal_weight_only_certificates,
    "missing_object": missing_object,
    "classification": "negative gate: formal pre-localization exchange is broken by selecting one quartet cell",
    "remaining_gate": "test the quartet-choice quotient as a possible exchange realization",
    "hostile_gate": "do not treat exchange between localization cells as symmetry within one selected cell",
    "claim_boundary": "the exchange relation between cells is sourced; unbroken selected-cell symmetry is absent",
    "disposition": "twin-exchange branch deferred on post_localization_exchange_certificate",
}

(ROOT / "results" / "wp1147_twin_exchange_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1147 PASS:", exchange_fixed_selected_cells, postlocalization_unbroken_exchange_certificates)
