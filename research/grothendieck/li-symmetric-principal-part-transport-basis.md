# Symmetric principal parts form the canonical prime-transport basis

## Decomposition theorem

For a degree-`d` polynomial `p`, its rational-square test has the unique form

`R_p(s)=sum_(k=1)^(d+1) A_k(p)[s^(-k)+(1-s)^(-k)]`.

The coefficients `A_k(p)` are the Laurent principal-part coefficients at
zero. Reflection supplies the identical coefficients at one. After removing
both principal parts, the remainder is an entire rational function that
vanishes at infinity, hence zero. This proves existence and uniqueness.

## Endpoint jet formula

Write the completed logarithmic derivative locally as

`L(s)=sum_(j>=0) ell_j s^j`.

Then the pair-normalized Li energy is

`E(p)=-Res_0 R_p(s)L(s)`

`    =-sum_(k=1)^(d+1) A_k(p) ell_(k-1)`.

Thus all ranks use one universal pairing between symmetric principal parts
and completed-xi jets. Polynomial degree only truncates the basis; it does
not change the functional.

## Transport significance

The basis kernels `s^(-k)` and `(1-s)^(-k)` have standard Laplace/Mellin
interpretations as polynomial-exponential distributions. They are the
natural objects to transport to `Re(s)>1`, where `-zeta'/zeta` becomes the
von Mangoldt series. This is preferable to transporting each expanded
quadratic test separately.

A complete transport theorem must fix transform conventions and derive the
prime kernel, including all endpoint and gamma residues. The present theorem
provides the algebraic basis and exact jet pairing but does not yet perform
that analytic transform.

## Coupling warning

The coefficients `A_k(p)` are quadratic in the polynomial coefficients.
Even if individual basis evaluations have mixed signs, their completed sum
is fixed. Positivity must be proved for the whole quadratic image of `p`, not
by demanding positivity of every principal-part basis element separately.
