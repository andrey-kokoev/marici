# What mechanical recoil the existing exchange can represent

## Start with the established port, not a new dynamics

The prior native-port adapter binds primitive seed occurrences to normalized
features f in the existing exchange carrier. At any one port let

    a=f^T H y, b=r.

Because f^T H f=1, its update is EXACTLY `(a,b)->(b,a)`; the carrier component
orthogonal to f stays fixed. This note tests possible mechanical readings
of that same two-mode exchange. It does not replace it by a fitted kick.

## Direct local body assignment selects equal masses

Suppose body momenta are separately `p1=alpha*a` and `p2=beta*b`, with
nonzero positive calibration scales. Total-momentum preservation for all
inputs requires alpha=beta. Preservation of kinetic energy
`p1²/(2m1)+p2²/(2m2)` then requires m1=m2.

Thus a literal carrier-mode/body-1 and record/body-2 assignment gives
an equal-mass exchange collision, not the earlier unequal-mass response.
For m1=2,m2=3, unit scales and (a,b)=(0,1), the kinetic increment is 1/12.
The naive unequal-mass identification fails.

## Unequal-mass recoil via a declared mixed view

For ANY supplied positive masses define M=m1+m2,

    e+=(1,1)/sqrt(2), e-=(1,-1)/sqrt(2),
    u=(sqrt(m1),sqrt(m2))/sqrt(M),
    n=(sqrt(m2),-sqrt(m1))/sqrt(M),
    O=u e+^T+n e-^T,
    p=diag(sqrt(m1),sqrt(m2)) O (a,b).

O is orthogonal. This view mixes carrier and record; it is not the local
assignment that failed above. In declared numerical units the source pair's
half-norm becomes physical kinetic energy. An actual unit conversion would
still require calibration.

The SAME exchange now induces

    p1' = ((m1-m2)p1+2m1 p2)/M,
    p2' = (2m2 p1+(m2-m1)p2)/M.

This is the standard one-dimensional elastic-collision transformation.
It preserves total momentum and kinetic energy, is involutive, and gives

    J = p1'-p1 = 2m1*m2/M * (p2/m2-p1/m1),
    p2'-p2 = -J,
    delta_v1=J/m1, delta_v2=-J/m2.

Thus the inertial/recoil part of today's triangle has a concrete conditional
reading of the existing exchange. The source did not select those masses:
EVERY positive pair admits this construction.

For m1=2,m2=3 and initial momenta (0,1), the final momenta are (4/5,1/5).
The impulse is 4/5; the velocity-increment ratio is -2/3. Unlike the
externally driven impulse-from-rest fixture, this is an isolated elastic
redistribution of already-present kinetic energy. It creates no motion from
zero physical momenta.

## Charge is still absent—not hidden in normalization

The exchange impulse has no charge variable. Reversing an assigned charge
therefore does not reverse it; declaring a neutral body does not switch it
off. The original charge triangle requires both properties for its supplied
fixed-kernel law.

One could DEFINE G=J/(charge1*charge2) for nonzero charges, making the
triangle commute. That is circular fitting, not a derived coupling law,
and is singular at neutrality. The checker explicitly distinguishes this
identity from physical selection. A charge-dependent scheduler or coupling
would be NEW data; none is inserted here.

## Position and multiport boundaries

The real two-amplitude pair does not already contain two positions and
two momenta. One can add positions and take the cotangent lift

    p'=E p, x'=E^(-T) x.

It is symplectic. It generally changes positions; keeping arbitrary positions
fixed while applying E to momenta is not symplectic on unrestricted phase
space. On the contact subspace x1=x2, the cotangent lift DOES fix the
positions. This permits a conditional contact-scattering interpretation,
not a source-derived collision event, free-flight law or physical clock.

The mixed readout is constructed for ONE port. Different seed ports overlap
in the shared carrier. A single consistent global body/mass assignment across
those events has not been proved, nor has a three-dimensional spatial reading.

## Disposition

Positive: the prior exchange admits exact inertial, momentum-balanced,
energy-conserving recoil through a specified mechanical readout.

Negative: it does not yet supply the signed-charge interaction, initial
excitation, physical masses, source-selected body map, positions or timing
needed to close today's full programme. The driven impulse fixture and
this elastic collision must not be silently treated as the same process.

## Verification

    uv run --with sympy python research/nima/checkers/check_exchange_recoil_readout.py

22 exact symbolic checks pass. Receipt:
`results/exchange-recoil-readout.json`. These are symbolic mechanical-readout
checks; no new native-source or Agda physical-model theorem is claimed.
