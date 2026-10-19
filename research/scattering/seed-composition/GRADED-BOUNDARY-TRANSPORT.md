# Retaining primitive length requires a four-dimensional constant boundary carrier

**Iteration 4 of the requested ten-turn work-net run.**

**Strength:** exact polynomial intertwining and minimal constant invariant-carrier theorem for the supplied boundary family. Not a physical clock, a new particle sector or an exclusion of parameter-dependent two-planes.

[Previous all-parse transport](ALL-PARSE-TRANSPORT.md) · [Checker](check_graded_boundary_transport.py) · [Receipt](results/graded-boundary-transport.v1.json)

## 1. Fresh state and declared operator

Retained all-parse transport now closes at primitive-prefix level, but neither tested fixed-primitive-step endpoint readout carries the oscillatory reference C3 plane. The earlier macro-step identity remains correct under its different event count.

Keep the existing segmented boundary return family without setting its grading variable to one:

    F(z)=z A+z^2 C,    C=B D,    A+C=K.

A records returns using one primitive arrow. BD records returns using two primitive arrows through an internal state. The matrices are reused from the checked segmented controller. The variable z records primitive length; it is not identified with energy, a measured frequency or physical time.

Let V be the existing 12-by-2 synchronized reference frame. At z=1,

    K V=V T,
    T=((-1/2,1/2),(-3/2,-1/2)),
    T^2+T+I=0.

The question is whether this same plane survives when the one- and two-step terms remain distinct.

## 2. An exact fixed-plane defect

Take the linear functional

    ell(y)=y_BC_first - y_DpC_second.

These two entries agree on the synchronized reference frame, so ell V=0. Direct computation from the source blocks gives

    ell A V = (-1,0),
    ell C V = ( 1,0),
    ell F(z) V = (z(z-1),0).

Consequently the full reference plane cannot be invariant at any z other than 0 or 1. At z=0 the entire operator is zero; at z=1 the original macro identity is recovered. Invariance at z=1 is independently checked, not inferred merely from this necessary condition.

In particular, replacing T by a scalar multiple or another two-by-two matrix on the **unchanged V** cannot account for F(z) generically: its output has a component outside that plane. This does not reject a changing frame V(z), nor identify a physical clock law.

## 3. Construct the minimal constant enlargement

Write V=(v_s,v_t). Starting from these two columns, repeatedly apply A and C and retain every independent generated direction. The exact dimensions are

    2 -> 3 -> 4 -> 4.

A concrete resulting basis is

    H=(v_s, v_t, A v_s, A^2 v_s).

The checker proves rank H=4 and constructs rational four-by-four matrices A4,C4 satisfying

    A H=H A4,
    C H=H C4.

Therefore, coefficient-by-coefficient in z,

    F(z) H = H M(z),
    M(z)=z A4+z^2 C4.

No desired spectrum is inserted into A4 or C4. Their coordinates are extracted from the actual images of H using four independent coordinate rows; no physical inner product or energy metric is selected by this basis calculation. The receipt contains the full matrices and a rational left inverse of H.

### Minimality scope

Every constant linear carrier containing V and invariant under both A and C must contain the four independent columns generated above. H itself is invariant. Hence four is the minimal dimension in this class.

For a constant carrier, invariance under F(z) for every z implies invariance under its two coefficient blocks, so this also gives minimality for constant carriers of the polynomial family. It does **not** establish minimality among z-dependent subspaces or bundles.

## 4. Where the extra coordinates enter

Order the H-coordinates with the original reference plane first. The lower-left block of M(z) is

    ((z-z^2,0),
     (0,0)).

Thus a generic graded return excites a third coordinate from the original s direction. Further application generates the fourth coordinate. At z=1 this coupling cancels, and the original reference plane again carries T with period three.

The two additional coordinates are required comparison/continuation directions of this finite boundary calculation. They are not new emitted particles or two independently prepared output modes.

There was already a four-dimensional common-role carrier in the earlier macro-only construction. Equal dimensions do not identify the two: the union of that carrier and H has rank six. The checker explicitly prevents substituting one for the other.

## 5. Current disposition and next test

**Constructed:** an exact clock-graded boundary transport on the smallest constant carrier containing the synchronized reference plane.

**Obstructed:** treating the original fixed two-plane as invariant under the length-graded family, or describing its generic evolution merely by rescaling the old two-by-two step.

**Still open:** whether the explicit four-dimensional M(z) has a z-dependent rank-two invariant continuation of the reference plane near z=1, how such a continuation behaves at other z, and whether any associated weighting/clock operation is source-authorized.

That is the next nonredundant executable test. It should examine the actual polynomial family and any singularities, not impose an invariant plane or choose a root solely to reproduce the desired phase. The supplied dictionary, control, correlated preparation, physical metric and independent-output questions remain unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_graded_boundary_transport.py
python research/scattering/seed-composition/check_graded_boundary_transport.py --check
python research/scattering/seed-composition/check_all_parse_transport.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

All ranks and identities use exact rational arithmetic. The polynomial intertwining is verified through its coefficients, not only at sample z values. Samples at 0, 1, -1, 1/2 and 2 provide additional controls. Existing pinned contracts and formal outcomes remain unchanged.
