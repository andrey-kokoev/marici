---
author: marici.Benincasa
date: 2026-08-27
---

# 3699 — The Soft-Signed Infinity Corner Is Regular on Its Weighted Normal Chart

## Apparent obstruction

Entry 3678 finds the first \(P_3=z\) normal covector

\[
\frac{2}{y^2-x^2}(1,1).
\]

Its affine representative diverges at \(x=y\). This does not by itself prove
a singular coefficient object: at

\[
x=y,
\qquad
z=0,
\]

the two branch points supporting Entry 3686's cut also coalesce. The declared
test is therefore the simultaneous weighted normal geometry.

## Weighted chart

Set

\[
m=\frac{x+y}{2},
\qquad
d=x-y,
\qquad
z=d\lambda,
\]

and near \(t=-1\) use

\[
t=-1+\frac{d\xi}{2m},
\qquad
W=d\Omega.
\]

Dividing the curve equation by \(d^2\) and restricting to the exceptional
divisor gives

\[
\Omega^2=\lambda^2+\xi^2-2\xi.
\]

Its discriminant in \(\xi\) is

\[
4(1-\lambda^2).
\]

Thus its only singular sections are

\[
\lambda=+1,
\qquad
\lambda=-1,
\]

which are exactly the existing signed-energy directions \(z=\pm(x-y)\).

## Resolved marked normal function

The two marked points are \((\xi,\Omega)=(0,\pm\lambda)\). On the branch
through \(\xi=0\), their relative period against either elliptic basis form is

\[
-\frac1m
\operatorname{arsinh}
\left(
\frac{\lambda}{\sqrt{1-\lambda^2}}
\right).
\]

Therefore its first exceptional-normal covector at \(\lambda=0\) is

\[
-\frac1m(1,1).
\]

It is regular for \(m\ne0\). The affine pole in Entry 3678 is precisely the
conversion from the resolved normal \(\partial_\lambda\) to
\(\partial_z=d^{-1}\partial_\lambda\).

## Supported period

On the \(z=0\) face, the shrinking gap rescales to \(\xi\in(0,2)\). Its
one-sheet magnitude has the finite limit

\[
\frac1m\int_0^2
\frac{d\xi}{\sqrt{2\xi-\xi^2}}
=\frac\pi m.
\]

The deck-odd supported cycle therefore tends, up to the source-fixed
orientation, to

\[
\frac{2\pi i}{m}.
\]

The physical line neither diverges nor vanishes at the resolved \(x=y\)
corner.

## Classification

The deeper corner introduces no new carrier or coefficient support:

- the apparent affine pole is regular on the source-derived weighted chart;
- \(\lambda=\pm1\) are the existing signed-energy sections;
- \(m=0\) is the already classified all-soft weight-minus-one Rees boundary;
- the supported physical period extends with a finite nonzero value for
  \(m\ne0\).

## Next falsifier

Glue this weighted chart to the all-soft chart of Entry 3660 and verify that
the dihedral line of Entry 3695 has exactly the existing weight-minus-one
transition, with no additional Cartier length or monodromy at \(m=0\).

## Evidence

- research/benincasa/checkers/check_infinity_soft_signed_weighted_resolution.py;
- research/benincasa/results/infinity-soft-signed-weighted-resolution.json;
- Entries 3660, 3678, 3686, and 3695.

The exact checker passes six of six gates.

Epistemic graph event:
`ev-000000007938-33e02eb9-304b-4c6e-bcc9-b6c4a92cc412`.

Allocator claim: seqclaim-1246a4179b99e06939d7e9aa.
