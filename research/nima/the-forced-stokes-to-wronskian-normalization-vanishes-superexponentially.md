# The forced Stokes-to-Wronskian normalization vanishes superexponentially

## Result

Let

\[
L=\log p,
\qquad
s_p=4\bigl(H(L)-H(2L)\bigr)
=4\int_L^{2L}e^{-\pi q^2}\,dq>0,
\]

and let the arithmetic-to-theta incidence coefficient be

\[
\kappa_p
=2L\sum_{k\ge1}p^{-k/2}\Phi'(kL)<0.
\]

The scalar forced on any faithful one-dimensional comparison between the
retained Stokes odd line and the Wronskian odd line is

\[
\lambda_p=\frac{-\kappa_p}{2s_p}>0.
\]

Then

\[
\lambda_p\longrightarrow0
\]

faster than every inverse power of \(p\).

## Lower bound for the Stokes denominator

For \(L\ge1\), the interval

\[
[L,L+L^{-1}]
\]

lies in \([L,2L]\).  Since the Gaussian decreases on the positive half-line,

\[
s_p
\ge \frac4L
\exp\!\left(-\pi(L+L^{-1})^2\right).
\]

Thus \(s_p\) has logarithmic-Gaussian scale
\(e^{-\pi(\log p)^2}\), up to elementary factors.

## Upper bound for the incidence numerator

The established theta derivative estimate gives constants \(A,B>0\) such
that

\[
|\Phi'(u)|\le A e^{-Be^{2u}}
\]

for large \(u\).  At \(u=kL\),

\[
|\Phi'(kL)|\le A e^{-Bp^{2k}}.
\]

Consequently, after enlarging a constant for finitely many small primes,

\[
|\kappa_p|
\le C L p^{-1/2}e^{-Bp^2}.
\]

The terms \(k\ge2\) are absorbed into the first-label majorant because their
exponents are at most \(-Bp^4\).

Combining the estimates yields

\[
0<\lambda_p
\le C' L^2p^{-1/2}
\exp\!\left(
-Bp^2+\pi(L+L^{-1})^2
\right).
\]

Since \(p^2\) dominates \((\log p)^2\), this tends to zero faster than
\(p^{-N}\) for every fixed \(N\).

## Closed-range consequence

Suppose the primewise comparison is assembled diagonally on unweighted
\(\ell^2\):

\[
T e_p=\lambda_p e_p.
\]

Then \(T\) is not bounded below, because

\[
\|Te_p\|=\lambda_p\to0
\]

while \(\|e_p\|=1\).  An injective bounded operator between Hilbert spaces has
closed range only if it is bounded below.  Hence this unweighted diagonal
assembly cannot be the closed-range analytic--arithmetic pushout required by
G1.1.

Indeed, the superexponential decay makes the diagonal operator compact (and,
under the displayed majorant, trace class).  An injective compact operator on
an infinite-dimensional Hilbert space cannot have closed range.

## Interpretation

This is not a contradiction in the source programme.  It proves that the
source-authorized comparison, if it exists globally, must carry a weighted
pullback metric that absorbs \(\lambda_p\), or must retain additional
noncompact source ports.  Such weighting must be derived from the incidence
map; inserting \(\lambda_p^{-1}\) by hand would be circular.

Therefore the local normalization is forced and positive, but its raw
all-prime assembly supplies an obstruction rather than a uniform coercivity
theorem.  The weighted-metric identification, radical descent, and full
closed-range theorem remain open.  No RH conclusion is authorized.
