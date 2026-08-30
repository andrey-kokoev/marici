# Optical audit of theta coherency hemisphere transport

## Question

Does the rank-one theta tail-seam coherency admit a physical polarization
interpretation, and what transport law would preserve one Stokes hemisphere?

## Coherency interpretation

The matrix in Grothendieck's packet is exactly the outer product of the
two-component amplitude vector `(U, conjugate(V))`. Algebraically it is a pure
two-mode Jones coherency matrix: positive, rank one, and null in Stokes
coordinates.

This is a faithful optical isomorphism only after the two transform components
are admitted as labelled physical modes with a record map. The algebra alone
does not establish that the theta transforms are laboratory optical fields.

## Positivity does not orient the sheet

Every Jones matrix sends a rank-one coherency matrix to another rank-one
positive matrix. That says nothing about the sign of `S3`. Even an ordinary
lossless unitary rotation can take the north-pole state across the equator.
The checker uses the exact rotation with cosine `3/5` and sine `4/5`; it sends
`S3=1` to `S3=-7/25`.

Unequal diagonal gain also preserves rank one and positivity but can reverse
the sheet. Thus neither purity, positivity, reciprocity, nor ordinary unitary
propagation proves hemisphere preservation.

## Required source-derived propagation law

Let `K=diag(1,-1)`, so `S3=psi† K psi`. A transport `J` preserves the sign of
`S3` for every non-seam state if it obeys

```text
J† K J = lambda K, with lambda > 0.
```

Then the transported coordinate is `S3' = lambda S3`. The checker verifies an
exact noncompact `K`-unitary example. Reciprocal exchange instead satisfies
`P† K P = -K` and reverses the sheets, matching the two-sheet involution.

This identifies the missing constructor precisely. A completed Clark or
boundary propagation must derive a positive `K`-conformal connection, or a
weaker path-specific cone invariance, from its source laws. Assuming
Hermite-Biehler positivity would merely assume the desired hemisphere.

## Falsifiers

The global falsifier is any admitted transition whose `J† K J` is not a
positive multiple of `K` and which maps one authorized state across the seam.
The packet contains two exact examples: an ordinary unitary rotation and an
unequal-gain diagonal map.

For a path-specific claim, global `K`-conformality may be stronger than
necessary. The cheaper test is to transport the actual initialized state and
verify that `S3` never reaches zero. Such a numerical path test remains a
finite-sector result unless backed by a source-derived invariant or monotonic
quantity.

## Verification

Run:

```text
uv run --with sympy python research/aspect/checkers/check_theta_coherency_hemisphere_transport.py
```

The checker verifies the unitary and unequal-gain counterexamples, exact
`K`-unitary preservation, and reciprocal sign reversal.
