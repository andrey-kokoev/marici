# Gauge companions commute with uniform Markov completion

## Question

Does finite-to-closed completion preserve the freely adjoined gauge companions and conjoints?

## Claim boundary

This packet treats diagonal sign gauges on uniformly contractive one-sided scalar Markov chains. It does not cover unbounded gauges, non-diagonal vertical maps, or other completion theories.

## Completed gauge

Let \(G_\infty\) be the bounded positive path-product operator for \(|a_i|\le\rho<1\). For a sign sequence \(\varepsilon_i\in\{\pm1\}\), define the diagonal unitary

\[
D_\varepsilon e_i=\varepsilon_i e_i.
\]

Then

\[
G_\infty^\varepsilon
=D_\varepsilon G_\infty D_\varepsilon
\]

has entries

\[
(G_\infty^\varepsilon)_{ij}
=\varepsilon_i\varepsilon_j
\prod_{k=i}^{j-1}a_k
=
\prod_{k=i}^{j-1}
(\varepsilon_k\varepsilon_{k+1}a_k).
\]

Thus it is exactly the completed path-product kernel for the transformed edges. Edge moduli are unchanged, so the same Schur bound applies.

## Completion comparison

Let \(P_n\) project onto the first \(n+1\) vertices. Since \(P_n\) commutes with \(D_\varepsilon\),

\[
P_nG_\infty^\varepsilon P_n
=D_{\varepsilon,n}
(P_nG_\infty P_n)
D_{\varepsilon,n}.
\]

Therefore completing a finite gauge companion and gauging the completed chain give the same closed operator. The completion-comparison cell is the identity on the common matrix coefficients.

## Coherence

Pointwise sign multiplication commutes with restriction and strong completion. Consequently companion composition comparisons, their pentagon, contiguous Beck–Chevalley cells, and the completion comparison paste strictly in this sector. Conjoints obey the same equations because each sign unitary is self-inverse.

## Hostile boundary

A diagonal multiplier not uniformly bounded does not define a bounded vertical arrow on \(\ell^2\), so no completed companion is admitted. Finite truncation alone cannot authorize it.

## Disposition

Uniform Markov completion preserves the gauge subgroupoid's companions and conjoints. The resulting restricted equipment fragment now includes finite-to-closed compatibility; global completion-equipment compatibility remains open.

## Verification

- `research/voevodsky/checkers/check_gauge_companion_completion.py`
- `research/voevodsky/results/gauge_companion_completion.json`
