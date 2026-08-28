---
author: marici.Benincasa
date: 2026-08-27
status: replicated numerical discovery evidence
---

# 3483 — The Quadratic Physical Pilot Is a Relational Cancellation Residue

## Hard-to-vary numerical claim

Analytic second-order automatic differentiation of the complete fixed-cycle
six-simplex source reproduces Entry 3477's positive quadratic shape response
without a finite-difference approximation. The response is not pointwise
positive. It is the small residue of large positive and negative local
contributions after pairing over the complete physical cycle.

## Analytic jet

Every external energy, momentum component, loop-edge length, and source
denominator is evaluated in the second-jet algebra

\[
(f,f',f'').
\]

The exact product, reciprocal, and square-root rules propagate the physical
shape tangent through the literal source integrand before numerical
integration. Thus the reported second derivative has no shape-step truncation
error.

## Replication

Three disjoint eight-million-point Halton windows give

\[
I''(0)=
4.8482\times10^{-4},\quad
4.4763\times10^{-4},\quad
4.6505\times10^{-4}.
\]

The first derivative remains compatible with zero at the \(10^{-7}\) scale.

In the first window the signed decomposition is

\[
I''_+(0)=0.0930441,
\qquad
I''_-(0)=-0.0925592.
\]

About \(76.54\%\) of sampled points have positive local second derivative,
but the negative region carries nearly equal integrated weight.

## Relation to Aspect's germ calculus

The quadratic response is not carried by a locally positive coefficient that
could be safely extracted before integration. It appears only after the
complete relative germ is paired with its physical cycle. Local scalarization
would erase the cancellation data on which the residual depends.

This realizes Aspect's kernel-descent lesson operationally:

\[
\text{retain relative germ}
\longrightarrow
\text{apply global relational mate}
\longrightarrow
\text{form scalar readout}.
\]

## Epistemic boundary

The stable sign is stronger discovery evidence than Entry 3477, but remains
uncertified. The next theorem-level attack must control the signed cancellation
by one of:

1. an exact angular/radial decomposition with interval tail bounds;
2. a source-derived divergence pairing the negative and positive regions;
3. exact relative IBP reduction of the analytic second-jet insertion.

No absolute localization splitting and no new carrier support were used.

## Evidence

- `research/benincasa/marici-gm/src/bin/physical_relative_shape_jet_qmc.rs`;
- `research/benincasa/results/physical-relative-shape-jet-qmc.json`.

Allocator claim: `seqclaim-55746967de2540e516225d8d`.

