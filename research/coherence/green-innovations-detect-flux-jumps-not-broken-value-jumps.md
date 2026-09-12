# Green innovations detect flux jumps, not broken value jumps

## The apparent comparison fails

The finite Green extension and broken-domain refinement both add one local line, but their quotient maps differ.

For every context point \(x\),

\[
k_x(t)=e^{-|t-x|}
\]

is continuous at \(x\). Every finite Green packet and every orthogonal innovation is therefore globally continuous. Consequently the broken-Sobolev value-jump functional satisfies

\[
J_x^{\rm value}(r)=r(x+)-r(x-)=0
\]

for every Green innovation \(r\).

Hence the induced map from the Green innovation quotient to the existing value-jump quotient is zero, not an isomorphism. Equal extension rank and locality do not authorize identifying the two cells.

## What the massive operator detects

The derivative of a kernel section has jump

\[
k_x'(x+)-k_x'(x-)=-2.
\]

Distributionally,

\[
(1-\partial_t^2)k_x=2\delta_x.
\]

For an interior innovation

\[
r_{x\mid S}=k_x-c_ak_a-c_bk_b,
\]

one has

\[
(1-\partial_t^2)r_{x\mid S}
=2(\delta_x-c_a\delta_a-c_b\delta_b).
\]

Modulo distributions supported on the old context set \(S\), its new quotient class is

\[
2\delta_x.
\]

Thus the Green extension canonically detects a flux or derivative-jump cell.

## Required repair

A common graph target must retain two seam channels:

```text
value jump: f(x+) - f(x-)
flux jump:  f'(x+) - f'(x-)
```

This requires a piecewise \(H^2\), maximal massive-operator, or equivalent graph domain. On such a domain, value jumps produce delta-prime terms and flux jumps produce delta terms. The existing broken \(H^1\) quotient records only the first channel, while Green innovations occupy the second.

The corrected comparison is therefore:

```text
Green innovation line
  -> flux-jump quotient
  != value-jump quotient
```

## Consequence

The scalar Green ind/pro realization has not yet been connected to the previously constructed value-jump recollement diagram. It instead proves that the graph constructor alphabet needs a value/flux refinement before a universal comparison functor can exist.

This is a typed obstruction, not a numerical one: both candidate quotients are one-dimensional, but they represent different boundary roles.
