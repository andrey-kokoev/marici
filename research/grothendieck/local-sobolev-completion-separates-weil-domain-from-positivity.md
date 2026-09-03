# Local Sobolev completion separates the Weil domain problem from positivity

## Question

Can the common-core and completion gates be constructed independently of a positive spectral measure?

## Fixed-support core

For `L>0`, let

`C_L=C_c^infinity((-L,L))`

in logarithmic coordinates, with reciprocal involution `f*(x)=conj(f(-x))`. For `f,g in C_L`, their convolution `f*g*` is supported in `[-2L,2L]`. The completed Weil form is defined source-side by endpoint, archimedean, and prime-power terms on this common core.

This core is arithmetic-independent and nested in `L`. It does not assume RH.

## Prime term is bounded without positivity

Only prime powers with `log n<=2L` occur. For every displacement `a`,

`|(f*g*)(a)| <= ||f||_2 ||g||_2`

by Cauchy--Schwarz. Hence the finite prime contribution satisfies

`|P_L(f,g)| <= C_prime(L) ||f||_2 ||g||_2`,

where `C_prime(L)` is the explicit finite sum of the absolute prime-power coefficients. This is a source-derived bound, not a positivity assertion.

## Endpoint term is bounded without positivity

Polar evaluations become weighted integrals of `f` and `g` over the compact interval. Since `exp(plus/minus x/2)` is bounded on `[-L,L]`, Cauchy--Schwarz gives

`|E_L(f,g)| <= C_endpoint(L) ||f||_2 ||g||_2`.

Thus neither endpoint nor prime terms obstruct a local Hilbert completion.

## Archimedean gate

The remaining task is to place the gamma distribution on a fixed Sobolev scale. Since the completed archimedean functional is a finite-order distribution on compact support, there exists some integer `s(L)` and constant `C_gamma(L)` with

`|Gamma_L(f,g)| <= C_gamma(L) ||f||_{H^s} ||g||_{H^s}`.

For a usable theorem, the order and constant must be derived explicitly from the digamma kernel rather than invoked abstractly. The likely minimal scale is low because the logarithmic singularity is locally integrable, but that claim remains to be proved.

Once this bound is explicit, the full Weil form extends continuously to

`H_0^s((-L,L))`.

By Riesz representation it is a bounded self-adjoint operator `A_L` relative to the independently positive Sobolev inner product:

`Q_L(f,g)=<A_L f,g>_(H^s)`.

## What this gains

This construction separates two questions:

1. **domain/completion:** boundedness of `A_L`, derivable from the explicit formula without RH;
2. **RH-bearing positivity:** `A_L>=0` for every `L`.

No positive zeta spectral measure is needed to define the ambient Hilbert spaces or the operators. The inverse-limit phantom problem is avoided by taking ordinary Sobolev closures on each fixed support window.

## What remains

Positivity of every `A_L` is still Weil's criterion in operator form. Compact-support inclusions must also be checked: extension by zero from the `L` window to a larger window should intertwine the forms on the common core, but the representing Sobolev operators depend on the chosen ambient norms and need not commute literally.

The first exact missing theorem is an explicit archimedean Sobolev bound with stated order and constants. After that, a certified negative eigenvalue of any finite Galerkin compression falsifies positivity, while positive compressions remain finite evidence.

## Disposition

The completion blocker is potentially solvable without RH: construct local Sobolev Weil operators from the source formula. This does not solve positivity, but it removes the false choice between assuming a positive spectral measure and using an unrestricted inverse quotient limit.
