# Bounded relative Gram convergence transfers the reference Widom law to the Tate regulator

## Two positive regulator forms

Fix a finite observer packet `E_0`. Let

\[
G_\Lambda^0
\succeq0
\]

be the pure-translation/reference positive residual Gram matrix, and let

\[
G_\Lambda^T
\succeq0
\]

be the Tate-scattered positive residual Gram matrix, with identical volume-bulk and dyadic-filter conventions.

Define

\[
\boxed{
D_\Lambda
=G_\Lambda^T-G_\Lambda^0.
}
\]

Assume the centered regulator comparison gives

\[
\boxed{
D_\Lambda
\longrightarrow
W
}
\]

in matrix norm on `E_0`.

## Reference Widom law

Let

\[
a_\Lambda
\to\infty
\]

be the positive edge scale. In the one-dimensional prolate model this is proportional to `log c_Lambda`, equivalently to `log Lambda` under the relevant cutoff calibration.

Assume only the reference asymptotic

\[
\boxed{
\frac1{a_\Lambda}
G_\Lambda^0
\longrightarrow
G_{edge}.
}
\]

No Tate-scattered positive asymptotic is separately assumed.

## Transfer theorem

Since `D_Lambda->W`, the sequence `D_Lambda` is bounded. Therefore

\[
\frac1{a_\Lambda}
D_\Lambda
\longrightarrow0.
\]

Using

\[
G_\Lambda^T
=G_\Lambda^0+D_\Lambda,
\]

one gets

\[
\begin{aligned}
\frac1{a_\Lambda}
G_\Lambda^T
&=
\frac1{a_\Lambda}
G_\Lambda^0
+
\frac1{a_\Lambda}
D_\Lambda\\
&\longrightarrow
G_{edge}.
\end{aligned}
\]

Hence

\[
\boxed{
\frac1{a_\Lambda}
G_\Lambda^T
\longrightarrow
G_{edge}.
}
\]

The Tate and reference positive regulators necessarily have the same leading edge Gram.

## Polarized scalar convergence suffices on a packet

Suppose centered regulator comparison is initially known only for every polarized observer pair:

\[
D_\Lambda(g_i,g_j)
\to
W(g_i,g_j).
\]

There are finitely many matrix entries. Hence entrywise convergence implies matrix/operator-norm convergence on `E_0`.

Thus no uniform infinite-dimensional estimate is needed for this transfer at fixed packet rank.

## Consequence for common-edge positivity

If `G_edge>0` on the packet, then both positive regulators are eventually coercive at scale `a_Lambda`:

\[
G_\Lambda^{0,T}
\succeq
\frac12
a_\Lambda
\lambda_{min}(G_{edge})I.
\]

Meanwhile `(D_Lambda)_+` and `(D_Lambda)_-` remain bounded. Therefore

\[
\boxed{
C_\Lambda
=G_\Lambda^T-(D_\Lambda)_+
=G_\Lambda^0-(D_\Lambda)_-
\succeq0
}
\]

for sufficiently large cutoff.

Thus the finite-packet positive common-edge decomposition follows from:

1. one reference Widom law;
2. bounded centered relative convergence.

A separate positive Tate Widom theorem would be redundant.

## Fixed dyadic level

For the `j`-th dyadic defect filter

\[
f_j(t)
=t^{2^j}
(1-t^{2^j}),
\]

the classical reference coefficient is

\[
\boxed{
\beta_j
=C_W
\left(
H_{2^{j+1}-1}
-H_{2^j-1}
\right).
}
\]

The expected observer-weighted reference law is

\[
\boxed{
\frac1{\log c_\Lambda}
G_{\Lambda,j}^0(g,h)
\longrightarrow
\beta_jG_{Pl}(g,h),
}
\]

where `G_Pl` is the Mellin--Plancherel observer Gram.

If the centered relative matrices at level `j` converge, the identical law follows for `G_(Lambda,j)^T`.

## Finite accumulated depth

For the first `n` levels, the reference coefficient is

\[
\boxed{
\beta_{<n}
=C_WH_{2^n-1}.
}
\]

Thus

\[
\frac1{\log c_\Lambda}
G_{\Lambda,<n}^{0,T}
\longrightarrow
\beta_{<n}G_{Pl}
\]

for fixed `n`, provided the reference weighted Widom law and bounded relative convergence hold.

The statement is not uniform as `n->infinity`.

## Reduction to the pure Hardy model

The remaining leading-edge calculation can be performed with the pure phase

\[
\sigma_L^0(s)
=e^{2iLs}
\]

and observer localization retained on both Gram legs.

This reference model has:

- no gamma-factor derivative;
- no conductor phase;
- no endpoint winding beyond the chosen Hardy orientation;
- a translation-invariant difference kernel.

Consequently its leading observer dependence should be exactly Plancherel, while the scalar coefficient is the universal Widom integral of the chosen spectral filter.

This is a substantially simpler theorem than the full Tate-scattered positive asymptotic.

## Angular sectors

In the pure reference pair, the radial edge profile is independent of angular character. At finite conductor level there are finitely many character sectors, and the same scalar coefficient applies to each.

Therefore

\[
G_{edge,F}
=
\beta_fZ_F
\]

in the ideal normalized model. It is coercive on `ran Z_F` whenever `beta_f>0`.

This supplies exactly the common edge metric required by conductor-filtered positive removal.

## Global limitation

On the completed observer space, pointwise form convergence

\[
D_\Lambda(g,h)
\to
W(g,h)
\]

does not imply

\[
\|D_\Lambda\|_{op}
=O(1).
\]

Hence the transfer argument globalizes only under a uniform form bound or on conductor/observer packets where finite-dimensional norm equivalence applies.

This agrees with the necessity of the filtered system.

## Physical-alignment caveat

The identity

\[
D_\Lambda
=G_\Lambda^T-G_\Lambda^0
\]

must use positive regulator features with the same:

- cutoff geometry;
- volume-bulk removal;
- dyadic depth/filter;
- observer localization;
- outer and angular regulators.

The signed Connes-versus-Hardy scalar identity does not automatically prove this exact finite-cutoff Gram-difference identity. Establishing the physical alignment of regulators is the remaining sewing step.

Once alignment is proved and `D_Lambda` has the known centered limit, the Tate leading Widom law follows formally from the reference law.

## Revised analytic workload

For each fixed conductor level and dyadic depth, it is sufficient to prove:

1. the observer-weighted pure-reference Widom law;
2. exact alignment of Tate and reference positive Gram regulators;
3. convergence of their signed difference to `W`.

Then common-edge coercivity, Tate leading asymptotics, and convergent finite Jordan legs follow by finite-dimensional functional calculus.

## Disposition

The implication is

\[
\boxed{
\begin{aligned}
&G_\Lambda^T-G_\Lambda^0
\to W,\\
& a_\Lambda^{-1}G_\Lambda^0
\to G_{edge}
\end{aligned}
\Longrightarrow
 a_\Lambda^{-1}G_\Lambda^T
\to G_{edge}.
}
\]

Thus the leading positive edge theorem only needs to be proved for the pure Hardy/reference regulator. The nontrivial arithmetic information is confined to the bounded relative Gram difference and its Tate--Weil limit.
