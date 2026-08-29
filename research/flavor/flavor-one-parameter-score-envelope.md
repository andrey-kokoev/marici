# One-parameter score envelope: WP1007

## Question

Does the same Hermitian family contain a configuration that is genuinely
exposed against the whole continuous family, rather than only a hand-picked
finite competitor set?

## Exact family

Fix

\[
X=\operatorname{diag}(-1,0,1),
\qquad
Y_t=\begin{pmatrix}0&1&-it\\1&0&1\\it&1&0\end{pmatrix},
\qquad t>0.
\]

Writing (x=t^2), its normalized scores are

\[
K(x)=\frac{1+2x}{2+x},
\qquad
P(x)=\frac{x}{4(2+x)^3}.
\]

Eliminating (x) gives the exact score curve

\[
P(K)=\frac{(2K-1)(2-K)^2}{108},
\qquad \frac12<K<2.
\]

## A continuous-family exposed witness

Take (t=6/5), so

\[
K_\star=\frac{97}{86},
\qquad
P_\star=\frac{5625}{636056}.
\]

For the positive ratio

\[
r_\star=\frac{R}{Q}=\frac{44376}{275},
\]

the score (K+r_\star P(K)) has stationary points at
(K_\star) and (3-K_\star=161/86). The derivative changes from positive
to negative at (K_\star), and from negative to positive at the second point.
Exact endpoint comparison gives

\[
K_\star+r_\star P_\star>2,
\]

so (K_\star) is the unique global maximizer over the complete (t>0)
family. This passes a continuous-family support test that WP1005 failed.

## What this repairs and what it does not

The positive cone contains a genuine interior exposed orbit of this declared
Hermitian subfamily. Varying the positive ratio produces a continuum of such
orbits near the determinant-dominated side, so three affinely independent
records can be chosen within the subfamily.

However, the subfamily itself was analyst-selected. A configuration outside it
may still dominate the witness, and no source symmetry or potential restricts
the full Hermitian domain to this curve. The parameter (t=6/5) is likewise a
witness, not a source-selected value.

## Classification

WP1007 is a continuous-subdomain capacity theorem. It supplies neither a
flavor selector nor a physical preparation instrument.

## Smallest exact falsifier

Any admitted Hermitian pair whose score exceeds
(K_\star+r_\star P_\star) falsifies full-domain exposure. Within the frozen
family, changing the response ratio away from (r_\star) moves the unique
maximizer and falsifies numerical selection of (t=6/5).

## Claim boundary

The global maximum is global only on the one-parameter family (Y_t), not on
the full Hermitian coefficient-field domain. No physical time or dynamical
trajectory is assigned to (t).

## Disposition

Retain the score curve as an exact search manifold. The next gate is either a
source-derived restriction to this family or a hostile optimization over
transverse Hermitian directions.

