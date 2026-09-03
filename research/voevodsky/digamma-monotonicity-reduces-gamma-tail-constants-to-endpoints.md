# Digamma monotonicity reduces gamma tail constants to endpoint values

## Question

Can the gamma constants in the explicit time--band dimension bound be reduced to evaluations at \(0\) and \(R\), rather than global interval optimization?

## Claim boundary

Yes, for the standard core multiplier

\[
d(u)
=
\operatorname{Re}\psi\left(\frac14+\frac{iu}{2}\right)-\log\pi.
\]

It is even and strictly increasing for \(u>0\). Therefore its minimum on \([-R,R]\) occurs at zero and its infimum on \(|u|>R\) is the boundary value at \(R\). A positive normalization scale preserves these statements. The exact scale and interval enclosures remain convention-dependent inputs.

## Series proof

For \(a>0\), the digamma series gives

\[
\operatorname{Re}\psi(a+iy)
=
-\gamma
+
\sum_{n=0}^{\infty}
\left[
\frac1{n+1}
-
\frac{n+a}{(n+a)^2+y^2}
\right].
\]

Set \(a=1/4\) and \(y=u/2\). For \(u>0\), each nonconstant summand has derivative

\[
\frac{(n+1/4)u}
{2\left((n+1/4)^2+u^2/4\right)^2}
>0.
\]

The differentiated series converges locally uniformly away from no singularity on the real \(u\)-axis, so termwise differentiation is valid. Hence

\[
d'(u)>0
\qquad(u>0).
\]

Evenness follows from complex conjugation of \(\psi\).

## Exact low-band constant

The special value

\[
\psi\left(\frac14\right)
=
-\gamma-rac\pi2-3\log2
\]

gives

\[
d(0)
=
-\gamma-rac\pi2-3\log2-
\log\pi
<0.
\]

Thus, before a positive overall scale is applied,

\[
C_{\rm low}
=
-d(0)
=
\gamma+rac\pi2+3\log2+
\log\pi.
\]

It is independent of \(R\).

## Exterior constant

Monotonicity gives

\[
\inf_{|u|>R}d(u)=d(R).
\]

Therefore the high-frequency constant is a single endpoint evaluation:

\[
m_R=d(R).
\]

Since \(d(R)\sim\log(R/2)-\log\pi\), it tends to positive infinity.

## Normalization gate

The source packet records a factor \(1/(4\pi)\) on the digamma integral and says the \(-\log\pi\) constant is absorbed, but it does not freeze whether that constant is inside the same factor under every Fourier convention. Before combining gamma and prime constants, one exact multiplier normalization must be read back from the canonical explicit formula.

If the complete gamma multiplier is \(\kappa d(u)\) with \(\kappa>0\), then

\[
C_{\rm low}^{\Gamma}
=
\kappa[-d(0)],
\qquad
m_R^{\Gamma}
=
\kappa d(R).
\]

## Disposition

The gamma optimization problem is reduced to two scalar evaluations. The first missing datum is the frozen source normalization \(\kappa\), followed by rigorous enclosure of \(d(R)\). The finite prime constant remains separate. No RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_digamma_multiplier_monotonicity.py`
- `research/voevodsky/results/digamma_multiplier_monotonicity.json`
