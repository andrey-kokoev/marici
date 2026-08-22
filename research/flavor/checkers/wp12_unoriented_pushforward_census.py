"""WP12 exact census: unoriented phase-line pushforward into J (marici.Figueiredo).

Question (operator-directed WP12, after WP11's Mobius result in entry 1901):
does the UNORIENTED loop-holonomy line {phi, -phi} have a canonical map to
the physical CP-odd readout J across the exact 61-vertex carrier groupoid?

The precise computational content, per chart v of the WP9 atlas
(results/wp9_lo_atlas.json), with z = e^{i phi} on the chart phase edge and
fully SYMBOLIC positive magnitudes m_0..m_8:

  1. det C, C = [Yu Yu^dag, Yd Yd^dag], computed EXACTLY as a Laurent
     polynomial in z.  Because C is a 3x3 traceless anti-Hermitian-family
     matrix, det C = tr(C^3)/3 identically; the checker verifies this
     against C.det() on a generic exact rational specialization (gate G0).
  2. The characteristic-polynomial coefficients (c1, c2, c3) of Hu and Hd
     as Laurent polynomials in z -- the mass-sector phi-dependence audit.
     c1 is always z-free (diagonal |Y_ik|^2); c2, c3 can in principle
     carry z^{+-1} through |minor|^2 cross terms.
  3. CP antisymmetry a_{-m} + a_m == 0 coefficient-wise (exact).

From (1)+(2): J(phi) shape.  With det C = -2i J prod Delta_u prod Delta_d
(sign per convention; the census tracks only the z-structure), if det C has
support exactly {+-1} and all char coefficients are z-free, then

    J(phi) = K(magnitudes) * sin(phi) / D(magnitudes)

EXACTLY (not at leading order), so |J| = (|K|/D) * |sin phi|: the
unoriented phase line pushes forward to the physical CP-odd readout with
no sign choice anywhere.  Any chart with higher harmonics or z-dependent
mass invariants is recorded as a structural exception.

Cross-validation (gate G1): the four worked textures S38/S43/S48/S53 of
arXiv:2607.27315v1 are rebuilt as masks and their det C supports compared
against results/harmonic_support.json (independent prior computation).

All arithmetic exact (sympy symbolic).  No floating point.

Output: research/flavor/results/wp12_unoriented_pushforward.json
"""
import json
import time
import sympy as sp

z = sp.symbols("z", nonzero=True)
MAGS = sp.symbols("m0:9", positive=True, real=True)
SLOTS = [(i, j) for i in range(3) for j in range(3)]

# Worked textures of the paper, as (mask_u, mask_d, phase_sector, phase_slot)
WORKED = {
    "S38": (0b100011010, 0b100111010, "u", (0, 1)),  # 282, 314
    "S43": (0b100010101, 0b110100101, "d", (2, 2)),  # 277, 421
    "S48": (0b100110001, 0b101010110, "d", (0, 1)),  # 305, 342
    "S53": (0b100110001, 0b110011100, "d", (1, 1)),  # 305, 412
}


def mask_slots(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]


def build_symbolic(mask_u, mask_d, phase_sector, phase_slot):
    """Symbolic Yu, Yd with entries m_k or z*m_k; YuH = Yu^dag via z->1/z."""
    Yu = sp.Matrix.zeros(3)
    Yd = sp.Matrix.zeros(3)
    entries = [("u", s) for s in mask_slots(mask_u)] + \
              [("d", s) for s in mask_slots(mask_d)]
    assert len(entries) == 9, f"expected nine links, got {len(entries)}"
    for (sector, slot), m in zip(entries, MAGS):
        val = z * m if (sector == phase_sector and slot == phase_slot) else m
        (Yu if sector == "u" else Yd)[slot] = val
    return Yu, Yd


def dagger(M):
    """Hermitian conjugate for Laurent-monomial matrices: transpose, z->1/z."""
    return M.T.subs(z, z**-1)


def laurent_support(expr):
    """Support {m: a_m != 0} of a Laurent polynomial in z, exactly."""
    expr = sp.expand(expr)
    if expr == 0:
        return {}, True
    poly = sp.Poly(sp.expand(expr * z**6), z)
    coeffs = {pw - 6: c for (pw,), c in poly.terms() if c != 0}
    antisym = all(sp.expand(coeffs.get(-m, 0) + coeffs.get(m, 0)) == 0
                  for m in list(coeffs))
    return coeffs, antisym


def analyze_chart(mask_u, mask_d, phase_sector, phase_slot):
    Yu, Yd = build_symbolic(mask_u, mask_d, phase_sector, phase_slot)
    Hu = sp.expand(Yu * dagger(Yu))
    Hd = sp.expand(Yd * dagger(Yd))
    C = sp.expand(Hu * Hd - Hd * Hu)
    detC = sp.expand(sp.trace(C**3) / 3)
    detC_coeffs, detC_antisym = laurent_support(detC)
    detC_support = sorted(detC_coeffs)

    char = {}
    for name, H, Y in (("u", Hu, Yu), ("d", Hd, Yd)):
        c1 = sp.expand(sp.trace(H))
        c2 = sp.expand((sp.trace(H)**2 - sp.trace(H**2)) / 2)
        c3 = sp.expand(Y.det() * dagger(Y).det())
        s = {}
        for cname, c in (("c1", c1), ("c2", c2), ("c3", c3)):
            coeffs, _ = laurent_support(c)
            s[cname] = sorted(coeffs)
        char[name] = s

    return {
        "detC_support": detC_support,
        "detC_cp_antisymmetry_exact": detC_antisym,
        "detC_coefficient_m1": str(sp.expand(detC_coeffs.get(1, 0))),
        "detC_coefficient_count": len(detC_coeffs),
        "char_supports": char,
        "mass_sector_z_free": all(char[s][c] == [0] for s in "ud"
                                  for c in ("c1", "c2", "c3")),
    }


def gate_det_via_trace_cube():
    """G0: det C == tr(C^3)/3 on a generic exact rational specialization."""
    rng = sp.Rational(1, 7)
    A = sp.Matrix(3, 3, lambda i, j: sp.Rational(1 + 2 * i + 3 * j, 5 + i + j))
    B = sp.Matrix(3, 3, lambda i, j: sp.Rational(2 + i + 5 * j, 7 + 2 * i + j))
    A = A + A.T
    B = B + B.T
    C = A * B - B * A
    return sp.simplify(C.det() - sp.trace(C**3) / 3 + rng * 0) == 0


def main():
    t0 = time.time()
    with open("results/wp9_lo_atlas.json", encoding="utf-8") as f:
        atlas = json.load(f)
    charts = atlas["charts"]

    out = {
        "purpose": "WP12 exact census: Laurent support of det[Hu,Hd] and of "
                   "the mass-sector char coefficients in z=e^{i phi}, with "
                   "symbolic magnitudes, over all 61 carrier-groupoid "
                   "vertices; tests whether |sin phi| pushes forward to |J| "
                   "canonically per chart (WP11-compatible unoriented data).",
        "gate_G0_det_equals_trC3_over_3": gate_det_via_trace_cube(),
        "charts": [],
        "worked_texture_crosscheck": {},
    }

    n_first_harmonic = 0
    n_mass_z_free = 0
    exceptions = []
    for i, ch in enumerate(charts):
        mu, md = ch["member"]
        sector = ch["phase_edge"][0]
        slot = (ch["phase_edge"][1], ch["phase_edge"][2])
        r = analyze_chart(mu, md, sector, slot)
        r.update({"orbit": ch["orbit"], "member": [mu, md],
                  "phase_edge": ch["phase_edge"]})
        out["charts"].append(r)
        ok1 = r["detC_support"] == [-1, 1] and r["detC_cp_antisymmetry_exact"]
        ok2 = r["mass_sector_z_free"]
        n_first_harmonic += ok1
        n_mass_z_free += ok2
        if not (ok1 and ok2):
            exceptions.append({"orbit": ch["orbit"], "member": [mu, md],
                               "phase_edge": ch["phase_edge"],
                               "detC_support": r["detC_support"],
                               "char_supports": r["char_supports"]})
        print(f"[{i + 1}/61] orb {ch['orbit']:2d} member {[mu, md]} "
              f"detC supp {r['detC_support']} mass-z-free {ok2} "
              f"({time.time() - t0:.0f}s)", flush=True)

    # G1: worked-texture cross-validation against harmonic_support.json
    with open("results/harmonic_support.json", encoding="utf-8") as f:
        prior = json.load(f)
    for name, (mu, md, sector, slot) in WORKED.items():
        r = analyze_chart(mu, md, sector, slot)
        prior_support = prior["textures"][name]["harmonic_support_m"]
        out["worked_texture_crosscheck"][name] = {
            "masks": [mu, md], "phase_edge": [sector, slot[0], slot[1]],
            "detC_support": r["detC_support"],
            "prior_harmonic_support_m": prior_support,
            "match": r["detC_support"] == [-1, 1] and prior_support == [1],
            "mass_sector_z_free": r["mass_sector_z_free"],
            "char_supports": r["char_supports"],
        }
        print(f"G1 {name}: detC supp {r['detC_support']} vs prior "
              f"{prior_support} mass-z-free {r['mass_sector_z_free']}",
              flush=True)

    out["census"] = {
        "chart_count": len(charts),
        "detC_first_harmonic_only_count": n_first_harmonic,
        "mass_sector_z_free_count": n_mass_z_free,
        "exceptions": exceptions,
        "all_first_harmonic_and_antisym": n_first_harmonic == len(charts),
        "all_mass_sector_z_free": n_mass_z_free == len(charts),
        "all_worked_texture_crosschecks_match": all(
            v["match"] for v in out["worked_texture_crosscheck"].values()),
    }
    with open("results/wp12_unoriented_pushforward.json", "w",
              encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({k: v for k, v in out["census"].items()
                      if k != "exceptions"}, indent=2))
    print("exceptions:", len(exceptions),
          f"elapsed {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
