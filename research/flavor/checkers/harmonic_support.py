"""Exact harmonic support of det[Hu, Hd] in z = e^{i phi} (marici.Figueiredo).

Responds to marici.Nima's proposed test (epistemic event ev-000000000672):
determine whether the connected b1 = 1 sparse topology forces the COMPLETE
commutator determinant to carry only the first harmonic,

    det[Hu, Hd] = sum_m a_m (z^m - z^{-m})  =  2i sum_m a_m sin(m phi),

at finite epsilon, or whether higher odd harmonics sin(m phi) appear.

For each of the four worked textures of arXiv:2607.27315v1 (S38, S43, S48,
S53) with the placed phase generalized to z = e^{i phi}:

  1. compute det C, C = [Yu Yu^dag, Yd Yd^dag], EXACTLY (no epsilon
     truncation) as a Laurent polynomial in z with symbolic magnitudes;
  2. verify the CP antisymmetry a_{-m} = -a_m coefficient-wise (z -> z^{-1}
     is complex conjugation; the commutator of Hermitian matrices is
     anti-Hermitian, so only sine harmonics can appear);
  3. report the harmonic support {m : a_m != 0} and, for each harmonic,
     the leading epsilon order and coefficient monomial structure.

All arithmetic exact (sympy symbolic).  No floating point.

Output: research/flavor/results/harmonic_support.json
"""
import json
import sympy as sp

I = sp.I
eps = sp.symbols("epsilon", positive=True, real=True)
phi = sp.symbols("phi", real=True)
z = sp.symbols("z", nonzero=True)
EPHI = sp.exp(I * phi)


def sym(name):
    return sp.symbols(name, positive=True, real=True)


def build(name):
    u11, u12, u13 = sym("u11"), sym("u12"), sym("u13")
    u21, u22, u23, u33 = sym("u21"), sym("u22"), sym("u23"), sym("u33")
    d11, d12, d13 = sym("d11"), sym("d12"), sym("d13")
    d21, d22, d23 = sym("d21"), sym("d22"), sym("d23")
    d31, d32, d33 = sym("d31"), sym("d32"), sym("d33")
    Yu = sp.Matrix.zeros(3); Yd = sp.Matrix.zeros(3)
    if name == "S38":          # Example I: phase on Yu_12
        Yu[0, 1] = EPHI * u12 * eps**4; Yu[1, 0] = u21 * eps**5
        Yu[1, 1] = u22 * eps**3;        Yu[2, 2] = u33
        Yd[0, 1] = d12 * eps**5; Yd[1, 0] = d21 * eps**5
        Yd[1, 1] = d22 * eps**4; Yd[1, 2] = d23 * eps**3
        Yd[2, 2] = d33 * eps**2
    elif name == "S43":        # Example II: phase on Yd_33
        Yu[0, 0] = u11 * eps**5; Yu[0, 2] = u13 * eps**2
        Yu[1, 1] = u22 * eps**2; Yu[2, 2] = u33
        Yd[0, 0] = d11 * eps**5; Yd[0, 2] = d13 * eps**4
        Yd[1, 2] = d23 * eps**3; Yd[2, 1] = d32 * eps**2
        Yd[2, 2] = EPHI * d33 * eps**2
    elif name == "S48":        # Example III: phase on Yd_12
        Yu[0, 0] = u11 * eps**5; Yu[1, 1] = u22 * eps**2
        Yu[1, 2] = u23 * eps;    Yu[2, 2] = u33
        Yd[0, 1] = EPHI * d12 * eps**4; Yd[0, 2] = d13 * eps**4
        Yd[1, 1] = d22 * eps**3
        Yd[2, 0] = d31 * eps**3; Yd[2, 2] = d33 * eps**2
    elif name == "S53":        # pi/4 example: phase on Yd_22
        Yu[0, 0] = u11 * eps**6; Yu[1, 1] = u22 * eps**3
        Yu[1, 2] = u23 * eps**2; Yu[2, 2] = u33
        Yd[0, 2] = d13 * eps**5; Yd[1, 0] = d21 * eps**5
        Yd[1, 1] = EPHI * d22 * eps**4
        Yd[2, 1] = d32 * eps**2; Yd[2, 2] = d33 * eps**2
    else:
        raise ValueError(name)
    return Yu, Yd


def laurent_coeffs(d):
    """Expand det C and read off coefficients of z^m as a dict."""
    d = sp.expand(d).subs({sp.exp(I * phi): z, sp.exp(-I * phi): z**-1})
    d = sp.expand(d)
    # clear denominators: find most negative power
    terms = sp.Poly(sp.expand(d * z**8), z)  # z-degree of det C <= 6
    out = {}
    for (pw,), coeff in terms.terms():
        out[pw - 8] = coeff
    return {m: c for m, c in out.items() if c != 0}


def analyze(name):
    Yu, Yd = build(name)
    Hu, Hd = Yu * Yu.H, Yd * Yd.H
    C = Hu * Hd - Hd * Hu
    d = C.det()
    coeffs = laurent_coeffs(d)
    support = sorted({abs(m) for m in coeffs})
    # CP antisymmetry audit: a_{-m} == -a_m exactly
    antisym = all(sp.simplify(coeffs.get(-m, 0) + coeffs.get(m, 0)) == 0
                  for m in support)
    harmonics = {}
    for m in support:
        a = sp.expand(coeffs[m])
        ser = sp.series(a, eps, 0, 40)
        lead = ser.removeO()
        # leading epsilon power
        if lead == 0:
            harmonics[m] = {"leading": "vanishes to eps^40", "coefficient": str(a)}
            continue
        powers = [t.as_exponent_of(eps) if hasattr(t, "as_exponent_of") else None
                  for t in sp.Add.make_args(lead)]
        harmonics[m] = {
            "leading_eps_order": str(ser.getO() or "exact"),
            "leading_coefficient": str(lead),
            "full_coefficient": str(a),
        }
    return {"harmonic_support_m": support,
            "cp_antisymmetry_exact": bool(antisym),
            "harmonics": harmonics}


def main():
    out = {"purpose": "exact harmonic support of det[Hu,Hd] in z=e^{i phi} "
                      "at finite epsilon (Nima's test, ev-000000000672)",
           "textures": {}}
    for name in ("S38", "S43", "S48", "S53"):
        out["textures"][name] = analyze(name)
    with open("results/harmonic_support.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    for name, r in out["textures"].items():
        print(name, "support m =", r["harmonic_support_m"],
              "CP-antisym:", r["cp_antisymmetry_exact"])
        for m, h in r["harmonics"].items():
            print("   m =", m, "->", h.get("leading_coefficient"))


if __name__ == "__main__":
    main()
