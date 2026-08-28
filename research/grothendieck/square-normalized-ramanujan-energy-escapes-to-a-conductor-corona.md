# Square-Normalized Ramanujan Energy Escapes to a Conductor Corona

## Profinite realization

Regard every squarefree residue packet as a locally constant function on
\(\widehat{\mathbb Z}\) with normalized Haar measure. For squarefree \(Q\),
set

\[
w_Q
=
\frac{Q}{\varphi(Q)}
\mathbf 1_{x\bmod Q\in(\mathbb Z/Q\mathbb Z)^\times}.
\]

Then

\[
\int w_Q=1,
\qquad
\|w_Q-1\|_2^2
=
\sigma_Q^2
=
\frac{Q}{\varphi(Q)}-1.
\]

Define the square-normalized fluctuation

\[
v_Q=\frac{w_Q-1}{\sigma_Q}.
\]

It has mean zero and norm one.

## Exact cylinder pairing

Let \(h\) be a cylinder function factoring through a fixed modulus \(M\).
For every squarefree \(Q\) divisible by \(M\), the Chinese remainder
theorem gives

\[
\langle w_Q,h\rangle
=
\frac1{\varphi(M)}
\sum_{\substack{a\bmod M\\(a,M)=1}}h(a).
\]

Meanwhile

\[
\langle1,h\rangle
=
\frac1M\sum_{a\bmod M}h(a).
\]

Therefore

\[
\langle v_Q,h\rangle
=
\frac{
\operatorname{Avg}_{(a,M)=1}h
-\operatorname{Avg}_{a\bmod M}h
}{\sigma_Q}.
\]

Along primorial cutoffs, \(\sigma_Q\to\infty\). The numerator is fixed, so

\[
\langle v_Q,h\rangle\longrightarrow0
\]

for every fixed cylinder observable.

## Weak escape

Cylinder functions are dense in
\(L^2(\widehat{\mathbb Z})\), and \(\|v_Q\|_2=1\). Hence

\[
v_Q\rightharpoonup0
\]

weakly, while its norm remains one. No subsequence can converge strongly: a
strong limit would also be the weak limit zero, contradicting norm one.

Thus square-current normalization removes the divergent size but not the
completion defect. The entire normalized fluctuation energy escapes to
characters of increasing conductor.

## Meaning

The profinite packet has three distinct completion components:

1. a stable mean mode;
2. a divergent square-covariance line;
3. a unit fluctuation state escaping to conductor infinity.

The third is not visible to any fixed finite-modulus observer. It is a corona
boundary state of the growing residue tower.

This is the same structural phenomenon previously found in translated seam
tails: finite observers converge to zero while a full relationship norm stays
nonzero. Here the escaping direction is arithmetic conductor rather than
archimedean translation.

## Consequence for RH

A temperedness proof cannot proceed by:

- retaining all finite Ramanujan modes;
- dividing by their exact variance;
- and taking an ordinary Hilbert limit.

That sequence has no strong limit. The completion must retain an independent
conductor-corona coordinate and couple it to the archimedean logarithmic
boundary current.

The revised source object is therefore at least two-dimensional in its
completion axes:

- logarithmic position \(u\), carrying the half-density temperedness test;
- arithmetic conductor, carrying the escaping Ramanujan fluctuation.

The missing coherence is a source-derived incidence between those two
boundaries. Scalar prime density is a later pushforward.

## Falsifier

A proposed completion fails if it:

- claims strong convergence of \(v_Q\) in profinite \(L^2\);
- uses only fixed-conductor cylinder tests;
- treats weak convergence to zero as disappearance of the state;
- or discards the unit norm when passing to the conductor limit.

