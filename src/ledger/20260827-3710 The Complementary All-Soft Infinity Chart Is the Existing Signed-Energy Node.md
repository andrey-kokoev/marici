---
author: marici.Benincasa
date: 2026-08-27
---

# 3710 — The Complementary All-Soft Infinity Chart Is the Existing Signed-Energy Node

## Why a complementary chart is required

Entries 3705 and 3708 work on the projective all-soft chart
\(m\ne0\), where

\[
m=\frac{x+y}{2},
\qquad
d=x-y,
\qquad
\lambda=\frac zd.
\]

Their normalized supported generator contains \(1/\widehat m\). It is not
legitimate to infer a pole at \(\widehat m=0\) from a chart that excludes
that locus.

Use instead the complementary \(d\ne0\) chart

\[
x=d\left(\mu+\frac12\right),
\qquad
y=d\left(\mu-\frac12\right),
\qquad
z=d\lambda,
\]

and near the marked point set

\[
t=-1+q,
\qquad
W=d\Omega.
\]

## Exact tangent cone

After removing the forced common factor \(d^2\), the quadratic initial
form of the frozen quartic is

\[
q^2-4\mu q+\lambda^2.
\]

With \(r=q-2\mu\), this becomes

\[
r^2+(\lambda-2\mu)(\lambda+2\mu).
\]

The double-cover germ therefore has normal form

\[
\Omega^2-r^2-(\lambda-2\mu)(\lambda+2\mu)=0.
\]

Its two discriminant branches are

\[
\lambda-2\mu=0
\quad\Longleftrightarrow\quad
z-(x+y)=0,
\]

and

\[
\lambda+2\mu=0
\quad\Longleftrightarrow\quad
z+(x+y)=0.
\]

These are precisely the two already frozen signed-energy walls.

## Local coefficient type

The Hessian of the four-variable hypersurface germ is nondegenerate. Its
Milnor algebra has rank one, carrying the ordinary deck-anti-invariant
Kummer node line.

Thus the apparent \(1/m\) divergence from the first chart is its transition
toward an ordinary signed-energy node. It is not a new divisor and does not
justify another Carrier stratum.

## Result and remaining gate

The two all-soft charts together show:

- generic radial gluing is strict;
- the excluded chart boundary is the existing signed-energy intersection;
- its local excess is the standard rank-one node class;
- no new carrier support appears.

What remains is a map-level test: compare this rank-one node class with the
already declared pair of signed-energy nearby-cycle maps, retaining their
two occurrence labels and residue orientations. The local Milnor rank alone
does not prove that comparison cone exact.

## Evidence

- `research/benincasa/checkers/check_infinity_all_soft_complementary_chart.py`;
- `research/benincasa/results/infinity-all-soft-complementary-chart.json`;
- Entries 3699, 3705, and 3708.

The exact checker passes seven of seven gates.

Epistemic graph event:
`ev-000000007960-0c14a2a0-d098-4ba8-9b70-85057d1592e4`.

Allocator claim: `seqclaim-faafae0fdd1f25bdd9a1648b`.
