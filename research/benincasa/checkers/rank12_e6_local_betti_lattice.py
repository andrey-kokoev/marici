"""Integral Betti comparison for the two-sheet node and first-Rees e6 residue."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/rank12-e6-local-betti-lattice.json"

# Ordered sheet basis (e_+, e_-).  The physical boundary from Entry 1131 is
# d=e_- - e_+=(-1,+1).  A symmetric representative of the primitive dual
# reduced-H^0 class is eta=(-1/2,+1/2), so eta(d)=1.
d = (Fraction(-1), Fraction(1))
eta = (Fraction(-1, 2), Fraction(1, 2))
rho = (Fraction(-1, 8), Fraction(1, 8))

def pair(covector, chain):
    return sum(a * b for a, b in zip(covector, chain))

assert pair(eta, d) == 1
assert pair(rho, d) == Fraction(1, 4)
assert rho == tuple(Fraction(1, 4) * x for x in eta)

packet = {
    "schema": "marici.benincasa.rank12_e6_local_betti_lattice.v1",
    "sheet_order": ["e_plus", "e_minus"],
    "primitive_physical_boundary": ["-1", "1"],
    "primitive_dual_reduced_cohomology_symmetric_representative": ["-1/2", "1/2"],
    "primitive_pairing": "1",
    "first_rees_e6_covector": ["-1/8", "1/8"],
    "first_rees_physical_pairing": "1/4",
    "comparison": "rho_e6=(1/4)*eta",
    "integral_betti_lattice_inside_e6_rational_line": "Z*eta = 4*Z*rho_e6",
    "saturation_quotient": "Z*rho_e6 / Z*eta = Z/4",
    "topological_cohomology_has_torsion": False,
    "interpretation": "The local reduced Betti group is free. Z/4 is the lattice-index defect of the source-normalized e6 de Rham line, not torsion in the node cohomology.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))
