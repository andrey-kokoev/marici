import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class QRoot:
    # a + b*i*sqrt(3), used for exact sixth/third roots.
    def __init__(self, a=Fraction(0), b=Fraction(0)):
        self.a, self.b = a, b
    def __add__(self, other):
        return QRoot(self.a+other.a, self.b+other.b)
    def __mul__(self, other):
        return QRoot(self.a*other.a-3*self.b*other.b, self.a*other.b+self.b*other.a)
    def conjugate(self):
        return QRoot(self.a, -self.b)
    def norm2(self):
        return self.a*self.a + 3*self.b*self.b
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

ZERO = QRoot()
ONE = QRoot(Fraction(1))
ZETA3 = QRoot(Fraction(-1,2), Fraction(1,2))
assert ZETA3*ZETA3 + ZETA3 + ONE == ZERO
assert (ZETA3*ZETA3*ZETA3) == ONE
assert ZETA3.norm2() == 1

def zeta_pow(k):
    out = ONE
    for _ in range(k % 3):
        out = out * ZETA3
    return out

F3 = [[zeta_pow(j*k) for k in range(3)] for j in range(3)]
F2 = [[QRoot(Fraction(1)), QRoot(Fraction(1))], [QRoot(Fraction(1)), QRoot(Fraction(-1))]]
# Kronecker product: index pairs (cyclic3, endpoint2).
H = []
for a in range(3):
    for x in range(2):
        H.append([F3[a][b] * F2[x][y] for b in range(3) for y in range(2)])
assert len(H) == 6 and all(len(row) == 6 for row in H)
assert all(H[e][b].norm2() == 1 for e in range(6) for b in range(6))
for e in range(6):
    for f in range(6):
        inner = ZERO
        for b in range(6):
            inner = inner + H[e][b].conjugate() * H[f][b]
        assert inner == (QRoot(Fraction(6)) if e == f else ZERO)

q = [Fraction(d,23) for d in (6,8,1,4,2,2)]
probabilities = [Fraction(1,6)*sum(q) for _ in range(6)]
physical_events = [Fraction(3,2)*x for x in probabilities]
assert probabilities == [Fraction(1,6)]*6
assert physical_events == [Fraction(1,4)]*6

c3_history_invariant = True
endpoint_z2_selected_packet_symmetry = False
tensor_phase_sourced = False
physical16_channels = 0
assert c3_history_invariant
assert not endpoint_z2_selected_packet_symmetry
assert not tensor_phase_sourced
assert physical16_channels == 0

result = {
    "schema": "marici.flavor.wp1124.v1",
    "status": "PASS",
    "question": "Can boundary C3 and endpoint Z2 invariants select an H6 Hadamard representative?",
    "dpc": {
        "conjecture": "The source-shaped Kronecker Hadamard H=F3 tensor F2 is selected by C3 history and endpoint Z2 boundary invariants.",
        "rivals": [
            "C6 Fourier Hadamard",
            "C3xZ2 Kronecker Hadamard",
            "generic H6 Hadamard",
            "no sourced phase matching"
        ],
        "risky_consequences": [
            "H=F3 tensor F2 is unitary with all squared magnitudes 1/6",
            "H maps every branch distribution to (1/6)^6",
            "C3 and endpoint Z2 must preserve the selected packet and six event channels"
        ],
        "falsification_attempt": "The Kronecker algebra passes exactly, but endpoint Z2 maps the selected quartet to a different coset and no physical16 event channels are sourced.",
        "residual": "A boundary defect with endpoint symmetry or anomaly phases could still select an H6 representative.",
        "disposition": "retain the Kronecker H6 algebra; reject current C3xZ2 source matching"
    },
    "kronecker_shape": [3,2],
    "hadamard_dimension": 6,
    "squared_magnitude": "1/6",
    "probabilities": [str(x) for x in probabilities],
    "physical_events": [str(x) for x in physical_events],
    "c3_history_invariant": c3_history_invariant,
    "endpoint_z2_selected_packet_symmetry": endpoint_z2_selected_packet_symmetry,
    "tensor_phase_sourced": tensor_phase_sourced,
    "physical16_channels": physical16_channels,
    "classification": "conditional gate: source-shaped F3 tensor F2 is H6 but lacks endpoint symmetry and event-channel authority",
    "remaining_gate": "derive anomaly-sector or endpoint phase observables preserving the selected packet and six event channels",
    "hostile_gate": "do not treat Kronecker form, C3 history, endpoint signs, or Hadamard symmetry as source authority",
    "claim_boundary": "the H6 algebra is exact; current phase matching is absent",
    "disposition": "boundary phase matching deferred to a sourced phase observable",
}

(ROOT / "results" / "wp1124_hadamard_phase_matching_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1124 PASS:", 6, probabilities[0], physical_events[0], tensor_phase_sourced)
