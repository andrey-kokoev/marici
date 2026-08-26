# Translation-commutant metric cannot collocate theta source and endpoint

## Bounded question

Can a positive metric derived from the logarithmic translation carrier turn
the theta source-to-endpoint cross transfer into a diagonal Herglotz
coefficient?

## Finite spectral criterion

Let \(A=A^*\) act on a finite-dimensional Hilbert space. A positive metric
\(G>0\) preserves self-adjointness of the same carrier exactly when

\[
GA=A^*G=AG.
\]

To rewrite

\[
b_f^*(A-zI)^{-1}b_0
\]

as the diagonal coefficient of \(b_0\) in the \(G\)-metric, one also needs

\[
Gb_0=b_f.
\]

Let \(P_\lambda\) be the spectral projections of \(A\), and set

\[
x_\lambda=P_\lambda b_0,
\qquad
y_\lambda=P_\lambda b_f.
\]

Because \(G\) commutes with \(A\), it acts independently on every eigenspace.
A positive-definite block \(G_\lambda\) satisfying

\[
G_\lambda x_\lambda=y_\lambda
\]

exists exactly under the following conditions:

- if \(x_\lambda=0\), then \(y_\lambda=0\);
- if \(x_\lambda\ne0\), then
  \[
  \langle x_\lambda,y_\lambda\rangle
  \]
  is strictly positive and real.

Necessity follows from positivity:

\[
\langle x_\lambda,y_\lambda\rangle
=
\langle x_\lambda,G_\lambda x_\lambda\rangle>0.
\]

For sufficiency, choose a basis whose first vector is parallel to
\(x_\lambda\). The required first column is fixed by \(y_\lambda\); Hermitian
symmetry fixes the first row. A sufficiently large positive lower block makes
the Schur complement positive.

For simple spectrum, this says more transparently that every visible spectral
ratio

\[
\frac{(b_f)_j}{(b_0)_j}
\]

must be positive and real.

## Translation carrier

For the full logarithmic transport

\[
A=-i\partial_q,
\]

every bounded metric commuting with \(A\) is a Fourier multiplier:

\[
\widehat{G\psi}(\xi)=g(\xi)\widehat\psi(\xi).
\]

An equivalent Hilbert metric requires constants \(0<c\le C<\infty\) such that

\[
c\le g(\xi)\le C
\]

almost everywhere.

The endpoint port satisfies

\[
\widehat{\delta_0}(\xi)=1
\]

up to the fixed Fourier normalization. Therefore the colocation condition

\[
G\delta_0=f
\]

forces

\[
g(\xi)=\widehat f(\xi).
\]

## Source-decay obstruction

The completed theta source used in the tail construction is integrable in its
logarithmic coordinate. By the Riemann--Lebesgue lemma,

\[
\widehat f(\xi)\longrightarrow0
\]

as \(|\xi|\) tends to infinity. Consequently \(g\) cannot have a positive
lower bound.

Hence no boundedly invertible positive metric in the translation commutant can
collocate the endpoint distribution with the theta source.

This obstruction precedes any analysis of theta zeros. It uses only source
decay and carrier covariance. Allowing a nonnegative or unbounded multiplier
changes the topology and reopens the completion-at-infinity problem: the
metric can lose entire high-frequency directions.

## Meaning

The two ports are not different coordinates of one positive state within an
equivalent translation-covariant Hilbert geometry. Their distinction is
structural. Any successful diagonalization must therefore do at least one of
the following:

1. enlarge the state space with an independent seam or boundary sector;
2. change the carrier rather than merely its commuting metric;
3. use a rigged or relative metric and prove strict completion stability;
4. retain the cross transfer as the primary non-self-adjoint observable.

## Relation to resistance

An effective-resistance bound controls anchored scalar deviation. It does not
supply a lower Hilbert-frame bound, and it does not change the spectral
multiplier obstruction above. It may certify a scalar normalization unit after
the relevant graph energy is source-derived, but cannot collocate the ports in
an equivalent translation metric.

## Result

The shortest Herglotz promotion route is closed for the native translation
carrier. A source-derived equivalent metric commuting with logarithmic
translation cannot identify \(\delta_0\) with the integrable theta source.
The missing construction must change or enlarge the operator system rather
than reweight the existing carrier.

## Sharp falsifier

Any proposed translation-covariant colocation metric must exhibit its
multiplier \(g\). It fails if:

- \(g\ne\widehat f\);
- \(g\) is not positive real almost everywhere;
- \(g\) or \(g^{-1}\) is unbounded in the claimed equivalent topology;
- the endpoint distribution is silently removed from the declared domain.
