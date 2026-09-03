# Minimal source enlargement classification

## Question

What is the smallest source enlargement capable of filling the primitive exceptional horn after complete rank-26 absorption?

## Claim boundary

Let new sourced degree-one generators have differential vectors

`d h_j = n_j Xi_log + r_j sigma123 + other_j`.

They fill the required horn exactly when an integral coefficient vector `a` satisfies:

- `sum a_j n_j = 1`;
- `sum a_j r_j = -1`;
- every additional differential component cancels.

For one generator this forces a primitive unit `Xi_log` coefficient and the matching opposite residue coefficient, up to orientation. For several generators, gcd one of the `Xi_log` coefficients is necessary and sufficient only for the `Xi_log` projection; the complete boundary matrix must contain `(1,-1,0,...)` in its integral column lattice. Coprime nonunit faces can therefore work jointly, while an all-even family cannot.

The existing rank-26/DNC module, fixed-open blow-ups, toroidal/SNC resolutions, smooth proper SNC compactifications of `G_m^2`, and unsourced mapping cones are excluded. A realization must change the source pair or category by genuine degree-one incidence data; subdivision cannot attach the primitive filling.

## Disposition

The universal minimality leaf is complete. The next leaf searches source geometry outside fixed-open SNC modifications for a primitive integral face or precycle and tests its entire boundary vector. This classification does not authorize adding the required cell tautologically.

## Verification

- `research/voevodsky/check_cosmology_minimal_source_enlargement_classification.py`
- `research/voevodsky/results/cosmology_minimal_source_enlargement_classification.json`
