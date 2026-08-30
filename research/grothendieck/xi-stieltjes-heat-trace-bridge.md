# The Li resolvent and heat-flow targets are Laplace dual

## Positive heat trace under RH

For the squared-coordinate Stieltjes function

`S(x)=sum_gamma m_gamma/(x+gamma^2)`,

use

`1/(x+gamma^2)=integral_0^infinity exp(-xt)exp(-gamma^2t)dt`.

Then

`S(x)=integral_0^infinity exp(-xt) Theta(t) dt`,

where

`Theta(t)=sum_gamma m_gamma exp(-gamma^2t)`.

This is the heat trace of the squared conditional Hilbert--Pólya operator.
It is positive for every `t>0` and completely monotone in `t` after the
appropriate spectral conditions.

Differentiation gives

`(-1)^n S^(n)(x)=integral_0^infinity t^n exp(-xt)Theta(t)dt`.

Thus the complete-monotonicity hierarchy is the moment hierarchy of one
positive heat trace.

## Hostile quartet in heat time

An off-line centered zero `a=alpha+i beta` contributes a squared pole at
`a^2`. Its conjugate pair produces the formal heat term

`exp(a^2t)+exp(conjugate(a)^2t)`

` =2 exp((alpha^2-beta^2)t) cos(2alpha beta t)`.

For a genuine off-axis quartet (`alpha beta!=0`), this term oscillates in
sign. Depending on `alpha^2-beta^2`, it may also grow. A positive background
can hide that oscillation pointwise, so the decisive failure is of complete
monotonicity/Stieltjes pole location, not necessarily of the order-zero sign
of the total heat kernel.

## Coupling of research gates

The Li/Toeplitz, Stieltjes-resolvent, Hilbert--Pólya, and heat-flow programs
are four transforms of the same proposed positive object:

`positive squared spectral measure`

` -> heat trace Theta(t)`

` -> Stieltjes resolvent S(x)`

` -> Caratheodory phase function`

` -> Li Toeplitz moments`.

Independent constructions no longer count. A source mechanism must commute
with these transforms and reproduce all four readouts.

## Source-side target

Construct `Theta(t)` arithmetically, without zero locations, and prove it is
the Laplace transform of a positive measure supported on `[0,infinity)`.
Then identify its Laplace transform with the completed-xi function `S(x)`.

This could proceed through an explicit-formula heat kernel, but prime,
archimedean, and endpoint terms must remain coupled. The isolated prime heat
contribution is not expected to be positive.

## Falsifiers

- A negative value of the source heat functional.
- Oscillation or exponential growth incompatible with nonnegative squared
  spectrum.
- Failure of the Laplace transform to reproduce `S(x)`.
- A heat construction depending on zeros or on the requested time/rank.
- Mismatch between heat multiplicities and Stieltjes residues.

This bridge is exact conditionally; it does not construct the source-positive
heat trace or prove RH.
