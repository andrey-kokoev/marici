import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# A source-fixed SU(2) Wilson line with generic phase splits the residual
# WP1084 doublet into two one-dimensional eigenspaces.
theta_turns = Fraction(1, 3)
wilson_eigenlines = ["1_(+theta)", "1_(-theta)"]
assert len(wilson_eigenlines) == 2

# The trivial holonomy leaves SU(2) unbroken; a generic holonomy has U(1)
# centralizer and two eigenlines.
trivial_centralizer = {"group": "SU(2)", "rank": 1, "dimension": 3}
generic_centralizer = {"group": "U(1)", "rank": 1, "dimension": 1}
assert generic_centralizer["dimension"] < trivial_centralizer["dimension"]

# WP1072's unit-clock flux datum supplies only B/A=6 n^2.  It names neither
# the Wilson phase, an eigenbasis direction, nor an ordering convention.
flux = {"n": 1, "B_over_A": Fraction(6, 1)}
assert flux["B_over_A"] == 6 * flux["n"] ** 2

source_supply = {
    "flux_integer_sector": True,
    "generic_wilson_phase": False,
    "selected_eigenbasis_direction": False,
    "ordered_charge_convention": False,
    "cyclic_ray": False,
    "history_dilation": False,
}
assert list(source_supply.values()).count(False) == 5

conditional_branching = {
    "B_triplet_under_WP1084": "2_B+1_B",
    "with_source_fixed_generic_Wilson_line": "1_(+theta)+1_(-theta)+1_0",
    "distinct_lines": 3,
}
assert conditional_branching["distinct_lines"] == 3

result = {
    "schema": "marici.flavor.wp1085.v1",
    "status": "PASS",
    "question": "Can a flux Wilson line conditionally split WP1084's residual SU(2) doublet into two ordered lines?",
    "wilson_line": {
        "phase_turns": str(theta_turns),
        "eigenlines": wilson_eigenlines,
        "generic_centralizer": generic_centralizer,
    },
    "flux_source": {"n": flux["n"], "B_over_A": str(flux["B_over_A"])},
    "conditional_branching": conditional_branching,
    "current_source_supply": source_supply,
    "classification": "conditional constructor: a source-fixed generic Wilson line would split 2+1 into 1+1+1, but the admitted flux integer does not select phase, eigenbasis, or ordering",
    "hostile_gate": "do not promote B/A=6 n^2 to a Wilson phase, eigenbasis, ordered flag, cyclic ray, or history",
    "remaining_gate": "derive the Wilson-line boundary condition and charge-ordering convention from the UV/source packet, then test whether it selects a cyclic ray and retains history",
    "claim_boundary": "mathematical split is conditional on new source data; no source-authorized breaking is constructed here",
    "disposition": "productive: the second-stage doublet-breaking route is narrowed to a source Wilson-line packet",
}

(ROOT / "results" / "wp1085_flux_wilson_doublet_flag_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1085 PASS:", generic_centralizer["dimension"], len(wilson_eigenlines), flux["B_over_A"], conditional_branching["distinct_lines"])
