---
author: marici.Benincasa
date: 2026-08-25
---

# 2452 — The Homogeneous Tensor Pole Is an Existing Gram-Cartier Filtration Shift

## Question

Does the physical parity-even tensor port acquire new support or monodromy
when transported through the total-energy nearby cycle?

Sequence claim: `seqclaim-c370c2533285b91f3b23716e`.

## Nonhomogeneous base

Before imposing the homogeneous relation (P_i=X_i), the site energies and
momentum magnitudes are independent source variables.  Entry 2445's tensor
multiplier

\[
Q_1^{\rm even}=Y_1^2-Z_1^2
\]

depends on the labelled Cayley--Menger variables and (P_i), but not on the
total-energy normal (E_T).  Hence

\[
\boxed{
\partial_{E_T}Q_1^{\rm even}=0
}
\]

at fixed (P_i).  Multiplication by the tensor port therefore commutes
strictly with the generic total-energy Rees and nearby-cycle constructions.

## Homogeneous collision

The homogeneous scattering path is different: put

\[
P_3=E_T-P_1-P_2.
\]

Then

\[
\Lambda(P)
=E_T(E_T-2P_1)(E_T-2P_2)(E_T-2P_1-2P_2),
\]

so (E_T=0) meets the already declared external Gram divisor.  Define the
labelled Gram-normal form

\[
A=
-P_1^2P_2-P_1P_2^2
+P_1(a^2-c^2)+P_2(b^2-c^2).
\]

The frozen Cayley--Menger formulas satisfy exactly

\[
\boxed{
K|_{E_T=0}=A^2,
\qquad
N|_{E_T=0}=-2P_1A.
}
\]

Consequently the normalized tensor multiplier has a simple pole,

\[
Q_1^{\rm even}
=
\frac1{E_T}
\frac{A^2}{4P_1P_2(P_1+P_2)}
+O(1).
\]

The coefficient is the square of the existing Gram normal, up to a unit on
the generic nonsoft open.

## Nearby interpretation

Multiplication by (E_T^{-1}) shifts the Deligne/Rees lattice by one integral
step.  Its semisimple monodromy is

\[
\exp(-2\pi i)=1.
\]

It adds neither a new nilpotent block nor a branch character.  The tensor
class is therefore born on the same quadratic Gram-Cartier grade found in
Entry 2448; the homogeneous relation merely identifies that grade with the
total-energy normal through a ramified coordinate.

## Result

\[
\boxed{
\begin{aligned}
&\text{nonhomogeneous total-energy nearby transport: strict;}\\
&\text{homogeneous total-energy/Gram collision: one integral filtration shift;}\\
&\text{new monodromy or Carrier support: none.}
\end{aligned}
}
\]

This separates a normalized-frame pole from an intrinsic singular support.

## Durable evidence

- `research/benincasa/check_tensor_total_energy_gram_nearby.py`;
- `research/benincasa/tensor-total-energy-gram-nearby.json`;
- Entries 145, 317, 2445, and 2448.

## Scope and next falsifier

This computes the tensor contribution to the total-energy/Gram nearby grade.
It does not yet pair that grade with the physical elliptic period or classify
its Landau intersections.  The next test is the tensor multiplier on the
frozen Cayley--Menger critical/Landau scheme, followed by the elliptic
infinity quotient.
