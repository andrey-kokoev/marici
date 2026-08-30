# Localized `D(S3)` charge projectors have a source-derived operator lift

Owner: `marici.Kitaev`

## Question

Does the frozen quantum-double lattice supply any microscopic lift of the
eight-dimensional central endpoint record, or are the sector projectors still
only abstract block coordinates?

For a localized endpoint site, the lift exists algebraically. The primitive
central idempotents of the local `D(S3)` crossed-product algebra are finite
linear combinations of based flux effects followed by compatible gauge
actions. They form an exact eight-outcome projective charge observable with
finite support around the chosen site.

This closes only the operator-valued incidence arrow. The idempotents are not,
apart from the vacuum constraint, native terms of the fixed-point Hamiltonian.
Their coherent controlled extraction, pointer coupling, fanout, and
fault-tolerant implementation remain unproved.

## Claim boundary

The result concerns a localized anyon endpoint with a chosen site consisting
of a plaquette and base vertex. It is not the global torus ground-sector
projector problem. Torus-sector projectors require noncontractible Wilson
support or an equivalent global protocol.

The formula uses the frozen crossed-product convention from the local square
model. Reversing multiplication or edge orientation changes basis formulas
and must be transported explicitly.

## Local crossed-product algebra

Let `G` be a finite group. Write

\[
(g,x)=B^gU_x,
\qquad
g,x\in G,
\]

where `B^g` projects onto based plaquette holonomy `g` and `U_x` is the based
gauge action.

The frozen multiplication law is

\[
(g,x)(h,y)
=
\delta_{g,xhx^{-1}}(g,xy).
\]

The identity is

\[
1=\sum_{g\in G}(g,e).
\]

This is the finite transformation-group algebra

\[
\operatorname{Fun}(G)\rtimes G,
\]

with `G` acting on itself by conjugation.

## Simple-label data

Choose a conjugacy class `C`, a representative `c` in `C`, and an irreducible
unitary representation `pi` of the centralizer

\[
Z_c=\{z\in G:zc=cz\}.
\]

For each `g` in `C`, choose `x_g` satisfying

\[
g=x_gc x_g^{-1}.
\]

Transport the centralizer character to `Z_g` by

\[
\chi_{\pi^g}(z)
=
\chi_\pi(x_g^{-1}zx_g).
\]

Changing `x_g` by an element of `Z_c` conjugates the representation internally
and leaves its character unchanged. The transported character is therefore
well defined.

## Primitive central idempotent

Define

\[
Q_{C,\pi}
=
\frac{d_\pi}{|Z_c|}
\sum_{g\in C}
\sum_{z\in Z_g}
\chi_{\pi^g}(z^{-1})(g,z),
\]

where

\[
d_\pi=\dim\pi.
\]

These elements obey

\[
Q_{C,\pi}^*=Q_{C,\pi},
\]

\[
Q_{C,\pi}Q_{C',\pi'}
=
\delta_{C,C'}\delta_{\pi,\pi'}Q_{C,\pi},
\]

and

\[
\sum_{C,\pi}Q_{C,\pi}=1.
\]

They are the primitive central idempotents of `D(G)`.

## Why the formula is central

Multiplication by a gauge basis element transports

\[
g\longmapsto xgx^{-1}
\]

and simultaneously transports its centralizer element and character. The sum
over the full conjugacy orbit is invariant.

Multiplication by a flux function restricts the orbit component but does not
mix the centralizer character projector. The character-weighted centralizer
sum is the ordinary primitive central idempotent in the stabilizer group
algebra.

Thus the orbit sum and stabilizer character sum solve the two independent
requirements:

- gauge conjugation cannot change the result;
- different electric charges inside one flux class remain orthogonal.

Character orthogonality supplies idempotence and mutual orthogonality. Summing
over all stabilizer irreducibles gives the identity on each flux orbit, and
summing over all orbits gives the crossed-product identity.

## `S3` charge census

The conjugacy classes and centralizers of `S3` are:

| flux class | class size | centralizer | irreducible counts |
|---|---:|---|---:|
| identity | 1 | `S3` | 3 |
| transpositions | 3 | `C2` | 2 |
| three-cycles | 2 | `C3` | 3 |

Hence the primitive central idempotent count is

\[
3+2+3=8.
\]

Their simple-module dimensions are

\[
(1,1,2,3,3,2,2,2),
\]

matching the previously frozen labels

\[
(A,B,C,D,E,F,G,H).
\]

The dimension-square check is

\[
1^2+1^2+2^2+3^2+3^2+2^2+2^2+2^2
=
36
=
|S_3|^2.
\]

## Identity-flux projectors

For the identity conjugacy class, the centralizer is all of `S3`. The three
projectors are the character idempotents inside the identity-flux component.

For the trivial and sign representations,

\[
Q_A
=
\frac16\sum_{x\in S_3}(e,x),
\]

\[
Q_B
=
\frac16\sum_{x\in S_3}\operatorname{sgn}(x)(e,x).
\]

For the two-dimensional standard representation,

\[
Q_C
=
\frac13
\sum_{x\in S_3}
\chi_{\rm std}(x^{-1})(e,x).
\]

The vacuum charge projector is `Q_A`. On the local lattice source it is the
joint flatness and gauge-invariance projector at the chosen site, up to the
frozen ordering convention.

The other two identity-flux projectors distinguish pure electric charges.
They are not separate native terms of the fixed-point Hamiltonian.

## Transposition-flux projectors

For a transposition `t`,

\[
Z_t=\{e,t\}.
\]

The two one-dimensional centralizer characters give

\[
Q_D
=
\frac12
\sum_{g\in C_t}
\bigl((g,e)+(g,g)\bigr),
\]

\[
Q_E
=
\frac12
\sum_{g\in C_t}
\bigl((g,e)-(g,g)\bigr).
\]

Unlike an individual element-flux projector `B^t`, these sums are invariant
under based gauge conjugation. They resolve the two electric charges carried
by the transposition flux class without choosing one transposition as an
absolute gauge frame.

## Three-cycle projectors

For a three-cycle `r`,

\[
Z_r=\langle r\rangle\simeq C_3.
\]

Its three characters produce `Q_F,Q_G,Q_H` through the general formula. The
two nonreal characters require coherent cube-root phase weights in the
operator sum. Hermiticity follows because inversion conjugates the character
coefficient and the `*` operation reverses the centralizer element.

This already signals an implementation resource. A classical mixture of the
terms does not realize the character-weighted projector; their amplitudes must
combine coherently.

## Finite support

Every basis term

\[
(g,z)=B^gU_z
\]

acts on the union of the chosen plaquette boundary and base-vertex star. The
central idempotents therefore have finite site support independent of total
lattice size when the charge endpoint is localized.

Locality of support does not mean membership in the native Hamiltonian. The
fixed-point Hamiltonian contains Haar gauge and trivial-flux projectors, not
all character-weighted charge projectors as independently tunable terms.

## What has been lifted

The following arrow is now source-derived at operator level:

\[
\{A,B,C,D,E,F,G,H\}
\longrightarrow
\{Q_A,Q_B,Q_C,Q_D,Q_E,Q_F,Q_G,Q_H\}
\subset D(S_3).
\]

It supplies:

- exact charge labels;
- mutually orthogonal Hermitian projectors;
- a complete central PVM;
- gauge-invariant finite support around a localized site;
- compatibility with the previously frozen eight-dimensional central readout
  algebra.

This is stronger than an abstract block decomposition and weaker than a
physical measuring instrument.

## What remains missing

To create a physical record, the source must still implement a controlled
charge extraction such as

\[
\sum_aQ_a\otimes V_a
\]

on a pointer system, or an equivalent projective instrument.

That requires:

1. coherent synthesis of the character-weighted sums;
2. a pointer with at least eight distinguishable labels or a faithful binary
   encoding;
3. uncomputation or a declared dephasing update;
4. bounded leakage from the accepted excitation space;
5. geometric scheduling on the star-plus-plaquette support;
6. fault propagation and repeated-readout analysis;
7. calibration of the complex `C3` character phases;
8. an independent frame test for common label permutations.

The operator PVM does not supply these constructors automatically.

## Distinction from element-resolved control ports

The two endpoint ports that generate the full 36-dimensional algebra are an
individual transposition-flux projector and an individual three-cycle-flux
projector. They choose elements inside conjugacy classes and do not commute
with the gauge average.

The central projectors derived here sum over conjugacy orbits and stabilizer
characters. They preserve gauge invariance but generate only the
eight-dimensional center.

Therefore the new lift does not solve full endpoint controllability. It solves
the physically easier and algebraically smaller charge-record problem.

The distinction is exact:

- central charge PVM: gauge invariant, finite support, eight-dimensional;
- element-resolved flux ports: gauge framed, potentially gauge breaking,
  sufficient with gauge actions for 36-dimensional associative closure.

Replacing the latter by the former loses the noncentral matrix units needed
for full control.

## Distinction from torus ground sectors

A localized endpoint charge can be enclosed by a contractible site
neighborhood. Its projector is supported near that endpoint.

A torus ground-sector label has no localized excitation. Every contractible
native projector compresses to a scalar on the ground space. Resolving those
eight global sectors requires noncontractible Wilson loops or an equivalent
global protocol.

The labels may share modular data, but their physical incidence maps differ.
Local endpoint charge measurement cannot be silently substituted for torus
sector measurement.

## Record dynamics consequence

If a controlled implementation of the local PVM is supplied, the pointer-Gram
and fanout theorems apply directly. Orthogonal pointer labels can make the
central charge locally redundant while preserving all within-charge block
operators.

The many-body light-cone theorem then bounds how quickly those records can
propagate away from the localized endpoint. The CNOT-tree theorem describes
one abstract fanout schedule and its correlated fault spread.

Thus the record programme now has a typed starting observable. The remaining
gap is constructor dynamics, not absence of a central charge operator.

## Hostile fixtures

### Individual flux called gauge invariant

Use `B^t` for one transposition and claim it is a physical charge projector.
Gauge conjugation moves it around its three-element orbit.

### Conjugacy-class sum called charge complete

Measure only flux class membership and infer the electric centralizer irrep.
Each nontrivial class supports multiple charges.

### Character-weighted sum replaced by mixture

Randomly choose basis terms with classical probabilities and call the result
the coherent central idempotent.

### Local support called native pulse

Observe that `Q_a` has finite star-plus-plaquette support and infer that the
fixed-point Hamiltonian contains an independently tunable `Q_a` term.

### Endpoint projector used on torus ground sectors

Apply the localized charge PVM to an excitation-free torus and claim it
resolves the global topological ground-state label.

### Central lift called full control

Use all eight charge projectors and infer the missing noncentral endpoint
matrix units.

### Abstract controlled sum called apparatus

Write `sum_a Q_a tensor V_a` without supplying a microscopic interaction,
pointer initialization, or fault model.

## Falsifiers

- The displayed `Q_(C,pi)` fails centrality, Hermiticity, orthogonality, or
  completeness in the frozen crossed-product convention.
- The `S3` class-centralizer census produces other than eight simple labels or
  the frozen dimensions.
- An individual noncentral element-flux projector commutes with the gauge
  average.
- A conjugacy-class measurement distinguishes all centralizer charges.
- The central projectors generate noncentral within-block matrix units.
- A localized endpoint projector resolves excitation-free torus ground
  sectors by contractible support.
- Operator-level existence is promoted to controlled, fault-tolerant physical
  extraction.

## Shared Carrier geometry and coefficient lens

Shared Carrier geometry supplies the plaquette-plus-vertex site, oriented
support union, endpoint localization, and distinction between contractible
and noncontractible incidence.

The quantum coefficient lens supplies the crossed-product multiplication,
conjugacy orbits, centralizer representations, character idempotents,
Hermitian projectors, and charge interpretation.

The source-derived operator lift uses both. No other sector inherits the
`S3` character formula merely from sharing the Carrier site geometry.

## Disposition

The eight localized `D(S3)` charge projectors are no longer missing abstract
coordinates. They have an exact source-derived lift as primitive central
idempotents of the finite site algebra, built from based flux and gauge
operations with finite support.

This advances the objective-record programme while preserving the main
control obstruction. The central charge observable exists; its controlled
measurement and redundant fanout remain unbuilt. The element-resolved ports
needed for full 36-dimensional endpoint controllability remain gauge-framed
and are not replaced by these central sums.

No checker, build, or Git operation was run for this research-only packet.
