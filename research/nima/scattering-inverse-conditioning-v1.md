# Finite inverse stability and exact failure domains

## Result and scope

The exact two-rim inverse is stable on a stated regular domain with explicit finite perturbation bounds. It is not uniformly stable near the source blind energy or across unbounded high energies. The high-energy failure is exhibited by admissible positive model pairs, not just by a large formal derivative in an unphysical direction.

The core/energy/channel convention and equal-threshold balanced contact class remain fixed. The finite eta/beta bounds below assume a known fixed threshold; they do not certify conditioning of the two-energy unknown-threshold inverse. All perturbations are algebraic model tests. No empirical noise law, detector calibration, measurement protocol or acquired data is admitted.

## A better observation chart

For the declared transmission amplitude t_s, set

    b_s=1/a_s=i t_s/(1-t_s),
    Delta=r0_odd-r0_even,
    z=(b_even-b_odd)/Delta,
    q=1/eta=r0_even+b_even/z.

This chart makes the cancellation explicit: the inverse recovers a lead impedance from the small difference of two reciprocal phase ratios. It is defined away from t_s=1, source poles and zero contrast; the previous regular inverse also excludes zero transmission and requires positive z,q and an open lead.

The finite identity is

    b(t+dt)-b(t)=i dt/[(1-t-dt)(1-t)].

Its derivative is i/(1-t)^2. A small source contrast and transmission approaching one both amplify algebraic amplitude perturbations.

## Finite, non-infinitesimal bounds

Fix nominal regular data and an exact source contrast. Suppose

    |1-t_s| >= d > 0,
    |dt_s| <= h < d,
    |Delta| >= c > 0,
    0 < z_lower <= z <= z_upper,
    |b_even|/z <= H,
    q > 0,       D_E=E-theta > 0.

Also keep perturbations inside the chosen observation/preparation domain. If preserving the old nonzero-transmission guard, require h below the nominal transmission magnitude too.

Define

    U=h/[d(d-h)],
    Z=2U/c,
    Q=(U+H Z)/(z_lower-Z).

If Z<z_lower and Q<q, the algebraic inverse satisfies

    |db_s| <= U,
    |dz| <= Z,
    |dq| <= Q,
    |deta| <= Q/[q(q-Q)],
    |dbeta| <= (2 z_upper Z+Z^2)/(4 D_E).

Proof: use the exact finite reciprocal identity, then the linear contrast quotient for z. For q use the common-denominator difference of b_even/z with |z+dz|>=z_lower-Z. Finally apply reciprocal and square identities. These bounds do not assume a Gaussian error, a sample size or a probability of failure. For complex perturbed inputs they bound the algebraic extension of the inverse; physical model admissibility remains a separate guard. Restricting to consistent model data preserves the bound.

A concrete exact control uses the principal model at E=2, eta=2,beta=1,theta=1/2. Both |t_s| and |1-t_s| exceed 1/2, 2<z=sqrt(6)<3 and |b_even|/z<1. Change b_even by z/10^6 and leave b_odd unchanged. The induced transmission perturbation has radius at most h=3/10^6. The reconstructed positive eta,beta are exact rational numbers and their actual errors satisfy the bounds. The receipt retains the exact margins, parameters and errors; no floating acceptance threshold is used. For orientation only, actual eta error is about 1.0075553e-5 versus bound 3.2125440e-4; actual beta error is about 1.2382337e-5 versus bound 1.4859308e-4. The acceptance comparisons use the underlying exact rational numbers.

## Exact source contrast and blind-point instability

The source contrast is

    Delta(E)=2504107(3292E-5391)
      /[E(3292E-4485)(10837264E^3-43349056E^2+44361887E-6431463)].

At E_b=5391/3292 it has a simple zero with exact nonzero slope. The inverse z Jacobian in b coordinates is (1/Delta,-1/Delta), hence diverges there. In the amplitude chart,

    |partial z/partial t_even|
       =1/[|Delta| |1-t_even|^2].

The nominal amplitude factors remain finite and nonzero at this blind point. The checker computes a positive finite limit of (E-E_b)^2 times the squared gain, establishing the simple-pole divergence. The exact admissible one-energy alias from the predecessor inverse is retained. No uniform blind-neighborhood inverse bound is claimed.

## High-energy failure is stronger than simple identifiability suggests

The exact source has

    Delta(E) = C E^-4 + lower-order terms,
    C=2504107/10837264 > 0.

The parity responses agree through the first three high-energy resolvent moments. Their distinction first enters the fourth inverse-energy power; high-energy coherent channels therefore lose source contrast rapidly.

For the principal eta=2,beta=1,theta=1/2, exact squared-gain limits give

    |partial z/partial t_even| ~ E^5/C,
    |partial eta/partial t_even| ~ E^(9/2)/C,
    |partial beta/partial t_even| ~ E^(9/2)/C.

These are absolute local gains in the declared complex-amplitude coordinates, not measured uncertainties or global error estimates. In particular, exact generic identifiability does not imply uniform robustness as energy grows.

## Admissible rival family proving no uniform high-energy inverse

Write q=1/2 for eta=2 and q'=1 for eta'=1. For each energy E>=4 choose

    beta'(E)=[(q-r0_even(E))/(q'-r0_even(E))]^2,
    theta'=theta=1/2.

The actual core metric proves all visible bare poles are below 4; both normalized bare responses at 4 lie between 0 and 1/2. Positive residues make them decrease above that point. Thus the displayed family has positive beta' and the same response-sign convention for every E>=4.

This choice holds even transmission EXACTLY equal to the principal eta=2,beta=1 model. The odd impedance difference is

    a'_odd-a_odd=(q-q')Delta
       /[z(q-r0_even)(q'-r0_odd)(q-r0_odd)].

The exact limits are

    beta'(E) -> 1/4,
    E^9 |t'_odd-t_odd|^2 -> C^2.

Thus the contact strengths stay separated by one and the kinetic parameters stay separated asymptotically by 3/4, while the complete two-port on-shell amplitude gap tends to zero like E^-9/2. Since reflection differences equal transmission differences, the full on-shell S operator norm gap is exactly twice the odd transmission gap. This is a statement about the whole on-shell S in the fixed model convention, not only one display value.

| Model energy | Odd transmission amplitude gap |
|---|---:|
| 4 | 0.006210236305414198 |
| 8 | 0.00006214238703490521 |
| 16 | 0.0000014986688185355257 |
| 32 | 0.000000050369910546444616 |

These display values come from exact rational squared gaps; monotonicity over the entire axis is not inferred from four samples. The families depend on the comparison energy: they are not a claim of equal broadband S for two fixed models.

The source and native energy labels are held fixed, so this is not the common energy-unit gauge or coordinate dilation of the predecessor audit. It supplies a direct failure of any uniform inverse-continuity modulus over the unbounded single-energy model class. It does not refute recovery from a predeclared bounded multi-energy observation vocabulary.

## Net disposition and next executable conceptual task

Work-net v5 records parameter-inverse-conditioning as constructed: explicit regular-domain bounds plus blind-point and high-energy failure witnesses. Native continuum-operation selection and the broader root remain open.

The next executable task tests another real assumption of this chain: the balanced mismatch class a=b=g=eta. Positivity alone also permits reciprocal scalar-port contact blocks

    [[a I,-g W^dagger],[-g W,b W W^dagger]],
    a,b>=0,       ab>=g^2.

Classify that larger conservative contact family against the actual source response, quotient coordinate gauges, and determine which prior inverse conclusions depend on the balanced rank-one assumption. This addresses the positive-completion freedom already found in iteration 3; it is not a task waiting on external delivery.

## Verification

Checker: `research/nima/checkers/check_scattering_inverse_conditioning.py`.

Receipt: `research/nima/results/scattering-inverse-conditioning-v1.json`.

The initial successful execution passed 44 exact controls, exit 0: `structured_command_execution:e_12616_1791931555385372300_125`. The final replay additionally checks full-S operator-gap normalization and exhausted/invalid finite-bound margins, and hashes this final report.

Exact symbolic/rational controls cover live predecessors, source contrast limits, actual spectral margins, inverse Jacobians, a finite admissible perturbation and rational bounds, and source-specific high-energy rival gaps. Scope controls reject uniform-global, empirical-noise and root/native-selection promotion. The analytic finite-bound and failure-domain implications are written arguments, not a new formal-kernel proof. No stationary field solver, measurement execution or source-owner mutation occurs.
