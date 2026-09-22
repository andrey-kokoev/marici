# The current calibration refinements fix one physical sector ratio, not a family of observers

## Audit result

The present physical calibration fixes A=2, spectral point 3i and receiver weight gamma=2. The numerical refinements enclose the SAME actual source-response quantities more tightly. They do not declare a sweep of physical detector settings.

Consequently the actual old two-sector ratio is one fixed number. Under these enclosure refinements the actual source evaluation, saturated kernels and filtered attachment remain unchanged, with identity comparisons. This is not a theorem that every hypothetical point in a calibration box defines an isomorphic observer.

The proposed physical-variation gate therefore needs a scope correction: there is no parameterized physical variation in the current calibration contract on which to perform that test. The prior whole-row gain theorem remains the applicable result for genuine coordinate changes. Detector redesign remains a separate question.

## 1. What the owning contracts actually fix

`arb-calibrates-the-improved-cubic-observer-on-the-original-six-event-witness.md` and its saved result `results/certified-private-sector-cubic-observer.json` specify:

- background A=2;
- spectral point 3i;
- receiver weight gamma=2;
- fixed arithmetic windows A1=[2,4] and A2=[4,12];
- L=L(7/2);
- exact completed-theta definitions of the window moments.

The subsequent source-realization note `../nima/arb-certifies-a-minimum-source-lift-and-an-all-depth-realizable-tail.md` explicitly keeps this protocol.

`../nima/acquisition-branches-now-use-independently-verified-task-certificates.md` allows observation/calibration intervals to narrow while retaining the declared task and source assumptions. Its A=3 and A=4 vacuum acquisitions are additional translated observations, not a physical sweep of the old A=2 two-sector detector.

Finally `../nima/calibration-dependent-source-witnesses-close-the-thin-data-certificate-gap.md` explicitly distinguishes the actual fixed calibration from its enclosure. Its policies x(E) do not assert that the actual source changes when an enclosure is refined.

Thus neither interval width nor the policy variable E establishes a realized family of old source functionals.

## 2. A certified enclosure for the actual ratio

After removing the common positive prefactor, the old functional on the two actual lower-filtration source shapes is

    ell(x_early)=-a, ell(x_late)=b,
    a=mu_A1-L, b=mu_A2-L.

The saved enclosing printed Arb balls give, using exact rational interval arithmetic,

    a in [115710013/200000000, 23522803/40000000],
    b in [249542013/200000000, 51156403/40000000].

Both are positive. Moreover

    b-a=mu_A2-mu_A1
        in [16491/25000,17509/25000].

In particular the actual ratio rho=a/b obeys

    115710013/255782015 <= rho <= 117614015/249542013,
    0.45 < rho < 0.48.

These bounds intentionally use conservative enclosing printed balls, not unrecorded floating-point midpoints. The original Arb analysis remains the external justification for those balls.

The chosen lower-filtration lift normalization is c=1-rho. It is therefore one fixed number in the positive interval

    [131927998/249542013,140072002/255782015].

Refining the enclosure changes our bounds on c, not the exact chosen homotopy defined using c.

## 3. What follows for kernels and what does not

On the span of x_early and x_late, the actual kernel line is

    span(x_early+rho x_late).

The fixed exact theta formula defines this line even when no finite numerical computation has returned an exact decimal representation of rho.

Replacing a bounding interval for rho by a smaller bounding interval leaves that actual line unchanged. The same applies to the complete actual observer: no seed functional has been changed merely by improving an enclosure. Consequently its full saturated source kernel and the associated filtered extension diagram have identity comparisons through the refinement sequence.

By contrast, if a hypothetical model independently allows two distinct ratios rho_1 and rho_2, then the corresponding kernel lines differ. A box enclosing rho does not show that either endpoint, let alone both, is attained by the physical theta family.

The earlier algebraic counterexample used ratios 1/3 and 2/3. BOTH lie outside the certified actual interval above. It cannot be used as two physical settings of the present calibration, even after common positive rescaling of the sector factors. Its role remains to disprove an unrestricted inference from positivity and restricted-task diagonal structure.

## 4. Do not confuse refinement with installing a new detector

There are three separate situations:

1. **Sharper enclosures of the same ideal coefficients.** The mathematical detector is fixed; source-marked comparisons are identities.
2. **Whole-row coordinate gains.** The detector families have fixed normalized source functionals; the coherent comparisons are proved in `whole-row-calibration-gains-transport-the-filtered-attachment-but-internal-reweighting-need-not.md`.
3. **New implemented coefficients or a different detector recipe.** Changing relative sector weights changes the actual functional unless a separate identity is proved. An error bound does not make this an exact frame change.

The ideal-versus-rational coefficient distinction is explicit in the owning Arb note. A newly installed rational midpoint is not merely an improved enclosure of an unchanged implementation. The ideal structural statements cannot silently be transferred to it as equalities.

Actual admitted detector redesigns also already have a source-kernel audit: `cubic-recalibration-preserves-nonsplitting-but-changes-the-source-marked-observer-tower.md` exhibits lower-filtration sources separating the original, two-private and sixteen-private extensions at fixed analytic parameters. Their agreement on cubic task coefficients does not make their saturated source evaluations identical. This is a recipe change, not physical variation deduced from calibration uncertainty.

## 5. Remaining physical-variation question

To ask whether rho is constant under a genuine physical parameter change, first specify:

- the varied parameter and its admitted domain;
- which source labels, detector templates and normalizations remain fixed;
- the common source comparison across settings;
- whether the change is analytical recalculation, coordinate re-expression or a new implemented detector.

One could then certify two realizable settings with distinct ratios, or prove constancy of their exact response ratio. No such parameterized physical family is supplied by the currently audited numerical calibration contract. This note neither invents one nor claims invariance under all future parameter variations.

## Verification

    python research/voevodsky/checkers/check_fixed_calibration_sector_ratio.py

The checker pins the saved calibration parameters, hashes its input artifact, computes exact rational enclosures, proves positivity of the old gap and lift normalization, and excludes the two earlier algebraic counterexample ratios from the actual enclosure.

It does not rerun the owning Arb integrals, certify interval endpoints as physical settings, or reconstruct the source module from numerical readings.
