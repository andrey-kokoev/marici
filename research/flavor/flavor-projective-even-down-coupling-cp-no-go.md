# The minimal projective even coupling descends but destroys three-family CP: WP956

## Question

Following Nima's gate, can WP955's sign-blind projective axis be coupled evenly into the WP350 family operator module while retaining generic three-family flavor?

## Exact even constructor

For the WP326 projectors

\[
P=\operatorname{diag}(1,0,0),
\qquad
Q=\frac12
\begin{pmatrix}
1&1&0\\
1&1&0\\
0&0&0
\end{pmatrix},
\]

the oriented WP350 down operator is

\[
B=P-Q.
\]

The projective flag identifies only the line `span(B)`, so the smallest even family-module lift is `B^2`. Exact multiplication gives

\[
B^2=\operatorname{diag}\left(\frac12,\frac12,0\right).
\]

It is invariant under `B -> -B` and transforms covariantly under simultaneous weak-basis conjugation. Thus the even lift descends through both the projective sign quotient and the full left-handed weak-basis groupoid.

## Even-functional exhaustion

The minimal polynomial is

\[
B\left(B^2-\frac12I\right)=0.
\]

Consequently every even polynomial or analytic function on the finite spectrum reduces to

\[
f_{\rm even}(B)=\alpha I+\beta B^2.
\]

Its spectrum has a repeated value on the two-dimensional nonzero eigenspace of `B^2`. Any Gram constructed solely from this even functional calculus is therefore twofold degenerate.

For a three-family pair, degeneracy of either Gram annihilates the Jarlskog commutator determinant and

\[
\operatorname{Tr}[H_u,H_d]^3=0.
\]

This conclusion does not depend on the democratic up-sector amplitude.

## Exact WP350 hostile test

Keep the WP350 up operator `I+P+Q+R`, with the complex third projector `R`, and replace its oriented down lift by

\[
Y_d=2I+B^2.
\]

The up discriminant remains `181/54`. The down discriminant becomes zero, the Gram commutator has rank two, and its cubic trace is zero. By contrast, the odd lift `2I+B` has nonzero cubic trace `-3658i/3` at the same benchmark.

## Classification and disposition

The projective even coupling is a genuine source-compatible descent map but selects the wrong physical locus. The result exposes a sharp trilemma:

- retain only the projective axis and lose three-family CP;
- lift the axis to an oriented operator `B` and reintroduce sign authority;
- add another independently sourced tensor that combines with the axis to form an orientation-insensitive but spectrally simple operator.

An external orientation port would define a new relational experiment over its stabilizer groupoid; it would not reveal an absolute sign already present in the projective source. The remaining minimal research target is the third option. No composition is assigned physical time.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp956_projective_even_down_coupling_cp_no_go.py

Generated result: `research/flavor/results/wp956_projective_even_down_coupling_cp_no_go.json`.
