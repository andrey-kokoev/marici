# Quartic environmental response of the tetrahedral mode and its dual witness

## Question and frozen test

The operator conjectures that the fractional excess comes from the difference between a proton-like structure's response to its surroundings alone and the response with an electron-like witness. The proposed interaction is quartic. Test this against the existing twelve-triangle coefficients, without fitting weights to 0.15.

This test uses five explicitly chosen equal-strength probe partitions: whole space, four parent faces, twelve triangles, three ambient axes, and thirty-six ports. These are candidate surroundings, not a source-derived universe. No new WG transition or independent electron operator is constructed.

## Source and coupling

Reconstruct the twelve rotations from the original cycles, then the collective vector u from the transported triangle eigenvectors. Its exact squared norm is 80. Set p=u/sqrt(80) and take the unit Hermitian dual as the witness; represent that dual by e=conjugate(p) in the conjugate space. This fixes both factors to unit norm and retains their normalized evaluation. The earlier unnormalized pair (u,u-dagger/80) has reciprocal norms; the quartic is unchanged by reciprocal rescaling.

For a probe partition with real diagonal projectors E_a, declare the unit-strength coupling

    K_U = sum_a E_a tensor conjugate(E_a)
    Q_U(p,e) = sum_a (p-dagger E_a p)(e-dagger conjugate(E_a) e).

Writing w_a for the squared norm of the proton mode in block a gives Q_U=sum_a w_a^2. Declare the test functional

    E_U(a p,b e) = |a|^2 + |b|^2 + |a b|^2 Q_U.

Inclusion-exclusion removes both isolated contributions and leaves Q_U. This is a model definition, not an independently derived energy law or a conversion between arrow counts and energy.

## Exact results

| Probe partition | Quartic excess |
|---|---:|
| Whole space | 1 |
| Four parent faces | 1/4 |
| Twelve triangles | 1/12 |
| Three ambient axes | 1/3 |
| Thirty-six ports | 11/300 |

The 36 port intensities consist of twelve entries 1/180 and twenty-four entries 7/180. Consequently their quartic sum is 12(1/180)^2+24(7/180)^2=11/300. None of the five fixed models gives 3/20.

Controls check zero-witness cancellation, quartic amplitude scaling, and detection of a reversed interaction sign. The result distinguishes dependence on the probe structure from the rival expectation that the normalized collective pairing alone fixes the excess. It does not select a probe partition or its interaction strength. The first missing input for a stronger calculation is a source-selected surrounding coupling operator with its normalization.

## Verification

Dependency-free exact rational and Q(sqrt(-3)) calculation:

```text
python research/nima/checkers/check_proton_witness_quartic_environment.py
```

Passed through structured-command execution `structured_command_execution:e_32876_1791215402594169500_5`. Results: `research/nima/results/proton-witness-quartic-environment.json`. Decimal values are display conversions only. No ledger publication or commit is claimed.
