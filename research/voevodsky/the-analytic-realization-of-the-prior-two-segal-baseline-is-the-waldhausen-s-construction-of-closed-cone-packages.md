# The analytic realization of the prior 2-Segal baseline is the Waldhausen S-construction of closed cone packages

## Existing indexing object

Prior work constructs a 2-Segal simplicial object with two directional path spaces and a reversal involution. That object supplies the indexing law for forward and backward decomposition.

The missing bridge is an analytic realization of its simplices.

## Stable analytic target

Let

\[
\mathcal C_{\rm cl}
\]

be the proposed stable category of admitted closed cone packages. Its objects retain:

- a closed graph domain;
- a differential or closed relation;
- kernel and cokernel data;
- reciprocal transport;
- an independently admitted adjoint mate when present.

Define the Waldhausen-style simplicial object

\[
S_\bullet(\mathcal C_{\rm cl}).
\]

An \(n\)-simplex consists of interval objects

\[
X_{ij},
\qquad
0\le i\le j\le n,
\]

with

\[
X_{ii}=0,
\]

and cofiber triangles

\[
X_{ij}
\to
X_{ik}
\to
X_{jk}
\]

for every

\[
i\le j\le k.
\]

Thus every interval in a path carries its compressed quotient, and every subdivision carries its comparison triangle.

## Low dimensions

### Degree one

A 1-simplex is one closed analytic object or correspondence.

### Degree two

A 2-simplex contains

\[
X_{01},
\qquad
X_{02},
\qquad
X_{12},
\]

with one cofiber triangle

\[
X_{01}
\to
X_{02}
\to
X_{12}.
\]

This is the derived quotient-of-quotients cell.

### Degree three

A 3-simplex contains all six interval objects

\[
X_{01},X_{12},X_{23},X_{02},X_{13},X_{03}.
\]

Its four compatible cofiber triangles assemble into the octahedral diagram. The octahedron is therefore the degree-three analytic realization of the 2-Segal decomposition law.

### Degree four

A 4-simplex contains all interval cones for a four-step filtration. Its tetrahedral restrictions are compatible octahedra. This is the natural home of the previously sought top coherencer.

## 2-Segal law

A polygonal decomposition selects smaller interval packages. The 2-Segal map compares:

1. the complete \(n\)-simplex of interval cones;
2. the compatible collection attached to the chosen polygonal decomposition.

In a stable category, cofiber composition and the octahedral law provide the required reconstruction equivalence.

Thus quotient-of-quotient associativity is the analytic content of the 2-Segal property.

## Reciprocal duality

Let

\[
\mathbb D:
\mathcal C_{\rm cl}^{op}
\to
\mathcal C_{\rm cl}
\]

be the reciprocal adjoint operation. On interval objects it acts by

\[
\mathbb D(X_{ij})
=
X_{n-j,n-i}^{\vee}.
\]

It reverses simplex order and exchanges the initial and final path spaces. This is the analytic realization of the previously constructed simplicial reversal.

For the bidirectional cone cell, \(\mathbb D\) combines:

- reciprocal transport;
- adjoint reversal;
- orientation sign;
- reversal of filtration order.

## Realization functor

The required bridge is a simplicial functor

\[
\mathfrak R:
X_\bullet^{\rm prior}
\to
S_\bullet(
\mathcal C_{\rm cl}
).
\]

It must send:

- a labelled edge to a closed oriented correspondence;
- a two-edge decomposition to its cofiber triangle;
- a three-edge decomposition to its octahedral cone package;
- reversal to reciprocal adjoint duality;
- four-periodic type shift to the declared successor grading.

## Seam

The prior four-periodic system contains a conditional seam

\[
V_{4,k}
\simeq
V_{1,k+1}.
\]

Analytically, this must become an exact or controlled equivalence between the terminal cone package at stage \(k\) and the initial cone package at stage \(k+1\).

The seam must preserve:

1. graph domains;
2. reciprocal duality;
3. cofiber triangles;
4. Hodge domains when the metric enhancement is added;
5. determinant orientation.

This is the first genuinely source-dependent datum in the realization functor.

## Cutoff leakage

If finite restriction produces

\[
A_X=P_XF(I-P_X),
\]

then \(\mathfrak R\) is lax at finite cutoff. The leakage is retained as a specified 2-cell. The completed realization requires compatible nullhomotopies or convergence of these leakage cells.

Thus the correct target may first be a lax Waldhausen S-object in a pro-category, becoming strict only after completion.

## Position of the new finite checkers

The mapping-cone checker realizes the degree-two cofiber law.

The composed bidirectional octahedral checker realizes:

- the degree-three octahedral law;
- reciprocal reversal;
- adjoint-mate compatibility.

They are finite analytic fixtures for the first nontrivial simplices of \(S_\bullet(\mathcal C_{\rm cl})\).

## Disposition

The repository already had the 2-Segal indexing architecture. The new cone and octahedral cells identify its analytic target: the Waldhausen S-construction of closed cone packages with reciprocal duality. The remaining bridge is the source-derived realization functor, especially its completion-level seam.
