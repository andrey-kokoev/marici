"""Exact audit of the minimal faithful Gaussian readout completion."""

import json
from fractions import Fraction
from pathlib import Path


def determinant(q: Fraction, c: Fraction, p: Fraction) -> Fraction:
    return q * p - c * c


# Counterterm shear: Pi -> Pi + f zeta.
shear_tests = 0
for qn in range(1, 8):
    for cn in range(-5, 6):
        for pn in range(1, 9):
            q, c, p = Fraction(qn, 3), Fraction(cn, 4), Fraction(pn, 2)
            for fn in range(-3, 4):
                f = Fraction(fn, 5)
                c_new = c + f * q
                p_new = p + 2 * f * c + f * f * q
                assert determinant(q, c_new, p_new) == determinant(q, c, p)
                shear_tests += 1

# Intrinsic reconstruction from (P,S,Delta).
reconstruction_tests = 0
for nu_num in range(0, 13):
    nu = Fraction(nu_num, 4)
    for p_num in range(-6, 7):
        for y_num in range(-6, 7):
            anomalous_p = Fraction(p_num, 8)
            y = Fraction(y_num, 8)
            if anomalous_p**2 + y**2 > nu * (nu + 1):
                continue
            s = nu + y
            delta = nu * (nu + 1) - anomalous_p**2 - y**2
            assert s > Fraction(-1, 2)
            recovered_nu = (delta + anomalous_p**2 + s**2) / (2 * s + 1)
            recovered_y = s - recovered_nu
            assert recovered_nu == nu
            assert recovered_y == y
            reconstruction_tests += 1

packet = {
    "schema": "marici.symplectic-determinant-readout.v1",
    "counterterm_shear": "(q,c,p)->(q,c+fq,p+2fc+f^2q)",
    "determinant_invariant": "qp-c^2",
    "intrinsic_impurity": "Delta=nu(nu+1)-P^2-Y^2",
    "inverse_nu": "(Delta+P^2+S^2)/(2S+1)",
    "inverse_Y": "S-nu",
    "exact_shear_tests": shear_tests,
    "exact_reconstruction_tests": reconstruction_tests,
    "conclusion": "(P,S,Delta) is faithful on the complete positive one-mode Gaussian covariance space",
}

out = Path(__file__).parent / "results" / "symplectic-determinant-readout.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
