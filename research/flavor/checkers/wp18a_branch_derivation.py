#!/usr/bin/env python3
"""WP18a: the observable coordinate physical10 is two-to-one — derivation.

The CKM block of physical10, (|Vus|, |Vub|, |Vcb|, signed J), fixes the
PDG parameters s12 = |Vus|/c13, s13 = |Vub|, s23 = |Vcb|/c13 and
sin delta = J / (c12 s12 c23 s23 c13^2 s13).  cos delta is NOT fixed:
the two branches delta and pi - delta are both compatible with all ten
observables but differ in |Vtd|, |Vcd|, |Vcs|, |Vts| (and |Vub|-phase
sensitive quantities).

This checker derives both branches from the p* CKM data and matches
them against the two WP16 orbit-15 roots, which turn out to be exactly
one preimage per branch — the WP16 "two-phase fiber within one chart"
is the two-sheetedness of the observable coordinate, not a
chart-intrinsic multiplicity.

Outputs: research/flavor/results/wp18a_branch_derivation.json
"""
import json
import math
import sys

import numpy as np

sys.path.insert(0, "checkers")
import wp7_ensemble as wp7

# The two WP16 orbit-15 (85,234) roots over p* (results/wp16b rerun).
ROOT_A = [-8.05542, -11.85273, -0.03356, -5.64198, -9.63414, -4.12296,
          -6.37596, -7.28226, -8.14188, -1.575464]
ROOT_B = [-8.05479, -11.85273, -0.03356, -5.64199, -9.38774, -4.12083,
          -6.62024, -7.28438, -8.14617, 5.381368]


def main():
    pilot = json.load(open("results/wp16a_fiber_degree_pilot.json"))
    Vus, Vub, Vcb, J = (pilot["p_star"][6], pilot["p_star"][7],
                        pilot["p_star"][8], pilot["p_star"][9])

    s13 = Vub
    c13 = math.sqrt(1 - s13 * s13)
    s12 = Vus / c13
    s23 = Vcb / c13
    c12 = math.sqrt(1 - s12 * s12)
    c23 = math.sqrt(1 - s23 * s23)
    sin_delta = J / (c12 * s12 * c23 * s23 * c13 * c13 * s13)

    branches = {}
    for name, delta in (("cos_pos", math.asin(sin_delta)),
                        ("cos_neg", math.pi - math.asin(sin_delta))):
        z = complex(math.cos(delta), math.sin(delta))
        branches[name] = {
            "delta": delta,
            "Vtd": abs(s12 * s23 - c12 * c23 * s13 * z),
            "Vcd": abs(-s12 * c23 - c12 * s23 * s13 * z),
            "Vts": abs(-c12 * s23 - s12 * c23 * s13 * z),
            "Vcs": abs(c12 * c23 - s12 * s23 * s13 * z),
        }

    mu, md = 85, 234
    phase_sector, phase_slot = wp7.paper_phase_edge(mu, md)
    observed = {}
    for name, root in (("root_A", ROOT_A), ("root_B", ROOT_B)):
        Yu, Yd = wp7.build_texture(mu, md, phase_sector, phase_slot,
                                   np.array(root))
        su2, Uu = np.linalg.eigh(Yu @ Yu.conj().T)
        sd2, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
        V = Uu.conj().T @ Ud
        observed[name] = {"phi": float(root[9]),
                          "Vtd": float(abs(V[2, 0])),
                          "Vcd": float(abs(V[1, 0])),
                          "Vts": float(abs(V[2, 1])),
                          "Vcs": float(abs(V[1, 1]))}

    def match(obs, br):
        return max(abs(obs[k] - br[k]) / br[k]
                   for k in ("Vtd", "Vcd", "Vts", "Vcs"))

    pairing = {
        "root_A_vs_cos_pos": match(observed["root_A"], branches["cos_pos"]),
        "root_A_vs_cos_neg": match(observed["root_A"], branches["cos_neg"]),
        "root_B_vs_cos_pos": match(observed["root_B"], branches["cos_pos"]),
        "root_B_vs_cos_neg": match(observed["root_B"], branches["cos_neg"]),
    }
    out = {
        "purpose": "derive the two cos-delta branches of physical10 at "
                   "p* and identify the WP16 orbit-15 roots as one "
                   "preimage per branch",
        "p_star_ckm": {"Vus": Vus, "Vub": Vub, "Vcb": Vcb, "J": J},
        "sin_delta": sin_delta,
        "branches": branches,
        "observed_roots": observed,
        "max_relative_mismatch": pairing,
        "conclusion": ("root_A = cos>0 branch, root_B = cos<0 branch"
                       if pairing["root_A_vs_cos_pos"] < 1e-4
                       and pairing["root_B_vs_cos_neg"] < 1e-4
                       else "PAIRING FAILED — recheck"),
    }
    dest = "results/wp18a_branch_derivation.json"
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    for k, v in pairing.items():
        print(f"{k}: {v:.3e}")
    print(out["conclusion"])
    print("->", dest)


if __name__ == "__main__":
    main()
