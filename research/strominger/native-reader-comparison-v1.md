# Comparing the NE and NN reader alternatives

## Question

Can the two conflicting target labels from the first native batch attempt be
understood as presentations of the same retained object, rather than simultaneous
particle assignments? This test uses the actual target charts and native maps;
it neither changes the occupation validator nor supplies a new particle rule.

## Positive result: exact full-coefficient comparison

The source maps from the common N packet are

    NE = [0,4,2,3,1],
    NN = [0,3,4,1,2].

Here a row permutation p sends v to v[p[i]]. Hence the comparison from the E
coefficient presentation to the N presentation is

    Q = NN composed with inverse(NE) = [0,3,1,4,2].

It intertwines their actual five-slot maps from the root, preserves the full norm
and has an exact inverse. Thus a full-information algebraic comparison exists.
It is not an invented fit to a desired particle count.

## Why this is not yet a native reader equivalence

The E frame at origin0 is

    active: M1, C1, C2; context: M2.

The N frame at origin1 on the SAME primitive is

    active: M1, C2, M2; context: C3.

M1, C2 and M2 coincide as complete role/index/vertex occurrences. The remaining
geometric vertex is C1 in E and C3 in N. Equal coordinates therefore do not identify
its occurrence. The outside C0 reference also changes vertex and absolute index.
Q does not by itself witness these provenance changes.

The supplied `phaseAdvanceWitness` accepts matching P/P or N/N carriers, not E/N.
The E packet has no outgoing operation in this grammar. Inverse NE in the formula
for Q is valid linear recovery, not an admitted native reverse execution step.
This does not prove that no richer comparison can be supplied.

## A concrete observable obstruction

The declared active slot readers are

    E: [3,2,4],   N: [1,2,3].

Take the E-presentation vector v=(0,1,0,0,0). Its active E readout is zero, but
Qv=(0,0,1,0,0) has active N readout (0,1,0). Therefore no function of the active E
readout alone can produce the active N readout on the full five-slot domain: v
and zero have identical input readings and different required outputs. Retaining
the complement resolves this loss exactly. A zero visible endpoint is not a zero
retained state.

More importantly, the current assembly's particle-count reader gives

    NE alternative: 1P / 1N / 1E,
    NN alternative: 1P / 2N / 0E.

Those counts are not invariant under the proposed comparison. Thus Q cannot be
promoted to a SAME-physical-assembly equivalence while keeping this count reader
unchanged. Keeping both alternatives as simultaneous occupants still fails the
original species constraint.

## Precise next obligation

The constructive opening is a lossless full-coefficient chart comparison. The
remaining issue is the meaning of the reader versus the retained particle
inventory, not another geometric filling rule.

Supply a source-backed whole-assembly carrier/readout whose inventory is distinct
from its local P/N/E reader labels, then test its occurrence/context intertwiners
and composition invariance under actual operations. The count reader must be
independently grounded; defining a constant inventory merely to pass the square
would be another answer-prescribing substitution. Whole octahedral/composite
carrier binding remains separate.

This rejects identification under the CURRENT readouts, not all possible retained
whole-assembly interpretations. No Pb-208 construction is established.

## Reproduce

```sh
node research/strominger/checkers/check_native_reader_comparison.mjs
```

Twelve checks cover actual target maps, inverse recovery on every basis vector,
full norm, occurrence differences, native arrow admissibility, the invisible-input
counterexample, complement recovery and the non-invariant composition reader.
Full source/target payloads and controls are in
`results/native-reader-comparison/comparison.json`; the live-source receipt is
`results/native-reader-comparison/verification.json`.
