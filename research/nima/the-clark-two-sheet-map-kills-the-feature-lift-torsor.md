# The Clark Two-Sheet Map Kills the Feature-Lift Torsor

## Native feature and sheet carriers

The Clark bulk uses the source features

\[
X=G+f,
\qquad
Y=a\partial_zG,
\]

with two sheet readouts

\[
Z_+=X+iY,
\qquad
Z_-=X-iY.
\]

Let \(S\) denote the map

\[
S(X,Y)=(Z_+,Z_-).
\]

It has the explicit inverse

\[
X=\frac{Z_++Z_-}{2},
\qquad
Y=\frac{Z_+-Z_-}{2i}.
\]

Therefore \(S\) is an isomorphism whenever both typed sheet outputs are
retained.

## Feature-level lift uniqueness

Suppose \(A\) is a residual operator on the feature carrier that is invisible
to both Clark sheets:

\[
SA=0.
\]

Since \(S\) is invertible,

\[
A=0.
\]

The abstract boundary-invisible sign hostile cannot occur on the complete
two-feature Clark packet. Sheet doubling is not redundant here; its symmetric
and antisymmetric outputs reconstruct the full feature state.

## State-level kernel is exactly the observability kernel

Let

\[
J_X:\mathcal A_X\longrightarrow\mathcal F_X
\]

be the source map from admissible states to the feature packet
\(\mathcal F_X=(X,Y)\). The complete two-sheet observation is

\[
\tau_X=SJ_X.
\]

Because \(S\) is invertible,

\[
\ker\tau_X=\ker J_X.
\]

Thus every remaining boundary-invisible bulk lift acts entirely inside the
state-feature kernel already identified by Kitaev. There is no independent
Clark phase torsor after both sheets are retained.

## Control-theoretic form

The finite uniqueness gate is ordinary observability:

1. feature-level observation is full rank;
2. state-level observation is faithful exactly when \(J_X\) is injective;
3. completion stability requires a cutoff-independent lower bound for
   \(J_X\), not merely invertibility of \(S\).

The Clark Gram determinant proves the first item. It cannot prove the second
or third because those concern the constructor producing the features from
admissible states.

## Minimum hostile

Extend the four-real-dimensional feature carrier by one hidden state direction
\(n\), and let \(J_X\) forget \(n\). Then both Clark sheets remain complete on
features while the state \(n\) is invisible:

\[
J_Xn=0,
\qquad
\tau_Xn=0.
\]

This is the smallest remaining bulk-lift falsifier. Adding more sheet
algebra cannot detect it; only an additional source row or dynamics coupling
to \(n\) can.

## Frontier

The next calculation is no longer to classify abstract lifts. It is to derive
the actual finite-cutoff state-feature map \(J_X\), including seam, primitive,
square, and archimedean rows, and test:

\[
\ker J_X=0.
\]

For completion, the stronger requirement is uniform observability. A sequence
of normalized admissible states with \(\lVert J_Xv_X\rVert\to0\) is the exact
escape falsifier.

