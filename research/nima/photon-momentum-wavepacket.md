# Iteration 5: a normalizable momentum-profile one-photon state

## The fixed-mode normalization gap is closed conditionally

Retain the seed-derived helicity coefficients c=(beta,alpha) from iteration 4. Supply the future-light-cone measure

    dmu(k)=d^3k/(2 k^0),
    [a_h(k),a_j^dagger(p)]=delta_hj*2 k^0*delta^3(k-p).

Factors of (2pi)^3 are absorbed consistently into this declared operator convention. Neither the measure nor the continuum CCR is derived from the two-packet incidence.

Use the north light-front chart

    q=k^0+k^z>0, u=k^x/q, v=k^y/q,
    k=(q(1+u^2+v^2)/2, q*u, q*v, q(1-u^2-v^2)/2),
    dmu=(q/2)dq du dv.

Supply the compact box

    q in [1,2], u,v in [-1/2,1/2].

Its exact measure is V=3/4. With n=|beta|^2+|alpha|^2, define

    psi_h(k)=c_h*1_box(k)/sqrt(V*n),
    A_psi^dagger=sum_h integral dmu(k) psi_h(k) a_h^dagger(k),
    |gamma(v,box)>=A_psi^dagger|0>.

The analytic integral gives

    sum_h integral dmu |psi_h|^2=1,
    [A_psi,A_psi^dagger]=1.

Together with the declared vacuum and continuum number algebra, this is a normalizable exactly one-photon state, not a distribution-normalized sharp-momentum ket. The support and its scale remain supplied preparation data.

The top-hat is an L2 momentum profile. No smooth boundary, compact spatial localization, unique wavepacket shape or apparatus preparation is claimed.

## Exact moments and a mass false-positive control

All moments are calculated by integrating polynomial monomials against (q/2)dq du dv, not by numerical quadrature. For the stated box:

    <P>=(49/54,0,0,35/54),
    <(P^0)^2>=247/288,
    <(P^x)^2>=<(P^y)^2>=5/24,
    <(P^z)^2>=127/288.

Therefore

    <P_mu P^mu>=0,
    <P>_mu <P>^mu=98/243>0.

Every momentum component of the one-photon state lies on the null shell. The timelike mean four-vector arises from directional spread; its squared norm is not a particle mass Casimir.

Energy has finite positive variance. The same seed with a doubled radial support has double the mean energy while retaining unit norm. No packet coefficient determines this chosen energy scale.

## Momentum-dependent polarization frames

The implementation constructs a smooth north-patch spatial rotation taking +z to k/|k|, followed in application order by a longitudinal boost from the retained reference energy. It maps the previously checked Maxwell polarization modes to each momentum in the profile.

For a supplied Lorentz map Lambda, compare the transported source frame Lambda*Gamma(k) with the canonical target frame Gamma(Lambda k). Their relative little-group action has a unit-modulus helicity phase and a gauge term. Exact tests verify:

- the null momentum and Maxwell conditions at the sampled field points;
- momentum-wise gauge-independent decoding to the original seed;
- unit-modulus Wigner phases;
- the Wigner phase composition law;
- a genuinely momentum-dependent phase for a transverse boost.

A general boost therefore must not be replaced by one constant two-by-two polarization matrix acting uniformly on this packet. No invariance of a momentum-traced helicity density in an arbitrary frame convention is asserted.

## Measure and norm under transport

A longitudinal boost with positive scale s acts by

    q'=s*q, u'=u/s, v'=v/s.

This maps boxes to boxes and preserves their measure exactly. The checker verifies transformed mean momentum and analytic normalization. Quarter-turn z rotations also give exact box-level controls.

For additional boosts and rotations, exact first-order jets compute the chart Jacobian at three rational points. They satisfy

    q'*det(d(q',u',v')/d(q,u,v))=q.

These are local exact audits of the declared Lorentz-invariant measure, not an attempt to infer the global integral from samples. The unit norm of the base packet is established by the analytic integral. Transported norm follows from the measure change-of-variables law and unit-modulus phases.

## A chart pole is not zero physical amplitude

A rotation can send a supported momentum to the south ray, where q'=0 and the north canonical frame fails. The checker explicitly reaches such a point. Canonical-coordinate/phase evaluation rejects the chart request, but the transported frame Lambda*Gamma(k) still gives a valid Maxwell polarization and exact seed decode.

The implementation does not delete that point or identify the chart singularity with absent photon support. A full global canonical-frame description would require another chart; the retained transported frame is sufficient for the test and for describing the transformed support.

## Distinct profiles are not automatically orthogonal modes

Shift the u interval to [0,1] while keeping the same q and v intervals. The two normalized equal-volume profiles have overlap 1/2, not zero. Their coherent sum has squared norm 3, not 2. A disjoint radial support gives zero overlap.

Thus giving two profiles distinct identifiers does not make their smeared oscillators independent. The profile inner product, rather than record naming, determines the cross commutator and coherent normalization.

## Important source-emission boundary

The free Hamiltonian acts as multiplication by k^0 on a one-photon momentum wavefunction. For this broadband packet,

    ||(H-<H>)|gamma>||^2=Var(H)>0.

Consequently free evolution is not closed within the one-dimensional span of this fixed profile. The normalized collective creation operator is legitimate, but cannot be substituted for a stationary single-frequency oscillator when constructing an energy-conserving source model.

A source interaction must handle the continuum bandwidth, source depletion and any external driving/work. Choosing the source gap equal to mean photon energy would match a mean, not prove exact energy conservation or supply the missing energy coherence.

## Verification

    python research/nima/checkers/check_photon_momentum_wavepacket.py

Fresh checks cover exact normalization/moments, the smeared CCR coefficient, pointwise Maxwell/gauge conditions, longitudinal and rotational box transport, generic local measure Jacobians, Wigner cocycles, chart-pole controls, profile overlaps and invalid-input/provenance controls. The run reruns iteration 4 and all preceding conditional source/Maxwell/Lorentz checks.

Implementation: `checkers/photon_momentum_wavepacket.py`.

Report: `results/photon-momentum-wavepacket.json`.

## Next executable iteration

Construct a conditional excitation-conserving source-field interaction that emits this normalized broadband packet. Retain the un-emitted vacuum outcome and source state, and account explicitly for driving/work and the failure of stationary one-frequency closure. This would move from a valid state expression to a specified emission process, without pretending that its coupling or energy source was selected by the original seed.
