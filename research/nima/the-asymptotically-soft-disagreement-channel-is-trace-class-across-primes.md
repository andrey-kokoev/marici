# The asymptotically soft disagreement channel is trace class across primes

## Prime-labelled disagreement synthesis

For each prime \(p\), let

\[
d_p
=
W_{2\log p}-W_{\log p}
\in
\mathcal H_p^{\mathrm{win}},
\]

where the prime fibers are retained as orthogonal valuation-labelled
components.

Define

\[
J_{\mathrm{dis}}:
\ell^2(\mathbb P)
\longrightarrow
\bigoplus_{p}
\mathcal H_p^{\mathrm{win}}
\]

by

\[
J_{\mathrm{dis}}e_p=d_p.
\]

Because the target fibers are orthogonal, the singular values of this
diagonal rank-one synthesis are exactly

\[
s_p(J_{\mathrm{dis}})
=
\|d_p\|_\nu.
\]

## Super-polynomial estimate

The raw disagreement bound is

\[
\|d_p\|_\nu
\le
C(\log p)^{-1/2}
\exp\left[
-\frac\pi8(\log p)^2
\right].
\]

For every \(N>0\), the right-hand side is eventually bounded by \(p^{-N}\).
Choosing \(N>1\) gives

\[
\sum_p\|d_p\|_\nu<\infty.
\]

Therefore

\[
J_{\mathrm{dis}}\in\mathfrak S_1.
\]

The unweighted prime-labelled disagreement synthesis is already trace class.

## Euler-weighted channels

If a source coefficient \(a_p\) of at most polynomial growth or decay is
attached, define

\[
J_a e_p=a_pd_p.
\]

Then

\[
|J_a\|_{\mathfrak S_1}
=
\sum_p|a_p|\|d_p\|_\nu<\infty
\]

for every fixed polynomial-order profile \(|a_p|\le Cp^m\).

In particular, the primitive, square, and mixed Euler weights preserve trace
class.

## Cutoff convergence

Let \(P_X\) be projection onto primes \(p\le X\). Then

\[
\|J_{\mathrm{dis}}-J_{\mathrm{dis}}P_X\|_{\mathfrak S_1}
=
\sum_{p>X}\|d_p\|_\nu
\longrightarrow0.
\]

Thus finite-prime truncations converge in trace norm, not merely strongly or
in operator norm.

This provides a completion mode fully compatible with determinant-line
constructions on the disagreement channel.

## No contradiction with local area collapse

Each finite prime endpoint plane remains two-dimensional, but the
disagreement singular value tends to zero. Globally, these vanishing
singular values form a nuclear channel.

Therefore:

- local uniform inversion fails;
- global bounded synthesis succeeds;
- the disagreement incidence is compact and trace class;
- its inverse is unbounded and unauthorized.

Softness is not a defect when the constructor uses the forward relation only.

## Graph-relation formulation

The first Adams cell should retain the graph

\[
\Gamma(J_{\mathrm{dis}})
=
\{(c,J_{\mathrm{dis}}c):c\in\ell^2(\mathbb P)\}
\]

rather than identifying the source and target disagreement fibers
isomorphically.

The graph is closed because \(J_{\mathrm{dis}}\) is bounded. Its target
projection is compact; its source projection remains bounded.

This is the correct asymmetry for a completion-stable incidence relation.

## Determinant qualification

Trace class of \(J_{\mathrm{dis}}\) does not automatically make every
Schur return trace class. If a bounded resolved propagator \(R\) acts
between the incidence legs, then

\[
J_{\mathrm{dis}}^*RJ_{\mathrm{dis}}
\]

is trace class, indeed it is a product of Hilbert--Schmidt maps and a bounded
operator.

Thus a determinant-class endpoint return becomes available once the
auxiliary resolvent is uniformly bounded.

## Prime diagonality

The theorem uses the source valuation decomposition so that prime fibers are
orthogonal. If prime pushforward mixes fibers before the trace-class
factorization is formed, the singular values are no longer the one-index
norms above.

The trace-class result must therefore be established before any
nonfaithful prime pushforward.

## Hostile

Normalize each \(d_p\) to unit length before taking the direct sum. The
resulting synthesis has infinitely many singular values equal to one and is
not compact. The fitted local repair destroys the global nuclear structure.

## Frontier

The completion disposition of the soft endpoint direction is now fixed:

\[
\text{do not invert it;}
\qquad
\text{retain it as a trace-class prime-labelled incidence.}
\]

The remaining local Adams theorem is the quadratic Green identity for the
forward relation and the bounded auxiliary return.
