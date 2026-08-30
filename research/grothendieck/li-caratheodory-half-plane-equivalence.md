# The entire Li Toeplitz system is one Carathéodory function

## Generating-function identity

Let `lambda_0=0` and

`c_0=lambda_1`,

`c_k=(lambda_(k+1)-2lambda_k+lambda_(k-1))/2` for `k>=1`.

Define the Carathéodory series

`C(z)=c_0+2 sum_(k>=1)c_k z^k`.

Discrete summation gives

`C(z)=(1-z)^2/z sum_(n>=1)lambda_n z^n`.

Li's logarithmic generating identity is

`log xi(1/(1-z))=log xi(1)+sum_(n>=1)lambda_n z^n/n`.

Differentiating and combining the two formulas yields the exact collapse

`C(z)=xi'/xi(1/(1-z))`.

## Positivity equivalence

A sequence `c_k` is positive definite on the integers exactly when its
Carathéodory series has nonnegative real part in the unit disk:

`Re C(z)>=0` for `|z|<1`.

The inverse Möbius map `s=1/(1-z)` sends the unit disk onto the half-plane
`Re(s)>1/2`. Therefore the full Li Toeplitz gate is

`Re[xi'(s)/xi(s)]>=0` for `Re(s)>1/2`.

Subject to the standard boundary and nondegeneracy qualifications, this is
RH-equivalent. If RH holds, the zero-phase Herglotz measure supplies the
positive real part. Conversely, a zero of xi in the open right critical
half-plane would give a pole of `xi'/xi`, incompatible with an analytic
Carathéodory function there; functional reflection then handles the other
half-plane.

## Explanatory gain

All finite Toeplitz determinants, all Li inequalities, the GNS unitary, and
the Cayley operator are boundary shadows of one analytic mapping property.
The severe coefficient cancellations are expected because Taylor
coefficients are a poorly conditioned view of a positive-real function.

This redirects the attack:

> prove that the completed logarithmic derivative maps the open right
> critical half-plane into the closed right half-plane, using arithmetic
> completion rather than zero locations.

## Barrier made explicit

The Euler product controls `zeta'/zeta` only in `Re(s)>1`, and even there its
real part does not by itself give the completed sign. Extending the
positive-real property to `Re(s)>1/2` is essentially the RH-sized step. The
Abel prime germ and gamma/endpoint terms must be coupled at the function
level, not coefficient by coefficient.

## Falsifiers

- Any point with `Re(s)>1/2` where the completed real part is negative.
- A pole of `xi'/xi` in that half-plane.
- A proposed Herglotz measure whose moments fail to equal the Li second
  differences.
- A proof using the assumed location of the zero divisor to establish the
  mapping property.

This is an equivalence and attack reformulation, not an RH proof.
