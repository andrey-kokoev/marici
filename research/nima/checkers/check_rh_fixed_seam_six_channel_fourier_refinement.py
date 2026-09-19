#!/usr/bin/env python3
"""Exact Fourier action on the common six-channel moment/history refinement."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))
import sympy as s

pi = s.pi
I = s.I
# Ordered channels: B0,Q0,M,J,A0,C0.
T6 = s.Matrix([
    [0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, -2*pi*I, 0, 0],
    [0, 0, 1/(2*pi*I), 0, 0, 0],
    [s.Rational(1, 2), 0, 0, 0, 0, -1/(2*pi*I)],
    [0, -pi*I, 0, 0, 2*pi*I, 0],
])

# Coordinate projections from six channels to the two four-port packets.
P_mom = s.zeros(4, 6)
for row, col in enumerate([0, 1, 2, 3]):
    P_mom[row, col] = 1
P_hist = s.zeros(4, 6)
for row, col in enumerate([0, 1, 4, 5]):
    P_hist[row, col] = 1

T_mom = T6.extract([0, 1, 2, 3], [0, 1, 2, 3])
T_hist = T6.extract([0, 1, 4, 5], [0, 1, 4, 5])

checks = {
    "order_four": s.simplify(T6**4 - s.eye(6)) == s.zeros(6),
    "moment_projection_intertwines": s.simplify(P_mom*T6 - T_mom*P_mom) == s.zeros(4, 6),
    "history_projection_intertwines": s.simplify(P_hist*T6 - T_hist*P_hist) == s.zeros(4, 6),
    "moment_block_order_four": s.simplify(T_mom**4 - s.eye(4)) == s.zeros(4),
    "history_block_order_four": s.simplify(T_hist**4 - s.eye(4)) == s.zeros(4),
    "shared_even_ports": T6[0, 1] == 1 and T6[1, 0] == 1,
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-fixed-seam-six-channel-fourier-refinement.v1",
    "channels": ["B0", "Q0", "M", "J", "A0", "C0"],
    "fourier_rules": {
        "B0": "Q0",
        "Q0": "B0",
        "M": "-2*pi*i J",
        "J": "(2*pi*i)^(-1) M",
        "A0": "(1/2)B0-(2*pi*i)^(-1)C0",
        "C0": "2*pi*i A0-pi*i Q0"
    },
    "moment_projection": ["B0", "Q0", "M", "J"],
    "history_projection": ["B0", "Q0", "A0", "C0"],
    "checks": checks,
    "passed": True,
    "conclusion": "The six-channel packet is an exact order-four Fourier representation and both four-port systems are equivariant coordinate projections of it."
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "research/nima/results/rh-fixed-seam-six-channel-fourier-refinement.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
