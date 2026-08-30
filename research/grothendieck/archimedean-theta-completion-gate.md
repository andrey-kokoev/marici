# Theta completion crosses the Euler boundary only with archimedean input

Epistemic-graph event: 1388.

## Input separation

The conditional Carrier program derives the additive group completion
`Gr(M)`, canonically the initial ring and hence a rank-one integral lattice.
From that point, introduce the following explicit archimedean realization:

1. embed the lattice in a real line;
2. choose self-dual Haar measure and Fourier character;
3. use the self-dual Gaussian `exp(-pi x^2)`; and
4. admit Poisson summation and Mellin integration.

These are not consequences of the finite correspondence calculus.  They are
the minimal new analytic inputs audited here.

## Theta reciprocity

For

`theta(t)=sum_(n in Z) exp(-pi n^2 t)`,

Poisson summation gives

`theta(t)=t^(-1/2)theta(1/t)`.

For `Re(s)>1`, Mellin transformation yields

`Lambda(s)=pi^(-s/2) Gamma(s/2) zeta(s)`

`=(1/2) integral_0^infinity (theta(t)-1)t^(s/2) dt/t`.

Splitting at `t=1` and using theta reciprocity gives

`Lambda(s)=1/(s(s-1))`

`+(1/2) integral_1^infinity (theta(t)-1)`

`  *(t^(s/2)+t^((1-s)/2)) dt/t`.

The integral on the right is entire in `s`.  Therefore

`xi(s)=(1/2)s(s-1)Lambda(s)`

extends to an entire function and satisfies `xi(s)=xi(1-s)`.

## Explanatory verdict

This construction supplies the missing continuation, gamma factor, and
functional equation once the archimedean realization is admitted.  It does
not derive that realization from the Carrier.  The finite Euler product and
the archimedean theta completion therefore have different provenance:

- intrinsic primes and formal local determinants: conditionally derived;
- real topology, self-dual measure, Gaussian, Fourier transform, and Poisson
  summation: new analytic structure.

The next spectral question is now mathematically well-typed for `xi(s)`, but
no self-adjoint or trace-class global operator with determinant `xi` has been
constructed.

## Scope

This is a conditional analytic completion theorem and provenance audit.  It
does not claim that archimedean analysis emerges from the Carrier or that the
zeros are an operator spectrum.
