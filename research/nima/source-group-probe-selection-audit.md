# Does the existing whole-source group select the interaction geometry?

## Source-first test

Use the ACTUAL two triangle permutations of the existing Machian body
construction, recovered from the six primitive seed rows:

    ABC: (1,2,0,3), ADB: (3,0,2,1).

They generate the twelve-element A4 group. Restrict the two ALREADY EXISTING
S4 probe dictionaries to that source-generated group. Keep uniform counting,
unit probe normalization, and the established record-exchange rule explicit.
No new feature values, masses, impulse law or fitted normalization are added.

The inspected `WholePackageResolution.agda` comparison rule takes an
equivalence and its marked-value path as arguments; the higher rule takes
the higher equality. These signatures retain supplied evidence. They contain
no discovered selector of the physical probe, measure or preparation. This
is a bounded signature audit, not a claim that no such construction exists
anywhere in the project.

## Full-source outcome

| Existing query restricted to A4 | Six-feature rank | AB then BA transfer |
|---|---:|---:|
|Fix both endpoints|1|1|
|Send source endpoint to target endpoint|6|1/3|

Every nonidentity A4 permutation fixes at most one vertex, so all endpoint-
fixing edge probes reduce to the identity indicator. This loses more visible
coefficient information than the earlier S4 rank-five restriction. Keeping
separate records can still retain that information; noninjectivity of the
carrier probe alone is not a reason to declare this query inadmissible.

The directed-transition normalized kernel agrees with the earlier S4 kernel
on all 36 seed-pair entries. The generated group is already 2-transitive.
Thus changing the carrier group from S4 to the source's A4 need not change
this observed kernel at all.

Both queries remain well-defined. The source-generated group does not select
between them. The two-pulse values use the SAME supplied AB-record excitation
and named BA reader as the prior experiment; neither value selects a physical
query merely by being nonzero.

## Does the surrounding seed change the experiment?

Test one explicit extension: after an edge deletion, regenerate the group
using whichever of the TWO ORIGINAL triangle cycles remain intact. This
rebuilding policy is new counterfactual data; it is not silently inherited
from the old fixed-dictionary deletion test.

| Deleted edges | Group size | Endpoint-fixing transfer | Directed-transition transfer |
|---|---:|---:|---:|
|None|12|1|1/3|
|AD|3|1|0|
|BC|3|1|0|
|AD and BC|1|1|Unavailable|

After one deletion, some other surviving primitive arrows already have zero
directed-transition features: DB after deleting AD, CA after deleting BC.
After both deletions, the group is the identity, so AB and BA themselves
have zero directed-transition features. They cannot be normalized into the
unit-feature ports required by this exchange protocol.

Consequently the apparent joint environment effect CANNOT be calculated by
putting zero in the final corner. The experiment is unavailable there, not
a measured zero. Under this policy the directed probe is not a total exchange
adapter for all surviving primitive arrows across these source changes.

This gives genuine conditional dependence on the whole source, but not a
selected physical interaction law, nor a completed four-corner response test.

## Disposition

The source's existing global-group operation supplies a concrete carrier
ensemble after its construction assumptions are accepted. It still does not
choose what question a probe asks, supply an excited preparation, or license
an occurrence to execute the exchange.

The remaining input is a SOURCE-ADMITTED measurement/interaction operation
with those semantics. If it asks for literal fixed-label restriction, the
endpoint-fixing branch is determined by that task; if it asks for transition
matrix coefficients, the other branch is. The seed's incidence and retained
coherence constructors alone have not identified which physical task occurs.

Do not continue with another recovery theorem or fit a graph-dependent
normalization to resolve this. A further derivation needs an actual selecting
constructor/operational requirement, or an explicitly external hypothesis.
No source-selected physical closure is claimed.

## Verification

    uv run --with sympy python research/nima/checkers/check_source_group_probe_selection.py

51 exact checks pass. The existing seed-probe checker and its dependency
checks rerun. The Machian module's existing permutation-composition function
is reused; its numerical dynamics/main routine is NOT rerun by this checker.
Receipt: `results/source-group-probe-selection.json`, with source hashes,
all query ranks, zero-port lists and unavailable-corner status.
