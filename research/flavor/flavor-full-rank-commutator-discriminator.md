# Full-rank commutator discriminator

## Question

WP976 asks for the smallest declared CP-even invariant that directly separates
the WP973 embedded two-level commutator from a full-rank three-family
commutator. The domain is two Hermitian coefficient fields; the quotient is
full weak-basis equivalence.

## Discriminator

For \(C=[X,Y]\), define

\[
D(C)=\frac{|\det C|^2}{\lVert C\rVert_F^6}
\]

on the nonzero-commutator domain. It is invariant under simultaneous unitary
conjugation, common positive rescaling of \(C\), and CP conjugation. It
vanishes exactly when the three-by-three commutator is rank deficient.

The commutator is quadratic in the fields. Its determinant has field degree
six, while the CP-even numerator \(|\det C|^2\) has field degree twelve.
Therefore this direct full-rank discriminator lies outside the renormalizable
two-field trace grammar audited by WP974.

## Exact hostile pair

The WP973 equality witness has

\[
\lVert C_2\rVert_F^2=8,\qquad D(C_2)=0.
\]

The WP972 full-rank control has

\[
\lVert C_3\rVert_F^2=28,\qquad
\det C_3=12i,\qquad
D(C_3)=\frac{9}{1372}.
\]

Thus the discriminator separates two-level noncommutativity from genuine
three-family CP capacity without selecting an absolute CP sign.

## Classification

\(-\kappa|\det[X,Y]|^2\), after a separately proven stable completion, is a
conditional full-rank CP-magnitude selector. It is not currently
source-authorized: its coefficient, EFT suppression scale, radial completion,
and relation to the WP447 coefficient fields have not been derived.
Algebraic legality is not executable source control.

The smallest falsifier is a rank-deficient commutator with nonzero \(D\), or a
full-rank commutator with \(D=0\).

## Reproduction

Run:

    python research/flavor/checkers/wp976_full_rank_commutator_discriminator.py

The generated result is
research/flavor/results/wp976_full_rank_commutator_discriminator.json.
