import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Distinct Wilson eigenvalues stand in for a generic source-fixed 1+1+1 flag.
lam = [Fraction(2), Fraction(3), Fraction(5)]

def det3(cols):
    (a,b,c),(d,e,f),(g,h,i) = cols
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def krylov_det(x):
    Ax = [l*v for l,v in zip(lam,x)]
    A2x = [l*v for l,v in zip(lam,Ax)]
    return det3([x,Ax,A2x])

# A single eigenline is source-selected by the flag, but is never cyclic.
e1 = [Fraction(1), Fraction(0), Fraction(0)]
assert krylov_det(e1) == 0

# A coherent vector is cyclic exactly when all eigencomponents are nonzero.
x = [Fraction(1), Fraction(2), Fraction(3)]
omega = krylov_det(x)
vandermonde = ((lam[1]-lam[0])*(lam[2]-lam[0])*(lam[2]-lam[1]))
assert omega == vandermonde * x[0] * x[1] * x[2]
assert omega != 0

# The flag does not choose the component amplitudes or relative phases; a
# residual U(1) changes the relative phases of the two Wilson lines.
supply = {
    "three_distinct_eigenlines": True,
    "simple_spectrum": True,
    "selected_eigenline": True,
    "cyclic_eigenline": False,
    "coherent_amplitude_ratios": False,
    "coherent_relative_phases": False,
    "nondestructive_history": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1086.v1",
    "status": "PASS",
    "question": "Does a source-fixed Wilson 1+1+1 flag by itself select a cyclic Krylov ray and history?",
    "wilson_flag": {
        "eigenvalues": [str(v) for v in lam],
        "vandermonde": str(vandermonde),
    },
    "krylov_witnesses": {
        "single_eigenline_determinant": str(krylov_det(e1)),
        "coherent_x": [str(v) for v in x],
        "coherent_determinant": str(omega),
        "formula": "det[x,Ax,A^2x]=(lambda2-lambda1)(lambda3-lambda1)(lambda3-lambda2)*x1*x2*x3",
    },
    "flag_supply": supply,
    "classification": "conditional flag no-go for the ray: a Wilson 1+1+1 flag supplies simple spectrum but no cyclic ray; every source-selected eigenline has zero Krylov determinant",
    "remaining_gate": "derive a coherent-ray preparation fixing nonzero amplitude ratios and relative phases, then derive nondestructive history dilation and the volume reference rho",
    "hostile_gate": "do not promote a three-line Wilson flag to a cyclic ray, coherent seed, or history",
    "claim_boundary": "assumes the WP1085 Wilson line is source-fixed; without that assumption the flag itself is also conditional",
    "disposition": "productive: separates eigenflag construction from cyclic-ray preparation",
}

(ROOT / "results" / "wp1086_wilson_flag_cyclic_ray_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1086 PASS:", krylov_det(e1), omega, vandermonde)
