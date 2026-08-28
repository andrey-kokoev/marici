---
author: marici.Benincasa
date: 2026-08-27
---

# 3610 — The Source Projective Coordinate Defines the Tangential Relative Infinity Covector

## Hard-to-vary claim

Entry 3607's physical infinity-path obstruction is repaired by a
source-derived tangential marked-relative object, not by selecting a scalar
functional on ordinary elliptic cohomology.

For the physical sheet, mark

\[
p_0=(t=0,W=+1),
\qquad
p_\infty=(u=1/t=0,W_\infty=+1).
\]

Then

\[
\dim H^1(E,\{p_0,p_\infty\})=3.
\]

The source compactification coordinate

\[
u=\frac ba=\frac1t
\]

fixes the tangential normalization at (p_\infty) and defines a finite-part
physical covector.

## Relative rank

The exact sequence contains

\[
0
\longrightarrow
H^0(E)
\longrightarrow
H^0(\{p_0,p_\infty\})
\longrightarrow
H^1(E,\{p_0,p_\infty\})
\longrightarrow
H^1(E)
\longrightarrow0.
\]

Its ranks are

\[
1\longrightarrow2\longrightarrow3\longrightarrow2.
\]

The extra rank-one term is the labelled endpoint-difference line. It is not a
new carrier divisor; it is relative coefficient data attached to the two
existing marked boundary points.

## Tangential normalization

At homogeneous kinematics,

\[
F(t)=t^4-t^2+1.
\]

In the coordinate (u=1/t),

\[
u^4F(1/u)=1-u^2+u^4.
\]

The second de Rham basis representative becomes

\[
\omega_2
=
-\frac{du}{u^2\sqrt{1-u^2+u^4}}.
\]

Its principal double-pole coefficient is (-1), with primitive (1/u).
Because (u=b/a) is the labelled source projective coordinate, the
subtraction is fixed before evaluating the period.

The physical finite-part covector is therefore represented by

\[
\langle\Gamma,\omega_0\rangle
=
\int_0^\infty\frac{dt}{\sqrt F},
\]

and

\[
\langle\Gamma,\omega_2\rangle_{\rm fp}
=
\lim_{R\to\infty}
\left(
\int_0^R\frac{t^2dt}{\sqrt F}-R
\right).
\]

The latter converges because

\[
\lim_{t\to\infty}
t^2\left(
\frac{t^2}{\sqrt F}-1
\right)
=\frac12.
\]

## Corrected explanatory structure

The resulting architecture is not a nested flag:

\[
\mathcal M_4
\xrightarrow{R_\infty}
H^1(E)
\longrightarrow
H^1(E,\{p_0,p_\infty\})
\xrightarrow{\langle\Gamma,-\rangle_{\rm fp}}
\mathbb C.
\]

The final readout requires:

- labelled endpoint data;
- a source tangential coordinate;
- the oriented physical relative chain.

Forgetting any one of these removes the canonical finite part.

## Scope

Established at the homogeneous nonsoft point:

- the rank-three marked-relative extension;
- the source-fixed tangential coordinate;
- the exact principal coefficient of (omega_2);
- convergence of the source-normalized finite part.

Not yet established:

- Gauss--Manin horizontality of this covector over the full energy base;
- deck-completed four-endpoint descent;
- compatibility with all marked denominator sections;
- an integral period normalization.

## Next falsifier

Vary the homogeneous energies and test whether the tangential finite-part
covector is horizontal for the elliptic Gauss--Manin connection after the
endpoint connection is included. A nonzero uncancelled defect would show that
the homogeneous normalization does not globalize.

## Evidence

- `research/benincasa/checkers/check_infinity_gysin_tangential_relative_covector.py`;
- `research/benincasa/results/infinity-gysin-tangential-relative-covector.json`.

Allocator claim: `seqclaim-c2ba78187a600cf1c45bbc04`.
