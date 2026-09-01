import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

dims = [6,8,1,4,2,2]
C = sum(dims)
eigenvalue = Fraction(1,C)
sector_probabilities = [Fraction(d,C) for d in dims]
trace = sum(d*eigenvalue for d in dims)
assert C == 23
assert trace == 1
assert sector_probabilities == [Fraction(6,23),Fraction(8,23),Fraction(1,23),Fraction(4,23),Fraction(2,23),Fraction(2,23)]
assert all(p > 0 for p in sector_probabilities)

# Conditional density operator: rho = direct_sum_b I_{d_b}/23. Every sector is
# maximally mixed over its d_b microstates. This assumes a dimension-trace
# measure that the current UV source has not derived.
microstates = C
positive_eigenvalues = C
uniform_microstate_measure_sourced = False
boundary_state_matching_maps = 0
assert microstates == 23
assert positive_eigenvalues == 23
assert not uniform_microstate_measure_sourced
assert boundary_state_matching_maps == 0

# If admitted, rho yields exactly the preparation distribution q.
q = sector_probabilities
assert q == [Fraction(d,C) for d in dims]

result = {
    "schema": "marici.flavor.wp1132.v1",
    "status": "PASS",
    "question": "Can a dimension-trace ensemble explicitly prepare the six-sector distribution?",
    "dpc": {
        "conjecture": "The normalized dimension-trace ensemble rho=direct_sum_b I_{d_b}/23 explicitly prepares q=(6,8,1,4,2,2)/23.",
        "rivals": [
            "dimension-trace density operator",
            "sourced UV boundary ensemble",
            "microstate-uniform measure",
            "no sourced ensemble"
        ],
        "risky_consequences": [
            "rho is positive with trace one",
            "sector probabilities equal d_b/23",
            "the UV boundary state must be matched to rho",
            "microstate uniformity must be source-derived"
        ],
        "falsification_attempt": "The exact density algebra passes, but no boundary-state matching map or microstate-uniform measure is sourced.",
        "residual": "A future UV ensemble may derive the dimension-trace state.",
        "disposition": "construct the conditional dimension-trace preparation state; reject current-source authority"
    },
    "sector_dimensions": dims,
    "microstate_eigenvalue": str(eigenvalue),
    "microstates": microstates,
    "positive_eigenvalues": positive_eigenvalues,
    "trace": str(trace),
    "sector_probabilities": [str(x) for x in sector_probabilities],
    "uniform_microstate_measure_sourced": uniform_microstate_measure_sourced,
    "boundary_state_matching_maps": boundary_state_matching_maps,
    "classification": "conditional gate: dimension-trace density operator prepares q algebraically but lacks source authority",
    "remaining_gate": "derive UV boundary-state matching and microstate uniformity",
    "hostile_gate": "do not treat rho, trace one, positivity, or sector weights as a sourced boundary ensemble",
    "claim_boundary": "the preparation state is a conditional mathematical construction",
    "disposition": "dimension-trace preparation retained conditionally",
}

(ROOT / "results" / "wp1132_dimension_trace_preparation_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1132 PASS:", microstates, trace, sector_probabilities, uniform_microstate_measure_sourced)
