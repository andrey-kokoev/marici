# Finite Laurent cutoffs require a coherent negative-binomial remainder port

## Corrected tail theorem

For the invariant centered kernel

\[
 \widehat K_0^+=\frac{\bar z}{z(1+u)^3},\qquad u=z\bar z,
\]

write its exterior chart with `v=u^(-1)` as

\[
 \widehat K_0^+=z^{-4}\bar z^{-2}(1+v)^{-3}.
\]

Let

\[
 P_N=z^{-4}\bar z^{-2}\sum_{n=0}^N
 (-1)^n\binom{n+2}{2}v^n.
\]

Then the omitted tail is exactly

\[
 \boxed{
 R_N=(-1)^{N+1}z^{-4}\bar z^{-2}
 \frac{v^{N+1}Q_N(v)}{(1+v)^3},}
\]

where

\[
 2Q_N(v)=(N+2)(N+3)+2(N+1)(N+3)v+(N+1)(N+2)v^2.
\]

This replaces the geometric-tail identity derived from the noninvariant
coordinate Green representative.

## Grade-three tail certificate

Let `M3` be the magnetic grade-three density.  At the exact witness
`z=2, bar(z)=3`, ignoring only the harmless alternating overall sign,

\[
 M_3(R_N)=\frac{65\,6^{-N-7}}{1647086}\,P_6(N),
\]

with

\[
\begin{aligned}
P_6(N)={}&117649N^6+1142876N^5+4482667N^4\\
&+9331658N^3+11378290N^2+8050616N+2559072.
\end{aligned}
\]

Every coefficient is strictly positive. Therefore

\[
 \boxed{M_3(R_N)\ne0\quad\text{for every integer }N\geq0.}
\]

No late cutoff can become an exact physical stabilization.  The exact finite
presentation is the pair `(P_N,R_N)`, and linearity gives

\[
 M_3(P_N)+M_3(R_N)=M_3(\widehat K_0).
\]

## Meaning

The remainder is not an error bar. It is the continuation record required to
glue the finite Laurent chart back into the global spin-two section. Dropping
it changes both the source and its grade-three output. A passing finite matrix
census without this port therefore certifies only a presentation truncation.

## Evidence

`checkers/physical_laurent_completion_cutoff_checks.py` verifies the tail
identity through hostile cutoffs, derives the symbolic sextic witness, proves
its positivity for all nonnegative integer cutoffs, and checks readout
reconstruction.
