# The sheet-aware comoving lift fixes support, not prime multiplicity

## Reciprocal comoving correspondence

Fix prime `p`, prime-power depth `k`, and sheet sign

\[
\varepsilon\in\{+1,-1\}.
\]

Define the ambient comoving displacement by

\[
u=q-\varepsilon k\log p,
\qquad
q=\varepsilon k\log p+u.
\]

The projection to observed logarithmic scale is

\[
\pi_k(p,\varepsilon,u)
=\varepsilon k\log p+u.
\]

Fourier reversal lifts to

\[
\widetilde{\mathcal F}
(p,\varepsilon,u)
=(p,-\varepsilon,-u),
\]

and satisfies

\[
\pi_k\widetilde{\mathcal F}=-\pi_k.
\]

Thus the reciprocal action is linear and label-preserving on the comoving
correspondence.

## Moving atoms become one zero section

The two observed atoms at

\[
q=\pm k\log p
\]

both lift to `u=0`. Their relative orientation is retained by the sheet sign.
For coefficients `a_{p,k}`, define the zero-section current

\[
\mu_k
=
\sum_p a_{p,k}
\sum_{\varepsilon=\pm1}
\varepsilon\,
\delta_{(p,\varepsilon,0)}.
\]

It is anti-invariant:

\[
\widetilde{\mathcal F}_*\mu_k=-\mu_k.
\]

Its pushforward is exactly the relative atomic flux:

\[
(\pi_k)_*\mu_k
=
\sum_p a_{p,k}
\left(
\delta_{k\log p}-\delta_{-k\log p}
\right).
\]

The apparent traveling boundary has therefore become a fixed incidence
subobject before pushforward.

## Position pairing becomes sign multiplication

On the zero section,

\[
\pi_k=\varepsilon k\log p.
\]

For an even theta profile `Phi`, pairing the oriented current with the pulled
back position probe gives

\[
\begin{aligned}
\langle\mu_k,\pi_k\Phi(\pi_k)\rangle
&=
\sum_p a_{p,k}
\sum_{\varepsilon=\pm1}
\varepsilon
(\varepsilon k\log p)
\Phi(k\log p)\\
&=
2\sum_p a_{p,k}
k(\log p)\Phi(k\log p).
\end{aligned}
\]

The positivity is now structural: the flux orientation sign and the signed
position coordinate multiply to `+1`. With connected coefficient

\[
a_{p,k}=\frac1k p^{-k/2},
\]

the depth cancels and the remaining arithmetic weight is `log p`.

## Two independent chart axes

The earlier comoving scale-valuation theorem showed that an adjacent depth
cell has two front charts, inner and outer. Reciprocal completion adds a
different two-valued coordinate, the sheet sign. The complete local atlas is
therefore a product of two binary axes:

```text
reciprocal sheet:  plus / minus
valuation face:    inner / outer
```

Fourier exchanges the first axis. Čech boundary incidence exchanges the
second. The Toeplitz flux is the oriented zero-section boundary of this
four-chart cell. Treating either involution as the other loses source data.

## What the lift does not repair

For each bounded observed `q` interval, only finitely many zero-section prime
labels map into it, so the zero-section projection is locally proper. But the
mass over prime scale is unchanged. At critical primitive weight it still
grows exponentially under global pushforward.

Hence the comoving lift repairs traveling support but not arithmetic
multiplicity. It cleanly separates the two issues:

- support and reciprocal coherence live in `(epsilon,u)`;
- completion grade lives in the prime-scale measure.

The primitive, square, and connected measures must still land in different
target topologies.

## Result

The sheet-aware comoving correspondence turns every reciprocal prime-power
pair into one fixed oriented zero section and makes Fourier act by
`(epsilon,u) -> (-epsilon,-u)`. The positive Mellin-position pairing becomes
the product of two source signs. Together with the inner/outer front atlas,
the local source is a `2×2` chart system. This resolves support geometry but
leaves the critical primitive multiplicity as an independent completion
obstruction.
