#!/usr/bin/env python3
"""Check the non-circular polarized prime-cell four-unit and Pauli gates."""
import argparse
import json
from pathlib import Path


def cv(x):
    if isinstance(x, list) and len(x) == 2:
        return complex(x[0], x[1])
    return complex(x)


def mat(x):
    if not isinstance(x, list) or len(x) != 2 or any(not isinstance(r, list) or len(r) != 2 for r in x):
        raise ValueError("expected a 2x2 matrix")
    return [[cv(v) for v in r] for r in x]


def adj(a):
    return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def close(a, b, tol):
    return [[abs(a[i][j] - b[i][j]) <= tol for j in range(2)] for i in range(2)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("packet", type=Path)
    ap.add_argument("--tol", type=float, default=1e-12)
    args = ap.parse_args()
    packet = json.loads(args.packet.read_text(encoding="utf-8"))
    required = ["G_St", "G_theta", "Q_lin", "O_X", "O_Y"]
    missing = [k for k in required if packet.get(k) is None]
    result = {"packet": str(args.packet), "complete": not missing, "missing": missing, "passed": False}
    if missing:
        print(json.dumps(result, indent=2))
        raise SystemExit(2)
    gs, gt, q, ox, oy = (mat(packet[k]) for k in required)
    pullback = mul(adj(q), mul(gt, q))
    four = close(gs, pullback, args.tol)
    u = [[-1j, 0j], [0j, 1j]]
    covariance = close(oy, mul(ox, u), args.tol)
    result.update({
        "four_matrix_units": four,
        "pauli_covariance_entries": covariance,
        "passed": all(map(all, four)) and all(map(all, covariance)),
        "claim_boundary": "Checks supplied matrices only; provenance, common-core closure, uniform prime bounds, Evans cancellation, and RH are not certified."
    })
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
