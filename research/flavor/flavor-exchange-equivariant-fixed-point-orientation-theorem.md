# Exchange-equivariant fixed-point orientation theorem: WP728

## Question

Can an exact exchange-symmetric source make a nonzero ordered portal contrast
unique at an ultraviolet fixed point, or must the source already contain a
physical orientation of the two channels?

## Equivariant fixed-point theorem

Write the portal coordinates as an exchange-even coordinate (s) and an
exchange-odd contrast (a). The exchange involution is

\[
E(s,a)=(s,-a).
\]

Let the autonomous beta field be exchange equivariant:

\[
\beta(E x)=E\beta(x).
\]

If (x_*) is a fixed point, then (E x_*) is also a fixed point. Therefore a
unique fixed point must obey (E x_*=x_*), which forces

\[
a_*=0.
\]

At a symmetric fixed point the stability matrix commutes with (E), so its
even and odd eigenspaces do not mix. Making the odd fluctuation irrelevant
therefore predicts zero contrast; it cannot predict a unique nonzero one.

## Spontaneous route and its sign fiber

An equivariant nonlinear beta field may have nonzero fixed points, but they
occur in exchange-related pairs. The minimal example is

\[
\beta_a=a(a^2-v^2),
\]

with fixed points (a=0,+v,-v). The two nonzero values have equal status under
the source automorphism. Quotienting by exchange retains (|a|) but removes
its sign. Holding one label fixed to distinguish the signs introduces a
reference and changes the experiment to the corresponding stabilizer
groupoid. This route may select a magnitude or an orbit, but it does not fix
the absolute ordered sign in the original source theory.

## Explicit representation orientation

A unique nonzero contrast requires exchange not to be a source automorphism.
The minimal local normal form is

\[
\beta_a=\vartheta_a(a-a_*),
\qquad
a_*=\frac{b}{\vartheta_a},
\]

where (b) is a fixed exchange-odd source term. If (artheta_a>0), the
fluctuation about (a_*) is irrelevant in the convention of WP727 and its
boundary amplitude is not free. Both sign and magnitude are then fixed by the
source data (b) and (artheta_a).

For this to be physical rather than a relabelling convention, (b) must arise
from non-isomorphic, independently identifiable representation labels. Their
gauge charges, Casimirs, or other source invariants must prevent an admitted
automorphism from exchanging the channels. Merely naming two isomorphic
copies differently does not orient the source.

## Minimal fixed-point architecture

The exact affine witness

\[
\beta_s=-(s-s_*),
\qquad
\beta_a=2\left(a-\frac35\right)
\]

has one relevant clock direction and one irrelevant portal-contrast
direction. It fixes (a_*=3/5) with positive sign. This is an algebraic
acceptance witness, not an admitted matter model: the constant (3/5) must be
derived from a complete anomaly-free representation and beta-function packet.

Threshold survival and readout remain separate arrows. Finite matching must
have no dependence of the low-energy contrast on any free relevant deformation,
or the source must fix that deformation. Two calibrated labelled detector
channels must then retain rank two; an unlabelled sum still annihilates the
contrast.

## Disposition

WP728 identifies the necessary source principle more sharply:

1. physical orientation by non-isomorphic representation data;
2. a unique interacting fixed point with nonzero odd coordinate;
3. an irrelevant odd fluctuation about that coordinate;
4. one independently fixed or calibrated relevant clock deformation;
5. contrast-preserving finite matching; and
6. two source-labelled calibrated detector channels.

Only the first three items answer why the portal asymmetry is unavoidable.
The last three are necessary for its physical prediction. No current Marici
matter packet realizes the six-item composition.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp728_exchange_equivariant_fixed_point_orientation.py`

Generated result:
`results/wp728_exchange_equivariant_fixed_point_orientation.json`.
