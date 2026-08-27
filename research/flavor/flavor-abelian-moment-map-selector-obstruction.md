# Abelian moment-map selector obstruction: WP715

## Post-WP725 typing correction

The charge algebra below is conditional on complexifying each flavor triplet
or otherwise adding a charged partner. A single admitted real irreducible
\(SO(3)\) triplet has no nontrivial commuting orthogonal \(U(1)\) action.
Therefore this packet does not define a direct source operation on the original
real-triplet quotient. WP725 gives the exact commutant proof and supersedes the
earlier implicit carrier typing; the algebraic rank-one obstruction remains
valid on the enlarged charged domain.

## Hard-to-vary candidate

An ordinary symmetry can allow or forbid (chi^2|n|^2), but cannot fix its
continuous coefficient. The minimal mechanism that fixes relative portal
magnitudes is one gauged Abelian moment map

\[
V_D=\frac{G}{2}
\left(q_n|n|^2+q_m|m|^2+q_\chi\chi^2\right)^2,
\qquad G>0.
\]

Quantized unequal charges force

\[
g_n=Gq_nq_\chi,
\qquad
g_m=Gq_mq_\chi,
\qquad
g_n-g_m=Gq_\chi(q_n-q_m).
\]

The sign and relative magnitude are now consequences of one gauge constraint,
not separately tunable portal coefficients.

## Rank-one obstruction

The same moment map fixes

\[
\lambda_n=\frac{Gq_n^2}{2},
\qquad
\lambda_m=\frac{Gq_m^2}{2},
\qquad
\lambda_x=Gq_nq_m.
\]

Therefore

\[
4\lambda_n\lambda_m-\lambda_x^2=0.
\]

The quartic Gram has rank one and lies exactly on the WP708 radial boundary.
Because the moment map depends only on norms, it also generates no
((n\mathbin\cdot m)^2) angular stiffness.

## Deutschian assessment

The Abelian gauge principle is hard to vary in the relevant sense: changing a
portal coefficient independently breaks the single moment-map square. But it
explains the desired asymmetry only while failing two other independently
required phenomena—strict radial stability and faithful-frame rigidity.

It therefore cannot be the requested complete explanation. A viable repair
must contain at least two independent positive moment-map directions or a
non-Abelian source whose charge/weight geometry has rank at least two and also
provides angular stiffness. Its matter content must fix the weights and gauge
normalization independently, pass anomaly and RG closure, survive threshold
decoupling, and expose the same relational charges to a calibrated instrument.

The smallest exact falsifier is the identity
(4\lambda_n\lambda_m-\lambda_x^2=0), valid for every charge assignment.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp715_abelian_moment_map_selector_obstruction.py

Generated result: results/wp715_abelian_moment_map_selector_obstruction.json.
