# Intrinsic spin transport and declared networks for the five diagonal seeds

## Result

All five added triangle actions preserve **both** prior rank-two doublets, as well as their rank-four sum. This holds for both chiralities, using the intrinsic pentachoron face frames and exact reflection-word spin lifts—not copied identity-fiber transports.

For each triangle lift T, its operation-defect energy obeys

    (2I-T-T*) Q = Q,

where Q is the rank-four lowest seam-mismatch projector. Thus adding this defect with the prior common coefficient shifts both doublets equally by one; it does not choose between them. This is a dimensionless conditional operator identity, not a physical energy measurement.

## Source binding and checks

`checkers/check_diagonal_spin_networks.py` reads the existing diagonal source receipt. Every generated rotation is checked against its actual affine matrix and translation through the prior geometric basis. Source A maps to geometric E; source BCDE maps to geometric ABCD. This avoids confusing the two attachment label conventions.

For every source cycle and added triangle, in both chiralities, the checker verifies:

- the actual vertex permutation and affine intertwiner;
- a unitary spin lift from the displayed even reflection word;
- covariance of every directed face projector and every intrinsic fold;
- unitary all-cell transport and invariance of the mismatch operator;
- invariance of Q and each of its two doublets;
- reverse recovery of every prefix of a ten-step alternating-generator schedule.

For the chosen words, the triangle lifts cube to -I and the five-cycle lift has fifth power -I. These signs are retained lift conventions, not physical periods. Reversing the triangle lift changes its defect from I to 3I on Q, still without selecting a doublet.

Both doublet attachment isometries and their full face encodings are compared exactly with the prior exported records. No rounded coefficients are used. Input receipt hashes and all referenced prerequisite hashes are checked.

## An explicit staged coefficient protocol

Let J be the direct sum of the five intrinsic tetrahedral encodings, mapping ten logical cell coordinates to forty face coordinates. Let P be Q or either admitted doublet projector. Declare

    L = direct sum over directed face ports of P_cd,
    G = N = J P J*.

The checker verifies J*J=I, LJ=J, P*=P=P² and NL=N, hence

    N G L = N² L = N.

This is the global analogue of the existing local projector protocol. Choosing P and this factorization is explicit additional model data; neither the seed nor a return projector uniquely forces a staged implementation.

All five diagonal cases, for both chiralities, have:

| Carrier | L support | G support | N support | Total protocol transfers | Return rank |
|---|---:|---:|---:|---:|---:|
| Full lowest space Q | 80 | 1520 | 1520 | **3120** | 4 |
| Constant doublet | 80 | 1520 | 1520 | **3120** | 2 |
| Complementary doublet | 80 | 1520 | 1520 | **3120** | 2 |

Each protocol has forty raw complex coordinates, or 120 stage-typed ports. The exact operators are exported and recovered coefficient-for-coefficient. The equal counts do not mean the three projector matrices are equal.

**3120 is a count for this declared full-five-cell protocol, not a replacement for the native single-cell 144 or a physical particle identity.** The static protocol already uses the completed pentachoron; it is shared with the baseline five-cycle. Added generators are retained as distinct symmetry transports and are not silently inserted into L/G/N or their support totals. A protocol that executes transport as an additional stage needs its own declared schedule and count.

## What the five cases do and do not distinguish

The new triangle generators do not force a larger carrier or destroy either doublet. Their restricted traces are 1 on each doublet and 2 on Q under the displayed lift conventions. Their equal defect shifts and equal static protocol counts offer no distinction between the five additions. Their labelled transport matrices and marked-attachment behavior still differ.

This is stronger than the old rank-ten/720 direct-sum control, but it does not establish full equivalence of every marked-attachment experiment. No mass, charge, unique lift, physical clock or preferred doublet is inferred. Closed-cycle positivity and support minimality of this new global protocol were not tested here.

## Reproduction

```sh
python research/strominger/checkers/check_diagonal_spin_networks.py
```

Fresh execution passed all assertions for ten case/chirality combinations. Six exact network packets (three carriers, two chiralities) and the source-bound verification receipt are in `research/strominger/results/diagonal-spin-networks/`. Existing shared results were only read.
