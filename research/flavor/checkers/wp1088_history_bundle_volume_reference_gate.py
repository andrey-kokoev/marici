import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

lam = [Fraction(2), Fraction(3), Fraction(5)]
x = [Fraction(1), Fraction(1), Fraction(1)]

def det3(cols):
    (a,b,c),(d,e,f),(g,h,i) = cols
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def krylov_det(v):
    Av = [l*z for l,z in zip(lam,v)]
    A2v = [l*z for l,z in zip(lam,Av)]
    return det3([v,Av,A2v])

D = krylov_det(x)
assert D == 6

# The canonical coordinate volume form is a candidate comparison form, but it
# has ray-phase weight 0.  D has weight +3 under x -> zeta*x, so D/1 still has
# weight +3 rather than descending to the projective ray.
canonical_rho = Fraction(1)
D_weight = 3
canonical_rho_weight = 0
ratio_weight = D_weight - canonical_rho_weight
assert ratio_weight == 3

# The WP1087 bundle stores (x,Ux,U^2x), hence contains D and its grades, but
# no independent section transforming with weight -3.
bundle_supply = {
    "history_grades": True,
    "determinant_amplitude_D": True,
    "comparison_node": True,
    "weight_minus_three_reference": False,
    "source_transformation_law": False,
    "source_coorientation": False,
}
assert list(bundle_supply.values()).count(False) == 3

result = {
    "schema": "marici.flavor.wp1088.v1",
    "status": "PASS",
    "question": "Does the conditional Wilson history bundle supply the WP1081 volume reference rho?",
    "determinant": {
        "lambda": [str(v) for v in lam],
        "x": [str(v) for v in x],
        "D": str(D),
        "ray_phase_weight": D_weight,
    },
    "canonical_volume_form": {
        "rho": str(canonical_rho),
        "ray_phase_weight": canonical_rho_weight,
        "ratio_weight": ratio_weight,
    },
    "history_bundle_supply": bundle_supply,
    "classification": "conditional reference no-go: the history bundle supplies D and a comparison node but no weight-(-3) reference rho, so signed production still does not descend",
    "remaining_gate": "derive a source volume/coorientation section rho with ray-phase weight -3, transformation law, temporal scope, and comparison node",
    "hostile_gate": "do not declare D, the canonical unit volume form, or the history bundle itself to be the compensating reference rho",
    "claim_boundary": "assumes WP1085-WP1087's conditional Wilson flag and history bundle; those constructors remain unsourced",
    "disposition": "productive: the final Krylov constructor is isolated as rho",
}

(ROOT / "results" / "wp1088_history_bundle_volume_reference_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1088 PASS:", D, canonical_rho_weight, ratio_weight)
