# Does shared-face gluing force opposite circulation?

## Result

**No: passive endpoint matching does not reverse the physical mode.** It reverses the face-coordinate orientation. These are different operations.

The neutral opposite-branch belt remains a valid 1836-arrow intrinsic operator construction. Its branch selection is not derived by ordinary face identification.

## Exact face-chart test

For every shared radial face of both actual carriers, the checker constructs the induced oriented face orders from positively oriented tetrahedra. The two face orders differ by an odd permutation.

If a face has vertex matrix X and cyclic coefficient vector c, its physical mode is Xc. Reordering vertices by P changes the matrix to XP. The same physical field then has coefficients P⁻¹c:

```text
(XP)(P⁻¹c) = Xc.
```

The local cyclic eigencharacter changes from ω to ω², but the physical vector and its bivector remain unchanged. Interpreting that passive character change as reversed physical circulation counts the orientation reversal twice.

Keeping the same numerical coefficient vector c after reversing the chart is instead an active change of the physical mode. That can reverse circulation, but endpoint matching does not require it.

## Internal orientation balance

Suppose a single branch sign chi_i is extended over every face of constituent i. On a shared face, ordinary positive tetrahedral orientations induce opposite signs epsilon_i=-epsilon_j. The signed-chain boundary coefficient is

```text
chi_i epsilon_i + chi_j epsilon_j
= epsilon_i (chi_i-chi_j).
```

Thus internal cancellation requires equal piece signs, not opposite signs.

An exhaustive sign check gives:

| Carrier | Seam-free piece-sign assignments |
|---|---|
| Four-piece proton | all positive or all negative |
| Six-piece belt | all positive or all negative |

The alternating belt assignment leaves all six internal radial faces with coefficients +2 or -2. Those are missing interface records if one wants to extend the outer circulation sign uniformly through each tetrahedron.

The previous flux test specified outer modes, not these internal face modes. Consequently this is an extension obstruction, not a contradiction in the already verified neutral return.

## What operation is missing?

An active branch-converting interface, or additional interface state, must implement the opposite circulation. It cannot be replaced silently by a passive relabelling.

Actual complex conjugation also changes the scalar contract:

```text
conj(z v) = conj(z) conj(v),
```

whereas the previous intrinsic projector network is complex-linear and sends z v to z times its selected target vector. The checker verifies the mismatch at z=ω. A complex-linear branch converter may be built, but it is a distinct operation requiring an explicit source rule.

## Verification

```text
python research/voevodsky/checkers/check_face_gluing_circulation.py
```

Eight checks pass, including all twelve shared-face chart transitions across the two carriers, exact bivector comparisons, exhaustive uniform/alternating sign patterns and the six nonzero belt seams.

Artifact: `results/face_gluing_circulation.json`. Earlier sources and the neutral-mode construction are unchanged.
