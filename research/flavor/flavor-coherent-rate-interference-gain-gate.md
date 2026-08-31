# Coherent rate-interference gain gate: WP1044

## Question

What is the smallest coherent instrument that can attack the WP1042
`physical16` gain fiber?

## Conditional acquisition model

Use three retained rows on a factorized one-amplitude domain:

\[
B,
\qquad
S=B+\mathcal L g^2,
\qquad
D=S_+-S_-=4\mathcal L g.
\]

The coherent difference assumes calibrated reference amplitude, visibility,
threshold shape, and port phase. The plus and minus ports must be retained
separately; summing them erases \(D\).

At \(B=0\), \(\mathcal L=1\), and \(g=1\), the local rows on
\((B,\mathcal L,g)\) are

\[
(1,0,0),
\qquad
(1,1,2),
\qquad
(0,4,4).
\]

Their rank is three. The pure-rate pair has rank two and leaves the usual
\((g,\mathcal L)\) laundering symmetry.

## Exact reconstruction

For \(D\ne0\) and \(S>B\),

\[
g=\frac{4(S-B)}{D},
\qquad
\mathcal L=\frac{D^2}{16(S-B)}.
\]

The witnesses are exact:

\[
(B,S,D)=(0,1,4)\mapsto(\mathcal L,g)=(1,1),
\]

\[
(B,S,D)=(0,4,8)\mapsto(\mathcal L,g)=(1,2).
\]

Pure rates collide on

\[
(g,\mathcal L)=(1,4),
\qquad
(g,\mathcal L)=(2,1),
\]

since both have \(\mathcal Lg^2=4\). The coherent difference separates them:
\(4\mathcal Lg=16\) versus \(8\).

## Visibility caveat

If visibility is an unknown coordinate, the same three rows have rank three on
four coordinates \((B,\mathcal L,g,\nu)\). The gain is then confounded with
visibility. Visibility calibration is therefore a load-bearing part of the
instrument, not a detector detail.

## Classification

This is a conditional instrument gate. It identifies the signed gain locally
after reference and visibility calibration. It does not derive the source value
of \(g\), the existence of one coherent final state, or the applicability of
this one-amplitude model to a `physical16` process.

## Disposition

Productive but not a selector. WP1042's gain fiber now has a minimal
acquisition target: background row, absolute signal row, phase-flipped coherent
difference row, calibrated visibility, retained ports, and common source-frame
provenance. No current Flavor source or experiment instantiates that target.

Checker: `research/flavor/checkers/wp1044_coherent_rate_interference_gain_gate.py`

Result: `results/wp1044_coherent_rate_interference_gain_gate.json`
