# One retained-fiber promotion cycle for the minimal growing seed

## Connected construction

`RetainedRelationshipPromotion.agda` adds an explicit typed promotion adapter.
It uses `TableFibrationCycle` for reciprocal fibers and the existing
`WholePackageResolution` Pi rule to compile each two-packet vertex record. It
then constructs shared-endpoint witnesses and a new packet table suitable for
the next descent. The generative adjacency rule is new; it is not inferred from
reversible normalization or silently added as an equivalence.

The concrete source consists of the eight oriented packets of AB,AC,BC,AD.
Each packet identity is (relationship label, direction). Fibering by the
relationship label produces:

| Retained record | Original packets |
|---|---|
|AB|A->B, B->A|
|AC|A->C, C->A|
|BC|B->C, C->B|
|AD|A->D, D->A|

The generic kernel provides recovery of all packets from the total fibers. An
additional fiber isomorphism proves each individual reciprocal fiber has
exactly the two direction values.

## Generated connections and witnesses

The adapter enumerates ordered pairs of relationship keys and tests incidence
at each original vertex. It emits precisely these five connections:

| New relationship | Shared endpoint |
|---|---|
|AB--AC|A|
|AB--BC|B|
|AB--AD|A|
|AC--BC|C|
|AC--AD|A|

Each connection retains its two relationship keys, the shared endpoint, the
ordering witness, and incidence witnesses for both sides. The equality test is
supplied with a soundness proof; `real-left` and `real-right` recover actual
endpoint equalities from the Boolean incidence certificates. BC and AD have no
shared endpoint and generate no connection.

Each new connection supplies two next-cycle directed packets. The resulting
table has four vertex records, five undirected connections and ten directed
packets. It is the diamond, two triangles sharing the AB--AC edge.

## Native compilation and retention boundaries

For each reciprocal fiber, a native Pi node collects its two original packet
packages. Its only seeds are those input packets; arbitrary canonical target
seeds are not used for this grouping step.

The shared-endpoint generator is an explicit typed constructor in the new
adapter, not a derivation using only the old native Rule signature. Its output
`RetainedPromotion` keeps the original source table, original packet list,
reciprocal fibers, native vertex compilations, generated witnesses, and promoted
table. Equality fields tie these retained values to the actual construction.
The whole record is packaged as a next-level Complete input.

The generic adapter assumes meaningful vertex enumeration, relationship
ordering, and a sound equality test. The concrete paw supplies complete finite
enumerations and proves the equality test sound. We establish the output counts
and agreement for this concrete seed; no unrestricted theorem equating all
possible supplied order/enumeration choices with simple line graphs is claimed.

## Checked bridge to the existing cycle

`PawPromotionRegression.agda` reduces the actual generated lists to prove:

- eight source packets;
- four reciprocal fiber keys;
- exactly five generated connections;
- the exact endpoint-witness signature list above;
- ten next-cycle directed packets.

Its generated table is passed directly to the existing eight-step rung12-to-rung4
descent. Every next packet is recovered exactly. The source table also survives
inside the Complete promotion output.

The separate finite executor groups real packet objects, attaches original
packet-ID witnesses to each new incidence, and compares its output against an
independent pairwise-intersection line-graph calculation. Feeding the ten new
packets into its next promotion yields five records and eight relationships,
matching the previously computed second growth stage. Cycle-qualified new IDs
keep different generations distinct.

Controls verify that a repeated reference to one input ID leaves the output
unchanged; conflicting values for one ID and missing reverse packets are
rejected.

## Reproduction

```
python research/nima/checkers/check_retained_paw_promotion.py
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module PawPromotionRegression -Fresh
```

Both passed, including fresh safe Cubical Agda dependency checking.

- Adapter: `agda/RetainedRelationshipPromotion.agda`
- Formal regression: `agda/PawPromotionRegression.agda`
- Finite result: `results/retained-paw-promotion.json`
- Formal receipt: `results/agda-PawPromotionRegression.json`

This supplies one executable, provenance-preserving bridge between the fiber
construction and the combinatorial growth calculation. Selecting the promotion
rule as physical dynamics, and defining particle or spacetime readouts, remain
separate questions.
