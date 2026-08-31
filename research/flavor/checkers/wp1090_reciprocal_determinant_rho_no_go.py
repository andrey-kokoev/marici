import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1086 witness: simple spectrum and a cyclic ray.
lam = [Fraction(2), Fraction(3), Fraction(5)]
x = [Fraction(1), Fraction(1), Fraction(1)]
# det[x,Ax,A^2x] = (lam2-lam1)(lam3-lam1)(lam3-lam2) x1 x2 x3.
D = (lam[1] - lam[0]) * (lam[2] - lam[0]) * (lam[2] - lam[1]) * x[0] * x[1] * x[2]
assert D == Fraction(6)
rho = Fraction(1) / D
assert D * rho == 1

# Integer scaling witness: D has weight +3 and 1/D has weight -3.
z = Fraction(2)
D_scaled = z**3 * D
rho_scaled = z**-3 * rho
assert D_scaled == Fraction(48)
assert rho_scaled == Fraction(1, 48)
assert D_scaled * rho_scaled == 1

# The reciprocal is undefined on a noncyclic eigenline, so it is not a global
# nonsingular reference over rays.
x_eigen = [Fraction(1), Fraction(0), Fraction(0)]
D_eigen = (lam[1] - lam[0]) * (lam[2] - lam[0]) * (lam[2] - lam[1]) * x_eigen[0] * x_eigen[1] * x_eigen[2]
assert D_eigen == 0

supply = {
    "weight_minus_three_on_cyclic_domain": True,
    "tautological_inverse_relation": True,
    "defined_on_eigenline": False,
    "independent_source_section": False,
    "global_nonsingular_reference": False,
    "source_coorientation": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1090.v1",
    "status": "PASS",
    "question": "Can the reciprocal Krylov determinant 1/D(x) serve as the missing weight-(-3) reference rho?",
    "witness": {
        "spectrum": [str(v) for v in lam],
        "cyclic_ray": [str(v) for v in x],
        "D": str(D),
        "rho_reciprocal": str(rho),
        "scaled_D": str(D_scaled),
        "scaled_rho": str(rho_scaled),
        "eigenline_D": str(D_eigen),
    },
    "current_source_supply": supply,
    "classification": "negative gate: reciprocal determinant is a tautological meromorphic inverse, not an independent source-authorized rho",
    "remaining_gate": "source-authorized independent weight-(-3) section rho with stated line bundle, descent law, temporal scope, and comparison node",
    "hostile_gate": "do not promote 1/D(x), its pole-free cyclic domain, or D*rho=1 into an independent coorientation or global reference section",
    "claim_boundary": "the reciprocal has the requested homogeneity only where D is nonzero; it vanishes as a candidate precisely at noncyclic rays and carries no source authority",
    "disposition": "reciprocal-determinant loophole closed",
}

(ROOT / "results" / "wp1090_reciprocal_determinant_rho_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1090 PASS:", D, rho, D_scaled, rho_scaled, D_eigen)
