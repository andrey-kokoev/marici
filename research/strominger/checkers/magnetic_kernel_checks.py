"""Finite-cutoff magnetic-kernel and exactness checker (marici.Strominger)."""
import json
import os
import sympy as sp

z, zb = sp.symbols("z zb")
u = z * zb
G0 = -2 * zb / (1 + u)
results = []


def simp(e):
    return sp.cancel(sp.together(sp.expand(e)))


def sigma(e):
    return e.subs([(z, zb), (zb, z)], simultaneous=True)


def chain(g, datum, barred=False):
    gamma = sigma(G0) if barred else G0
    variable = zb if barred else z
    value = datum
    for weight in range(2, g + 2):
        value = simp(sp.diff(value, variable) - weight * gamma * value)
    return value


def outputs(g, datum):
    f = chain(g, datum)
    fb = chain(g, sigma(datum), barred=True)
    electric = simp(f + fb)
    magnetic = simp(sp.diff(f, zb) - sp.diff(fb, z))
    return f, fb, electric, magnetic


def check(cid, group, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    results.append({"id": cid, "group": group, "statement": statement,
                    "status": status, "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


def kernel_matrix(expressions, coefficients):
    combined = simp(sum(c * e for c, e in zip(coefficients, expressions)))
    polynomial = sp.Poly(sp.fraction(combined)[0], z, zb)
    equations = [coefficient for _, coefficient in polynomial.terms()]
    return sp.linear_eq_to_matrix(equations, coefficients)[0]


# SPOR: the grade-local zb^-2 accident is isolated at grade 3.
for grade in range(1, 5):
    _, _, electric, magnetic = outputs(grade, zb ** -2)
    check(f"SPOR.g{grade}.E", "SPOR", f"E is nonzero for zb^-2 at g={grade}",
          electric != 0)
    check(f"SPOR.g{grade}.M", "SPOR",
          f"M vanishes for zb^-2 iff g=3 in grades 1..4",
          (magnetic == 0) == (grade == 3))


# KER: exact QQ kernel on the preregistered 27-dimensional monomial grid.
basis = [z ** (-a) * zb ** m for a in (0, 2, 4) for m in range(-4, 5)]
labels = [(a, m) for a in (0, 2, 4) for m in range(-4, 5)]
coefficients = sp.symbols(f"c0:{len(basis)}")
expected = {
    2: [zb ** -1, 1 - zb ** -2, z ** -2 * zb ** -3],
    3: [zb ** -2, z ** -2 * zb ** -4],
}
kernel_data = {}
for grade in (2, 3):
    magnetic_images = [outputs(grade, datum)[3] for datum in basis]
    matrix = kernel_matrix(magnetic_images, coefficients)
    nullspace = matrix.nullspace()
    # Convert named expected data into coordinate vectors by Laurent-term lookup.
    expected_vectors = []
    for datum in expected[grade]:
        terms = sp.Add.make_args(sp.expand(datum))
        vector = []
        for term in basis:
            coefficient = sp.Integer(0)
            for summand in terms:
                ratio = simp(summand / term)
                if not ratio.has(z, zb):
                    coefficient += ratio
            vector.append(coefficient)
        expected_vectors.append(sp.Matrix(vector))
    span_rank = sp.Matrix.hstack(*(nullspace + expected_vectors)).rank()
    check(f"KER.g{grade}.rank", "KER", f"M map has rank {len(basis)-len(expected[grade])} at g={grade}",
          matrix.rank() == len(basis) - len(expected[grade]), f"matrix={matrix.rows}x{matrix.cols}")
    check(f"KER.g{grade}.basis", "KER", f"named data span the full M kernel at g={grade}",
          len(nullspace) == len(expected_vectors) and span_rank == len(nullspace),
          str(expected[grade]))
    kernel_data[grade] = expected[grade]


# EX/RAT: closedness gives a local potential; rational exactness has residue gates.
rational_potentials = {
    (2, 0): -20 / (1 + u),
    (2, 1): -20 * (z + zb) / (1 + u),
    (3, 0): -60 / (1 + u) ** 2,
}
for grade, data in kernel_data.items():
    for index, datum in enumerate(data):
        f, fb, _, magnetic = outputs(grade, datum)
        potential = sp.integrate(f, z)
        correction = simp(sp.diff(potential, zb) - fb)
        repairable = simp(sp.diff(correction, z)) == 0
        if repairable:
            potential = simp(potential - sp.integrate(correction, zb))
        exact = simp(sp.diff(potential, z) - f) == 0 and simp(sp.diff(potential, zb) - fb) == 0
        check(f"EX.g{grade}.k{index}", "EX", "kernel line has a local elementary gradient potential",
              magnetic == 0 and repairable and exact)
        residues = [simp(sp.residue(f, z, pole)) for pole in (0, -1 / zb)]
        if (grade, index) in rational_potentials:
            phi = rational_potentials[(grade, index)]
            rational_exact = simp(sp.diff(phi, z) - f) == 0 and simp(sp.diff(phi, zb) - fb) == 0
            check(f"RAT.g{grade}.k{index}", "RAT", "rational kernel line has certified rational potential",
                  rational_exact, str(phi))
        else:
            check(f"RAT.g{grade}.k{index}", "RAT", "logarithmic kernel line is not rational-exact",
                  any(residue != 0 for residue in residues), f"residues={residues}")


# FAIL: deliberate nonkernel controls exhibit the promised obstruction.
for grade in (2, 3):
    magnetic = outputs(grade, sp.Integer(1))[3]
    check(f"FAIL.g{grade}", "FAIL", "constant datum is a deliberate nonclosed control",
          magnetic != 0)

passes = [item for item in results if item["status"] == "pass"]
fails = [item for item in results if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_kernel_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "finite-cutoff theorem", "grades": [2, 3],
              "grid": {"a": [0, 2, 4], "m": [-4, 4], "dimension": 27}},
    "checks": results, "n_pass": len(passes), "n_fail": len(fails),
    "verdict": "On the declared 27-dimensional monomial grid, ker(M) has dimension 3 at g=2 and 2 at g=3. Every kernel pair is locally an elementary gradient. The rational-exact subkernel has dimension 2 at g=2 and 1 at g=3; the remaining line at each grade has nonzero opposite residues at z=0 and z=-1/zb and therefore requires logarithms. Magnetic-zero is closedness exactly, but rational pure gauge is a proper subspace.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_kernel.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passes)} passed, {len(fails)} failed", flush=True)
raise SystemExit(1 if fails else 0)
