# Euler--gamma logarithmic gluing is exact but not termwise positive

Epistemic-graph event: 1428.

## Source-derived logarithmic gluing

Let \`y=s-1/2>1/2\` and \`x=y^2\`. From

\`xi(s)=(1/2)s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)\`,

the Stieltjes candidate of Ledger 1385 satisfies

\`R_Xi(y^2)=[xi'(1/2+y)/xi(1/2+y)]/(2y)\`.

In the honest Euler half-plane this is

\`R_Xi(y^2)=1/(2y)[
1/(y+1/2)+1/(y-1/2)
-(1/2)log pi
+(1/2)psi((y+1/2)/2)
-sum_(n>=2) Lambda(n)n^(-y-1/2)]\`.

Here the final series is the source-derived intrinsic-prime-power trace. This
is the first exact formula gluing the archimedean completion and intrinsic
primes at the logarithmic-resolvent level rather than multiplying their
scalar scattering phases.

## The sign obstruction

Every von Mangoldt coefficient is positive, but the complete prime trace
enters \`R_Xi\` with a minus sign:

\`R_prime(y^2)
=-(1/(2y))sum_(n>=2)Lambda(n)n^(-y-1/2)<0\`.

Thus the desired positive Stieltjes measure cannot be the direct positive
pushforward of intrinsic primes or prime powers. The gamma and polar terms
must cancel this signed contribution globally.

Those pieces are not separately spectral measures. The term
\`1/(y-1/2)\` is singular at the zeta pole, while the zeta logarithmic
derivative has the opposite singularity; only completed \`xi'/xi\` is regular
there. Termwise measure assignments therefore depend on a noncanonical
subtraction of cancelling singularities.

## Continuation gate reappears as positivity

If \`R_Xi\` is Stieltjes, its measure is recovered from the negative-axis
boundary values by Stieltjes inversion,

\`d mu(t)=-(1/pi) Im R_Xi(-t+i0)dt\`,

with atoms supplied by negative-axis poles. But the Euler series above exists
only for \`y>1/2\`, equivalently \`x>1/4\`. Reaching \`x=-t\` crosses the
Euler convergence boundary and requires the theta continuation.

After continuation, the desired measure is purely atomic at \`t=gamma^2\`
exactly when RH holds. Before continuation, the source decomposition is
signed and contains no such atom locations. Hence neither the prime trace nor
the gamma factor alone provides the positive Weyl measure.

## Consequence

The logarithmic/connected extraction is necessary but not sufficient:

- it prevents the scalar phase cancellation of Ledger 1380;
- it combines the exact prime and archimedean traces;
- it exposes the correct resolvent \`R_Xi\`; but
- positivity and atomicity emerge only after a global continuation whose
  required Stieltjes property is equivalent to RH.

A successful source boundary must categorify this cancellation: gamma and
prime defect spaces must combine before decategorification so that their
indefinite contributions form a positive quotient. No such positive quotient
is presently derived.

## Scope

This is an exact half-plane decomposition and a no-go for termwise positive
prime pushforward. It does not prove that the completed combination is
non-Stieltjes.
