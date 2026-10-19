# Certified positivity of the analytic arithmetic Gaussian packet

## Result

The previous packet is now certified at the **analytic arithmetic-form level**,
not merely after decimal rounding. The unchanged three Gaussian tests at

    t=1/10, frequency centres 0,14,21

give a real symmetric matrix whose interval LDL pivots are strictly positive:

    [2.10479979582235e-9 +/- 2.54e-24],
    [0.253159106194430 +/- 5.65e-16],
    [0.584806590983386 +/- 1.63e-16].

Arb ball integration encloses the gamma integral, and analytical bounds enclose
both infinite gamma and prime tails. Therefore every nonzero complex linear
combination of these three tests has positive arithmetic-form value, in the
repository's specified explicit-formula convention.

No zeta-zero locations are used in this certificate. The result does not prove
positivity for every Weil test, exhaust the zeros, or realize the arithmetic
and spectral operations on the two geometric seed faces.

## Same source, stronger verification

Source:
`research/grothendieck/explicit-two-variable-weil-heat-source-formula.md`.
The endpoint, gamma and prime terms remain separately labelled and use the
same centered half-divisor normalization as the previous scout. Prime powers
up to 1000 are enumerated directly. The integrator operates at 160-bit precision
with absolute and relative tolerance goals 1e-25. These are goals; the returned
ball radii, not the requested tolerance, determine the enclosure.

The entire arithmetic form is certified from its definition. Identifying that
definition with the classical completed-zeta explicit formula still carries
the repository's stated external-source verification boundary. The positive
packet calculation does not discharge that boundary by numerical agreement.

## Analytic gamma integrand

For real u, the gamma term contains Re psi(1/4+iu/2). Applying `.real` to a
complex quadrature ball would destroy the analyticity needed by the integrator.
Instead use its meromorphic continuation

    [psi(1/4+iu/2)+psi(1/4-iu/2)]/2.

It equals the desired real expression on the real axis. Digamma poles are
detected by nonfinite ball evaluation; the integrator must certify its analytic
subregions rather than assume the callback is entire. Multiplication by the
Gaussian preserves analyticity away from those poles.

The finite integral is evaluated over [-64,64], split at explicit integer
cuts. The imaginary part of each complete integral encloses zero. Taking the
real ball afterward is valid for the real integral; it is not used inside the
analytic callback.

## A rigorous bound on the omitted gamma integral

For a=1/4 and real b=u/2, the digamma series gives

    Re psi(a+ib)=psi(a)
      + sum_(n>=0) b^2/[(n+a)((n+a)^2+b^2)].

The summand is nonnegative and decreasing in n. Its sum is bounded by its first
term plus its integral:

    sum <= 1/a + (1/2)log(1+b^2/a^2).

Using |psi(1/4)|<6 and log(1+4u^2)<=4u^2 gives

    |Re psi(1/4+iu/2)| <=10+2u^2.

The bound |psi(1/4)|<6 follows from
psi(1/4)=-EulerGamma-pi/2-3log(2), with EulerGamma<1, pi/2<2 and log(2)<1.
No RH or zero data is used.

For the scalar shifted Gaussian at centre xi, set d=64-|xi|>0. On either
omitted tail put r=|u-xi|. Then r>=d and u^2<=2r^2+2xi^2. Define

    J0 = sqrt(pi) erfc(sqrt(t)d)/(2sqrt(t)),
    J2 = d exp(-t d^2)/(2t)+J0/(2t).

These are the exact Gaussian integrals of 1 and r^2 over [d,infinity).
The omitted digamma contribution, including its 1/(4pi) normalization, is
bounded in absolute value by

    2[(10+4xi^2)J0+4J2]/(4pi).

Arb evaluates that positive bound and proves it less than 1e-70 for every
packet entry. A zero-centred radius 1e-70 is added to each scalar gamma term.
The separate -log(pi) Gaussian integral is evaluated over the whole line
analytically, so it is not part of the omitted digamma integral.

## A rigorous bound on the infinite prime sum

The positive majorant and integral formula were derived in
`rh-gaussian-seed-packet-v1.md`. This turn evaluates them with outward-rounded
Arb arithmetic. It proves the decreasing-majorant condition at N=1000 and gives

    prime-tail bound
      = [8.9036215290353805383870465301728258139945531e-52
          +/- 2.11e-96]
      < 1e-50.

A radius 1e-50 is added to the prime partial sum. The mixed-Gaussian
polarization prefactor is applied afterward to all three scalar source terms.
The entrywise bound applies uniformly to their complete infinite prime sums,
not just the enumerated prime powers.

## Interval positivity and relation to the existing attachment

The six independent source entries are enclosed as balls and reflected to
form a symmetric 3-by-3 matrix enclosure. Interval LDL elimination proves
each pivot strictly positive, so the defined analytic packet is positive
definite for every nonzero coefficient vector in this three-test span.

The source values from the repaired numerical scout lie inside the new balls.
Differences between the analytic enclosure and the old rational rounding are
retained explicitly; they are no longer assessed solely by precision stability.

The signed native attachment theorem applies to this analytic Hermitian G:

    B_G=X+Y D^-1 G,
    B_G^dagger K B_G=G.

Thus the exact analytic packet has a mathematical native signed representation,
with its coefficient values enclosed by the certified source calculation.
The previous rational matrix B remains the exact attachment of G_round, not
literally B_G. Its exact pullback certificate must not be relabelled as a
certificate that its rounded entries equal the transcendental source.

This is still a global packet attachment into source/sink coefficient channels.
A local geometric assignment of prime translations and spectral operations
to ABC and ADB has not been constructed. Positive finite form representation
and operation-level shared-edge realization are different claims.

## Surviving and missing scope

**Established:** positivity of one analytic arithmetic packet with all its
prime and gamma tails enclosed; no zero-location input.

**Still absent:** an exhaustive zero-side certificate, independently verified
classical source normalization, incidence-respecting two-face operations,
restriction-compatible completed attachment, and positivity for all admissible
test packets. No finite positive packet removes the last all-test quantifier.

## Reproduction

    python research/voevodsky/checkers/certify_rh_gaussian_source_packet.py

The checker uses the existing read-only python-flint installation. No network,
dependency provisioning, scientific owner mutation or old supplier execution
occurs. Source formula, parameters, scout receipt, checker and dependency
entrypoint are hashed.

Prospective SCC fingerprint:
`f1852a076f6f3f82a26a84e7e7fd04f9f614921fc6e36c72f6b68202cf239767`.

Artifacts:

- `inputs/rh-gaussian-source-certification-v1.json`.
- `results/rh-gaussian-source-certification-v1.json`.
- `scc-models/rh-gaussian-source-certification-v1.json`.

Arb provides rigorous interval computation for the stated formulas and analytic
tail bounds. This is not a proof-assistant formalization of those bounds or
an RH proof.
