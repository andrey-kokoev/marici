# Prime transport must preserve completed endpoint cancellation

## Completed logarithmic derivative

For

`xi(s)=1/2 s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)`,

the logarithmic derivative is

`L(s)=1/s+1/(s-1)-log(pi)/2+psi(s/2)/2+zeta'(s)/zeta(s)`.

Although `L` is holomorphic at `0` and `1`, this displayed decomposition is
not termwise regular there.

At zero,

`1/s+psi(s/2)/2 -> -EulerGamma/2`.

At one,

`1/(s-1)+zeta'(s)/zeta(s) -> EulerGamma`.

These are coupled completion identities. Dropping either partner before
taking the rational-test residue changes the functional.

## Why a direct prime residue is invalid

The prime expansion

`-zeta'(s)/zeta(s)=sum_(n>=2) Lambda(n)n^(-s)`

is available only in the half-plane `Re(s)>1`. It cannot be inserted
termwise into the endpoint residue at `s=0`. Analytic continuation of the
sum is not a positive prime decomposition and may conceal precisely the
completion terms whose sign is at issue.

## Required transport theorem

Starting from the canonical completed residue

`E(p)=-Res_0 R_p(s)L(s)`,

derive an equivalent contour or distributional formula in which the zeta
logarithmic derivative is evaluated on a line `Re(s)=c>1`. Only there may it
be replaced by its von Mangoldt series. The contour shift must record all
crossed endpoint, pole, and gamma contributions under the same fixed
normalization.

The resulting source formula should have the schematic form

`E(p)=E_endpoint(p)+E_infinity(p)+sum_n Lambda(n) K_p(log n)`,

with a rigorously derived kernel `K_p`, convergence prescription, and
reflection partner. No term is allowed to be discarded merely because it is
indefinite in isolation.

## Positivity burden

The earlier isolated-prime obstruction predicts that the von Mangoldt sum
will not be a positive Gram form by itself. The objective is a universal
coupled identity in which its negative directions are repaired by the
endpoint and archimedean pieces.

## Falsifiers

- Using the prime Dirichlet series at `s=0` or `s=1` termwise.
- Splitting the two endpoint cancellation pairs before regularization.
- Losing a residue during the transport to `Re(s)>1`.
- A kernel whose definition depends on the polynomial degree.
- Claiming positivity of the isolated prime-power contribution.

This transport gate is the next analytic step toward a genuinely arithmetic
proof of the rational-square positivity cone.
