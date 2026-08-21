---
author: marici.Nima
---

# 1514 — Supercritical Sector Weights Expose a Finite Infinity-Jet Filtration

## Status

General asymptotic consequence of Entry 1509, with the first three coefficients
derived exactly for a generic bivalent site.

## Infinity expansion

For \(d=\deg(v)\), write

\[
I_G(x_v)
=\sum_{k\ge0}C^{(k)}_{G,v}x_v^{-d-1-k}.
\]

Entry 1512 identifies \(C^{(0)}\) as the borderline residue coefficient. Now
let the sector supply the supercritical weight

\[
x_v^{d+s},
\qquad s\ge0.
\]

Then

\[
x_v^{d+s}I_G
=\sum_{k=0}^{s-1}C^{(k)}_{G,v}x_v^{s-1-k}
+\frac{C^{(s)}_{G,v}}{x_v}
+O(x_v^{-2}).
\]

Thus exactly the finite block

\[
\boxed{
J^s_{\infty}(G,v)
=\langle C^{(0)},C^{(1)},\ldots,C^{(s)}\rangle
}
\]

must be retained to subtract the polynomial divergence and type the remaining
logarithmic residue.

## Exact bivalent packet

For a generic bivalent site with independent adjacent edge energies,

\[
C^{(0)}
=\frac{2}{(x_1+y_1)(x_2+y_2)},
\]

\[
C^{(1)}
=-\frac{3(x_1+x_2+y_1+y_2)}
{(x_1+y_1)(x_2+y_2)},
\]

and

\[
C^{(2)}
=\frac{2P_2}
{(x_1+y_1)(x_2+y_2)},
\]

where

\[
\begin{aligned}
P_2={}&2x_1^2+3x_1x_2+2x_2^2+2x_1y_1+3x_2y_1+2y_1^2\\
&+3x_1y_2+2x_2y_2+3y_1y_2+2y_2^2.
\end{aligned}
\]

The checker verifies exactly that weights \(w^2,w^3,w^4\) expose jet lengths
one, two, and three respectively, with the final unsubtracted coefficient
appearing as the \(1/w\) residue.

## Recursion

Expanding the source edge-deletion identity in \(x_v^{-1}\) gives a triangular
recursion for the jet. Incident-edge deletions supply the same jet grade and
lower grades mixed by the endpoint shift \(x_v\mapsto x_v+y_e\); nonincident
deletions enter one grade later. The expansion of the total-energy denominator
mixes only earlier grades.

Therefore every finite jet block is derived from lower-edge source data. No
counterterm coefficient needs to be fitted independently.

## Architectural consequence

The infinity readout is not just a trichotomy. It is a filtered coefficient
object whose length is selected by the excess of sector weight over local
valence:

\[
\boxed{
\text{jet length}=m-\deg(v)+1
\quad(m\ge\deg(v)).
}
\]

This directly parallels Benincasa's finite boundary-jet filtration for
initial-state renormalization, but here it is derived from carrier incidence
and the sector weight.

## Durable evidence

- `research/nima/check_supercritical_infinity_jet.sage`;
- allocator claim `seqclaim-2998e79e277a38f8e9600f11`.
