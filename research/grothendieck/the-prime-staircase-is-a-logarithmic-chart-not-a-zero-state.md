# The prime staircase is a logarithmic chart, not a zero-state

## Bounded question

How does the nonvanishing tensor product of local prime towers relate to the
additive prime-power staircase used in the Green identities?

## Finite Euler tensor product

For a finite prime set \(S\), define

\[
Z_S(s)=\prod_{p\in S}(1-p^{-s})^{-1}.
\]

Every local factor and hence \(Z_S\) is nonzero. Its connected logarithm is

\[
\log Z_S(s)
=\sum_{p\in S}\sum_{k\geq1}\frac1k p^{-ks},
\]

and its logarithmic derivative is

\[
-\frac{Z_S'(s)}{Z_S(s)}
=\sum_{p\in S}\sum_{k\geq1}(\log p)p^{-ks}.
\]

These are exactly the Euler-log and logarithmic-derivative prime-power weight
systems underlying the additive staircase currents.

## Typing of the aggregation map

The tensor-product object is multiplicative. The staircase is its connected
additive coordinate obtained by applying logarithm or logarithmic
differentiation. This coordinate is legitimate at finite cutoff because
\(Z_S\ne0\).

It is not a linear compression of the tensor product, and it does not preserve
all overlap geometry. In particular, local nonvanishing of every factor does
not give a lower bound for an additively summed cross-kernel.

## Failure at a zero

For a completed scalar section \(X(s)\), the logarithmic coordinate

\[
\frac{X'(s)}{X(s)}
\]

is undefined at a zero and acquires a pole under meromorphic continuation.
Therefore a staircase state identified through the logarithmic chart cannot
be used as a regular zero-state without additional determinant-line or
relative-boundary data carrying the divisor.

Defining the zero-state by canceling the pole after inspecting \(X\) would
encode the zero into the construction.

## Euler-chamber boundary

The infinite Euler product converges in its ordinary chamber and is nonzero
there. Continuing the completed scalar toward the critical strip leaves that
ordinary tensor-product realization. The local prime-tower nonvanishing
theorem remains true, but it no longer controls the analytically continued
scalar section.

Thus zeros do not arise because one local prime overlap vanished. They arise
only after the multiplicative object is passed through completion and a
different global readout chart.

## Result

The additive staircase is a source-derived and informative boundary observer,
but it is a logarithmic chart on the nonzero Euler object. It cannot itself
supply the missing zero-to-state bridge.

This closes the shortcut in which local acute overlap was expected to pass
through additive staircase aggregation directly.

## Remaining bridge

One must construct a boundary-bearing determinant or relative section that:

- agrees with the finite Euler tensor product without taking logarithms;
- continues through the critical strip;
- retains primitive, square, and archimedean currents;
- has a regular state space at its zeros;
- derives the additive staircase only as a tangent observable away from the
  divisor.

That object, not the logarithmic staircase alone, is the appropriate carrier
for a zero-confinement theorem.
