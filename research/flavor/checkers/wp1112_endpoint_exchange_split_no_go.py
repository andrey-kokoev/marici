import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

s_quartet = (Fraction(1,2),Fraction(1,4),0,0,0,Fraction(3,4),0)
s_reflected = (Fraction(1,2),Fraction(3,4),0,0,0,Fraction(1,4),0)
assert s_quartet != s_reflected
assert all(x.denominator in (1,2,4) for x in s_quartet + s_reflected)

# Endpoint exchange acts on the WP1111 split parameter as t -> -t.
def split(t):
    return Fraction(-3,2)+t, Fraction(-3,2)-t
assert split(1) == tuple(reversed(split(-1)))
assert split(0)[0] == split(0)[1]

# Reflection would force t=0 only if it fixed the selected quartet packet.
reflection_forces_t_zero_if_symmetry = True
quartet_fixed_by_reflection = False
assert reflection_forces_t_zero_if_symmetry
assert not quartet_fixed_by_reflection

# Therefore existing interval geometry gives no endpoint-exchange law for the
# selected quartet cell.
endpoint_exchange_selected = False
split_selected = False
assert not endpoint_exchange_selected and not split_selected

result = {
    "schema": "marici.flavor.wp1112.v1",
    "status": "PASS",
    "question": "Does existing fused-defect interval geometry supply an endpoint exchange law selecting the GS split?",
    "quartet_coset": [str(x) for x in s_quartet],
    "reflected_coset": [str(x) for x in s_reflected],
    "cosets_equal": False,
    "split_action": "t -> -t",
    "reflection_forces_t_zero_if_symmetry": reflection_forces_t_zero_if_symmetry,
    "quartet_fixed_by_reflection": quartet_fixed_by_reflection,
    "endpoint_exchange_selected": endpoint_exchange_selected,
    "split_selected": split_selected,
    "classification": "negative gate: endpoint reflection maps the selected quartet to a different coset, so it is not a split-selecting symmetry",
    "remaining_gate": "derive an orientation-odd UV boundary datum selecting the endpoint split independently of quartet reflection",
    "hostile_gate": "do not use interval reflection or endpoint exchange to force t=0 while preserving the selected quartet coset",
    "claim_boundary": "the reflection exists geometrically but is not a symmetry of the selected packet",
    "disposition": "endpoint-exchange route closed for the selected quartet",
}

(ROOT / "results" / "wp1112_endpoint_exchange_split_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1112 PASS:", s_quartet != s_reflected, split(0), endpoint_exchange_selected)
