# Newman zero velocity gives a two-parameter heat bridge, but no monotonicity

## Simple-zero velocity

Let `H_lambda(z)` obey

`partial_lambda H_lambda=-partial_z^2 H_lambda`.

Suppose `gamma_j(lambda)` is a real simple zero. Differentiating
`H_lambda(gamma_j(lambda))=0` gives

`gamma_j'(lambda)`

` =[partial_z^2 H_lambda/partial_z H_lambda]_(z=gamma_j(lambda))`.

This is the exact motion law while the zero remains simple.

## Two-parameter spectral heat derivative

On a real-zero interval define

`Theta_lambda(t)=sum_j exp(-t gamma_j(lambda)^2)`.

Then formally, under justified termwise differentiation,

`partial_lambda Theta_lambda(t)`

` =-2t sum_j gamma_j gamma_j' exp(-t gamma_j^2)`.

There is no universal sign because the velocities need not point uniformly
toward or away from the origin.

## Exact finite hostile model

For

`H(z)=(z^2-a^2)(z^2-b^2)`, with `0<a<b`,

the positive-zero velocities are

`a'=(5a^2-b^2)/[a(a^2-b^2)]`,

`b'=(5b^2-a^2)/[b(b^2-a^2)]`.

The outer velocity is positive, while the inner velocity changes sign at
`b=sqrt(5)a`. Thus even a reflection-symmetric real-rooted model has no
automatic monotonicity of individual zeros or of its spectral heat trace.

## Collision boundary

The velocity formula becomes singular when `partial_z H=0`, exactly at a
multiple-zero collision. This is the locus where a positive real spectral
measure may change topology and where the Newman threshold is detected.

## Research consequence

A Newman bridge cannot merely assert that `Theta_lambda(t)` is monotone in
`lambda`. A viable two-parameter theorem needs a more subtle order, convexity,
or comparison principle that survives interacting zero velocities and
controls collisions.

Possible targets include:

1. a Loewner order on the Stieltjes resolvents `S_lambda(x)`;
2. a transport equation for the squared spectral measure with a positive
   dissipation functional;
3. a determinant convexity inequality rather than pointwise heat
   monotonicity;
4. a collision discriminant that detects loss of the Stieltjes property.

The zero-velocity formula is conditional on a real simple divisor and does
not construct the source measure or determine the Newman constant.
