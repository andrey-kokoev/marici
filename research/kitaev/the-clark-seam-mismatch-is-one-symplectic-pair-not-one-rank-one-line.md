# The Clark seam mismatch is one symplectic pair, not one rank-one line

## Question

When the two Clark charts are compared on the common first-jet trace, what is
the exact rank and signature of their boundary-metric mismatch?

## Common jet module

Let

\[
x=\begin{pmatrix}F\\F'\end{pmatrix}
\]

and let (a\ne0). The two Clark rows are

\[
P=\begin{pmatrix}1&ia\end{pmatrix}x,
\qquad
Q=\begin{pmatrix}1&-ia\end{pmatrix}x.
\]

Their positive rank-one boundary metrics are (P^*P) and (Q^*Q).

## Exact mismatch

Direct subtraction gives

\[
\Delta_a=P^*P-Q^*Q
=
\begin{pmatrix}
0&2ia\\
-2ia&0
\end{pmatrix}.
\]

This matrix is Hermitian. Its characteristic polynomial is

\[
\lambda^2-4a^2,
\]

so its eigenvalues are

\[
2a,
\qquad
-2a.
\]

For (a\ne0),

\[
\operatorname{rank}\Delta_a=2,
\qquad
\operatorname{signature}\Delta_a=(1,1).
\]

The mismatch is a nondegenerate indefinite form on the complete first jet.

## Scalar expression

On one jet vector,

\[
|P|^2-|Q|^2
=
2ia\bigl(\overline F F'-\overline{F'}F\bigr).
\]

It is the oriented symplectic area of (F) and (F'), multiplied by the
Clark scale. It vanishes on real-collinear jets but is not zero on the full
jet module.

For the two-variable analytic kernel, the transpose-conjugate convention
gives the equivalent polarization

\[
P(z)\overline{P(w)}-Q(z)\overline{Q(w)}
=
2ia\bigl(F'(z)\overline{F(w)}
-F(z)\overline{F'(w)}\bigr).
\]

## Correct channel count

The form factors as the difference of the two scalar Clark observation
energies. It therefore requires two rank-one positive rows if represented as
a signed Gram decomposition.

Equivalently, it is one complex symplectic pair. Calling it one complex seam
line is safe only if “line” denotes the resulting indefinite current after
both Clark rows have already been retained. It is not a rank-one form on the
source first-jet module.

Any literal rank-one reduction requires an additional source relation that
restricts admissible jets to a one-dimensional subspace. The Clark formulas
alone provide no such relation; indeed they reconstruct both (F) and (F').

## Relation to the smooth seam theorem

The underlying theta source germ and all its globally oriented jets match
across the seam. The nonzero (Delta_a) is therefore produced by applying
opposite Clark boundary metrics to the same jet. It is an interface supply
rate, not a distributional state jump.

## Consequence for the primitive seam claim

The statement that reflection cancels all but one primitive seam channel must
specify which of the following it means:

1. one complex scalar output per already-polarized chart comparison;
2. one symplectic pair on the source first jet;
3. a genuine rank-one form after a proved source restriction;
4. one arithmetic anomaly line receiving a rank-two jet form.

These types are inequivalent. The exact compiler arrow into the primitive
arithmetic line must state which factorization it uses and whether it is
faithful on both jet directions.

## Falsifier certificate

    {
      "code": "clark_seam_rank_one_mistyping",
      "jet_dimension": 2,
      "mismatch_matrix": [[0, "2ia"], ["-2ia", 0]],
      "rank": 2,
      "signature": [1, 1],
      "rank_one_reduction_requires_extra_relation": true
    }

## Disposition

The Clark boundary mismatch is exactly one nondegenerate symplectic pair on
the common first-jet module. It is not a rank-one defect. The next theta audit
must type the map from this pair into the claimed primitive seam or anomaly
line.

## Claim boundary

This is an exact finite-dimensional calculation for the unnormalized Clark
rows on the first source jet. It does not include additional theta
normalizations, arithmetic aggregation, reflection restrictions, or source
relations that may alter the pulled-back rank.
