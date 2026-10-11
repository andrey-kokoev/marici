# Closing the common charging law excludes this mass branch

## Result

Reusing the existing one-gap-per-occupied-channel charging law closes the previously free carrier baselines. The resulting shared mediator model cannot reproduce both the proton/electron ratio and the neutron–proton splitting, at ANY coupling strength within the assumptions below.

This is stronger than the earlier failed half-gap numerical fixture. It eliminates adjustment of the field strength, overall clock and belt contact as repairs of this particular common charging branch.

## 1. Recovered charging construction

`research/nima/mass-comparison-charged-core-dressing.md` supplies the occupation law

    H_channel = n + 2(n-c)^2.

For c=0 the unique minimum is n=0 with energy zero. For c=1 it is n=1 with energy one. Both terms can be read as shared-gap occupation/consistency projectors, with two identical consistency contributions. The full occupied source programme costs N gap units. This energy is stored occupation energy, not the work of traversing arrows.

The geometry bridge freshly records N=1836 intrinsic channels for both carriers. Applying that recovered rule gives

    bare proton baseline = bare belt baseline = 1836,
    bare elementary occupation baseline = 1.

All charging registers are distinct from the mediator pool. Their number terms commute with the carrier/field operators, so their occupied-sector energies add. The neutral field and common empty-reference subtraction remain exactly as constructed previously.

Equal charging gaps and occupation locking are the recovered construction rules, not new fitted offsets. Particle-sector protection and physical admission of those registers remain separate. The neutral belt uses its declared occupied particle sector; no electric charge is inferred from its slot norm.

The prior compact-rotor quotient action also yields N versus one under equal charging inertias, but permits different inertias. It does not select an alternative numerical baseline and therefore cannot repair this branch just by changing the reference terminology.

## 2. Complete absolute readout

Write d=g^2/Delta for the field displacement magnitude in elementary-gap units. The source-derived all-face contacts of both proton and elementary spinor are their coherent modes. They attain the same exact downward shift -d.

The belt shift e_b satisfies -d<=e_b<0. Its actual profile gives strict e_b>-d.

Thus

    E_e = 1-d,
    E_p = N-d,
    E_b = N+e_b.

The elementary sector is stable when d<1. No clock factor changes these ratios.

For the frozen d=1/4 fixture:

    E_p/E_e = (1836-1/4)/(1-1/4) = 7343/3
            = 2447.6666666667.

The retained proton/electron reference is 1836.152673. The earlier relative-only calculation concealed this larger absolute discrepancy by leaving the proton bare baseline unspecified.

## 3. Eliminate the field strength exactly

Let R_p=E_p/E_e. Then

    R_p-N = (N-1)*d/(1-d).

Since E_b-E_p=e_b+d<=d,

    (E_b-E_p)/E_e <= (R_p-N)/(N-1).

This is a profile-independent inequality for the stated shared-law family, not a sampled fit.

If R_p is constrained to the retained reference 1836.152673, the maximum splitting is

    152673/1835000000 electron rest-energy units,
    approximately 42.5153911 eV.

The retained splitting is 2.530989 electron units, approximately 1293332.72146155 eV. The intervals are disjoint by over four orders of magnitude.

Consequently no g or Delta can satisfy both mass comparisons while keeping the recovered common baseline law, coherent proton/elementary contacts and shared normalized displacement interaction. A different belt profile cannot evade the bound because its energy is bounded below by the same -d.

At the frozen half-gap vertex there is an additional elementary-only bound:

    (E_b-E_p)/E_e <= (1/4)/(3/4)=1/3.

The retained splitting 2.530989 also violates that bound without even specifying N.

## 4. Scope of the exclusion and productive next branch

This excludes the combination of:

1. one shared charging gap on all N retained intrinsic channels;
2. a one-gap elementary occupied-sector baseline;
3. the same normalized projector-displacement field for each carrier;
4. coherent proton and elementary all-face contacts;
5. a positive elementary sector above the same empty reference.

The contact construction, finite signed-record mediator and heavier-belt ordering remain valid mathematics. They cannot be promoted to the observed mass ratios under this charging law.

The next change must be a real source-supported charging form or elementary-sector interaction. The prior gap-symmetry and source-cost audits already show why generic symmetry, traversal counts and preparation effort cannot supply it. Recompiling a controller or rescaling this field does not address the excluded relation.

A productive candidate must specify its new physical record degree of freedom and charging action, then test the absolute and relative ratios together. Changing a baseline solely to match a measured deficit is not fed back into this construction.

## Verification

    python research/voevodsky/checkers/check_common_charging_mass_closure.py

Results: `results/common_charging_mass_closure.json`. Exact checks recover channel counts, verify single-channel minima, reproduce the interacting elementary denominator, eliminate the common displacement parameter, and test the universal inequality on independent rational fixtures. Geometry, interacting field and held-out reference receipts are separately hashed. The algebraic proof above establishes the general bound; fixture checks are regression coverage.
