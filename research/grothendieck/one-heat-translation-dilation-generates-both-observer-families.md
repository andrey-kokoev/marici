# One heat--translation dilation generates both observer families

## Question

What single positive constructor would reproduce both all heat jets and all fixed-width translate-Gram observers?

## Joint kernel

Introduce the completed two-parameter source transform

\[
\mathcal K(t,z)
=
\langle\mathcal W,e^{-tu^2}e^{izu}\rangle,
\qquad t>0.
\]

The heat and translation coordinates are linked by the source identity

\[
\partial_t\mathcal K(t,z)
=
\partial_z^2\mathcal K(t,z).
\]

Fixed-width Gram observers use

\[
\mathcal K(t,a_i-a_j),
\]

while heat jets use

\[
(-1)^k\partial_t^k\mathcal K(t,0).
\]

Thus the two observer families are restrictions of one analytic object, not independent lists.

## Positive dilation contract

The desired constructor consists of:

- a Hilbert space `H`;
- a nonnegative self-adjoint operator `L`;
- a strongly continuous unitary representation `U_a` of real translations;
- a cyclic source vector `xi`;
- the commutation relation `U_a L = L U_a`;
- the source identity

\[
\mathcal K(t,a-b)
=
\left\langle
 e^{-tL/2}U_a\xi,
 e^{-tL/2}U_b\xi
\right\rangle_H.
\]

Every translate-Gram matrix is then positive because it is a Gram matrix in `H`. Every heat jet is simultaneously

\[
(-1)^k\partial_t^k\mathcal K(t,0)
=
\left\|L^{k/2}e^{-tL/2}\xi\right\|^2,
\]

with the usual domain condition. The heat equation follows from the relation between the translation generator and `L`.

## Spectral meaning

By the spectral theorem, the dilation is equivalent to one positive measure in the squared spectral variable together with its symmetric translation lift. Conversely, such a measure supplies `H`, `L`, `U`, and `xi`. This is the common positive constructor sought by both observer presentations.

## Meta-observer cells

A conformance meta-observer should verify:

1. semigroup composition in `t`;
2. group composition in `a`;
3. commutation of heat and translation actions;
4. the heat equation relating their generators;
5. agreement of the dilation matrix coefficient with the endpoint--gamma--prime explicit formula;
6. common arithmetic cutoff and tail control in every computed coefficient.

The first four cells prevent observer-dependent Hilbert spaces or regularizations. The fifth is the noncircular arithmetic crossing.

## Falsification boundary

Constructing this dilation from already positive Gram matrices is the GNS/RKHS theorem and assumes the target. Assigning the zero-side positive measure assumes RH. The open theorem is a prime/completion-derived construction of the same `H,L,U,xi`, or equivalently of the global Douglas contraction producing its feature map.

## Disposition

Unify the heat-jet and translate-Gram pyramids through one heat--translation dilation. This precisely answers which common transformation would generate every observer value and every coherence identity. Its existence is equivalent to positivity; its source derivation remains the RH-strength gate.
