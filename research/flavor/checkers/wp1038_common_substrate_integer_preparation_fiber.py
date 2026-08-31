import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Minimal common finite substrate around the WP1036 capacity packet.
D = [(2, 22), (2, 23), (2, 24)]

# h(k,C)=12*C*pi^2/(1367*k), represented as a rational coefficient of pi^2.
def h_coeff(k, C):
    return Fraction(12 * C, 1367 * k)

# Two admissible integer-polynomial preparations on the same substrate.
E23 = {(k, C): (C - 23) ** 2 for k, C in D}
E22 = {(k, C): (C - 22) ** 2 for k, C in D}
sel23 = [p for p in D if E23[p] == min(E23.values())]
sel22 = [p for p in D if E22[p] == min(E22.values())]
assert sel23 == [(2, 23)]
assert sel22 == [(2, 22)]

# Same domain, same polynomial degree, same positive gap type, distinct selected label.
gap23 = sorted(set(E23.values()))[1] - sorted(set(E23.values()))[0]
gap22 = sorted(set(E22.values()))[1] - sorted(set(E22.values()))[0]
assert gap23 == gap22 == 1
delta = h_coeff(2, 23) - h_coeff(2, 22)
assert delta == Fraction(6, 1367)

# A symmetric middle-of-three law selects a relative slot only. Translating the
# three-point substrate changes the absolute selected coefficient.
translated_middle = Fraction(D[0][1] + D[-1][1], 2)
assert translated_middle == 23
hostile_shifted_domain = [(2, 21), (2, 22), (2, 23)]
shifted_middle = Fraction(hostile_shifted_domain[0][1] + hostile_shifted_domain[-1][1], 2)
assert shifted_middle == 22

result = {
    "schema": "marici.flavor.wp1038.v1",
    "status": "PASS",
    "question": "Does placing the WP1036 integer labels in one finite common substrate select (k,C)=(2,23)?",
    "common_substrate": {
        "domain": D,
        "selected_capacity_packet": [2, 23],
        "neighbor_falsifier": [2, 22]
    },
    "same_grammar_preparations": {
        "E23=(C-23)^2": {"selector": sel23, "gap": gap23},
        "E22=(C-22)^2": {"selector": sel22, "gap": gap22}
    },
    "exact_physical_difference": "h(2,23)-h(2,22)=6*pi^2/1367",
    "translation_fiber": {
        "domain_22_23_24_middle": str(translated_middle),
        "domain_21_22_23_middle": str(shifted_middle),
        "classification": "middle-of-three selection fixes a relative slot, not the absolute coefficient C=23"
    },
    "first_nonfaithful_arrow": "common finite source support plus positive-gapped preparation grammar to a source-derived absolute label order",
    "classification": "common-substrate preparation rigidifier only; the selecting energy/order is additional source data",
    "remaining_gate": "derive the integer domain, its absolute origin, and a unique source energy/order selecting C=23 before invoking the fitted h interval, threshold transport, or physical16 instrumentation",
    "claim_boundary": "finite three-point k=2 neighborhood and same-degree integer-polynomial preparations; does not exclude a representation theorem that uniquely fixes C=23",
    "disposition": "negative for bare common-substrate repair; source authority must act on the preparation law, not merely on the state space"
}

(ROOT / "results" / "wp1038_common_substrate_integer_preparation_fiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1038 PASS:", sel23, sel22, f"{delta}*pi^2")
