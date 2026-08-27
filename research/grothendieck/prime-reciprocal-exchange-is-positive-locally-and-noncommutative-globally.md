# Prime reciprocal exchange is positive locally and noncommutative globally

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact doubled arithmetic constructor

## Local exchange

For a prime \(p\), retain the direct and reciprocal Mellin amplitudes in one
two-sector operator:

\[
E_p(s)=
\begin{pmatrix}
0&p^{-s}\\
p^{s-1}&0
\end{pmatrix}.
\]

Their product is independent of \(s\):

\[
E_p(s)^2=p^{-1}I.
\]

Consequently

\[
(I-E_p)^{-1}=\frac{I+E_p}{1-p^{-1}},
\qquad
\det(I-E_p)=1-p^{-1}.
\]

The local norm factor is not fitted. It is the pull–push composite of the two
reciprocal amplitudes.

## Positivity on the unitary seam

Put \(s=1/2+it\). Then

\[
p^{s-1}=\overline{p^{-s}},
\]

so \(E_p\) is Hermitian. Its eigenvalues are

\[
\pm p^{-1/2}.
\]

Therefore

\[
I-E_p>0
\]

with eigenvalues \(1\mp p^{-1/2}\). The local two-sector comparator is
strictly positive at every prime and every height on the seam.

This positivity is unavailable after scalar projection: each diagonal entry
alone is free, while the off-diagonal exchange retains the reciprocal
relationship.

## Two primes create a nonabelian channel

For distinct primes \(p,q\),

\[
[E_p,E_q]
=
\begin{pmatrix}
p^{-s}q^{s-1}-q^{-s}p^{s-1}&0\\
0&p^{s-1}q^{-s}-q^{s-1}p^{-s}
\end{pmatrix}.
\]

On the seam its upper entry is

\[
\frac{2i}{\sqrt{pq}}
\sin\left(t\log\frac qp\right),
\]

and the lower entry is its negative. Hence the prime exchanges fail to
commute except at isolated resonant heights.

This is the first source-derived nonabelian comparison channel in the current
Hilbert–Pólya lane. It cannot be removed by the scalar gauge transformation of
ledger 3059.

## Global obstruction

The local determinant product is

\[
\prod_p(1-p^{-1}),
\]

which collapses. Thus the primitive boundary divergence reappears exactly as
the determinant anomaly of the doubled exchange system. A global operator
requires the already identified primitive and prime-square currents; simply
normalizing each block and multiplying is not a completed construction.

There is a second gate. Because exchanges for different primes do not
commute, a product requires a source-derived ordering or a path-ordered
connection. Ordering by prime norm is canonical as a filtration, but it must
be proved compatible with cutoff completion and reciprocal sewing. An
order-dependent product cannot silently replace the commutative Euler
product.

## Next falsifier

Form the ordered two-prime product for \(2,3\) and compare:

\[
(I-E_2)(I-E_3)
\]

and

\[
(I-E_3)(I-E_2).
\]

Their residual is the displayed commutator. Any proposed scalar determinant
or trace that erases it before proving a boundary law has returned to the
gauge-trivial channel.

## Scope

The local algebra, seam positivity, two-prime commutator, and determinant
divergence are exact. No canonical global ordered product, self-adjoint Dirac
operator, determinant equal to \(\xi\), discrete spectrum, or RH theorem is
constructed.
