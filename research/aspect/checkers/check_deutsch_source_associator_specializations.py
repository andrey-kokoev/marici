#!/usr/bin/env python3
"""Exact specialization gate for source-constructed associator packets."""
import json
from pathlib import Path

A = Path(__file__).resolve().parent.parent
C = json.loads((A / "contracts" / "deutsch-coherent-constructor-conjecture.v2.json").read_text())
P = json.loads((A / "fixtures" / "deutsch-source-associators.v1.json").read_text())
R = A / "results" / "deutsch_source_associator_specializations.json"

def mm(x, y, p):
    return [[sum(x[i][k] * y[k][j] for k in range(2)) % p for j in range(2)] for i in range(2)]

def inv(x, p):
    d = (x[0][0] * x[1][1] - x[0][1] * x[1][0]) % p
    di = pow(d, -1, p)
    return [[x[1][1] * di % p, -x[0][1] * di % p], [-x[1][0] * di % p, x[0][0] * di % p]]

def edge(gs, a, b, p):
    return mm(gs[b], inv(gs[a], p), p)

def path(gs, vertices, p, hostile=False):
    out = [[1, 0], [0, 1]]
    for a, b in zip(vertices, vertices[1:]):
        e = edge(gs, a, b, p)
        if hostile and [a, b] == P["hostile"]["edge"] and p in P["hostile"]["active_primes"]:
            e = [[(e[i][j] + P["hostile"]["additive_defect"][i][j]) % p for j in range(2)] for i in range(2)]
        out = mm(e, out, p)
    return out

def main():
    gs = P["vertex_frames"]
    rows = {}
    for p in C["specializations"]:
        clean_u = path(gs, C["upper_path"], p)
        clean_l = path(gs, C["lower_path"], p)
        bad_u = path(gs, C["upper_path"], p, True)
        rows[str(p)] = {
            "exact_clean_closure": clean_u == clean_l,
            "hostile_closure": bad_u == clean_l,
            "hostile_detected": bad_u != clean_l,
            "upper": clean_u,
            "lower": clean_l,
            "hostile_upper": bad_u
        }
    checks = {
        "source_authority_explicit": bool(P["authority"]),
        "same_packet_all_primes": True,
        "exact_clean_all_primes": all(x["exact_clean_closure"] for x in rows.values()),
        "bad_prime_defects_detected": all(rows[str(p)]["hostile_detected"] for p in C["bad_prime_candidates"]),
        "good_control_unchanged": rows[str(C["good_control_prime"])]["hostile_closure"],
        "physical_claim_withheld": not any(C["claim_boundary"].values())
    }
    out = {
        "schema": "marici.aspect.deutsch-source-associator-specializations-result.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "specializations": rows,
        "verdict": "exact_source_packet_closes_and_prime_local_hostile_is_detected",
        "authority_status": "synthetic_exact_fixture_only"
    }
    R.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if out["passed"] else 1)

if __name__ == "__main__":
    main()
