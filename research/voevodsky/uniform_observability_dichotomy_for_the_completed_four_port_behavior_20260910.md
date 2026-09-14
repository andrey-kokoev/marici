# Uniform observability dichotomy for the completed four-port behavior

## Question

Does the completed four-port behavior admit a cutoff-independent lower bound?

## Claim boundary

The answer depends on the declared record topology. The source-labelled Fourier--Bohr coefficient port gives an isometric lower bound. The Euler-weighted analytic boundary synthesis alone cannot be bounded below. This does not identify the scalar analytic readout with the full observer.

## Problem

For a behavior map \(\beta\), decide whether there is a cutoff-independent \(c>0\) such that

\[
\|\beta x\|_{\rm rec}\ge c\|x\|_{\rm src}.
\]

A norm cannot be discussed before specifying which record coordinates it retains.

## Bold conjecture

The Euler-weighted four-port analytic boundary records alone are uniformly observable on the unweighted prime-power source.

## Named rivals

1. Euler half-density forces the analytic lower margin to zero.
2. The full source-labelled Fourier--Bohr coefficient record is uniformly observable, but this is a larger record topology.
3. A finite jet or finite constructor-word packet is sufficient uniformly over unbounded prime and grade cutoffs.

## Risky consequences

The conjecture requires every unit source atom \(e_{p,k}\) to have analytic image norm bounded below independently of \(p\) and \(k\). Rival 2 requires an exact Parseval identity for the complete labelled coefficient signal. Rival 3 requires one fixed truncation to remain injective at every cutoff.

## Strongest falsification attempt

For Euler-weighted synthesis \(U\), prior exact normalization gives

\[
\|Ue_{p,k}\|^2
=
\frac{1}{k^2}p^{-k}\|\Phi\|_2^2.
\]

Every \(e_{p,k}\) has unit norm in the unweighted arithmetic source. Hence, already at grade one,

\[
\|Ue_{p,1}\|=p^{-1/2}\|\Phi\|_2\longrightarrow0
\]

as \(p\) ranges through the primes. Therefore

\[
\inf_{x\ne0}\frac{\|Ux\|}{\|x\|}=0.
\]

The conjecture is false. This is not an off-diagonal Gram problem: a single normalized basis atom supplies the escaping sequence.

For the complete typed Fourier--Bohr coefficient record

\[
(\mathcal Mc)(t)=\sum_{\nu,\alpha}c_{\nu,\alpha}e^{it\ell(\nu)}e_{\nu,\alpha},
\]

the invariant-mean norm instead satisfies

\[
\|\mathcal Mc\|_{B^2}^2
=
\sum_{\nu,\alpha}|c_{\nu,\alpha}|^2.
\]

Thus this record has lower bound one on the labelled coefficient Hilbert module. Tensoring with a unitary-normalized faithful four-character observer preserves a positive fixed lower bound; with the standard normalized character transform, the bound remains one.

Finite jet and bounded word-depth rivals fail because the required detecting grade or native word length grows with source support.

## Exact residual

Uniform observability fails precisely under the projection

\[
\text{full labelled behavior record}
\longrightarrow
\text{Euler-weighted analytic boundary record}.
\]

Its singular values on \(e_{p,k}\) include

\[
\frac{1}{k}p^{-k/2}\|\Phi\|_2,
\]

whose infimum is zero. Endpoint, seam, and scalar attachments cannot restore a lower bound unless the completed record norm independently retains a uniformly faithful labelled coordinate.

## Disposition

The bold conjecture is rejected. Two non-equivalent completed observer statements survive:

- **Full behavior topology:** retain the source-labelled Fourier--Bohr coefficient port together with the normalized four-character packet. The observer is uniformly bounded below, with coefficient-channel lower bound one.
- **Analytic boundary topology:** retain only Euler-weighted four-port boundary synthesis and its scalar attachments. Uniform observability is impossible on the unweighted prime-power source; the normalized sequence \(x_p=e_{p,1}\) has record norm tending to zero.

Therefore the architecture is uniformly observable only because its full record retains the discrete labelled source coordinate. No downstream scalar or Euler-weighted analytic projection inherits that coercivity.
