# Spectral heat time is not the de Bruijn--Newman parameter

## Spectral heat trace

The complete-Bernstein/Stieltjes program produces

`Theta(t)=sum_gamma m_gamma exp(-t gamma^2)`.

Here the ordinates are fixed and `t>0` damps their squared values. If a
self-adjoint operator `H` exists, this is `Tr exp(-tH^2)`. The atom obeys

`partial_t exp(-t gamma^2)=-gamma^2 exp(-t gamma^2)`.

## de Bruijn--Newman deformation

In a standard convention, the deformed Xi family has Fourier form

`H_lambda(z)=integral exp(lambda u^2) Phi(u) cos(zu) du`.

It obeys the backward-heat equation

`partial_lambda H_lambda=-partial_z^2 H_lambda`.

Changing `lambda` changes the entire function and moves its zero divisor.
The de Bruijn--Newman constant concerns the parameter at which those moving
zeros become entirely real.

## Separation theorem

The variables have different roles:

- spectral `t` evolves functions of a fixed operator or fixed divisor;
- Newman `lambda` evolves the entire function whose divisor is being studied.

They are not interchangeable, and positivity of `Theta(t)` does not by
itself establish a statement about the Newman constant.

## Possible legitimate bridge

A real bridge would require a two-parameter source object

`Theta_lambda(t)=sum_gamma(lambda) exp(-t gamma(lambda)^2)`

on the range where the deformed zeros are real, together with a theorem for
how its Stieltjes measure changes under the backward-heat PDE. At collision
or nonreal bifurcation times this positive spectral representation may fail.

Such a theorem could connect monotonicity of a measure-valued flow to the
Newman constant, but it is new work. It may not be inferred from the
single-parameter heat trace.

## Charter consequence

The long-horizon explanation still demands compatibility with the
de Bruijn--Newman flow, but only after the fixed-divisor complete-Bernstein
gate is crossed. The two heat mechanisms must remain separately named and
their connecting map must be proved.

## Falsifier

Any argument identifying `t` with `lambda`, or using fixed-spectrum heat
positivity as direct evidence for the Newman constant, is invalid without a
two-parameter intertwining theorem.
