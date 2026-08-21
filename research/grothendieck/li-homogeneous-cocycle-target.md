# Gate C target: a homogeneous cocycle space, not a finite vector orbit

## Why the finite-orbit no-go is informative

For a critical-line zero `rho`, put `u_rho=1-1/rho`. Then `|u_rho|=1` and
the paired Li feature is `|1-u_rho^n|^2`. Formally this suggests

`lambda_n = sum_[functional pairs rho] |1-u_rho^n|^2`.

The counting measure on zero pairs has infinite total mass. Consequently the
constant section `1` is not a vector in its ordinary `L^2` space, so the
finite-vector estimate `||(I-U^n)e|| <= 2||e||` does not apply. Nevertheless
the differences `1-u_rho^n` may be square summable: for fixed `n` they are
`O(n/|rho|)` high in the spectrum, and the corresponding inverse-square tail
is the relevant convergence scale.

The right conditional object is therefore an affine or homogeneous Hilbert
space in which constants are discarded and the cocycles

`b_n(u)=1-u^n`

have finite energy. They obey

`b_(m+n)=b_m+u^m b_n`.

This is exactly the cocycle law already forced by the Cauchy-jet features.

## Noncircular source-side construction target

Construct, without using the zero divisor as input:

1. a source-defined positive energy form `E` on Cauchy-kernel jets modulo
   its null constants;
2. a source-defined isometry implementing multiplication by `u=1-1/s` on
   the completed homogeneous space;
3. finite-energy classes `[V_n]`, where `V_n=1-u^n`, satisfying the cocycle
   law;
4. an explicit-formula comparison proving `E([V_n])=lambda_n`;
5. a closability/domain theorem showing that the quotient and completion are
   canonical rather than fitted to `n` or to the zeros.

If these five clauses hold, Li positivity follows from a source energy. If
the construction first installs one fibre per zero, it is only the
conditional spectral model and does not meet the gate.

## Immediate falsifiers

- `E` is indefinite on a finite Cauchy-jet span.
- multiplication by `u` does not preserve `E` or its null space.
- some `[V_n]` has infinite energy.
- closability requires prior knowledge that all `|u_rho|=1`.
- the explicit-formula comparison leaves an uncontrolled archimedean or
  endpoint remainder.

This reformulation converts “find Li vectors” into a more precise question:
find the arithmetic Dirichlet form whose finite-energy coboundaries are the
Li features.
