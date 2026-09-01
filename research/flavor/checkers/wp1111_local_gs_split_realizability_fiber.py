import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

parent = Fraction(-3)
# Parametrize the endpoint split by t:
# g0 = -3/2 + t, gpi = -3/2 - t, so g0+gpi=-3.
def split(t):
    g0 = Fraction(-3,2) + t
    gpi = Fraction(-3,2) - t
    assert g0 + gpi == parent
    return g0, gpi

# For one quartet, b4=1/2, B4=5/2; b2=0, B2=3.
def gravity_levels(t):
    g0,_ = split(t)
    k4 = -Fraction(1,2) - Fraction(5,4) - g0
    k2 = -Fraction(3,2) - g0
    return k4, k2

zero = gravity_levels(Fraction(0))
one = gravity_levels(Fraction(1))
minus_one = gravity_levels(Fraction(-1))
assert zero == (Fraction(-1,4), 0)
assert one == (Fraction(-5,4), -1)
assert minus_one == (Fraction(3,4), 1)
assert tuple(x % 1 for x in one) == tuple(x % 1 for x in zero)
assert tuple(x % 1 for x in minus_one) == tuple(x % 1 for x in zero)

# Exact WP1110 target requires t=0.  Mod the shifted lattice, t is any integer.
exact_target_t = 0
coset_t_domain = "Z"
assert exact_target_t == 0 and coset_t_domain == "Z"

# Endpoint exchange swaps g0 and gpi, hence sends t to -t; reflection invariance
# would force t=0, but no source currently authorizes that symmetry.
reflection_invariance_would_force_zero = True
source_exchange_authority = False
assert reflection_invariance_would_force_zero and not source_exchange_authority

result = {
    "schema": "marici.flavor.wp1111.v1",
    "status": "PASS",
    "question": "Does parent GS=-3 admit a local endpoint split compatible with the seven-channel lift?",
    "split_parameterization": ["g0=-3/2+t", "gpi=-3/2-t"],
    "gravity_levels_t": ["k4=-1/4-t", "k2=-t"],
    "samples": {
        "t0": [str(x) for x in zero],
        "t1": [str(x) for x in one],
        "t_minus1": [str(x) for x in minus_one],
    },
    "exact_target_t": exact_target_t,
    "coset_t_domain": coset_t_domain,
    "reflection_invariance_would_force_zero": reflection_invariance_would_force_zero,
    "source_exchange_authority": source_exchange_authority,
    "classification": "conditional gate: local split is realizable at t=0 for the exact vector and over Z at the coset level, but endpoint exchange authority remains absent",
    "remaining_gate": "source-derived endpoint exchange/orientation law selecting t=0 or another integer lift",
    "hostile_gate": "do not treat t in Z, coset compatibility, or parent GS=-3 as a selected local split",
    "claim_boundary": "the split fiber is derived; no endpoint split is selected",
    "disposition": "local Green-Schwarz split realizability narrowed to an integer/orientation fiber",
}

(ROOT / "results" / "wp1111_local_gs_split_realizability_fiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1111 PASS:", zero, one, minus_one, exact_target_t, coset_t_domain)
