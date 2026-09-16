# The archimedean phase-energy boundary is gapless, so completion must retain the zero spectral filtration

## Archimedean multiplier

For the even real archimedean channel, the regular Tate logarithmic derivative is, up to the fixed positive normalization used in the carrier measure,

\[
w_\infty(t)
=
\operatorname{Re}
\psi\left(\frac14+\frac{it}{2}\right)
-
\log\pi.
\]

The phase-energy normalized symbol is

\[
a_\infty(t)
=
\frac{w_\infty(t)}{e_\infty(t)},
\qquad
e_\infty(t)>0.
\]

Multiplication by a fixed positive normalization does not affect its zero set or the existence of arbitrarily small nonzero values.

## Value at the origin

The classical special value is

\[
\psi\left(\frac14\right)
=
-\gamma
-\frac\pi2
-3\log2.
\]

Therefore

\[
w_\infty(0)
=
-\gamma
-\frac\pi2
-3\log2
-\log\pi
<0.
\]

## Exterior sign

The digamma asymptotic gives

\[
\operatorname{Re}
\psi\left(\frac14+\frac{it}{2}\right)
=
\log\frac{|t|}{2}
+O(|t|^{-1}).
\]

Hence

\[
w_\infty(t)
\longrightarrow +\infty
\]

as \(|t|\to\infty\).

Since the digamma function is continuous on this vertical line, there exists

\[
t_0>0
\]

with

\[
w_\infty(t_0)=0.
\]

## Zero-gap consequence

Continuity gives a sequence \(t_n\to t_0\) such that

\[
0<|w_\infty(t_n)|\longrightarrow0.
\]

Because \(e_\infty\) is positive and locally finite near \(t_0\),

\[
0<|a_\infty(t_n)|
=
\frac{|w_\infty(t_n)|}{e_\infty(t_n)}
\longrightarrow0.
\]

Therefore

\[
\boxed{
\operatorname*{ess\,inf}_{a_\infty\ne0}
|a_\infty|
=0.
}
\]

The reduced minimum modulus of the archimedean boundary operator is

\[
\boxed{
\gamma(|\mathcal A_\infty|)=0.
}
\]

## Completion consequence

The archimedean boundary has a well-defined bounded positive operator

\[
|\mathcal A_\infty|
=
M_{|a_\infty|},
\]

with nonclosed range at zero. Its completion belongs to the gapless branch.

Use the spectral tower

\[
\mathscr E_{\infty,\eta}
=
1_{[\eta,\infty)}
\left(
|\mathcal A_\infty|
\right)
\mathscr E_\infty,
\qquad
\eta>0.
\]

Each stage satisfies

\[
\langle u,
|\mathcal A_\infty|u\rangle
\ge
\eta\|u\|^2.
\]

The full boundary is recovered as

\[
\eta\downarrow0.
\]

## Semilocal extension

For a larger semilocal set \(S\), finite-place phase derivatives modify the symbol. The same gapless conclusion follows on any character fiber where the full normalized symbol has a continuous zero or a sequence of nonzero values tending to zero.

Thus the semilocal test is fiberwise. The archimedean base case already shows that the universal completion formalism must support gapless spectral towers.

## Program correction

The positive completion interface should have two output modes:

1. a coercive radical quotient when the reduced minimum modulus is positive;
2. a spectral-tower completion when zero lies in the closure of the nonzero essential range.

The archimedean Tate boundary selects the second mode.
