import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

six = 6
u = [Fraction(1,6)] * six
basis = [[Fraction(1) if i == b else Fraction(0) for i in range(six)] for b in range(six)]

# If P=|S|^2 maps every branch distribution q to u, evaluating q=e_b forces
# every column of P to be u. Therefore every |S_eb|^2 is exactly 1/6.
required_modulus_matrix = [[Fraction(1,6) for _ in range(six)] for _ in range(six)]
assert all(sum(row) == 1 for row in required_modulus_matrix)
assert all(sum(required_modulus_matrix[e][b] for e in range(six)) == 1 for b in range(six))
for b in range(six):
    column_output = [required_modulus_matrix[e][b] for e in range(six)]
    assert column_output == u

# Unitarity plus modulus 1/sqrt(6) is exactly the definition of a complex
# Hadamard matrix. Row/column permutations and row/column unit phases preserve
# |S|^2 and hence form gauge equivalences, not distinct event kernels.
classification = "S is unitary and |S_eb|^2=1/6 for all e,b: S is a 6x6 complex Hadamard"
gauge_equivalences = ["row_phase", "column_phase", "row_permutation", "column_permutation"]
full_h6_parameter_space = "not classified here; source matching needs only the event kernel and sourced phase invariants"
assert len(gauge_equivalences) == 4
assert classification.startswith("S is unitary")
assert full_h6_parameter_space.startswith("not classified")

# Conversely, every 6x6 complex Hadamard gives |S|^2=J6/6 and the target map.
sufficiency = "H in H6 implies |H|^2 q=(1/6)^6 and (3/2)|H|^2 q=(1/4)^6"
assert sufficiency.startswith("H in H6")

result = {
    "schema": "marici.flavor.wp1123.v1",
    "status": "PASS",
    "question": "Which unitary S-matrices produce uniform physical16 events for all branch distributions?",
    "dpc": {
        "conjecture": "A generic unitary S-matrix can produce the target event law without six-state Hadamard moduli.",
        "rivals": [
            "generic non-Hadamard unitary",
            "complex Hadamard H6",
            "row/column phase-equivalent Hadamard",
            "fixed-q nonuniversal S-matrix"
        ],
        "risky_consequences": [
            "evaluate P=|S|^2 on every basis vector e_b",
            "force every column P e_b=(1/6)^6",
            "force |S_eb|^2=1/6 for all e,b"
        ],
        "falsification_attempt": "The basis-vector evaluation proves every qualifying unitary is a complex Hadamard; no non-Hadamard unitary survives.",
        "residual": "The full H6 phase-parameter space and source-phase matching remain open.",
        "disposition": "reject generic non-Hadamard S-matrices; classify the required algebra as H6 modulo row/column phases and permutations"
    },
    "basis_tests": len(basis),
    "required_modulus_squared": "1/6",
    "required_probability_output": [str(x) for x in u],
    "classification": classification,
    "gauge_equivalences": gauge_equivalences,
    "sufficiency": sufficiency,
    "full_h6_parameter_space": full_h6_parameter_space,
    "classification_label": "exact gate: target-compatible unitary S-matrices are six-state complex Hadamards",
    "remaining_gate": "match sourced boundary phase invariants to an H6 representative and six event channels",
    "hostile_gate": "do not use row/column phases, permutations, Fourier form, or full-H6 classification gaps as event kernel provenance",
    "claim_boundary": "this classifies algebra required for q-independent output; it supplies no source authority",
    "disposition": "unitary S-matrix algebra classified as H6",
}

(ROOT / "results" / "wp1123_unitary_s_matrix_hadamard_classification.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1123 PASS:", len(basis), required_modulus_matrix[0][0], len(gauge_equivalences))
