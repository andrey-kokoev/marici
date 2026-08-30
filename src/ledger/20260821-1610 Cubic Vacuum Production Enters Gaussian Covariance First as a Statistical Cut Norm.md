# Entry 1610 — Cubic Vacuum Production Enters Gaussian Covariance First as a Statistical Cut Norm

## Claim

A cubic vacuum-production amplitude cannot generate a first-order anomalous
two-point coordinate.  Its first covariance contribution is the second-order
statistical Cut norm.

## Finite Fock-space test

For three labelled modes, take

\[
|\Psi\rangle=
\frac{|0,0,0\rangle+gA|1,1,1\rangle}
{\sqrt{1+g^2|A|^2}}.
\]

For any one observed mode,

\[
\langle aa\rangle=0,
\qquad
\langle a^\dagger a\rangle
=\frac{g^2|A|^2}{1+g^2|A|^2}.
\]

Thus

\[
\operatorname{gr}^{(1)}\beta=0,
\qquad
\operatorname{gr}^{(2)}n=|A|^2.
\]

The coefficient is the norm square obtained by cutting the two unobserved
mode lines.

## Consequence for the source calculation

The next source-derived identity is now fixed in type:

\[
n_{2,p}^{\rm Dyson}
\stackrel?=
\int d\Pi_{qk}\,
|A_{p;qk}^{\rm cubic}|^2,
\]

with the source normalization, physical phase-space measure, and labelled
\(q/k\) occurrence trace retained.  No first-order anomalous source should be
fitted to the cubic vacuum channel.

## Scope

The Fock-space result is exact, but the equality for the cosmological kernel
remains conjectural until both sides are derived in the frozen normalization.

## Artifacts

- `research/benincasa/checkers/cubic_three_particle_covariance_cut.rs`
- `research/benincasa/results/cubic-three-particle-covariance-cut.json`

Allocator claim: `seqclaim-6a4a10ff093114b54ba58607`.
