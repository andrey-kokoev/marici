import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).parents[1]
wp503 = json.loads((ROOT/"results"/"wp503_noncollinear_entrance_vacuum.json").read_text())
wp505 = json.loads((ROOT/"results"/"wp505_complex_entrance_kernel_closure.json").read_text())
ensemble = json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())

assert wp503["passed"]
assert wp505["passed"]

u = sp.symbols("u0:6", real=True)
d = sp.symbols("d0:6", real=True)
Hu = sp.Matrix([[u[0], u[1], u[2]], [u[1], u[3], u[4]], [u[2], u[4], u[5]]])
Hd = sp.Matrix([[d[0], d[1], d[2]], [d[1], d[3], d[4]], [d[2], d[4], d[5]]])
C = sp.expand(Hu*Hd-Hd*Hu)

assert C.T == -C
assert all(C[i, i] == 0 for i in range(3))
assert sp.factor(C.det()) == 0

# Noncollinearity can produce mixing without CP violation.
A = sp.diag(1, 2, 4)
B = sp.Matrix([[3, 1, 0], [1, 5, 1], [0, 1, 7]])
C_real = A*B-B*A
assert C_real != sp.zeros(3)
assert C_real.rank() == 2
assert C_real.det() == 0
assert sp.discriminant(A.charpoly().as_expr(), A.charpoly().gen) != 0
assert sp.discriminant(B.charpoly().as_expr(), B.charpoly().gen) != 0

Js = [sp.Rational(str(record["J"])) for record in ensemble["records"]]
assert len(Js) == 1210
assert all(value != 0 for value in Js)

# Deliberate-failure test: leaving the real CP-even source domain permits a
# complex Hermitian pair with a nonzero CP-odd determinant.
t = sp.Rational(6, 5)
X = sp.diag(-1, 0, 1)
Y = sp.Matrix([[0, 1, -sp.I*t], [1, 0, 1], [sp.I*t, 1, 0]])
complex_obstruction = sp.factor((X*Y-Y*X).det())
assert complex_obstruction == 24*sp.I/5
assert complex_obstruction != 0

result = {
    "schema": "marici.flavor.wp1016.v1",
    "status": "PASS",
    "source_domain": "WP503 real CP-even two-entrance vacuum, with WP505 neutral complex-kernel closure retaining a real orthogonal vacuum",
    "source_constraints": "two nonzero orthogonal entrance directions; independent norms remain inputs",
    "gram_domain": "real symmetric positive nondegenerate 3x3 pairs",
    "weak_basis_descent": "CP-even real form is preserved by the admitted real row group; physical J=0 statement descends under full weak basis",
    "proper_image": "CP-conserving physical quotient locus J=0",
    "mixing_capacity": "noncommuting rank-two real antisymmetric commutator is possible",
    "ensemble_sheets_tested": len(Js),
    "ensemble_sheets_surviving": sum(value == 0 for value in Js),
    "contextual_partition": "noncommuting CP-even source class versus 1210 fitted CP-violating sheets",
    "classification": "source-derived noncollinearity selector and rigidifier, but CP selector is experimentally falsified",
    "smallest_exact_falsifier": {
        "removed_gate": "real CP-even source domain",
        "complex_pair_commutator_determinant": str(complex_obstruction),
    },
    "instrument": "existing signed Jarlskog/CKM readout",
    "claim_boundary": "neutral entrance theorem only; no charged-sector completion, pole instrument, or source-derived CP-odd phase is supplied",
    "remaining_gate": "derive a complex CP-odd entrance invariant and its phase minimum without inserting the fitted CKM phase or a reference port",
}

out = ROOT/"results"/"wp1016_two_entrance_cp_even_no_go.json"
out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print("WP1016 PASS: two real entrances allow mixing but still select J=0")
