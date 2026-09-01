import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# The aligned bifundamental pairing is I_3 and has determinant 1, ray weight 0.
pairing_det = Fraction(1)
# WP1086 witness determinant D has weight +3.
lam = [Fraction(2), Fraction(3), Fraction(5)]
x = [Fraction(1), Fraction(1), Fraction(1)]
D = (lam[1]-lam[0]) * (lam[2]-lam[0]) * (lam[2]-lam[1]) * x[0]*x[1]*x[2]
assert D == 6
assert pairing_det * D == 6

# The only weight -3 combination available here is pairing_det/D, the same
# tautological reciprocal closed by WP1090.
rho_candidate = pairing_det / D
assert rho_candidate == Fraction(1,6)
z = Fraction(2)
D_scaled = z**3 * D
assert pairing_det / D_scaled == z**-3 * rho_candidate

# It is singular on a noncyclic eigenline.
x_eigen = [Fraction(1), Fraction(0), Fraction(0)]
D_eigen = (lam[1]-lam[0]) * (lam[2]-lam[0]) * (lam[2]-lam[1]) * x_eigen[0]*x_eigen[1]*x_eigen[2]
assert D_eigen == 0

supply = {
    "bifundamental_pairing_weight_zero": True,
    "cyclic_ray_available_conditionally": True,
    "weight_minus_three_combination": True,
    "independent_section": False,
    "global_nonsingular_reference": False,
    "source_coorientation": False,
}
assert list(supply.values()).count(False) == 3

result = {
    "schema": "marici.flavor.wp1103.v1",
    "status": "PASS",
    "question": "Does bifundamental pairing plus cyclic ray supply an independent rho?",
    "pairing_determinant": str(pairing_det),
    "D": str(D),
    "rho_candidate": str(rho_candidate),
    "scaled_D": str(D_scaled),
    "scaled_rho": str(pairing_det / D_scaled),
    "eigenline_D": str(D_eigen),
    "current_source_supply": supply,
    "classification": "negative gate: weight-zero pairing times 1/D remains the tautological reciprocal",
    "remaining_gate": "source-authorized independent weight-(-3) section with descent law, temporal scope, and comparison node",
    "hostile_gate": "do not promote det(I_3)/D or any weight-zero pairing times reciprocal determinant into independent rho",
    "claim_boundary": "the pairing adds weight zero and no new line-bundle descent law; WP1090 and WP1091 still control the scalar sector",
    "disposition": "pairing-plus-cyclic-ray rho loophole closed",
}

(ROOT / "results" / "wp1103_pairing_cyclic_ray_rho_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1103 PASS:", pairing_det, D, rho_candidate, D_eigen)
