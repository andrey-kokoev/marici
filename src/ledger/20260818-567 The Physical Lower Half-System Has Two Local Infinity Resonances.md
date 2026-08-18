---
id: 567
date: 2026-08-18
title: The Physical Lower Half-System Has Two Local Infinity Resonances
authors:
  - marici.Nima
---

# The Physical Lower Half-System Has Two Local Infinity Resonances

Entry 566 proves physical half-weight critical rank five but leaves the
quartic infinity resonance unresolved. This entry computes the local
singularity and character data at both infinity points.

At generic kinematic point A, the restricted wall polynomial is affine-smooth
and irreducible. Its degree-four part is

\[
K_4=25(a-b)^2(a+b)^2.
\]

Thus the projective closure meets infinity at

\[
[a:b:s]=[1:1:0],\qquad[1:-1:0].
\]

In local coordinates \((x,y)\) at either point, with \(y=0\) the infinity
line, the exact quadratic tangent cone is

\[
100x^2+776xy-755y^2.
\]

Its discriminant is

\[
904176\ne0,
\]

so the quartic has two transverse local branches. Neither branch is the
infinity line. Consequently the union of the quartic and infinity divisor is
an ordinary triple point at each of the two locations.

## Physical character calculation

The half-weight local system has monodromy \(-1\) around each quartic branch.
The total quartic degree is four, so its infinity monodromy is

\[
(-1)^4=+1.
\]

The local character triple is therefore

\[
\boxed{(-1,-1,+1)},
\]

with product \(+1\). For the ordinary triple-point complement, the trivial
total character and nontrivial base character give

\[
\boxed{\dim H^1_{\rm local}=1.}
\]

Since there are two infinity points, the local resonance supply is

\[
\boxed{1+1=2.}
\]

## Consequence

The failure of generic critical-point concentration at exponent
\(\tfrac12\) is now concrete, not merely a degree warning. Two local
cohomology classes are available at infinity. Their count matches the
rank-two deck-odd boundary sector

\[
\langle D_+-D_-,\gamma\rangle
\]

found in Entries 559--560.

This match does not yet prove both local classes survive in global
hypercohomology. A global Čech differential could identify or kill a
combination. Therefore no global Betti numbers are asserted here.

## Next gate

Construct the two-point infinity Čech complex for the physical sign local
system and compute its global differential. If both local classes survive,
then \(b_1=2\); since the Euler characteristic is five, one obtains
\(b_2=7\). If one relation occurs, the resulting Betti numbers change
accordingly.

The executable audit is
\`research/benincasa/check_generic_lower_half_infinity_resonance.py\`.
