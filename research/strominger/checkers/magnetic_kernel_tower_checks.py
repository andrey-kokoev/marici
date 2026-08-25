"""Expanded finite-cutoff magnetic-kernel tower checker."""
import json
import os
import sympy as sp

z, zb = sp.symbols("z zb")
u = z * zb
G0 = -2 * zb / (1 + u)
checks = []


def simp(value):
    return sp.cancel(sp.together(sp.expand(value)))


def sigma(value):
    return value.subs([(z, zb), (zb, z)], simultaneous=True)


def chain(grade, datum, barred=False):
    gamma = sigma(G0) if barred else G0
    variable = zb if barred else z
    value = datum
    for weight in range(2, grade + 2):
        value = simp(sp.diff(value, variable) - weight * gamma * value)
    return value


def fold_pair(grade, datum):
    return chain(grade, datum), chain(grade, sigma(datum), barred=True)


def magnetic(grade, datum):
    f, fb = fold_pair(grade, datum)
    return simp(sp.diff(f, zb) - sp.diff(fb, z))


def record(cid, group, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "group": group, "statement": statement,
                   "status": status, "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


def coordinate_vector(datum, basis):
    vector = []
    terms = sp.Add.make_args(sp.expand(datum))
    for basis_term in basis:
        coefficient = sp.Integer(0)
        for summand in terms:
            ratio = simp(summand / basis_term)
            if not ratio.has(z, zb):
                coefficient += ratio
        vector.append(coefficient)
    return sp.Matrix(vector)


def image_matrix(images, coefficients):
    combined = simp(sum(c * image for c, image in zip(coefficients, images)))
    numerator = sp.Poly(sp.fraction(combined)[0], z, zb)
    equations = [coefficient for _, coefficient in numerator.terms()]
    return sp.linear_eq_to_matrix(equations, coefficients)[0]


# The source space is fixed before comparison: 42 labelled monomials.
basis = [z ** (-a) * zb ** m for a in (0, 2, 4) for m in range(-9, 5)]
coefficients = sp.symbols(f"c0:{len(basis)}")
rational_coefficients = {2: 20, 3: 60, 4: 280, 5: 1680}

for grade in (2, 3, 4, 5):
    tower = [z ** (-a) * zb ** (-(grade + a - 1)) for a in (0, 2, 4)]
    expected = list(tower)
    if grade == 2:
        expected.insert(1, 1 - zb ** -2)

    images = [magnetic(grade, datum) for datum in basis]
    matrix = image_matrix(images, coefficients)
    nullspace = matrix.nullspace()
    expected_vectors = [coordinate_vector(datum, basis) for datum in expected]
    joined_rank = sp.Matrix.hstack(*(nullspace + expected_vectors)).rank()
    record(f"GRID.g{grade}.rank", "GRID",
           f"expanded-grid kernel dimension is {len(expected)} at g={grade}",
           matrix.rank() == len(basis) - len(expected),
           f"matrix={matrix.rows}x{matrix.cols}")
    record(f"GRID.g{grade}.basis", "GRID",
           f"named lines span the full expanded-grid kernel at g={grade}",
           len(nullspace) == len(expected) and joined_rank == len(nullspace))

    for a, datum in zip((0, 2, 4), tower):
        f, fb = fold_pair(grade, datum)
        obstruction = simp(sp.diff(f, zb) - sp.diff(fb, z))
        record(f"TOWER.g{grade}.a{a}", "TOWER",
               f"D=z^-{a} zb^-({grade}+{a}-1) lies in ker(M)",
               obstruction == 0)
        if a == 0:
            phi = -rational_coefficients[grade] / (1 + u) ** (grade - 1)
            record(f"RAT.g{grade}.a0", "RAT",
                   "a=0 tower line has the displayed rational potential",
                   simp(sp.diff(phi, z) - f) == 0 and
                   simp(sp.diff(phi, zb) - fb) == 0, str(phi))
        else:
            residues = [simp(sp.residue(f, z, pole))
                        for pole in (0, -1 / zb)]
            record(f"RES.g{grade}.a{a}", "RES",
                   f"a={a} tower line has a nonzero opposite residue pair",
                   residues[0] != 0 and residues[0] + residues[1] == 0,
                   str(residues))

    # The two positive-depth residues occupy the same divisor line.  Their
    # weighted difference is rational-exact; individual nonzero residues do
    # not imply two independent cohomology classes.
    residue_a2 = -grade * (grade + 1) * sp.catalan(grade + 1) * sp.rf(2, grade - 1)
    residue_a4 = -grade * (grade + 1) * sp.catalan(grade + 1) * sp.rf(4, grade - 1)
    relative = residue_a4 * tower[1] - residue_a2 * tower[2]
    relative_f, relative_fb = fold_pair(grade, relative)
    relative_phi = simp(sp.integrate(relative_f, z))
    record(f"RATCOMB.g{grade}", "RATCOMB",
           "the residue-cancelling positive-depth combination is rational-exact",
           not relative_phi.has(sp.log) and
           simp(sp.diff(relative_phi, z) - relative_f) == 0 and
           simp(sp.diff(relative_phi, zb) - relative_fb) == 0)

    neighbor = z ** -2 * zb ** (-grade)
    record(f"FAIL.g{grade}", "FAIL",
           "neighboring exponent is a deliberate nonkernel control",
           magnetic(grade, neighbor) != 0)


# The isolated grade-2 extra line is rational-exact.
extra = 1 - zb ** -2
f_extra, fb_extra = fold_pair(2, extra)
phi_extra = -20 * (z + zb) / (1 + u)
record("EXC.g2.closed", "EXC", "grade-2 exceptional combination lies in ker(M)",
       magnetic(2, extra) == 0)
record("EXC.g2.rational", "EXC", "grade-2 exceptional line is rational-exact",
       simp(sp.diff(phi_extra, z) - f_extra) == 0 and
       simp(sp.diff(phi_extra, zb) - fb_extra) == 0, str(phi_extra))

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_kernel_tower_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "finite-cutoff theorem", "grades": [2, 3, 4, 5],
              "grid": {"a": [0, 2, 4], "m": [-9, 4], "dimension": 42}},
    "checks": checks, "n_pass": len(passed), "n_fail": len(failed),
    "verdict": "On the expanded 42-dimensional Laurent grid, ker(M_g) is spanned by D_{g,a}=z^-a zb^{-(g+a-1)} for a=0,2,4 at every tested grade g=2..5, plus one exceptional rational-exact line 1-zb^-2 at g=2. Thus kernel dimensions are (4,3,3,3). The a=0 tower and the exception are rational-exact. The a=2 and a=4 towers are individually nonexact, but their weighted zero-residue combination is rational-exact; hence the ordinary rational quotient has dimension one, not two.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_kernel_tower.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
