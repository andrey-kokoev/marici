import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# An integral lattice constrains values to integers but does not choose one.
lattice_witness = [-1, 0, 1, 2]
assert all(isinstance(n, int) for n in lattice_witness)
assert len(set(lattice_witness)) == 4

def clock(n):
    return 6 * n * n
clock_values = [clock(n) for n in lattice_witness]
assert clock_values == [6, 0, 6, 24]
assert clock(-1) == clock(1)

# Sign reversal is an automorphism of Z, so lattice integrality alone cannot
# select sigma.  A rank-one lattice also has two generators, +/-g.
assert set(-n for n in lattice_witness) != set(lattice_witness)
assert all(isinstance(-n, int) for n in lattice_witness)  # Z is closed under negation
rank_one_generators = [Fraction(1), Fraction(-1)]
assert rank_one_generators[0] == -rank_one_generators[1]

supply = {
    "integral_lattice_available_conditionally": True,
    "integer_values_constrained": True,
    "preferred_integer_lift": False,
    "clock_orbit_selected": False,
    "sigma_selected": False,
    "normalized_dual_cycle_present": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1099.v1",
    "status": "PASS",
    "question": "Does an integral-polarized lattice alone select n or sigma?",
    "lattice_witness": lattice_witness,
    "clock_values": [str(v) for v in clock_values],
    "rank_one_generator_pair": [str(v) for v in rank_one_generators],
    "sign_degeneracy": {"clock_minus_one": str(clock(-1)), "clock_one": str(clock(1))},
    "current_source_supply": supply,
    "classification": "negative gate: lattice integrality is not a chosen lift or orientation",
    "remaining_gate": "source-authorized normalized dual cycle or oriented generator selecting n and sigma",
    "hostile_gate": "do not promote membership in Z, a rank-one lattice, or an unoriented generator pair into n, sigma, or 6n^2",
    "claim_boundary": "an integral lattice may be necessary for a dual-cycle repair, but lattice membership and sign reversal leave the lift unresolved",
    "disposition": "bare integral-lattice clock loophole closed",
}

(ROOT / "results" / "wp1099_integral_lattice_clock_orientation_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1099 PASS:", len(lattice_witness), clock_values, rank_one_generators)
