#!/usr/bin/env python3
"""Exact synthetic reversible four-phase helix on the faithful 26-sample shadow."""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
N = 26
D = 4 * N


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(x) for x in zip(*a)]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def block_diag(*blocks):
    out = [[F(0) for _ in range(sum(len(b) for b in blocks))] for _ in range(sum(len(b) for b in blocks))]
    z = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                out[z+i][z+j] = b[i][j]
        z += len(b)
    return out


# Existing faithful sampled comparison: interleaved complex coordinates -> P,Q,M,J.
p = list(range(0, 24, 2)) + list(range(1, 24, 2)) + [24, 25]
C = [[F(p[i] == j) for j in range(N)] for i in range(N)]
Cinv = tr(C)

# A nontrivial exact seam: undo presentation permutation and apply Real parity.
J = [[F(0) for _ in range(N)] for _ in range(N)]
for i in range(N):
    J[i][i] = F(-1 if (i < 24 and i % 2 == 1) or i == 25 else 1)
R = mm(J, Cinv)
Rinv = mm(C, J)
S = mm(R, C)                 # full-turn successor = J
Sinv = mm(Cinv, Rinv)

# tau moves one phase forward; on phase 4 it applies S and wraps to phase 1.
tau = [[F(0) for _ in range(D)] for _ in range(D)]
tau_inv = [[F(0) for _ in range(D)] for _ in range(D)]
for phase in range(3):
    for i in range(N):
        tau[(phase+1)*N+i][phase*N+i] = 1
        tau_inv[phase*N+i][(phase+1)*N+i] = 1
for i in range(N):
    for j in range(N):
        tau[i][3*N+j] = S[i][j]
        tau_inv[3*N+i][j] = Sinv[i][j]

tau2 = mm(tau, tau)
tau4 = mm(tau2, tau2)
expected = block_diag(S, S, S, S)
checks = {
    "sample_comparison_inverse": mm(Cinv, C) == eye(N) and mm(C, Cinv) == eye(N),
    "seam_inverse": mm(Rinv, R) == eye(N) and mm(R, Rinv) == eye(N),
    "successor_inverse": mm(Sinv, S) == eye(N) and mm(S, Sinv) == eye(N),
    "phase_advance_inverse": mm(tau_inv, tau) == eye(D) and mm(tau, tau_inv) == eye(D),
    "four_phase_turn_equals_stage_successor": tau4 == expected,
    "successor_nontrivial": S != eye(N),
    "two_stage_turns_close_in_fixture": mm(S, S) == eye(N),
}
out = {
    "schema": "marici.voevodsky.sampled-observer-reversible-phase-helix.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "dimension_per_phase": N,
    "total_phase_carrier_dimension": D,
    "checks": checks,
    "relations": {"tau_four": "S", "S_fixture": "Real parity J", "S_square_fixture": "identity"},
    "interpretation": "An exact reversible four-phase helix exists on the synthetic jointly faithful 26-sample observer shadow.",
    "claim_boundary": "The 26-sample comparison is synthetic and not identified with the source all-jet/Aspect trace carrier. The chosen seam parity is a finite model, not the analytic C14 seam. This does not establish source-level invertibility.",
}
path = ROOT / "research/voevodsky/results/sampled_observer_reversible_phase_helix.json"
path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
raise SystemExit(out["status"] != "passed")
