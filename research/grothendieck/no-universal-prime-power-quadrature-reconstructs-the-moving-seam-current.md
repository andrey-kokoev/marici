# No universal prime-power quadrature reconstructs the moving-seam current

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact descent no-go

## The tempting closure

The moving-seam theorem expresses the continuous doubled forcing as

\[
\mathcal K(z)=\int_0^\infty \partial_L\mathcal K_{W_L}(z)\,dL.
\]

Prime-scale transport exposes only the discrete seam positions

\[
\Lambda=\{k\log p:p\in\mathbb P,\ k\ge1\},
\]

where \(\mathbb P\) denotes the primes. A tempting completion would assign
fixed weights (w_\lambda) and assert a
universal quadrature

\[
\int_0^\infty h(L)\,dL
=\sum_{\lambda\in\Lambda}w_\lambda h(\lambda)
\]

for every admissible moving-boundary density (h).

## Exact obstruction

The set (Lambda) is locally finite. In particular, the open interval

\[
(\log2,\log3)
\]

contains no logarithm of a prime power. Choose a nonzero nonnegative smooth
bump (h) supported strictly inside that interval. Then

\[
h(\lambda)=0
\]

for every (lambda\in\Lambda), while

\[
\int_0^\infty h(L)\,dL>0.
\]

No choice of fixed atomic weights can therefore reconstruct Lebesgue
integration on a source class containing such local variations.

## Meaning for the theta programme

The continuous moving-seam identity is genuine, and the finite Clark-cut
cocycle is exact. But arithmetic sampling cannot turn that identity into a
global conservation law by a universal quadrature rule.

A surviving descent theorem must restrict the seam densities to a special
theta-generated class and use additional relations among their unsampled
values. Poisson reflection, the heat equation, or a reproducing-kernel
property could supply such rigidity. The weights and interpolation law must
be derived from that source structure; they cannot be inferred from the
prime-power sample set alone.

This exposes the precise information gap:

- the continuous source knows every seam position (L);
- arithmetic transport observes only (Lambda);
- the missing constructor must recover the intervening seam variation from
  theta-specific coherence.

The problem is therefore sampling faithfulness, not another local positivity
or matrix-curvature calculation.

## Falsifier and next gate

Any proposed universal arithmetic quadrature is killed by a smooth bump in
the interval ((\log2,\log3)). A theta-specific proposal survives this
falsifier only if that bump is not an authorized source variation and the
reason is proved independently.

The next gate is to characterize the smallest source-generated function
space containing

\[
L\longmapsto
\Phi(L)\bigl(H_+(L,z)-H_-(L,z)\bigr)
\]

and decide whether evaluation on (Lambda) is faithful there. If it is not,
the moving-seam conservation route closes.

## Verification

The checker verifies the explicit empty interval between the first two
prime-power seam samples.
