# Whole-seed spectrum on the actual occurrence continuation carrier

## Existing whole-seed branch reused

`check_natural_tower_return.py` already constructs the four-vertex incoming incidence matrix M from the actual six endpoint packets, with exact eigenvalues and spectral projectors. The new bridge calls that checker directly and lifts its verified descriptors rather than introducing a different vertex operator.

Use the same primitive order

    (AB,BC,CA,BA,AD,DB).

Column convention is explicit: K[b,a]=1 when occurrence a can be followed by occurrence b. This INCOMING continuation matrix transposes the earlier local row-successor convention. Therefore the old local cyclic eigenvalue must be conjugated when compared to its incoming block; a sign/convention change is not new phase physics.

## Canonical incidence factorization

Let B be the 6x4 source-lift matrix, B[a,v]=1 when source(a)=v. Let H be the 4x6 target-aggregation matrix, H[v,a]=1 when target(a)=v. Then

    K = B H,       M = H B,
    H K = M H,     K B = B M.

The directly endpoint-extracted K has ten unit entries, exactly corresponding to the ten retained two-step words from the previous path bridge. Both factorizations and both intertwiners are checked exactly.

The matrices represent unit incidence, not supplied amplitudes of primitive traversal or a physical transition-probability law. Applying K to a coefficient state aggregates alternatives; it is not the lossless act of retaining every output path separately.

## Full occurrence spectrum: four plus two

The nonzero occurrence spectrum is exactly the prior vertex spectrum:

    (1+sqrt(5))/2, (1-sqrt(5))/2,
    (-1+i sqrt(3))/2, (-1-i sqrt(3))/2.

There are also TWO zero eigenvalue directions. All ranks B,H,M,K are four. For each prior vertex eigenprojector E_lambda with lambda!=0, the lifted occurrence projector is

    E_occ,lambda = B lambda^-1 E_lambda H.

Exact quadratic-field calculations verify rank-one idempotence, eigenvalue equations, pairwise annihilation and reconstruction. The summed nonzero projector is

    F = B M^-1 H,
    P_zero = I6-F.

F has rank four, P_zero rank two, and

    sum E_occ,lambda + P_zero = I6,
    sum lambda E_occ,lambda = K.

The zero eigenspace is retained as a complete rank-two sector. No distinguished split into two rank-one spectral identities is inferred from the repeated eigenvalue.

Unlike the triangle projectors, these are generally oblique rather than orthogonal in the counting metric. K is nonnormal. No conservation of the previous Euclidean coefficient budget is asserted, and the growing real eigenvalue rules out finite return of the raw operator. The prior phase-only extraction must not replace its full spectral data.

## Exact recovery of occurrence coefficients

Two independent zero-sector contrasts are

    CA-BA, AB-DB.

Each compares primitive occurrences entering the same vertex, so H kills it. K also kills it. Those differences are not absent source records; aggregation simply cannot see them.

For any occurrence coefficient vector x, retain

    z = M^-1 H x,
    k = P_zero x.

Then x=Bz+k exactly. Four active coordinates plus the two-dimensional kernel therefore retain the complete six-coordinate coefficient input. Applying K gives B M z and erases k unless it is stored separately or otherwise recoverable. This decomposition is a property of this invertible four-vertex incidence fixture, not a physical reference-return inverse law.

Recovery of coefficient vectors still does not recover original identity labels, vertex assignments, ordered path words or execution receipts from eigenvalues alone. The bridge keeps the ordered manifest, registry and all ten endpoint-bearing two-step records alongside the operator.

## Follow-up: source-indexed observation recovers the two contrasts

Reuse the source-family grouping from `check_natural_tower_return.py`. For each source vertex v, let S_v select the coefficients of its retained primitive occurrences. No state is changed merely by grouping. The source-resolved target observation is

    O(x) = (H S_A x, H S_B x, H S_C x, H S_D x).

This is a source-major sixteen-entry table with only six supported endpoint cells. Exact tests give

    rank(H)=4, rank(O)=6, rank(O P_zero)=2.

In this seed no two primitive records have the same ordered source/target pair. Each original coefficient therefore appears in exactly one distinct supported observation cell. The explicit decoder is O^T, with O^T O=I6. Summing over the source index recovers Hx exactly. The decoder identities hold on the full coefficient carrier; rational and complex fixtures are checked.

The two previously invisible contrasts have profiles:

| Contrast | Nonzero source-resolved entries |
|---|---|
|CA-BA|C->A: +1; B->A: -1|
|AB-DB|A->B: +1; D->B: -1|

Thus these directions are not intrinsically inaccessible in the retained source-indexed interface. They are invisible to the COARSE target aggregation H, which forgets where the incoming coefficients originated.

### Observation before aggregation is not inversion after K

The same source-resolved reader applied after the operator satisfies

    rank(O K)=4, O K P_zero=0.

For x and x+k with k in the zero sector, source-resolved observations differ BEFORE applying K but agree afterwards. Reindexing the stored input can expose a retained contrast; reindexing only Kx cannot recover an erased coefficient. Recovery then needs the saved input/kernel or another retained record.

All source selections tested fail to commute with K. Accordingly using a source-indexed observation should not be silently replaced by physically projecting to one source and evolving, or by selecting the same source after evolution. These are different operations. No selective physical preparation or measurement authority follows from the group keys.

### Endpoint cells do not universally replace occurrence provenance

A hostile fixture adds a distinct AB occurrence with the same endpoints. Its seven coefficients still give an endpoint-profile rank of six; the difference between the two AB occurrences is invisible. Their IDs remain distinct and must be retained. The original decoder is therefore scoped to the six-row primitive registry, not arbitrary parallel arrows or longer path histories.

Wrong-length observation tables and payload in an absent primitive cell (A->A) are rejected. No endpoint-profile result licenses reconstructing history IDs or execution receipts from numerical values alone.

### Revised interpretation of four plus two

The rank-four/rank-two spectral split is an exact property of K, and K genuinely annihilates those two directions when applied. It is NOT a universal observability split imposed by the seed: the existing source-indexed reading sees all six coefficients. The split's operational significance depends on whether the interface preserves source resolution, merely summarizes by target, or actually applies the incidence operator as an update.

## What happens to local triangle modes?

Remove the four cross-context entries and K becomes two incoming three-cycles. Their modes are exactly the previously promoted local modes, with the stated convention reversal.

Restoring actual glued incidence adds the four transitions

    AB->BA, BA->AB, CA->AD, DB->BC.

Every local rank-one mode now has a nonzero component outside itself. In the complete local spectral basis, each input mode has a nonzero block to itself and to ALL THREE modes of the other triangle; no other mode in its own triangle is reached directly by that single step. The checker records the complete exact nonzero block pattern.

Thus the local spectral records remain valid coordinate/provenance records, but are not invariant identities for the glued continuation operator. The full source incidence changes their response decomposition without fitted leg coefficients. This is a representation-level result, not a derivation of a physical execution schedule.

## Synthesis and boundary

There is now a precise connection between local spectral input, the ten-word glued composition domain and the already existing whole-seed spectral branch. No 9x9 tensor carrier or new three-slot triangle was forced onto the output.

The next layer must retain both the global spectral descriptors and the source records, including the two kernel directions when describing arbitrary input coefficients. Neither a zero eigenvalue nor an aggregated vertex reading authorizes deleting occurrence histories. Nothing here identifies the dimensions four and two with rungs or species.

## Retained extension versus the coarse operator

`retained-path-extension-and-coarse-summary.md` now locates the erasure explicitly: K=A L, where L injectively copies primitive coefficients onto their ten retained extensions and A sums by final occurrence. Both zero contrasts survive L and cancel only under A. A decoder on im(L) is verified; the lift is not norm-preserving or surjective onto arbitrary ten-path coefficients.

Repeated prefix-preserving extension is checked through length six (68 paths), with commuting final-occurrence summary squares. The lift from the six initial coefficients remains rank six, while its coarse response is rank four after the first extension. Growing the path carrier does not create independently prepared amplitudes, and the fixed K spectrum describes the coarse summary, not a square evolution on the full growing carrier.

## Verification

    python research/nima/checkers/check_whole_seed_occurrence_spectrum.py

Fresh exact checks pass for source/target factorization, all ranks/intertwiners, all ten path records, the inverse and oblique splitting, four lifted nonzero spectral modes, complete zero-sector retention, spectral reconstruction and the local-mode mixing pattern. The observation extension also checks source-indexed ranks 6/2, exact coefficient decoding, forget-source compatibility, rank-four loss after K, source-selection noncommutation, the parallel-occurrence hostile and malformed-profile controls. The existing natural-tower spectrum and path-composition regression are rerun through reuse.

Report: `results/whole-seed-occurrence-spectrum.json`.
