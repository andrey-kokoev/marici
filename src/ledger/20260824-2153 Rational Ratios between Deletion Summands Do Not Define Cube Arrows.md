---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2153 — Rational Ratios between Deletion Summands Do Not Define Cube Arrows

## Correction

Entries 2149--2152 promoted exact rational ratios between deletion summands
to morphisms between their coefficient systems. This inference is not
authorized by the frozen source and contradicts the typing distinction in
Entries 2113 and 2115.

## What the source defines

For every deletion subset \(S\), the source independently defines a port into
the common correlator base:

\[
T_S f_S
=
\left(\prod_{e\in S}y_e^{-1}\right)
f_S\!\left(x_v+\sum_{e\in S, e\ni v}y_e\right).
\]

The correlator is the signed sum of these port images. The source does not
define

\[
\mathcal M_S\longrightarrow\mathcal M_{S\cup\{e\}}.
\]

## Why the ratio test is insufficient

For two nonzero rank-one rational forms \(\omega_S\) and
\(\omega_{S\cup\{e\}}\), their ratio

\[
f=\frac{\omega_{S\cup\{e\}}}{\omega_S}
\]

always gives an open-locus identity

\[
\omega_{S\cup\{e\}}=f\omega_S.
\]

Conjugating a rank-one connection by \(f\),

\[
A' = A-d\log f,
\]

then makes multiplication by \(f\) horizontal by construction. This proves
only a presentation gauge on the complement of \(\operatorname{div}(f)\).
It does not prove:

- a morphism between the full marked relative complexes;
- compatibility with their independently derived Gauss--Manin connections;
- extension across the divisor;
- a map of physical relative chains;
- authority for a deletion-cube differential.

## Surviving evidence from Entries 2149--2152

The exact formulas remain useful as candidate gauges. In particular,

\[
f_{31}
=
\frac{X_1+X_3+y_{12}+y_{23}}{y_{31}}
\]

and its cyclic partners correctly identify the only divisors on which that
candidate gauge can fail. Entry 2151's radial exponent remains an
integrability statement. None of these facts creates a cube arrow.

## Consequence for the requested coherence test

Composing ratios around a square necessarily telescopes:

\[
\frac{\omega_{S\cup\{e,f\}}}{\omega_{S\cup\{e\}}}
\frac{\omega_{S\cup\{e\}}}{\omega_S}
=
\frac{\omega_{S\cup\{e,f\}}}{\omega_S},
\]

independently of order. Such strict commutativity is algebraic tautology, not
evidence that deletion is a strict cube functor.

Therefore the grade-one-to-grade-two comparison currently has the fourth
classification allowed by Entry 701:

\[
\boxed{\text{untyped}.}
\]

It is neither a proved strict square, a homotopy-commuting square, nor a
nonzero obstruction class.

## Evidence

- Entries 2113, 2115, and 2149--2152;
- `research/benincasa/three-site-correlator-cube-coefficient-typing.md`;
- allocator claim `seqclaim-133924869ff6c5b841c44d48`.

## Next falsifier

Audit all cyclic port-adapter compositions in their actual variance: each
deleted-sector coefficient object maps independently into the common
readout. Verify strict commutation of endpoint translations and integral
Kummer factors there, while explicitly refusing to interpret that result as
an inter-grade cube differential. A genuine cube coherence test must await an
independently derived localization, Gysin, or relative-chain map.
