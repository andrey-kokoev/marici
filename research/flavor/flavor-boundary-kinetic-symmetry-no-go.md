# Boundary-kinetic symmetry no-go: WP936

## Question

Can an ordinary sign, orbifold-parity, or endpoint-exchange symmetry supply
WP935's missing law by forcing the common boundary gauge-kinetic coefficient
to vanish?

## Exact character argument

Let `F_0` and `F_L` denote the boundary restrictions of the unbroken gauge
field strength and let

\[
O_0=\langle F_0,F_0\rangle,
\qquad
O_L=\langle F_L,F_L\rangle,
\]

where the pairing is invariant under the admitted gauge-algebra
automorphisms.  A sign or parity character acts by `F_i -> chi_i F_i`, with
`chi_i` equal to `+1` or `-1`.  Hence

\[
O_i\longmapsto \chi_i^2 O_i=O_i.
\]

Every such symmetry admits both boundary kinetic operators.  Endpoint
exchange sends `O_0` to `O_L` and therefore decomposes their coefficient
space into an even line `(1,1)` and an odd line `(1,-1)`.  Exchange removes
the odd coefficient but preserves the common operator

\[
O_+=O_0+O_L.
\]

Consequently the invariant coefficient space has dimension one, not zero.
The surviving coordinate is precisely WP772's common `tau`.

## Hostile pair

The packets

\[
(\tau_0,\tau_L)=(0,0)
\quad\text{and}\quad
(\tau_0,\tau_L)=(1,1)
\]

obey every sign, orbifold-parity, and endpoint-exchange condition above.  They
preserve the `SU(4)` parent, its gauge-link realization, and its pure-vector
spectral index, but WP935 gives distinct contrasts `1/10` and `1/20`.

This comparison is between two admitted objects; it carries no implicit time
or causal ordering.

## Classification

The symmetry family is a presentation rigidifier: it identifies the endpoint
coefficients and removes the exchange-odd direction.  It is not a selector of
the remaining common coefficient and therefore does not select a point of
`physical16`.

The result does not exclude a stronger source law.  A supersymmetric
nonrenormalization theorem, a derived UV fixed point, a boundary topological
constraint, or a source geometry with no legal codimension-one gauge
functional could remove or select the even line.  Each would require its own
complete operator and threshold audit.  Declaring `tau = 0`, or reading it
from a low-energy fit, supplies no authority.

WP770's two calibrated momentum ports can identify the even coefficient if a
physical production/decay realization exists.  That instrument remains a
readout and cannot replace the missing source selector.

## Result

WP935's missing completion-stable boundary law cannot be an ordinary sign,
parity, or exchange symmetry.  The smallest surviving kernel is the
one-dimensional exchange-even boundary kinetic line.

Reproduce with:

    uv run python research/flavor/checkers/wp936_boundary_kinetic_symmetry_no_go.py

Generated result:
`research/flavor/results/wp936_boundary_kinetic_symmetry_no_go.json`.
