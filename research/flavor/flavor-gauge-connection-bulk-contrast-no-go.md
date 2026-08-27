# Gauge-connection bulk contrast no-go: WP743

## Question

Does promoting WP742's ordinary bulk vector to the fifth component of an
(SO(5)) gauge connection make the (3+1) carrier and its asymmetric portal
unavoidable?

## What higher-dimensional gauge invariance fixes

Let the orbifold parity be

\[
P=\operatorname{diag}(1,1,1,1,-1).
\]

Conjugation by (P) leaves the six (SO(4)) generators even and makes the
four coset generators (T_{i5}) odd. Because (A=A_\mu dx^\mu+A_5dy) is a
one-form and reflection reverses (dy), the (A_5) parities are opposite to
the (A_\mu) parities. Hence (A_5) has exactly four even zero modes:

\[
SO(5)/SO(4)=4.
\]

Under the declared diagonal (SO(3)), they decompose as (3+1). Unlike an
ordinary scalar, the gauge connection has no independent intrinsic sign
choice. In a non-Abelian theory, (A\mapsto-A) sends
(dA+[A,A]) to (-dA+[A,A]), which is neither sign of the original curvature
for generic fields. Higher-dimensional gauge invariance therefore repairs
WP742's intrinsic-parity fiber and forces a single bulk coupling.

Gauge–Higgs unification literature identifies four-dimensional scalar fields
with extra-dimensional gauge components and generates their Wilson-line
potential dynamically. See [Hosotani](https://arxiv.org/abs/hep-ph/0504272).

## Exact bulk obstruction

The four coset modes form the irreducible vector of (SO(4)). The exact
symmetric commutant is

\[
\operatorname{Sym}(4)^{SO(4)}=\mathbb R I_4.
\]

Consequently, every bulk quadratic portal allowed by the source symmetry is
proportional to

\[
\phi_1^2+\phi_2^2+\phi_3^2+s^2.
\]

Its singlet–triplet ordered contrast is exactly zero. Higher-dimensional gauge
invariance supplies the carrier and parallelizes its coupling, but it does not
produce the required asymmetry.

## Where asymmetry reappears

At a boundary preserving only the declared diagonal (SO(3)), the symmetric
commutant enlarges to

\[
\operatorname{Sym}(4)^{SO(3)}
=\{\operatorname{diag}(a,a,a,b):a,b\in\mathbb R\}.
\]

The ordered contrast is (b-a). Thus the first locus where the desired
asymmetry is legal is also the first locus where an independent coefficient is
legal. The smallest falsifier is the residual-invariant boundary form
(operatorname{diag}(1,1,1,2)), whose contrast is (1). Nothing in the bulk
gauge principle selects that value or prevents a cancelling boundary term.

This is consistent with concrete gauge–Higgs models: localized gauge kinetic
terms modify coupling universality and the compactification scale, and
realistic symmetry breaking can require additional bulk matter. See
[Maru and Yatagai](https://arxiv.org/abs/1911.03465).

## Magnitude, basin, and readout

Dimensional reduction still gives

\[
g_4=\frac{g_5}{\sqrt\ell}.
\]

The magnitude retains both (g_5) and the compactification clock (ell).
The Hosotani potential depends on the admitted matter spectrum and geometric
moduli; explicit models can undergo phase transitions as those moduli vary.
See [Hosotani, Noda, and Takenaga](https://arxiv.org/abs/hep-ph/0410193).
Therefore neither a unique Wilson-line vacuum nor a complete RG basin follows
from the group and orbifold alone.

Bulk symmetry protects the equality of the four components, not a nonzero
contrast. Boundary thresholds can generate, change, or cancel the contrast.
No calibrated representation-labelled physical16 instrument is supplied by
the construction.

## Disposition

The gauge-connection construction is a genuine source-derived carrier selector
and coupling parallelizer. It removes the ordinary scalar's intrinsic parity
and fixes the (3+1) zero-mode packet. It is not an asymmetric portal selector:
bulk gauge invariance forces zero contrast, while the boundary locus that
permits contrast restores a free coefficient.

A progressive successor must derive an asymmetric boundary or holonomy
operation whose coefficient is quantized or otherwise fixed by the same source
dynamics, and must also fix the compactification clock, RG trajectory,
threshold completion, and calibrated physical16 readout.

Reproduce with
`uv run --with sympy python research/flavor/checkers/wp743_gauge_connection_bulk_contrast_no_go.py`.

Generated result:
`results/wp743_gauge_connection_bulk_contrast_no_go.json`.
