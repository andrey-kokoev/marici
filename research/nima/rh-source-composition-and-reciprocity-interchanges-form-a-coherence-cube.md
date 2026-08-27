# Source, composition, and reciprocity interchanges form a coherence cube

## Typing correction

The central `-I` fixture below is an anomaly only in an ungraded interchange
law. When the crossed constructors are both odd, `-I` is the canonical Koszul
sign and the cube is super-coherent. The fixture therefore proves that parity
typing is mandatory; it does not by itself prove a genuine cube anomaly. See
`rh-cube-coherence-must-be-koszul-normalized.md` for the corrected criterion.

## Three independent directions

The current architecture has three operations that may be performed in
different orders:

1. forward composition of operators;
2. source realization or refinement;
3. reciprocal transport between half-planes.

Each pair needs an interchange cell:

- source–composition interchange;
- composition–reciprocity interchange;
- source–reciprocity interchange.

Pairwise cells do not guarantee that the complete three-dimensional cube
commutes.

## Cube law

Let the three pairwise comparison operators be `Omega_SC`, `Omega_CR`, and
`Omega_SR`. The two routes around the cube must agree:

\[
\Omega_{SR}\Omega_{CR}\Omega_{SC}
=
\Omega_{SC}\Omega_{CR}\Omega_{SR},
\]

with the exact order adjusted to the declared variance of each port.

The residual

\[
\mathfrak A
=
\Omega_{SR}\Omega_{CR}\Omega_{SC}
\left(
\Omega_{SC}\Omega_{CR}\Omega_{SR}
\right)^{-1}
\]

is a mixed coherence anomaly. It can be central and invisible after scalar
projection while still changing the operator-level Cartan identity.

## Exact cube hostile

Take

\[
\Omega_{SC}=X,
\qquad
\Omega_{CR}=Z,
\qquad
\Omega_{SR}=I,
\]

where `X` and `Z` are the Pauli involutions. Every comparison is invertible and
individually normalized. But the two cube routes are

\[
XZI
\qquad\text{and}\qquad
IZX,
\]

and they differ by `-I` because `XZ=-ZX`.

Thus complete pairwise interchange data can leave a central cube residual.
Whether it is anomalous depends on the source-declared parities of the crossed
constructors.

## RH relevance

The right-sector source Cartan identity can be transported to the left sector
in two conceptually valid ways:

1. realize the source operators, compose them, then apply reciprocity;
2. apply reciprocity to the source pieces, realize them in the left sector,
   then compose them there.

If these routes differ by a sign, phase, boundary current, or domain
modification, the two half-plane contractions do not form one Ubersector even
though each sector is internally exact.

The reciprocal sign reversal of the contraction port is expected. The cube
must distinguish that declared sign from an additional anomaly.

## Does this require another tower?

Not necessarily. If all three pairwise cells are generated from one
source-normalized constructor, cube coherence may follow by telescoping. Then
the fifth tower includes the cube law as an axiom or theorem.

If the pairwise cells are supplied independently, their residual is a new
higher datum. Killing it with a fitted cell would begin another regress. The
proper repair is to derive all comparisons from a common normalization or
prove a source cocycle theorem.

## Strong DPC

Require:

1. all three pairwise interchange cells with ordered domains;
2. their source authority and normalization;
3. the declared reciprocal sign on the contraction port;
4. both complete cube composites;
5. their operator-level residual before scalar projection;
6. classification of any residual as exact boundary, central anomaly, domain
   mismatch, or rejection;
7. compatibility with seam incidence and completion;
8. a common source normal form if strict cube coherence is claimed.

Finite falsifiers:

- the `X,Z,I` central-sign cube;
- a cube whose scalar endpoints agree but graph domains differ;
- a reciprocal sign counted twice on one route;
- pairwise boundary corrections whose accumulated currents disagree;
- finite strict cubes with a nonzero completion cocycle.

## Corrected verdict

The two tower-four structures and the reciprocal sector pair generate a
graded coherence cube. The fifth tower is adequate only if it contains a
source-derived, Koszul-normalized cube law. Pairwise interchange is
insufficient, but the raw central sign is not a defect when it is exactly the
sign forced by declared odd parity.
