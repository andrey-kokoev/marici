#!/usr/bin/env python3
"""Certify the full helicity observer and its physical reflection quotient."""

import json
from pathlib import Path

import sympy as sp


Q_occ = sp.Matrix([[1,2,0],[1,-1,-1],[1,-1,1]])
B_pol = sp.Matrix([[1,1],[1,-1]])  # (h+,h-) -> (even,odd)
swap = sp.Matrix([[0,1],[1,0]])
parity_out = sp.diag(1,-1)

full_observer = sp.kronecker_product(Q_occ, B_pol)
deck_in = sp.kronecker_product(sp.eye(3), swap)
deck_out = sp.kronecker_product(sp.eye(3), parity_out)
assert Q_occ.det() == -6
assert B_pol.det() == -2
assert full_observer.rank() == 6
assert full_observer.det() == -288
assert full_observer*deck_in == deck_out*full_observer

# The physical loop cycle is invariant under internal reflection.  Its
# coefficient domain is therefore the coinvariant quotient.  Use the exact
# even inclusion and averaging retraction to model that quotient.
even_inclusion = sp.kronecker_product(sp.eye(3), sp.Matrix([1,1]))
even_average = sp.kronecker_product(sp.eye(3), sp.Matrix([[sp.Rational(1,2),sp.Rational(1,2)]]))
assert even_average*even_inclusion == sp.eye(3)
assert (deck_in-sp.eye(6))*even_inclusion == sp.zeros(6,3)
assert even_average*(deck_in-sp.eye(6)) == sp.zeros(3,6)

# Select the even polarization component after the full analyzer.
even_output = sp.kronecker_product(sp.eye(3), sp.Matrix([[1,0]]))
physical_observer = even_output*full_observer*even_inclusion
assert physical_observer == 2*Q_occ
assert physical_observer.rank() == 3
assert physical_observer.det() == -48

# The kernel of the unnormalized physical trace is exactly the odd deck line
# in each occurrence and therefore disappears, rather than persists, in the
# coinvariant domain.
cycle_trace = sp.kronecker_product(sp.eye(3), sp.Matrix([[1,1]]))
odd_inclusion = sp.kronecker_product(sp.eye(3), sp.Matrix([1,-1]))
assert cycle_trace.rank() == 3
assert cycle_trace*odd_inclusion == sp.zeros(3,3)
assert cycle_trace*even_inclusion == 2*sp.eye(3)
assert odd_inclusion.rank() == 3

packet = {
    "schema": "marici.benincasa.tensor-polarization-parity-observer.v1",
    "status": "passed",
    "occurrence_observer": [[int(value) for value in row] for row in Q_occ.tolist()],
    "polarization_analyzer": [[int(value) for value in row] for row in B_pol.tolist()],
    "full_rank": int(full_observer.rank()),
    "full_determinant": int(full_observer.det()),
    "deck_equivariant": True,
    "physical_cycle_projection_rank": int(cycle_trace.rank()),
    "physical_cycle_kernel": "three labelled parity-odd Tate lines",
    "physical_domain": "reflection coinvariants",
    "physical_observer": [[int(value) for value in row] for row in physical_observer.tolist()],
    "physical_rank": int(physical_observer.rank()),
    "physical_determinant": int(physical_observer.det()),
    "additional_physical_kernel": 0,
    "classification": (
        "the full helicity family is faithful; physical reflection descent "
        "removes exactly the anti-invariant coefficient lines and leaves a "
        "faithful rank-three occurrence observer"
    ),
    "new_carrier_support": False,
    "scope_warning": (
        "This proves the finite polarization/occurrence observer diagram. It "
        "does not by itself prove that physical period covectors recover every "
        "rank-seven contact-normal interaction class."
    ),
}

output = Path(__file__).with_name("tensor-polarization-parity-observer.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
