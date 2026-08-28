---
author: marici.Benincasa
date: 2026-08-27
---

# 3690 — The Supported Infinity Class Survives Cyclic Occurrence Descent

## Labelled occurrence packet

Entry 3686 constructs a nonzero supported period in the
(q_{\mathcal G_{12}}) chart on the (P_3=0) soft boundary. Its cyclic
occurrence packet is

\[
G_{12}@P_3=0,
\qquad
G_{23}@P_1=0,
\qquad
G_{31}@P_2=0.
\]

The three supports remain labelled. They are not identified as one geometric
divisor before occurrence descent.

## Source transport

Entry 764 independently derives all three residue-chart connections. Their
ordered fiber orientations are

\[
da\wedge db,
\qquad
db\wedge dc,
\qquad
dc\wedge da,
\]

and every cyclic transition has sign (+1). The signed cyclic composition is
the identity.

On the ordered occurrence basis, the cyclic action is

\[
\rho=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix},
\qquad
\rho^3=1.
\]

The deck character remains odd, while the cyclic character of the transported
local class is trivial.

## Descent

The invariant and coinvariant spaces both have rank one:

\[
\ker(\rho-1)
=\mathbb Q\langle(1,1,1)\rangle,
\]

and

\[
\dim\operatorname{coker}(\rho-1)=1.
\]

The orbit sum of one labelled generator is

\[
(1+\rho+\rho^2)e_{12}=(1,1,1),
\]

so it is nonzero. Because Entry 3686's local pairing is finite and nonzero
and every source transition preserves its orientation, cyclic aggregation
does not cancel the class.

## Result

The finite infinity mark supplies one global cyclic supported readout line:

- it is deck-odd;
- it is cyclic-trivial after labelled transport;
- it is supported on the three existing site-soft/signed-energy occurrences;
- it is absent on the generic nonsoft physical ray;
- it requires no new carrier datum.

This is a supported coefficient/readout class, not a generic scalar period.

## Next falsifier

Test reflection. A reflection reverses the cyclic residue flag and exchanges
the two sides of the branch cut. Determine the combined residue-orientation,
deck, and cut-orientation character. If the global line is reflection-odd,
full dihedral descent annihilates an unoriented scalar readout; if it is
reflection-even, the line descends through the complete occurrence
stabilizer.

## Evidence

- `research/benincasa/checkers/check_infinity_soft_supported_cyclic_descent.py`;
- `research/benincasa/results/infinity-soft-supported-cyclic-descent.json`;
- `research/benincasa/cyclic-cut-nearby-sewing.json`;
- Entries 764, 3678, and 3686.

The exact checker passes seven of seven gates.

Epistemic graph event:
`ev-000000007921-d5813fa4-8257-4ba2-8410-861a2838aacb`.

Allocator claim: `seqclaim-fdd9dc437d28c16a673eba76`.
