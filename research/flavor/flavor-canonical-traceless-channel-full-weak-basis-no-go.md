# The canonical traceless channel fails full weak-basis descent: WP948

## Question

After WP947 removes source-normal deformations of the Weyl pair, can its matrix carrier itself supply a canonical proper noncommutative channel through the traceless projection?

## Conjugation-equivariant classification

For the conjugation representation on `M3(C)`, every complex-linear equivariant endomorphism has the form

\[
E_{a,b}(X)=aX+b\operatorname{Tr}(X)I.
\]

Idempotence gives

\[
a^2=a,
\qquad
2ab+3b^2=b.
\]

There are exactly four solutions:

\[
0,
\qquad
I,
\qquad
X\mapsto\frac{\operatorname{Tr}X}{3}I,
\qquad
P_0(X)=X-\frac{\operatorname{Tr}X}{3}I.
\]

The first two are trivial. The scalar expectation has a commutative one-dimensional image. The traceless projector has the unique proper noncommutative image, of dimension eight.

## Full weak-basis hostile test

Simultaneous conjugation is not the full flavor groupoid. A Yukawa matrix transforms biunitarily:

\[
Y\longmapsto U_QYU_R^\dagger.
\]

Take

\[
Y=\operatorname{diag}(1,-1,0),
\qquad
U_Q=I,
\qquad
U_R=\operatorname{diag}(1,-1,1).
\]

Then `P0(Y)=Y`, but

\[
P_0(YU_R^\dagger)-P_0(Y)U_R^\dagger
=-\frac23I.
\]

Thus the traceless condition is not preserved by the full weak-basis groupoid and does not define a subfamily of `physical16`. It is chart data tied to an identification of left and right family frames.

## Positivity and instrument gate

The traceless projector is not positive. For the positive matrix

\[
X=\operatorname{diag}(1,0,0),
\]

its image has eigenvalues

\[
\frac23,-\frac13,-\frac13.
\]

It is therefore not a quantum channel or positive conditional expectation. A laboratory realization would require an enlarged signed or differential readout, with its own reference and calibration; it cannot be inferred from the matrix formula.

## Disposition

The canonical matrix-module escape is closed. The only conjugation-equivariant proper noncommutative projector is neither positive nor compatible with independent left and right weak-basis transformations. It is a presentation rigidifier, not a physical selector.

The next source object must be built directly from left-handed Grams or other full weak-basis covariants, or must explicitly declare a relational identification of left and right frames. Such an identification changes the physical groupoid and defines a new reference experiment. No physical time or causal order is used in this classification.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp948_canonical_traceless_channel_full_weak_basis_no_go.py

Generated result: `research/flavor/results/wp948_canonical_traceless_channel_full_weak_basis_no_go.json`.
