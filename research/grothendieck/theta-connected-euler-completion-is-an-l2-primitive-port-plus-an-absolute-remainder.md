# Theta connected Euler completion is an L2 primitive port plus an absolute remainder

## Connected expansion in the right open sector

Let \(s=\sigma+it\) with \(\sigma>1/2\). At finite prime support \(S\), write

\[
 \log Z_S(s)
 =\sum_{p\in S}\sum_{k\ge1}{p^{-ks}\over k}.
\]

Separate the primitive channel from the prime-square and higher channels:

\[
 P_S(s)=(p^{-s})_{p\in S},
\]

and

\[
 R_S(s)=\sum_{p\in S}\sum_{k\ge2}{p^{-ks}\over k}.
\]

## Canonical completion

The primitive packet has a canonical Hilbert completion because

\[
 \|P(s)\|_{\ell^2(\mathbb P)}^2
 =\sum_p p^{-2\sigma}<\infty.
\]

The remainder aggregates absolutely:

\[
 \sum_p\sum_{k\ge2}{|p^{-ks}|\over k}
 \le
 \sum_p{p^{-2\sigma}\over1-p^{-\sigma}}<\infty.
\]

Thus the finite connected packets converge in the source-derived target

\[
 Y_s^+=\ell^2(\mathbb P)\oplus\mathbb C,
\]

through

\[
 y_S(s)=(P_S(s),R_S(s)).
\]

Cutoff bonding extends the primitive vector by zero on new labels and adds
the absolutely convergent remainder. These maps are canonical and require no
division by an Euler product.

## The unique discontinuous scalar operation

Recovering the scalar logarithm requires summing the primitive coordinates:

\[
 \Sigma(P)=\sum_pP_p.
\]

This is not a continuous functional on \(\ell^2(\mathbb P)\), because its
formal representing vector is the constant sequence, which does not belong
to \(\ell^2(\mathbb P)\). Hence

\[
 \log Z(s)=\Sigma(P(s))+R(s)
\]

is a relative boundary pairing rather than an ordinary continuous functional
on \(Y_s^+\) throughout \(1/2<\sigma\le1\).

The completion defect has therefore been isolated to one typed operation:
primitive-prime aggregation.

## Agreement with the connected Dirac flux

Packet 194 gives the finite divided-diagonal flux

\[
 \sum_{p\in S}{\log p\over p-1}.
\]

Its \(k\ge2\) portion converges absolutely, since

\[
 \sum_p\log p\sum_{k\ge2}p^{-k}
 =\sum_p{\log p\over p(p-1)}<\infty.
\]

The divergent portion is exactly the primitive term

\[
 \sum_p{\log p\over p}.
\]

Thus the state completion and flux completion identify the same interface:
the primitive channel is Hilbert-visible but scalar aggregation is
unbounded; square and higher channels are already absolutely aggregable.

## Consequences for the full block

In the right open sector, the smallest non-lossy connected arithmetic block
is not five unrelated scalar corrections. It is:

- one labelled primitive \(\ell^2\) port;
- one absolutely convergent connected remainder, with the square channel
  retained as a type even though it causes no convergence defect here; and
- an external relative boundary functional supplied by Poisson and
  archimedean sewing.

This prime-labelled block is downstream of Fourier--Tate sewing. Prime support
is not closed under the additive Fourier transform, so the reciprocal
construction must act on the aggregate theta lattice first. The determinant
logarithm produces the primitive port only afterward. Packet 197 makes this
operation-ordering constraint explicit.

## Falsifiers

This decomposition fails if, at one fixed \(s\) with \(\sigma>1/2\):

1. \(P(s)\notin\ell^2(\mathbb P)\);
2. the \(k\ge2\) remainder is not absolutely convergent;
3. primitive aggregation extends continuously to all of
   \(\ell^2(\mathbb P)\); or
4. a divergent connected flux remains after deleting the \(k=1\) terms.

## Scope

This constructs the smallest completed connected arithmetic target in one
open sector and identifies its sole scalar boundary obstruction. It does not
construct the reciprocal relative trace, archimedean sewing, a Fredholm
parametrix, or an RH proof.
