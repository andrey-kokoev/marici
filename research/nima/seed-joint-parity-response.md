# A finite joint observer of the native geometric response

## Constructive advance

The finer geometric state now has an explicit finite observation interface. Read together the two Boolean families already used to distinguish the seed's independent AB and BA occurrences:

    read(p) = (transport AB-probe along p from false,
               transport BA-probe along p from false).

The new theorem binds this reader to the ACTUAL compiled native execution, not to a separately supplied matrix model. The observation task and initial probe values are declared mathematical choices; they are not claimed to be physically selected.

## Exact primitive and route squares

Transport composition determines the finite update:

- AB flips the first bit;
- BA flips the second bit;
- BC,CA,AD,DB preserve both bits.

For every current geometric state and every actual primitive occurrence,

    read(advance(e,p)) = update(e,read(p)).

All six finite updates are involutions. Induction gives the same square for every supplied typed seed word. The new `native-square` theorem then connects the reader to the exact output of `SeedGeometricResponseState.RunFrom`, including its source-only retained transport execution and raw route provenance.

This is a finite reversible observer of that state, not a claim that the full geometric state or history has only four values. In particular, AB and BA remain distinct primitive occurrences even though their observed updates are involutions.

## The complete seam response is now visible

Starting from the declared probe value(false,false):

| Corner | Actual directed word | Joint reading |
|---|---|---|
| C00 | AB BA |(true,true)|
| C01 | AB BC CA |(true,false)|
| C10 | AD DB BA |(false,true)|
| C11 | AD DB BC CA |(false,false)|

The formal `corner-recovered` theorem recovers BOTH direct/indirect choices from each compiled output. This extends beyond the arrival reader, which distinguished only the returning choice on the four-corner domain.

The original two-triangle context still consists only of C01 and C10. These four words are all valid endpoint paths, but evaluating their full product domain does not authorize replacing the original joint relation with it. The observer theorem and source-family admission remain different obligations.

## Exact mixed record, before physical scalar selection

The companion checker derives four-by-four integer permutation matrices directly from the formal Boolean update declarations. They are the ordinary linearization of the four-value observer, not tuned primitive response matrices.

Order the output records as

    (false,false), (false,true), (true,false), (true,true).

For Cij=Yj Xi, the mixed operator

    D=C11-C10-C01+C00=(Y1-Y0)(X1-X0)

has rank one and trace four. Applied to the declared initial record, it gives

    (1,-1,-1,1).

Thus the joint output record has a nonzero mixed contrast. Each single-bit reader annihilates that contrast. The extra Boolean question "are both bits true?", included explicitly in the formal module, has integer-indicator contrast1.

This scalar is a declared diagnostic question. It is NOT a derived physical amplitude, a calibrated energy, or a normalization chosen to match the earlier matrix fixture's1/15. The two bit updates commute, so the nonzero mixed response is not evidence of noncommutativity.

The two probes observe the same retained geometric state. No statistical independence or preparation of two independent physical copies is assumed by reading their values together.

## What has and has not been bound

The source-backed chain now includes

    actual seed word
      -> retained source-only native transport
      -> geometric current state
      -> paired Boolean probe reading
      -> optional declared Boolean question.

Every arrow through the paired reading has a checked native computation law. Its finite linearization has exact executable checks.

This is a different, more discriminating TASK than arrival alone. The parity pair is not claimed to recover the arrival occurrence on arbitrary histories, or to be a universal minimal state. Arrival and parity can remain separate observations of retained execution. One and three ABC traversals have the same finite parity action; full history is still retained independently.

Remaining gates:

- source/physical selection of this probe task rather than another admitted one;
- which context family the intended horizontal constructor actually consumes;
- construction of the next endpoint/table fields and identification with T9;
- a reader comparison with the unchanged matrix J4, if that is the intended target;
- physical instrument realization and calibration.

There is no justification for identifying four Boolean values with "rung4" or for rescaling the diagnostic contrast to fit another fixture. The present result supplies a real nonzero JOINT response in a declared source-derived observer, not completion by those identifications.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedGeometricResponseState -Fresh
    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedJointParityResponse -Fresh
    uv run research/nima/checkers/check_seed_joint_parity_response.py

Both fresh safe Cubical/guardedness checks pass with ignored interfaces and stable inputs.36 exact finite/matrix checks pass. They cover source hashes, extracted primitive actions, endpoint typing, sequential factorization, all four compiled corner readings, mixed factorization, rank, commuting controls, single-probe blindness, and a remaining history collision.

The geometric source module only received an import-list correction to remove a non-export warning; its operation was unchanged and freshly rechecked. No postulates or unresolved holes were added.

Artifacts:

- `agda/SeedJointParityResponse.agda`
- `results/agda-SeedJointParityResponse.json`
- `checkers/check_seed_joint_parity_response.py`
- `results/seed-joint-parity-response.json`
