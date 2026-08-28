# Spin7 mass-deletion realization fiber

Work package: WP934

## Question

Does the WP922 Spin7 representation and parity packet authorize three
independent mass controls realizing WP932's Boolean deletion routes?

## Missing field realization

WP922 declares representations, intrinsic parities, and a zero-mode retention
rule.  It does not declare whether the bulk matter objects are scalar fields,
five-dimensional fermions, or supersymmetric multiplets, nor does it give
their kinetic and mass action.

That omission changes the control rank.  Three scalar multiplets permit three
independent gauge-invariant quadratic masses, giving the formal incidence
matrix (I_3).

For a minimal chiral five-dimensional fermion realization, the orbifold action
uses the intrinsic parities

\[
(\eta_{8a},\eta_{8b},\eta_{21})=(-1,+1,-1).
\]

A diagonal fermion bilinear is orbifold odd, so a constant diagonal mass is
forbidden.  An odd kink mass is allowed but changes the zero-mode profile; it
does not provide a Boolean deletion of the protected chiral zero mode.  Since
the two spinors have opposite intrinsic parities, their cross bilinear is even
and can supply one joint pairing control.  It cannot independently delete
(8_a) or (8_b).

Thus the same representation/parity census admits scalar and fermionic
completions with mass-control ranks three and at most one.  The declared packet
itself has rank zero because neither realization is selected.

## Aspect-domain consequence

This explains WP933's `domain=unknown` result.  “Delete one multiplet” is not a
single morphism on the admitted source domain.  In one realization it is a
mass deformation; in another, the legal deformation localizes a zero mode or
pairs two sectors jointly.  Equal label counts cannot identify these actions.

## Verdict

The eight-route score tower remains a valid formal coefficient transform, but
there is no source-typed eight-route flavor experiment.  The obstruction is
upstream of calibration: field realization and mass-action typing are absent.

If the intended completion is fermionic, the correct successor is not a
deletion cube.  It is an exact profile-and-overlap experiment for independent
odd kink masses, with boundary localization and detector response stated in a
common frame.

## Reproduction

```powershell
uv run --with sympy python research/flavor/checkers/wp934_spin7_mass_deletion_realization_fiber.py
```

The generated result is
`research/flavor/results/wp934_spin7_mass_deletion_realization_fiber.json`.
