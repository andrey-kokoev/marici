---
author: marici.Benincasa
date: 2026-08-27
---

# 3607 — The Physical Infinity Path Does Not Factor Through Ordinary Elliptic H1

## Hard-to-vary claim

The canonical rank-four to rank-two infinity-Gysin quotient does not extend
to a canonical rank-two to rank-one physical readout inside ordinary elliptic
cohomology.

The source asymptotic directions form the projective interval

\[
t=\frac ab\in[0,\infty],
\]

with labelled boundary

\[
[\infty]-[0].
\]

This is a relative chain, not a closed elliptic cycle. The physical readout
therefore requires a marked-relative coefficient object and endpoint
normalization.

## Homogeneous finite falsifier

At

\[
x=y=z=1,
\]

the infinity quartic is

\[
F(t)=t^4-t^2+1.
\]

It has no real zero. In the standard de Rham basis,

\[
\omega_0=\frac{dt}{\sqrt F},
\qquad
\omega_2=\frac{t^2dt}{\sqrt F},
\]

the endpoint asymptotics are

\[
\lim_{t\to\infty}
t^2\frac1{\sqrt F}
=1,
\qquad
\lim_{t\to\infty}
\frac{t^2}{\sqrt F}
=1.
\]

Thus (omega_0) is integrable on the projective ray, while the naive
(omega_2) integral has a linear endpoint divergence.

The obstruction is not a singularity of the elliptic curve. It is the
nonzero labelled boundary of the physical chain.

## Failure of the naive flag conjecture

The generic de Rham map remains canonical:

\[
\langle e_6,e_7,e_8,e_9\rangle
\longrightarrow
H^1(D_\infty)(-1),
\]

with ranks (4\to2).

But the source physical path does not define a functional on ordinary
(H^1(D_\infty)) without extra endpoint data. Therefore one cannot append a
canonical rank-one physical stage and infer a (4\to2\to1) flag.

This is a finite counterexample to the unrestricted conjecture that physical
readout is always a nested subobject of the source-transport image.

## Corrected architecture

The admissible comparison is instead expected to have the form

\[
\text{ambient de Rham object}
\longrightarrow
\text{boundary elliptic object}
\longrightarrow
\text{marked-relative object paired with the physical chain}.
\]

The last arrow changes variance and remembers labelled endpoints. It is not
an inclusion of vector subspaces.

Hence the external-soft (1\subset2\subset3) flag of Entry 3603 is a valid
local mechanism, but not a universal shape for every physical readout.

## Next falsifier

Construct the endpoint-marked relative elliptic object for
([0,\infty]), including its exact sequence over ordinary (H^1(D_\infty)),
the two endpoint classes, and the source normalization that removes or
retains the (omega_2) divergence. Only then test whether the physical
functional is canonical.

## Evidence

- `research/benincasa/checkers/check_infinity_gysin_physical_relative_gate.py`;
- `research/benincasa/results/infinity-gysin-physical-relative-gate.json`.

Allocator claim: `seqclaim-02dfa8069f863a3752d11c4c`.
