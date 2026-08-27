# Flat composable networks can still project to scalar zeros

## Conjecture under attack

Perhaps RH remains open because the scalar projection hides a compositional invariant that becomes visible only after constructing a source-derived network of two reciprocal sheet objects, or two sheets plus a third reference object.

The conjecture is plausible as a research strategy. Its strong form is false: network composition, flatness, and reference framing do not by themselves constrain the zero locus of a scalar section.

## First categorical distinction

A failure to glue local sections is different from a zero of an already global section.

Let \(E=D\times\mathbb C\) be the trivial line bundle over a domain \(D\), with identity transition functions. The holomorphic section

\[
\psi(s)=s-s_0
\]

is globally defined and perfectly glued, but vanishes at \(s_0\).

Therefore a scalar zero is not generally a gluing obstruction.

Any RH use of the fourth tower needs an additional bridge theorem turning an off-seam scalar zero into a failure of a declared compositional invariant.

## Hostile network A: readout zero with nonzero lifted state

Take any connected graph, including a triangle. At every vertex let

\[
H_v=\mathbb C^2,
\qquad
A_v=M_2(\mathbb C),
\qquad
U_e=I.
\]

All transports are constructor-natural. Every loop holonomy is identity. Let the lifted state be the constant nonzero vector

\[
\Psi_v(s)=e_1.
\]

Define the scalar readout

\[
L_s(x,y)=(s-s_0)x.
\]

Then every object and every network composition is exact, while

\[
L_{s_0}\Psi_v(s_0)=0.
\]

The zero lies entirely in the source-to-scalar interface. Adding vertices, routes, or loop critics cannot remove it.

## Hostile network B: zero of a global lifted section

Keep the same trivial network and use a fixed readout

\[
L(x,y)=x.
\]

Let

\[
\Psi_v(s)=(s-s_0)e_1.
\]

The lifted section itself vanishes at \(s_0\). It is nevertheless global, analytic, path-independent, and compatible with every identity transport.

Thus even retaining the full lifted object does not prevent zeros without an independent nowhere-vanishing or strict-positivity theorem.

## Hostile network C: positive network norm with scalar kernel

Let the network energy be

\[
E_s(\Psi)=\lVert\Psi\rVert^2.
\]

For the constant state \(e_1\), this energy is one at every point. Choose instead a fixed scalar functional that annihilates \(e_1\). The network remains positive and faithful on states while the selected scalar output is zero everywhere.

Therefore positivity of a lifted network invariant does not constrain scalar zeros unless scalar vanishing is proved to imply vanishing of that invariant.

## Why the third-polarizer analogy is insufficient

The middle polarizer is an actuator. It inserts a new noncommuting projection into the optical evolution. It does not merely reveal a compositional relation already present in the original two-polarizer system.

Likewise, a third theta/Tate object can change the admissible dynamics only if its incidence maps and actions are independently source-authorized. Adding a mathematically convenient reference or seam object without such authority manufactures a new system rather than explains the original scalar section.

## Two versus three objects

Object count is not the invariant.

- One object with two independent endomorphisms can already form a loop.
- Two objects with parallel independent arrows can expose relative transport.
- Three objects form a triangle, but only if all three edges are independently authorized.
- Arbitrarily many objects add nothing when every arrow is derived from one path or every loop acts trivially.

The relevant quantity is the rank of independently authorized compositional routes and the coefficient module on which their discrepancies act.

## Reference limitation

A third reference fixes a gauge only on the orbit it spans. If its stabilizer

\[
\operatorname{Stab}_K(R)
\]

is nontrivial, loop transport remains ambiguous inside that stabilizer. A single vacuum or seam reference therefore does not automatically make all sheet holonomy observable.

## Required bridge theorem

For the network strategy to bear on RH, Grothendieck's source data must establish a typed implication of the form

\[
\xi(s)=0
\quad\Longrightarrow\quad
\mathcal N_s(\Psi_s)=0,
\]

where \(\mathcal N_s\) is a source-authorized network invariant, followed by an off-seam lower bound

\[
\mathcal N_s(\Psi_s)\ge c_K\lVert\Psi_s\rVert^2
\]

on compact off-seam sets, with \(c_K>0\), and a source normalization excluding \(\Psi_s=0\).

Without the first implication, the network invariant and scalar zero are unrelated. Without the lower bound, completion escape remains possible. Without nonzero source normalization, a global lifted section may simply vanish.

## Sharpened research conjecture

The defensible conjecture is not that composition explains RH automatically. It is:

> A source-derived multi-object network may supply a faithful invariant whose vanishing is forced by scalar Tate vanishing, even though no single projected object supplies such an invariant.

This is falsifiable by failure of source authority, failure of the scalar-to-network implication, a nontrivial reference stabilizer, or collapse of the network lower bound.

## Verdict

The strong claim is false. Perfectly flat, constructor-complete, reference-framed networks can carry scalar sections with arbitrary zeros. The network idea becomes RH-relevant only after a source-derived bridge theorem relates scalar vanishing to a nonnegative, completion-stable network invariant.

