# Standalone three-cycle versus proton face: inherited-rule test

## Result

**The same rules distinguish global assemblies, but do not select a neutrino-specific local mode.** Fifteen exact checks pass. No spin, charge or new attachment decoration is introduced.

## Frozen rules

Reuse the existing geometric assembler, its facet-centroid selector, and its attachment-pole operation:

- select a supporting facet F iff sum_g ||g(c_F)-c_F||_G^2 > 0;
- retain the unique supporting facet opposite a supplied attachment pole;
- preserve the registered arrow cycle and derived character action.

Candidate #1 uses its current unmarked single-three-cycle source. The optional pole comparison applies an existing operation, but remains an explicit extra mark. It is not silently inferred from its geometry.

## Selection comparison

| Datum | Standalone candidate | Proton source |
|---|---|---|
| Intrinsic dimension | 2 | 3 |
| Supporting facets retained | 3 edges | 4 triangular faces |
| Centroid scores | 2, 2, 2 | 8/9, 8/9, 16/9, 16/9 |
| No-mark attachment | none | proton already supplies a pole |
| Existing pole rule | one edge | one triangle |

The score magnitudes depend on generator presentation and are not particle observables. An exact affine frame change preserves the candidate's scores and admission.

The rule retains all candidate edges; it neither singles out an edge nor picks a nontrivial character. All three edges lie in one orbit, so an unmarked cycle-equivariant choice of exactly one edge is impossible within this edge set. A marked pole can choose one, but breaks the unmarked symmetry through retained source data.

## Local face equivalence

The first proton generator cycles the face with affine vertices

    (0,0,0), (1,0,0), (0,1,0).

Its three squared edge lengths are eight, exactly as in candidate #1. On ordered corner records both have

    C(a,b,c)=(b,c,a),
    C^3=I.

For omega=(-1+sqrt(-3))/2, both yield the same derived rank-one character projector

    P_omega = v v^dagger / 3,
    v=(1,omega,omega^2).

The checker verifies idempotence and C P_omega=omega P_omega exactly. Reversing the arrows conjugates the character in both cases; it supplies no neutrino-specific discriminator.

This compares the source geometric face action. It does not identify the full retained native proton coefficient protocol with a three-coordinate toy space.

## Why the centroid comparison must respect the ambient action

The whole candidate triangle's centroid is fixed by its cycle. The corresponding proton face centroid is also fixed by that face's cycle. Under the **full proton generator set**, however, that face centroid moves, with score 8/9.

This difference is genuine global assembly information. It is not a difference between the local cyclic characters. Treating the whole candidate disk as though it were one of its supporting edges, or applying the local stabilizer score to proton faces while applying the full group elsewhere, would change the frozen selection rule.

## Attachment obstruction

The unmarked candidate selects no attachment port. If the existing pole operation is applied, its port has dimension one (an edge). The proton's existing port has dimension two (a triangular face).

The candidate's entire disk is metrically congruent to a proton face, but the disk is not its own boundary port. Gluing it as that face would introduce a new attachment contract, not reuse the unchanged pole rule. No such operation is admitted by this test.

## Scientific disposition

Retain #1 as a standalone geometric hypothesis, not as an identified neutrino. Existing rules establish:

1. a distinct global carrier (triangle versus tetrahedral assembly);
2. the same local cyclic modes as an ordinary proton face;
3. no source-selected single attachment edge without a mark;
4. a port-dimension mismatch under the inherited pole rule.

First missing datum: an arrow-derived global selection or interaction/attachment witness distinguishing the standalone cycle as a separate particle sector. A charge/spin label or a new filling rule inserted to obtain the desired answer would not satisfy this obligation.

## Reproduction

```sh
python research/strominger/checkers/check_neutrino_triangle_selection_attachment.py
```

Fresh execution: 15/15 exact checks pass.
Result: `research/strominger/results/neutrino_triangle_selection_attachment.json`.
The result pins source and implementation hashes and preserves the exact local equivalence and attachment residual. No gallery verification or physical neutrino claim is made.
