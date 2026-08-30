# Every positive idempotent Gram-sector mixer is identity or equalization: WP950

## Question

Does dropping the unsupported up/down exchange symmetry from WP949 allow an asymmetric positive channel to select a viable proper family on the faithful Gram-pair quotient?

## General sector mixer

The most general positive unital linear channel that mixes only the two sector labels and introduces no matrix-space direction is

\[
\mathcal E_K(H_u,H_d)
=
\left(aH_u+(1-a)H_d,
bH_u+(1-b)H_d\right),
\]

with

\[
K=\begin{pmatrix}a&1-a\\b&1-b\end{pmatrix},
\qquad
0\leq a,b\leq1.
\]

It is positive, unital, and covariant under simultaneous weak-basis conjugation for every admitted pair `(a,b)`.

## Exact idempotent classification

The independent entries of `K^2-K` factor as

\[
(a-b)(a-1),
\qquad
b(a-b).
\]

Therefore idempotence has exactly two branches:

\[
(a,b)=(1,0),
\]

which is identity, or

\[
a=b=c,
\qquad
0\leq c\leq1.
\]

The second branch maps both sectors to the same positive Gram:

\[
(H_u,H_d)
\longmapsto
(H_c,H_c),
\qquad
H_c=cH_u+(1-c)H_d.
\]

Every nonidentity idempotent in the complete family thus erases the relative sector object and forces the Gram commutator to zero.

## Hostile coefficient fiber

Apply the channel to the positive comparator with

\[
\operatorname{Tr}[H_u,H_d]^3=-36i.
\]

At `c=1/3`, the selected common Gram has leading principal minors

\[
\frac53,
\quad4,
\quad\frac{452}{27},
\]

and trace `9`. At `c=2/3`, it has leading minors

\[
\frac43,
\quad3,
\quad\frac{340}{27},
\]

and trace `8`. Both are positive, both have output CP cubic zero, and they are numerically distinct. Positivity and idempotence do not choose the asymmetric weight.

## Claim boundary and disposition

This exhausts scalar stochastic mixing of the two Gram sectors. It does not exhaust matrix-dependent nonlinear operations such as commutator gradients, source actions, threshold maps, or channels with separately derived Kraus operators acting inside family space.

The result strengthens WP949: removing exchange symmetry creates a continuous coefficient fiber but no viable image. The channel is a quotient-descending equalizer and presentation-independent rigidifier, yet it selects the wrong commuting locus. A viable asymmetric operation must act on internal Gram geometry rather than only on the sector label, and its coefficients must be source-derived. Its calibrated instrument remains a separate gate. Channel composition carries no implicit physical-time interpretation.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp950_general_positive_gram_sector_mixing_exhaustion.py

Generated result: `research/flavor/results/wp950_general_positive_gram_sector_mixing_exhaustion.json`.
