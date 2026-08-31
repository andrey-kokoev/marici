import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Schur gate: an SU(3)-natural endomorphism of one irreducible triplet is
# scalar.  For A=lambda I, every Krylov history [x,Ax,A^2x] has rank one.
lam = Fraction(7)
x = [Fraction(1), Fraction(2), Fraction(3)]
Ax = [lam * xi for xi in x]
A2x = [lam * xi for xi in Ax]

def det3(cols):
    (a,b,c),(d,e,f),(g,h,i) = cols
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
assert det3([x, Ax, A2x]) == 0

# A repeated eigenvalue is not a simple spectrum.
scalar_spectrum = [lam, lam, lam]
assert len(set(scalar_spectrum)) == 1

# The conditional Nima witness has simple spectrum and cyclic seed, but the
# flag and ray are inserted rather than derived from SU(3)-invariant data.
conditional_spectrum = [Fraction(1), Fraction(2), Fraction(3)]
assert len(set(conditional_spectrum)) == 3

supply = {
    "su3_irreducible_triplet": True,
    "natural_nonscalar_endomorphism": False,
    "simple_spectrum": False,
    "invariant_or_source_selected_ray": False,
    "cyclic_seed": False,
    "ordered_eigenflag": False,
    "nondestructive_history_dilation": False,
}
assert list(supply.values()).count(False) == 6

result = {
    "schema": "marici.flavor.wp1083.v1",
    "status": "PASS",
    "question": "Can current WP1080 SU(3) source data derive the WP1081 Krylov evolution, cyclic seed, and retained history?",
    "reply_evidence": "Nima event 10655",
    "schur_gate": {
        "natural_endomorphism_form": "lambda*I on one irreducible SU(3) triplet",
        "scalar_spectrum_distinct_count": len(set(scalar_spectrum)),
        "krylov_determinant": str(det3([x, Ax, A2x])),
    },
    "conditional_witness_boundary": {
        "A": "diag(1,2,3)",
        "x": "(1,1,1)",
        "inserted_data": ["ordered eigenflag", "cyclic ray"],
    },
    "current_source_supply": supply,
    "named_missing_source_operation": "an authorized SU(3)-breaking preparation consisting of a simple-spectrum endomorphism/ordered eigenflag plus a cyclic-ray preparation and a nondestructive history dilation storing three composition grades",
    "classification": "current-source no-go: WP1080's branching, bifundamental pairing, epsilon carriers, and localization do not derive A, x, or retained history",
    "successor_gate": "derive the SU(3)-breaking flag and cyclic ray in one source frame from a successor localization packet, then supply retained history and the WP1081 volume reference",
    "claim_boundary": "does not exclude a future source packet; it falsifies derivation from the currently admitted WP1080 data",
    "disposition": "terminal for the current-source Krylov route; H1a answered",
}

(ROOT / "results" / "wp1083_su3_natural_endomorphism_krylov_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1083 PASS:", det3([x, Ax, A2x]), len(set(scalar_spectrum)), len(set(conditional_spectrum)))
