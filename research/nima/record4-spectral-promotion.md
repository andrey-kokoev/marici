# Cycle five: a spectral identity with a window into record four

## Implemented construction

The fifth stage now promotes a mode of the retained nested return into a fresh identity record:

    record5 = (fresh label, mode projector, eigenvalue, history window).

Its operator satisfies E²=E and acts as identity on its selected eigenline. The history window recovers the entry arrow, the nested return arrow, all three primitive occurrences and both folding presentations.

All three triangle modes are constructed. Choosing the common, positive-phase or negative-phase mode is an explicit argument. No fourth primitive identity is supplied to generate them.

## Record four retains the actual input

Start with directed two-endpoint packets f=AB, g=BC, h=CA. The stored stages are:

    1. (AB,BC,CA)
    2. ((AB,BC),CA)       fold through B
    3. (AB,(BC,CA))       fold through C
    4. entry AB, retained return (BC,CA), both fold witnesses
    5. fresh spectral identity record with a window to stage 4

The nested descriptor represents the intended A -> (B -> A) presentation by retaining an entry A -> B and its composable return B -> C -> A. A function-space semantics or automatic currying theorem is not assumed. The two folds flatten to the exact same ordered primitive occurrences; their different presentations remain stored.

## Extract a typed operator on the retained packet slots

The declared operator space is the three-dimensional coefficient space of the original packet occurrences. Let

    T4 = C,
    C(x_AB,x_BC,x_CA)=(x_BC,x_CA,x_AB).

Endpoint composability determines this cyclic successor. This is an operator extracted from the internal packet structure of record four, not a claim that the abstract nested-arrow type is already a linear endomorphism of the original vertex A.

The counting inner product on the packet slots is supplied. The construction reuses the exact triangle spectral calculation in `triangle-half-phase-primitive.md`. The same spectral package can be used by a history-window interface; the present checker binds its window directly to the nested root and ordered occurrence IDs.

## Derive the identity projector

With omega=exp(2*pi*i/3), the spectrum is

    lambda in {1,omega,conjugate(omega)}.

For each of these three distinct eigenvalues,

    E_lambda = (I + lambda^-1 C + lambda^-2 C²)/3.

These projectors obey

    E_lambda²=E_lambda,
    E_lambda^dagger=E_lambda,
    trace(E_lambda)=1,
    C E_lambda=lambda E_lambda.

They are pairwise orthogonal and sum to I. On an eigenvector v for lambda, E_lambda v=v. Its nonzero complex rescaling gives exactly the same projector vv^dagger/(v^dagger v), so a magnitude or phase convention for the eigenvector does not change the identity object.

For the oriented positive mode,

    v=(1,omega,omega²),
    E_positive=(1/3)*[[1,omega²,omega],
                     [omega,1,omega²],
                     [omega²,omega,1]].

This equals the previous half-weight expression

    E_positive=(P-iJ)/2.

The 1/3 averages the three cyclic positions; the 1/2 splits the complex plane into its two conjugate eigenmodes. These are compatible descriptions of the same operator.

## Mode choice and orientation

The common mode gives the real projector Q onto (1,1,1). The two other modes give the conjugate identities E_positive and E_negative. Reversing the cyclic operator from C to C^-1 exchanges the positive and negative eigenspaces. The package records the eigenvalue and the ordered packet basis, so the phase information remains accessible even though the projector itself is idempotent.

No unique preferred mode is inferred from having a spectrum. The caller specifies which mode is promoted, or retains the complete three-mode family as in this checker.

## Identity and provenance have separate jobs

Each mode record has

    label: one fresh address;
    projector: identity on the selected eigenline;
    eigenvalue: the retained phase response;
    window: original record-four ID and ordered primitive occurrence IDs;
    depth: the parent depth plus one.

Two independently executed triangles can yield identical projectors but different occurrence IDs and root labels. Their identity records remain distinct and resolve to different histories. A repeated promotion of the same mode also receives a fresh address while pointing back to the same immutable source record.

Thus the 1:1 interface is between labels and complete promoted records. There is no asserted bijection between projectors and histories. The projector provides spectral identity; the window provides exact reconstruction.

This constructs operators and records. It does not execute a destructive projection of a physical state, or claim that discarded amplitudes of an arbitrary input state can be recovered from a projector alone.

## Why record four must retain its internal action

Collapsing the three-step route to C³=I loses the simple spectrum. On this collapsed operator, the same polynomial construction gives

    E_1=I with rank three,
    E_omega=E_conjugate(omega)=0.

None is a rank-one selected identity. The implementation refuses this collapsed input at the spectral-promotion gate. All eigendirections of I are invariant, and selecting one would require additional data.

The stored cyclic structure therefore does real work: it distinguishes the eigenmodes used to construct the new identities.

## Depth and verification

The retained nested root has logical ancestry depth two; promotion creates a depth-three record. A parent already at depth three is refused. The five named presentation stages are not five recursive ancestry levels. No earlier history is reset or discarded when a promoted object is treated as one operand.

    python research/nima/checkers/check_record4_spectral_promotion.py

Fresh exact checks pass for typed packet closure, both fold reconstructions, all three spectral identities, eigenvector phase/scale invariance, orientation reversal, pairwise orthogonality and completeness, fresh labels, exact history-window recovery, distinct histories with equal projectors, collapsed-identity degeneracy, wrong modes, reordered/duplicated packets, forged windows/eigenvalues and the depth-three gate.

Artifact: `results/record4-spectral-promotion.json`.

## Available next operation

[Nine-cycle re-entry test](spectral-promotion-nine-cycles.md) now repeats deconstruction, fold recovery and promotion nine times in each mode. The projectors stay fixed while fresh execution receipts retain each pass; the same depth-three packet tree remains recoverable.

A promoted mode can now serve as a one-dimensional identity port at the next level, with its eigenphase and original return construction still recoverable. Defining composition between different promoted ports requires the next comparison map. This file supplies the fifth-stage spectral promotion itself; it does not assume those next-level maps or a physical particle realization.
