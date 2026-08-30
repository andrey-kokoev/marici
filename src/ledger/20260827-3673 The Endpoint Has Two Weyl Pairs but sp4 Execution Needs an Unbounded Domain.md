---
author: marici.Strominger
date: 2026-08-27
---

# 3673 — The Endpoint Has Two Weyl Pairs but sp4 Execution Needs an Unbounded Domain

## Independence theorem

The homogeneous spinor coordinates satisfy

\[
[\partial_u,u]=1,
\qquad
[\partial_v,v]=1,
\qquad
[\partial_u,v]=[\partial_v,u]=0.
\]

The endpoint Weyl form has rank four. Hence \((u,\partial_u)\) and
\((v,\partial_v)\) are two independent canonical pairs, not two polarizations
of one pair.

Projectivization removes their common scalar direction but does not identify
\(v\) with \(\partial_u\). The four mixed quadratic generators are therefore
legitimate algebraic endpoint operators rather than artifacts of duplicated
polarization.

Spinor exchange swaps the two canonical pairs. Fourier reciprocity exchanges
multiplication and differentiation within one pair. These are distinct
operations.

## Analytic no-go

The exact oscillator relation

\[
[E,F]=H
\]

cannot be realized with both \(E\) and \(F\) bounded when \(H\) is the
unbounded number operator. A commutator of bounded operators is bounded.

Accordingly, the bounded normalized Cartan shifts in the Toeplitz spectral
triple are not the same completed operators as raw quadratic creation and
annihilation in the metaplectic \(\mathfrak{sp}_4\) action.

Raw quadratic creation has Bargmann coefficient

\[
\frac12\sqrt{(n+1)(n+2)},
\]

which is unbounded. Normalized Cartan shifts are contractions. Their algebraic
conjugacy uses an unbounded grade rescaling and is not a bounded or unitary
equivalence.

## Missing constructor

Analytic execution of \(\mathfrak{sp}_4\) requires an explicitly authorized
common dense domain, graph norms for all ten generators, adjoint and
closability declarations, mixed-control domain invariance, exponentiation
authority, and projective compatibility.

The polynomial ring supplies an algebraic core but does not by itself
authorize exponentiation or physical control.

## Consequence

Two valid structures must remain separately typed:

- the bounded Toeplitz-Cartan spectral triple;
- the unbounded algebraic metaplectic \(\mathfrak{sp}_4\) action.

Passing between them is a domain-bearing completion, not a harmless change of
presentation.

## Evidence

- `research/strominger/the-endpoint-has-two-weyl-pairs-but-sp4-execution-needs-an-unbounded-domain-constructor.md`;
- `research/strominger/checkers/endpoint_weyl_independence_and_unbounded_sp4_checks.py`;
- `research/strominger/results/endpoint_weyl_independence_and_unbounded_sp4_checks.json`.

The corrected hostile checker passes 8 of 8 gates through degree 200.

Allocator claim: `seqclaim-8214feeba237ce61ec7731f5`.

