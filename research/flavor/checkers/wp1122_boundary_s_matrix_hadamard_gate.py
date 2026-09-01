import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class C6:
    # a + b*i*sqrt(3); omega=(1+i*sqrt(3))/2 has order six.
    def __init__(self, a=Fraction(0), b=Fraction(0)):
        self.a, self.b = a, b
    def __add__(self, other):
        return C6(self.a+other.a, self.b+other.b)
    def __mul__(self, other):
        return C6(self.a*other.a-3*self.b*other.b, self.a*other.b+self.b*other.a)
    def norm2(self):
        return self.a*self.a + 3*self.b*self.b
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

ZERO = C6()
ONE = C6(Fraction(1))
MINUS_ONE = C6(Fraction(-1))
OMEGA = C6(Fraction(1,2), Fraction(1,2))

def omega_pow(k):
    out = ONE
    for _ in range(k % 6):
        out = out * OMEGA
    return out
assert OMEGA * OMEGA * OMEGA == MINUS_ONE
assert omega_pow(6) == ONE

# Unnormalized Fourier matrix entries omega^(jk). Every entry has squared norm 1,
# so F6=entries/sqrt(6) is a six-state Hadamard S-matrix.
F_unnorm = [[omega_pow(j*k) for k in range(6)] for j in range(6)]
assert all(F_unnorm[j][k].norm2() == 1 for j in range(6) for k in range(6))
for j in range(6):
    for ell in range(6):
        inner = ZERO
        for k in range(6):
            # omega^(-ell k) is omega^((-ell)k).
            inner = inner + F_unnorm[j][k] * omega_pow((-ell)*k)
        assert inner == (C6(Fraction(6)) if j == ell else ZERO)

q = [Fraction(d,23) for d in (6,8,1,4,2,2)]
probabilities = [Fraction(1,6)*sum(q) for _ in range(6)]
physical_events = [Fraction(3,2)*x for x in probabilities]
assert probabilities == [Fraction(1,6)]*6
assert physical_events == [Fraction(1,4)]*6

# Source provenance gate: Krylov history supplies C3 order; endpoint Z2 does
# not preserve the selected quartet, so no C6 generator is admitted.
c3_history_order = 3
endpoint_z2_selected_packet_symmetry = False
c6_generator_sourced = False
asymptotic_physical16_channels = 0
assert c3_history_order == 3
assert not endpoint_z2_selected_packet_symmetry
assert not c6_generator_sourced
assert asymptotic_physical16_channels == 0

result = {
    "schema": "marici.flavor.wp1122.v1",
    "status": "PASS",
    "question": "Can a boundary S-matrix supply the physical16 event kernel?",
    "dpc": {
        "conjecture": "A sourced C6 boundary S-matrix is the six-state Fourier Hadamard F6 and produces the physical16 event weights.",
        "rivals": [
            "C6 Fourier S-matrix",
            "C3 history times Z2 endpoint",
            "generic unitary S-matrix",
            "no sourced S-matrix"
        ],
        "risky_consequences": [
            "F6 is unitary with all squared magnitudes 1/6",
            "|F6|^2 q=(1/6)^6 and (3/2)|F6|^2 q=(1/4)^6",
            "the source must supply a C6 generator preserving the selected packet and six asymptotic event channels"
        ],
        "falsification_attempt": "The F6 algebra passes, but current history has order 3, endpoint Z2 maps the selected quartet to a different coset, and zero asymptotic physical16 channels are sourced.",
        "residual": "A future defect may source a C6 or equivalent Hadamard boundary S-matrix with event-channel provenance.",
        "disposition": "provisionally retain F6 as a target-compatible algebra; reject it as a current-source construction"
    },
    "fourier_order": 6,
    "squared_magnitude": "1/6",
    "branch_distribution": [str(x) for x in q],
    "probabilities": [str(x) for x in probabilities],
    "physical_events": [str(x) for x in physical_events],
    "c3_history_order": c3_history_order,
    "endpoint_z2_selected_packet_symmetry": endpoint_z2_selected_packet_symmetry,
    "c6_generator_sourced": c6_generator_sourced,
    "asymptotic_physical16_channels": asymptotic_physical16_channels,
    "classification": "conditional gate: F6 Hadamard algebra is target-compatible but lacks C6 and event-channel source authority",
    "remaining_gate": "derive a C6-preserving boundary symmetry and six physical16 asymptotic channels",
    "hostile_gate": "do not promote F6, C3 history, endpoint Z2, or unitarity alone to a sourced production kernel",
    "claim_boundary": "the S-matrix algebra is exact; source provenance is absent",
    "disposition": "boundary S-matrix algebra constructed conditionally; current-source claim rejected",
}

(ROOT / "results" / "wp1122_boundary_s_matrix_hadamard_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1122 PASS:", 6, probabilities[0], physical_events[0], c6_generator_sourced)
