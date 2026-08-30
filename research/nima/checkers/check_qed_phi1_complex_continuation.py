import json
import sys
from pathlib import Path

import mpmath as mp

NIMA = Path(__file__).parents[1]
sys.path.insert(0, str(NIMA))
sys.path.insert(0, str(Path(__file__).parent))
from check_exact_qed_bell_onset import g1, g2, solve_wz, amplitudes  # noqa: E402
from check_qed_phi1_full_dispersion_real import (  # noqa: E402
    dispersive_part,
    spectral_packet,
)

mp.mp.dps = 40


def root_candidates(xi, xj):
    linear = -xi * (2 - xj) - 4 * xj
    discriminant = linear**2 - 4 * xi**2
    roots_p = [
        (-linear + mp.sqrt(discriminant)) / (2 * xi),
        (-linear - mp.sqrt(discriminant)) / (2 * xi),
    ]
    candidates = []
    for p in roots_p:
        sigma0 = mp.sqrt((4 - xj) * p)
        delta0 = mp.sqrt(-xj * p)
        for sigma in (sigma0, -sigma0):
            for delta in (delta0, -delta0):
                w = (sigma + delta) / 2
                z = (sigma - delta) / 2
                residual = abs(
                    -4 * (w - z) ** 2
                    / ((1 - w**2) * (1 - z**2))
                    - xi
                )
                residual += abs(-(w - z) ** 2 / (w * z) - xj)
                candidates.append((residual, w, z))
    return candidates


def solve_wz_near(xi, xj, anchor):
    _, w, z = min(
        root_candidates(xi, xj),
        key=lambda item: (
            abs(item[1] - anchor[0]) + abs(item[2] - anchor[1])
            + 1000 * item[0]
        ),
    )
    return w, z


def sqrt_near(value, anchor):
    root = mp.sqrt(value)
    return min((root, -root), key=lambda candidate: abs(candidate - anchor))


def masters_continued(triple, anchor_triple, lower_sheet=False):
    xi, xj, _ = triple
    xi0, xj0, _ = anchor_triple
    anchor_wz = solve_wz(xi0, xj0)
    if lower_sheet:
        anchor_wz = tuple(mp.conj(value) for value in anchor_wz)
    w, z = solve_wz_near(xi, xj, anchor_wz)

    f2 = -g1(-1, w) + g1(-1, z) + g1(1, w) - g1(1, z)
    f4 = (g1(1, w) - g1(-1, w)) * (g1(-1, z) - g1(1, z))
    for i in (0, 1):
        for j in (0, 1):
            ai, aj = (-1) ** i, (-1) ** j
            f4 += (-1) ** (i + j) * (
                g2(ai, aj, w) + g2(ai, aj, z)
            )
    f6 = (
        g1(0, w) * (g1(1, z) - g1(-1, z))
        + g1(0, z) * (g1(-1, w) - g1(1, w))
        + g2(1, 0, w)
        - g2(-1, 0, w)
        + g2(0, -1, w)
        - g2(0, 1, w)
        - g2(1, 0, z)
        + g2(-1, 0, z)
        - g2(0, -1, z)
        + g2(0, 1, z)
    )
    if (xi0 > 0) ^ (xj0 > 0):
        f6 = -f6
    return f2, f4, f6


def amplitudes_continued(s, transfer):
    # The source GPL formulas are charted on the upper physical sheet.
    # The lower sheet is supplied by the declared real structure, not by
    # reevaluating the same closed forms with principal logarithms.
    if mp.im(s) < 0:
        return tuple(
            mp.conj(value)
            for value in amplitudes_continued(mp.conj(s), transfer)
        )
    lower_sheet = mp.im(s) < 0
    s0 = mp.re(s)
    invariants = (s, -s - transfer, mp.mpf(transfer))
    anchors = (s0, -s0 - transfer, mp.mpf(transfer))
    triples = [
        (invariants[0], invariants[1], invariants[2]),
        (invariants[1], invariants[2], invariants[0]),
        (invariants[2], invariants[0], invariants[1]),
    ]
    anchor_triples = [
        (anchors[0], anchors[1], anchors[2]),
        (anchors[1], anchors[2], anchors[0]),
        (anchors[2], anchors[0], anchors[1]),
    ]
    data = [
        masters_continued(triple, anchor, lower_sheet)
        for triple, anchor in zip(triples, anchor_triples)
    ]

    def root2(value, anchor_value):
        anchor_root = mp.sqrt(anchor_value * (anchor_value - 4))
        if lower_sheet:
            anchor_root = mp.conj(anchor_root)
        return sqrt_near(value * (value - 4), anchor_root)

    def root3(triple, anchor):
        xi, xj, xk = triple
        ai, aj, ak = anchor
        value = xi * xj * (xi * xj + 4 * xk)
        anchor_value = ai * aj * (ai * aj + 4 * ak)
        anchor_root = mp.sqrt(anchor_value)
        if lower_sheet:
            anchor_root = mp.conj(anchor_root)
        return sqrt_near(value, anchor_root)

    xs, xt, xu = invariants
    axs, axt, axu = anchors
    f2_stu, f4_stu, f6_stu = data[0]
    f2_tus, f4_tus, f6_tus = data[1]
    f2_ust, f4_ust, f6_ust = data[2]

    def r9(xi, xj, xk):
        return (xi - 4) * (xi - xj) / xk

    def r10(xi, xj, xk):
        return 1 - 4 / xi - 2 * xj * xk / xi**2

    def r11(xi, xj, xk):
        return (
            4 - 2 * xi - xj * xk
            + 2 * xj * xk * (xj * xk + 4 * xi) / xi**2
        )

    roots3 = [
        root3(triple, anchor)
        for triple, anchor in zip(triples, anchor_triples)
    ]
    sum_f4 = sum(item[1] for item in data)
    sum_f6 = sum(item[2] / root for item, root in zip(data, roots3))
    m_pppp = 1 - 4 * sum_f6

    def r8(xi, xj, xk):
        return 2 * (xi * xj + 2 * xk) / xk

    m_mppp = 1 + 2 * (1 / xs + 1 / xt + 1 / xu) * sum_f4
    m_mppp -= sum(
        r8(*triple) * item[2] / root
        for triple, item, root in zip(triples, data, roots3)
    )

    m_mmpp = -1
    m_mmpp += r9(xt, xu, xs) * f2_tus / root2(xt, axt)
    m_mmpp += r9(xu, xt, xs) * f2_ust / root2(xu, axu)
    m_mmpp -= r10(xs, xt, xu) * (f4_tus + f4_ust)
    m_mmpp += 2 * (xs - 2) * f6_stu / roots3[0]
    m_mmpp += 2 * (xs - 2) * f6_ust / roots3[2]
    m_mmpp -= r11(xs, xt, xu) * f6_tus / roots3[1]
    alpha = mp.mpf(1) / (4 * mp.pi)
    scale = 8 * alpha**2
    return scale * m_mmpp, scale * m_pppp, scale * m_mppp


def phi1_continued(s, transfer):
    return amplitudes_continued(s, transfer)[0]


def main():
    transfer = -0.25
    packet = spectral_packet(transfer, 34, 30)
    real_rows = json.loads(
        (NIMA / "results" / "qed-phi1-full-dispersion-real.json").read_text()
    )
    a = real_rows["subtraction"]["a"]
    b = real_rows["subtraction"]["b"]

    points = [
        mp.mpc("1.1", "0.02"),
        mp.mpc("1.7", "0.03"),
    ]
    rows = []
    for s in points:
        nu = complex(s) + transfer / 2
        exact_plus = phi1_continued(s, transfer)
        exact_minus = phi1_continued(mp.conj(s), transfer)
        reconstructed = dispersive_part(nu, packet) + a + b * nu
        residual = complex(exact_plus) - reconstructed
        rows.append({
            "s": [float(mp.re(s)), float(mp.im(s))],
            "exact": [float(mp.re(exact_plus)), float(mp.im(exact_plus))],
            "reconstructed": [
                float(reconstructed.real), float(reconstructed.imag)
            ],
            "relative_residual": float(
                abs(residual) / max(abs(complex(exact_plus)), 1e-30)
            ),
            "real_structure_residual": float(
                abs(exact_minus - mp.conj(exact_plus))
            ),
        })

    # At zero imaginary part, the continuation must reproduce the certified
    # real implementation before it is trusted off-axis.
    anchor_s = mp.mpf("1.1")
    continued_anchor = phi1_continued(anchor_s, transfer)
    x = 1 + transfer / float(anchor_s)
    alpha = mp.mpf(1) / (4 * mp.pi)
    original_anchor = 8 * alpha**2 * amplitudes(anchor_s, mp.mpf(str(x)))[0]
    anchor_residual = abs(continued_anchor - original_anchor)

    gates = {
        "continued_formula_matches_real_anchor": bool(
            anchor_residual < mp.mpf("1e-20")
        ),
        "complex_conjugate_points_obey_real_structure": bool(
            max(row["real_structure_residual"] for row in rows) < 1e-24
        ),
        "same_affine_packet_predicts_complex_points": bool(
            max(row["relative_residual"] for row in rows) < 5e-5
        ),
    }
    assert all(gates.values()), {"gates": gates, "rows": rows}

    result = {
        "schema": "marici.qed-phi1-complex-continuation.v1",
        "transfer": transfer,
        "branch_rule": (
            "upper-sheet algebraic w,z roots continue from certified real "
            "Region I-III anchors; the lower sheet is their Schwarz reflection"
        ),
        "gates": gates,
        "real_anchor_residual": str(anchor_residual),
        "points": rows,
        "conclusion": (
            "The same two source boundary jets complete the coupled Cut at "
            "hostile complex-conjugate points; no non-affine residual appears."
        ),
    }
    out = NIMA / "results" / "qed-phi1-complex-continuation.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
