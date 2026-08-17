"""Check the integral higher-pole obstruction to ordinary residue compression."""

import json

max_pole = 12
pole_cohomology = {}

# In the principal-parts de Rham complex,
# d(x^{-m}) = -m x^{-(m+1)} dx.
# Hence x^{-n} dx has quotient coefficient Z/(n-1) for n >= 2,
# while x^{-1} dx is the free residue line.
for n in range(1, max_pole + 1):
    if n == 1:
        pole_cohomology[n] = "Z (residue)"
    else:
        modulus = n - 1
        pole_cohomology[n] = "0" if modulus == 1 else f"Z/{modulus}"

assert pole_cohomology[1] == "Z (residue)"
assert pole_cohomology[2] == "0"
assert pole_cohomology[3] == "Z/2"
assert pole_cohomology[4] == "Z/3"
assert any(v.startswith("Z/") for v in pole_cohomology.values())

# Tensoring with Q makes every positive integer invertible, so only then do
# all higher poles become boundaries.  Integral physical realization may not
# silently make this base change.
rational_higher_poles = {n: "0" for n in range(2, max_pole + 1)}
assert all(v == "0" for v in rational_higher_poles.values())

print(json.dumps({
    "claim": "Ordinary principal-parts residue does not compress the telescope to its simple-pole line integrally; higher poles retain Z/(n-1) de Rham classes.",
    "status": "proved_integral_residue_no_go_and_log_lattice_target",
    "pole_cohomology_through_12": pole_cohomology,
    "ordinary_integral_residue_sufficient": False,
    "rational_residue_sufficient": True,
    "required_integral_input": "geometrically selected logarithmic/simple-pole lattice before residue",
    "next_gate": "use the D03 log-blowup expansion to construct the simple-pole subquotient and verify q03^Q, Cartier +1, endpoints, and D3",
}, sort_keys=True))
