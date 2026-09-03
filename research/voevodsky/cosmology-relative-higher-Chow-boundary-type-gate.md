# Relative higher-Chow boundary type gate

## Question

Can the localization boundary of `{u,v}` be identified directly with the integral exceptional cycle `sigma123`?

## Claim boundary

No direct identification is typed. On the standard toric boundary of `G_m^2`, the tame symbols of `{u,v}` are four divisor-indexed residual units:

- at `u=0`: `v^-1`;
- at `u=infinity`: `v`;
- at `v=0`: `u`;
- at `v=infinity`: `u^-1`.

Their exponent sum satisfies reciprocity. This boundary lies in K1 groups of divisor function fields. By contrast, `sigma123` is a three-edge integral incidence cycle with coefficients `(1,-1,1)`.

Turning the residual units into integers requires sourced secondary valuations, flags, and orientations. Counting signs or exponents without those data discards the functions and silently replaces a four-divisor boundary by an unrelated three-edge vector.

## Disposition

The naive relative-precycle boundary claim is type-blocked. The next leaf must construct a Parshin-flag or iterated-residue comparison to the exceptional triangle, account for the fourth toric divisor, and test whether the complete oriented vector is `(1,-1)` in the required two components.

## Verification

- `research/voevodsky/check_cosmology_relative_higher_Chow_boundary_type_gate.py`
- `research/voevodsky/results/cosmology_relative_higher_Chow_boundary_type_gate.json`
