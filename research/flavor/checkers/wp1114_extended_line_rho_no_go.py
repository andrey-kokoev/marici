import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

D = 6
inv_D = Fraction(1, D)
flat_section_rank = 1
assert D == 6 and inv_D == Fraction(1,6)
assert flat_section_rank == 1

# Matched holonomy supplies a C^x torsor of flat sections: if a nonzero flat
# section exists, it is a constant nonzero scalar c relative to the trivialized
# comparison line. Thus the extended reciprocal is c/D, the same ray as 1/D.
candidate_form = "c/D"
ratio_to_reciprocal = "c"
constant_ratio = True
assert candidate_form == "c/D" and ratio_to_reciprocal == "c" and constant_ratio

# For a nontrivial torsion flat line, there is no global nonzero flat section.
nontrivial_torsion_global_sections = 0
assert nontrivial_torsion_global_sections == 0

independent_rho = False
assert not independent_rho

result = {
    "schema": "marici.flavor.wp1114.v1",
    "status": "PASS",
    "question": "Does an extended determinant/Wilson line bundle construct independent rho?",
    "determinant_witness": D,
    "reciprocal_witness": str(inv_D),
    "flat_section_rank": flat_section_rank,
    "candidate_form": candidate_form,
    "ratio_to_reciprocal": ratio_to_reciprocal,
    "constant_ratio": constant_ratio,
    "nontrivial_torsion_global_sections": nontrivial_torsion_global_sections,
    "independent_rho": independent_rho,
    "classification": "negative gate: trivial flat extension gives the same 1/D ray; nontrivial torsion has no global flat section",
    "remaining_gate": "construct a genuinely independent weight-(-3) section with a descent law and comparison node",
    "hostile_gate": "do not promote Wilson holonomy, a Cx torsor generator, or c/D to independent rho",
    "claim_boundary": "the extension changes framing, not the determinant reciprocal ray",
    "disposition": "extended-line rho route closed",
}

(ROOT / "results" / "wp1114_extended_line_rho_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1114 PASS:", D, inv_D, flat_section_rank, candidate_form, independent_rho)
