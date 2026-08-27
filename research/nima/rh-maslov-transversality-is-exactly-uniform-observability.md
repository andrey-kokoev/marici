# RH Maslov transversality is exactly uniform observability

Author: `marici.Nima`

Date: 2026-08-26

Status: exact categorical-control equivalence

## Canonical comparison operator

Let \(\mathbb H\) carry both its split evaluation form and a source-derived
positive generalized metric. Fix the product-formula Lagrangian \(L_+\), and
let \(L(z)\) be the reciprocal Lagrangian transported by the completed source
correspondence.

The positive metric defines the orthogonal projection

\[
P_{L_+^\perp}:\mathbb H\longrightarrow L_+^\perp.
\]

Restrict it to the transported relation:

\[
\mathcal O_z
=
P_{L_+^\perp}|_{L(z)}.
\]

This is the canonical cross-projection or observability operator. Its kernel
is exactly

\[
\ker\mathcal O_z=L(z)\cap L_+.
\]

Therefore the following are equivalent at finite rank:

1. the two Lagrangians are transverse;
2. \(L(z)\) avoids the Maslov divisor of \(L_+\);
3. \(\mathcal O_z\) is injective;
4. the observability Gramian
   \(W_z=\mathcal O_z^*\mathcal O_z\) is positive definite.

No analogy is involved. Maslov transversality and state observability are the
same kernel statement in two categories.

## Completion strength

At infinite rank, injectivity is only pointwise faithfulness. Stable
transversality requires closed range and a positive lower bound in the
source-derived state norm:

\[
\langle W_zx,x\rangle
\ge c_z\langle G_{\mathrm{src}}x,x\rangle.
\]

For one fixed \(z\), a positive \(c_z\) excludes a completed intersection.
Uniform control over a spectral region requires an appropriate lower bound on
that region. A sequence with \(c_z\to0\) is simultaneously:

- an escaping unobservable state in control theory;
- a nonclosed-range sequence in functional analysis;
- an angle collapsing into the Maslov divisor in Lagrangian geometry.

## Exact graph model

Take the fixed primal Lagrangian \(L_+=V\oplus0\) and the graph of a skew map

\[
L_t=\operatorname{graph}(A_t),
\qquad
A_t=
\begin{pmatrix}
0&t\\
-t&0
\end{pmatrix}.
\]

With the standard positive metric on \(V\oplus V^*\), the cross-projection is
represented by \(A_t\). Its Gramian is

\[
W_t=A_t^TA_t=t^2I.
\]

Thus its smallest observability eigenvalue is \(t^2\), and all four
formulations fail together at \(t=0\).

For the reciprocal hostile \(t(z)=z^2-a^2\), the observability margin is

\[
c(z)=|z^2-a^2|^2.
\]

Reciprocal symmetry makes this margin even but does not keep it positive.

## Placement of the current theta channels

The finite Clark bulk constructs a positive Gramian on the feature pair

\[
(G+f,a\partial_zG).
\]

Kitaev's audit correctly distinguished feature faithfulness from state
faithfulness. In the present language, the feature map is only a candidate
factor of \(\mathcal O_z\). It becomes the actual cross-projection only after
all source-state directions and boundary incidences have been constructed.

The seam is not an auxiliary positive term. It supplies observer rows for
directions invisible to the tail-only feature map. Primitive, square, and
archimedean currents may supply further rows or modify the admissible state
domain. Missing incidence means that the complete \(\mathcal O_z\) is not yet
defined.

## Correct next construction

Build the source Lagrangian \(L(z)\) and generalized metric first. Then derive
the rows of \(\mathcal O_z\) as projections of the complete labelled state.
For every finite cutoff, test:

1. kernel equality with the Lagrangian intersection;
2. full observability rank;
3. the smallest generalized eigenvalue against the source Gramian;
4. reciprocal transport of the entire Gramian, not only its determinant;
5. convergence of the cross-projection graph under restricted-product
   completion.

The finite falsifier is a nonzero state in \(L(z)\cap L_+\), equivalently a
PBH or Gramian kernel witness. The completion falsifier is a normalized state
sequence whose observed norm tends to zero.

## Consequence

The odd arrival of control theory is now explained. Once the RH object is
typed as a state--observer hyperbolic double, its Maslov crossing operator is
necessarily an observability map. Control theory did not enter by analogy;
it is the linear operational language of the same categorical structure.

## Verification

The checker verifies maximal isotropy of the graph family, equality of the
intersection and observability kernels, the exact Gramian \(t^2I\), the
reciprocal hostile margin, and a cutoff family that is observable at every
finite stage while losing its uniform lower bound.

