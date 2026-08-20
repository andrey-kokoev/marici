"""Exact low-order S43 beta-angle derivation without a cubic eigensystem.

The phase dependence of H_d is an exact diagonal conjugation.  Hierarchical
eigenvectors of the real matrix at phi=0 then suffice to type the quartet
through relative order epsilon^2.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from harmonic_support import EPHI, build, eps


OUTPUT = Path("research/flavor/results/wp4_s43_rephased_nlo.json")
z = sp.symbols("z", nonzero=True)


def trunc(expr: sp.Expr, order: int) -> sp.Expr:
    return sp.expand(sp.series(expr, eps, 0, order).removeO())


def main() -> None:
    Yu, Yd = build("S43")
    syms = {str(symbol): symbol for matrix in (Yu, Yd) for entry in matrix for symbol in entry.free_symbols}
    d13, d23, d33 = (syms[name] for name in ("d13", "d23", "d33"))
    d32, u13, u33 = (syms[name] for name in ("d32", "u13", "u33"))

    Hd = sp.expand(Yd * Yd.H)
    Hd0 = sp.expand(Hd.subs(EPHI, 1))
    phase_matrix = sp.diag(z, z, 1)
    conjugated = sp.expand(phase_matrix * Hd0 * sp.diag(1 / z, 1 / z, 1))
    phase_typed = sp.expand(Hd.subs({EPHI: 1 / z, sp.conjugate(EPHI): z}))

    # Real hierarchical eigenvectors.  Only the displayed orders can enter
    # R_beta through relative epsilon^2.
    a = d13 / d23
    light_d = sp.Matrix([
        1 - a**2 * eps**2 / 2,
        -a * eps + a**3 * eps**3 / 2,
        0,
    ])
    denom = d32**2 + d33**2
    heavy_b = sp.Matrix([
        d13 * d33 / denom * eps**2,
        d23 * d33 / denom * eps,
        1 - d23**2 * d33**2 / (2 * denom**2) * eps**2,
    ])
    heavy_t = sp.Matrix([u13 / u33 * eps**2, 0, 1])
    charm = sp.Matrix([0, 1, 0])

    d_phase = phase_matrix * light_d
    b_phase = phase_matrix * heavy_b
    Vcd = trunc((charm.T * d_phase)[0], 4)
    Vcb = trunc((charm.T * b_phase)[0], 4)
    Vtd = trunc((heavy_t.T * d_phase)[0], 5)
    Vtb = trunc((heavy_t.T * b_phase)[0], 3)

    def unit_conjugate(expr: sp.Expr) -> sp.Expr:
        return sp.conjugate(expr).subs({sp.conjugate(z): 1 / z})

    quartet = trunc(-Vcd * unit_conjugate(Vcb) / (Vtd * unit_conjugate(Vtb)), 3)
    reduced = sp.simplify(quartet * z)  # remove e^{+i phi}=1/z
    tests = {
        "T1_Hd_phase_is_diagonal_conjugation": all(
            sp.simplify(entry) == 0 for entry in (phase_typed - conjugated)
        ),
        "T2_light_vector_normalized_through_eps3": trunc((light_d.T * light_d)[0] - 1, 4) == 0,
        "T3_beta_quartet_has_only_exp_plus_i_phi_through_relative_eps2": not reduced.has(z),
        "T4_reduced_quartet_is_real_for_real_edges": sp.simplify(sp.conjugate(reduced) - reduced) == 0,
        "T5_relative_eps2_phase_coefficient_vanishes": sp.im(sp.expand(reduced).coeff(eps, 2)) == 0,
    }
    packet = {
        "schema": "marici.flavor.s43-rephased-nlo.v1",
        "tests": tests,
        "phase_conjugation": "H_d(phi)=diag(e^-iphi,e^-iphi,1) H_d(0) diag(e^iphi,e^iphi,1)",
        "elements": {name: str(value) for name, value in {
            "V_cd": Vcd, "V_cb": Vcb, "V_td": Vtd, "V_tb": Vtb
        }.items()},
        "R_beta": str(quartet),
        "R_beta_times_exp_minus_i_phi": str(reduced),
        "verdict": (
            "For S43 as written, arg R_beta = phi plus no epsilon^2 phase "
            "correction.  The nonzero S47 correction is not reproduced."
        ),
    }
    OUTPUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not all(tests.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
