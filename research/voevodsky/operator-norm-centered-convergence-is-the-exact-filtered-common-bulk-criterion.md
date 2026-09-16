# Operator-norm centered convergence is the exact filtered common-bulk criterion

## Filtered setting

Fix conductor level \(F\) and let

\[
Z_F=1_{[0,F]}(K_S).
\]

On

\[
H_F=Z_F\mathscr H_S,
\]

let \(A_F\) be the bounded-below Tate connection form after endpoint extraction. Write

\[
A_F=A_{F,+}-A_{F,-}
\]

with

\[
\boxed{A_{F,-}\preceq(F+C_S)I.}
\]

Let \(G_{L,F}^0\succeq0\) and \(G_{L,F}^T\succeq0\) be the complete cross-polarized physical reference and Tate Grams at cutoff \(L\), after the declared finite regulator removals. Define their centered difference

\[
D_{L,F}=G_{L,F}^T-G_{L,F}^0.
\]

## Two required estimates

Assume the reference mismatch strip has a coercive lower bound

\[
\boxed{
G_{L,F}^0\succeq(L-\delta_{L,F})I
}
\]

in the chosen normalization, and the centered physical difference converges in operator norm:

\[
\boxed{
\|D_{L,F}-A_F\|
\le\varepsilon_{L,F}.
}
\]

The scalar coefficient \(L\) may be replaced throughout by \(2L\) according to the Fourier convention.

## Lower bound for the Tate Gram

Since

\[
A_F\succeq-A_{F,-}
\succeq-(F+C_S)I,
\]

one has

\[
D_{L,F}
\succeq
-(F+C_S+\varepsilon_{L,F})I.
\]

Therefore

\[
\begin{aligned}
G_{L,F}^T
&=G_{L,F}^0+D_{L,F}\\
&\succeq
\left(
L-
\delta_{L,F}-
F-C_S-
\varepsilon_{L,F}
\right)I.
\end{aligned}
\]

Define the filtered common scalar edge

\[
\boxed{
C_{L,F}^{scalar}
=
\left(
L-
\delta_{L,F}-
F-C_S-
\varepsilon_{L,F}
\right)_+I.
}
\]

Then

\[
C_{L,F}^{scalar}
\preceq G_{L,F}^0,
\qquad
C_{L,F}^{scalar}
\preceq G_{L,F}^T.
\]

This gives a literal common positive feature by Douglas factorization.

## Sharp operator-valued common edge

The scalar lower bound is sufficient but not optimal. Define

\[
E_{L,F}=D_{L,F}-A_F.
\]

Since

\[
-E_{L,F,-}\preceq E_{L,F},
\]

a sharper reference-side candidate is

\[
\boxed{
C_{L,F}^{op}
=G_{L,F}^0-A_{F,-}-E_{L,F,-}.
}
\]

It is positive whenever

\[
A_{F,-}+E_{L,F,-}
\preceq G_{L,F}^0.
\]

Moreover,

\[
\begin{aligned}
G_{L,F}^T-C_{L,F}^{op}
&=D_{L,F}+A_{F,-}+E_{L,F,-}\\
&=A_{F,+}+E_{L,F,+}
\succeq0,
\end{aligned}
\]

while

\[
G_{L,F}^0-C_{L,F}^{op}
=A_{F,-}+E_{L,F,-}
\succeq0.
\]

Thus there is an exact decomposition

\[
\boxed{
G_{L,F}^T
=C_{L,F}^{op}+A_{F,+}+E_{L,F,+},
}
\]

\[
\boxed{
G_{L,F}^0
=C_{L,F}^{op}+A_{F,-}+E_{L,F,-}.
}
\]

This is the finite-regulator polarity cube with the physical centered error retained rather than discarded.

## Convergence of residual legs

If

\[
\varepsilon_{L,F}\to0
\]

for fixed \(F\), then

\[
\|E_{L,F,\pm}\|
\le\varepsilon_{L,F}
\to0
\]

because \(0\preceq E_{L,F,\pm}\preceq\|E_{L,F}\|I\). Standard continuous functional calculus then gives convergence of the associated square roots.

Hence the residual physical Grams converge to

\[
A_{F,+},
\qquad
A_{F,-}.
\]

Their square-root features converge in norm as well.

## Directed cutoff/conductor regime

A sufficient admissibility margin is

\[
\boxed{
L
\ge
F+C_S+
\delta_{L,F}+
\varepsilon_{L,F}.
}
\]

For every fixed \(F\), this holds at sufficiently large cutoff if

\[
\delta_{L,F}=o(L),
\qquad
\varepsilon_{L,F}=o(L).
\]

For residual convergence to the exact Tate Jordan legs, one needs the stronger

\[
\varepsilon_{L,F}\to0.
\]

These are distinct requirements:

- \(o(L)\) gives positivity of a common extensive edge;
- \(o(1)\) gives convergence of the finite residual boundary.

## Necessity of norm strength

Pairwise scalar convergence

\[
D_{L,F}(g,h)
\to A_F(g,h)
\]

on each fixed observer pair does not provide a uniform \(\varepsilon_{L,F}\) on an infinite-dimensional conductor sector. It is sufficient on a fixed finite observer packet, where entrywise convergence implies matrix-norm convergence.

Therefore the exact missing analytic estimate is not another scalar trace identity. It is either:

1. operator-norm centered convergence on \(H_F\); or
2. a direct form-order estimate
   \[
   -\varepsilon_{L,F}I
   \preceq D_{L,F}-A_F
   \preceq\varepsilon_{L,F}I.
   \]

## Physical interpretation

The reference mismatch strip supplies the extensive capacity. The negative part of the centered Tate connection consumes at most \(F+C_S\) units of that capacity. The centered regulator error consumes \(\varepsilon_{L,F}\) more. What remains is the common physical bulk.

The two residual polarities are exactly the positive and negative parts of the Tate connection plus the corresponding positive and negative parts of the finite-cutoff error.

## Disposition

At fixed conductor, the common-bulk theorem follows from two explicit quantitative estimates:

\[
\boxed{
G_{L,F}^0\succeq(L-\delta_{L,F})I,
\qquad
\|G_{L,F}^T-G_{L,F}^0-A_F\|
\le\varepsilon_{L,F}.
}
\]

Under them, the common edge and both residual legs are given explicitly by functional calculus. The unresolved analytic input is the operator-norm/form-order estimate for the exact physical centered regulator on each conductor level.
