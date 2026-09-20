# Xi-torsion lift iteration 4: the atomic endpoint projection restores a fixed exponential observer for varying shells

## Key separation

The full Clark primitive

\[
K_{1,b}=\delta_b-\frac12|\cdot-b|
\]

has two different endpoint regularities. In the endpoint distribution,
`delta_b` produces atomic masses, while the absolute-value leg produces a
locally integrable/piecewise polynomial contribution. Therefore the singular
atomic projection is source-derived and separates the delta channel before
Laplace transformation.

Let `A_end` denote this atomic endpoint projection.

## Shell formula

For a shell `[a,b]`, seam `c=b`, and `f=e^(z dot)`, the delta endpoint is

\[
e_{f,\delta_b}(t)
=\frac12\left[
 e^{zb}\delta(t)-e^{za}\delta(t-(b-a))
\right].
\]

Its Laplace coordinate is

\[
A_{\rm end}H_{a,b,b}(z)
=
\frac12e^{zb}-\frac12e^{z(2a-b)}.
\]

The varying shell width has become a pair of pure exponentials. No common
smooth atom needs to be divided out.

## Arithmetic distinctness

For consecutive primes `p<q`, put

\[
a=k\log p,
\qquad b=k\log q.
\]

The outgoing frequencies are `k log q`; unique factorization gives

\[
k\log q=\ell\log s
\Longrightarrow q=s,\ k=\ell.
\]

The reflected frequencies are

\[
k\log(p^2/q).
\]

Unique factorization also makes these pairwise distinct. An outgoing frequency
cannot equal a reflected one: exponentiating would give

\[
q_1^kq_2^\ell=p_2^{2\ell},
\]

which is impossible for consecutive distinct primes by comparison of prime
valuations.

Hence all atomic endpoint frequencies, with their orientation, remain labelled
after codiagonalization.

## Continuous coefficient recovery

For a loaded packet

\[
G(z)=\sum_{p,k}d_{p,k}
\left(e^{zk\log q(p)}-e^{zk\log(p^2/q(p))}\right),
\]

observe `G` on a vertical line `z=R+it`. Bohr averaging in `t` extracts the
outgoing coefficient:

\[
d_{p,k}e^{Rk\log q(p)}
=
\lim_{T\to\infty}\frac1{2T}
\int_{-T}^T G(R+it)e^{-itk\log q(p)}dt.
\]

Therefore

\[
|d_{p,k}|e^{Rk\log q(p)}
\le\sup_t|G(R+it)|.
\]

Since `log q(p)>log p`, any desired source weight
`e^(delta k log p)` is controlled once `R` exceeds `delta` plus the fixed loss
in the frozen loading. Summation over prime powers requires the same additional
Euler margin as in the two-line theta estimate.

Thus the atomic endpoint channel gives a continuous projective recovery map
without a lower bound on prime gaps.

## Scope and qualification

This proves strictness of the **atomic endpoint codiagonal** for the standard
consecutive-prime shells and their common grade scaling. It does not yet prove
strictness of the entire bordered packet map, but a continuous left inverse of
one component is sufficient to make the full labelled synthesis a topological
embedding onto its range.

The argument requires that the complete bordered target retain endpoint
singular order so that `A_end` is continuous. If the declared topology first
combines atomic and regular endpoint pieces into an undifferentiated scalar
Laplace value, this projection is unavailable.

## Consequence for H-border

`H_border` is assembled from exactly these shell primitives, so its atomic
endpoint coordinate is in a Fourier/Bohr-recoverable exponential range. This
proves recoverability of one faithful bordered coordinate and supplies a
candidate strict graph topology for `J_B`.

The next step is to verify from the declared bordered rigging that atomic
endpoint projection is continuous and survives all four Fourier charts and
cutoff completion. That continuity, rather than nonuniform shell width, is now
the remaining gate.