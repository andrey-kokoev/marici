"""Numerical exact one-loop QED Bell readout from arXiv:2312.16966 eqs. 53-55."""

import cmath
import hashlib
import json
from functools import lru_cache
from pathlib import Path

import mpmath as mp

mp.mp.dps = 35


def g1(a, z):
    if a == 0:
        return mp.log(z)
    return mp.log(1 - z / a)


@lru_cache(maxsize=None)
def g2_quadrature(a, b, z):
    """Direct defining integral, retained as an independent regression oracle."""
    def integrand(q):
        if q == 0:
            return mp.mpc(0)
        return z / (z * q - a) * g1(b, z * q)

    return mp.quad(integrand, [0, 1])


@lru_cache(maxsize=None)
def g2(a, b, z):
    """Closed dilogarithmic form of G(a,b;z) on the selected physical sheet."""
    if a == 0:
        return -mp.polylog(2, z / b)
    if b == 0:
        if abs(mp.im(z)) < mp.mpf("1e-25"):
            return mp.log(z) * mp.log(1 - z / a) + mp.polylog(2, z / a)
        v = 1 - z / a
        return mp.log(a) * mp.log(v) - mp.polylog(2, v) + mp.polylog(2, 1)
    if a == b:
        return mp.log(1 - z / a) ** 2 / 2
    return (
        mp.log((b - a) / b) * (mp.log(z - a) - mp.log(-a))
        - mp.polylog(2, (z - a) / (b - a))
        + mp.polylog(2, -a / (b - a))
    )


def solve_wz(xi, xj):
    tol = mp.mpf("1e-20")

    def physical_branch(w, z):
        """Implement the below-threshold regions following arXiv:2312.16966."""
        wr, wi = mp.re(w), mp.im(w)
        if xi < 0 and xj < 0:  # Region I
            return (
                abs(mp.im(w)) < tol
                and abs(mp.im(z)) < tol
                and 0 < mp.re(w) <= mp.re(z) < 1
            )
        if xi > 0 and xj < 0:  # Region II
            lower2 = max(mp.mpf(0), 1 - 2 * wr - wr**2)
            upper2 = 1 - wr**2
            return (
                0 < wr < 1
                and wi > 0
                and upper2 > 0
                and mp.sqrt(lower2) - tol < wi < mp.sqrt(upper2) + tol
                and abs(z - w / abs(w) ** 2) < tol
            )
        if xi < 0 and xj > 0:  # Region III
            upper2 = 1 + 2 * wr - wr**2
            return (
                1 - mp.sqrt(2) < wr < 0
                and wi > 0
                and upper2 > 0
                and wi < mp.sqrt(upper2) + tol
                and abs(z + mp.conj(w)) < tol
            )
        return False

    # Put p=wz and sigma=w+z.  Eliminating sigma and (w-z)^2 gives
    # xi*p^2 + [-xi*(2-xj)-4*xj]*p + xi = 0.
    linear = -xi * (2 - xj) - 4 * xj
    discriminant = linear**2 - 4 * xi**2
    sqrt_discriminant = mp.sqrt(discriminant)
    # Rationalize the cancellation-prone small root.
    p_plus = 2 * xi / (-linear - sqrt_discriminant)
    p_minus = (-linear - sqrt_discriminant) / (2 * xi)
    for p in (p_plus, p_minus):
        sigma0 = mp.sqrt((4 - xj) * p)
        delta0 = mp.sqrt(-xj * p)
        for sigma in (sigma0, -sigma0):
            for delta in (delta0, -delta0):
                w, z = (sigma + delta) / 2, (sigma - delta) / 2
                eq1 = -4 * (w - z) ** 2 / ((1 - w**2) * (1 - z**2)) - xi
                eq2 = -(w - z) ** 2 / (w * z) - xj
                residual = abs(eq1) + abs(eq2)
                if residual < mp.mpf("1e-25") and physical_branch(w, z):
                    return w, z
    raise RuntimeError(f"no (w,z) branch found for {(xi, xj)}")


def masters(xi, xj, xk):
    w, z = solve_wz(xi, xj)
    f2 = -g1(-1, w) + g1(-1, z) + g1(1, w) - g1(1, z)

    f4 = (g1(1, w) - g1(-1, w)) * (g1(-1, z) - g1(1, z))
    for i in (0, 1):
        for j in (0, 1):
            ai, aj = (-1) ** i, (-1) ** j
            f4 += (-1) ** (i + j) * (g2(ai, aj, w) + g2(ai, aj, z))

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
    if (xi > 0) ^ (xj > 0):
        f6 = -f6
    return f2, f4, f6


def amplitudes(y, x=mp.mpf("0.5")):
    y, x = mp.mpf(y), mp.mpf(x)
    xs, xt, xu = y, -y * x, -y * (1 - x)
    triples = [(xs, xt, xu), (xt, xu, xs), (xu, xs, xt)]
    data = [masters(*triple) for triple in triples]

    def root2(x):
        return mp.sqrt(x * (x - 4))

    def root3(xi, xj, xk):
        return mp.sqrt(xi * xj * (xi * xj + 4 * xk))

    sum_f4 = sum(d[1] for d in data)
    sum_f6 = sum(d[2] / root3(*triple) for d, triple in zip(data, triples))
    m_pppp = 1 - 4 * sum_f6

    def r8(xi, xj, xk):
        return 2 * (xi * xj + 2 * xk) / xk

    m_mppp = 1 + 2 * (1 / xs + 1 / xt + 1 / xu) * sum_f4
    m_mppp -= sum(r8(*triple) * d[2] / root3(*triple) for d, triple in zip(data, triples))

    # Eq. 54, specialized only after retaining the labelled permutations.
    f2_stu, f4_stu, f6_stu = data[0]
    f2_tus, f4_tus, f6_tus = data[1]
    f2_ust, f4_ust, f6_ust = data[2]

    def r9(xi, xj, xk):
        return (xi - 4) * (xi - xj) / xk

    def r10(xi, xj, xk):
        return 1 - 4 / xi - 2 * xj * xk / xi**2

    def r11(xi, xj, xk):
        return 4 - 2 * xi - xj * xk + 2 * xj * xk * (xj * xk + 4 * xi) / xi**2

    m_mmpp = -1
    m_mmpp += r9(xt, xu, xs) * f2_tus / root2(xt)
    m_mmpp += r9(xu, xt, xs) * f2_ust / root2(xu)
    m_mmpp -= r10(xs, xt, xu) * (f4_tus + f4_ust)
    m_mmpp += 2 * (xs - 2) * f6_stu / root3(xs, xt, xu)
    m_mmpp += 2 * (xs - 2) * f6_ust / root3(xu, xs, xt)
    m_mmpp -= r11(xs, xt, xu) * f6_tus / root3(xt, xu, xs)
    return m_mmpp, m_pppp, m_mppp


def bell(y, x=mp.mpf("0.5")):
    a, b, c = amplitudes(y, x)
    signed = 4 * mp.sqrt(2) * mp.re(a * mp.conj(b)) / (abs(a) ** 2 + abs(b) ** 2 + 2 * abs(c) ** 2)
    return abs(signed)


def bisect_onset(lo, hi, x=mp.mpf("0.5"), iterations=32):
    flo, fhi = bell(lo, x) - 2, bell(hi, x) - 2
    assert flo < 0 < fhi
    for _ in range(iterations):
        mid = (lo + hi) / 2
        fmid = bell(mid, x) - 2
        if fmid > 0:
            hi, fhi = mid, fmid
        else:
            lo, flo = mid, fmid
    return lo, hi, flo, fhi


if __name__ == "__main__":
    rows = []
    for y in ("0.01", "0.1", "0.4", "0.5"):
        amps = amplitudes(y)
        rows.append({"y": y, "amplitudes": [str(v) for v in amps], "bell": str(bell(y))})

    # Low-energy coefficient gate in the normalization of eq. 54 (common 8 removed).
    y0 = mp.mpf("0.01")
    a0, b0, c0 = amplitudes(y0)
    expected = (
        mp.mpf(11) / 360 * y0**2,
        -mp.mpf(1) / 80 * y0**2,
        -mp.mpf(1) / 10080 * y0**3,
    )
    relative_errors = [abs((got - want) / want) for got, want in zip((a0, b0, c0), expected)]
    assert max(relative_errors) < mp.mpf("0.002")

    lo, hi, flo, fhi = bisect_onset(mp.mpf("0.4"), mp.mpf("0.5"))
    angular_census = {}
    for sample_y in (mp.mpf("0.4"), mp.mpf("0.43")):
        samples = [(mp.mpf(k) / 50, bell(sample_y, mp.mpf(k) / 50)) for k in range(1, 26)]
        monotone_to_transverse = all(samples[i][1] >= samples[i + 1][1] for i in range(len(samples) - 1))
        assert monotone_to_transverse
        angular_census[str(sample_y)] = {
            "grid": "x=k/50, 1<=k<=25; reflection supplies 1/2<=x<1",
            "minimum": {"x": str(samples[-1][0]), "bell": str(samples[-1][1])},
            "maximum": {"x": str(samples[0][0]), "bell": str(samples[0][1])},
            "monotone_toward_transverse": monotone_to_transverse,
        }
    payload = {
        "schema": "marici.exact-one-loop-qed-bell-onset.v1",
        "strength": "numerical evaluation of the exact analytic one-loop helicity amplitudes with a low-energy coefficient gate",
        "source": "arXiv:2312.16966v2 equations 50 and 53-55",
        "energy_variable": "y=s/m_e^2",
        "low_energy_gate": {
            "sample_y": str(y0),
            "expected_stripped_amplitudes": [str(v) for v in expected],
            "relative_errors": [str(v) for v in relative_errors],
            "verdict": "all three amplitudes reproduce g2, f2, and h3 within the expected finite-y remainder",
        },
        "samples": rows,
        "onset_bracket": {
            "lo": str(lo),
            "hi": str(hi),
            "bell_minus_2_lo": str(flo),
            "bell_minus_2_hi": str(fhi),
            "midpoint": str((lo + hi) / 2),
            "sqrt_s_over_m_e": str(mp.sqrt((lo + hi) / 2)),
        },
        "comparison": {
            "d10_truncated_amplitude": "0.4680304498848546",
            "d12_truncated_amplitude": "0.4236925576731669",
            "exact_one_loop": str((lo + hi) / 2),
        },
        "bounded_angular_census": angular_census,
        "conclusion": "The transverse fixed-analyzer Bell crossing predicted by consecutive EFT truncations survives in the exact one-loop QED amplitude below pair production.",
        "scope": "A 25-point half-interval census identifies the transverse point as the minimum immediately below and above onset, supporting but not proving an all-angle theorem. Two-loop radiative corrections are not included.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
    out = Path(__file__).parent / "results" / "exact-qed-bell-onset.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"low_energy_gate": True, "onset": payload["onset_bracket"], "sha256": payload["content_sha256"]}, indent=2))
