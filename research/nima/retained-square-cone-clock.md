# The retained-square cycle embeds faithfully in the tetrahedral whole

## Question

Operator correction: is the retained whole already the proposed intrinsic-time carrier, with a full square traversal constituting a cycle? Treat this as a request to test the identification, not as evidence that physical time has been derived.

Fresh source inputs are `agda/ObserverCoherenceCube.agda`, `agda/RetainedSquareReversal.agda` and `agda/ThreeWitnessRetainedCone.agda`. Active SCC obligations: attachment transport, route/coherencer compatibility, then clock-readout descent.

Conjecture: the ACTUAL retained-square return record can be encoded in the new tetrahedral cone without losing its information, and a count of completed returns is invariant under that encoding and additive under record concatenation. Rivals are endpoint-only counting, loss of the two schedule records during encoding, and treating tetrahedral packaging itself as an additional tick.

## Claim boundary

### What the previous square really contains

For a supplied equivalence e:O~R, the source has a two-coordinate type family `axis(i) × axis(j)` and a section determined by a source pair s:O×O. It retains the distinct left-first and right-first schedules and their equal-effect comparison. Reflecting both interval coordinates provides the return section and exact endpoint recovery.

This is the concrete meaning of “square” in this test. The two schedules are alternative descriptions retained together, not a theorem that two sequential traversals happened. Neither an intensity square nor a spinorial double revolution is substituted for it.

### Bind that completed record to the cone

At a fixed source s, a Tick stores the existing full `RetainedReturn` and a proof attaching its source to s. It therefore retains the forward comparison, target law, return section and return endpoint laws.

Use three focus maps on Tick:

1. the first forward schedule, its target and its realization certificate;
2. the second forward schedule, its target and its realization certificate;
3. the return section over the square.

These are the actual square-cycle interfaces, not a relabelling of charge, mass and recoil. The same generic retained-cone constructor now applies to them. Its apex is the entire Tick. A `ConeRecord` retains the filled tetrahedron and a certificate identifying its apex payload type with Tick. This certificate makes a standalone decoder possible; decoding does not secretly take the original Tick as a second input.

Fresh safe Cubical checking proves

    decode(encode(t)) = t.

It also proves encoding is injective. Thus distinct schedule records cannot collapse merely because they have equal numerical endpoints. This is a split injection into typed tetrahedral records, not an equivalence with every possible tetrahedron or a claim that the two constructors are literally the same operation.

### A precise intrinsic clock convention

Define one well-typed completed square-and-return record to count as one tick. A history is a list of such records attached to the same source. The clock readout is its length N.

The formal bridge proves

    encodeHistory(h ++ k) = encodeHistory(h) ++ encodeHistory(k),
    decodeHistory(encodeHistory(h)) = h,
    N(h ++ k) = N(h) + N(k),
    N(encodeHistory(h)) = N(h).

Composition here is concatenation of completed closed-return records. It is not a theorem about geometric gluing of tetrahedral interiors. The unit convention N([t])=1 is declared. No continuous rate, autonomous production rule or independently preferred orientation is inferred.

Encoding a record does NOT add a completion: it preserves its count. The accumulated retained history carries N; an isolated copy of the latest tetrahedron is insufficient to distinguish repeated identical cycles. If “retained whole” means the whole accumulated record, it can support this intrinsic completion clock. The whole contains more information than that clock value.

## Tests and disposition

`agda/RetainedSquareConeClock.agda` freshly passes safe Cubical checking. Besides the bridge and composition laws, it proves two discriminating controls:

- No function of the returned endpoint alone can read N for every history. The empty history and a single completed square return to the same s but have counts 0 and 1.
- Swapping which forward schedule is retained first gives provably distinct Tick records with the same count. The scalar clock is therefore not a faithful encoding of the whole history.

The existing Bool negation equivalence supplies an inhabited, nontrivial square fixture. The accompanying Python checker verifies the formal receipt and current hashes of seven direct source files, all four Boolean source pairs, and 225 finite word-concatenation controls. Those word controls are not extended body executions and do not prove the generic theorem; the Agda proofs do.

**Disposition:** the square-to-tetrahedral bridge now exists at the retained-record level, and an additive completion-count clock survives it. This supports the proposed intrinsic-time interpretation as a structured clock convention rather than requiring an unrelated fourth vertex. It does not identify the retained whole with a scalar duration.

Remaining boundaries are specific: no law has been supplied that autonomously produces the successive returns; no comparison identifies this count with the separate continuous rotor clock; and the charge–mass–recoil model still lacks a source-derived physical-time interface. These are not repaired by changing units or by calling the tetrahedral apex “time.”

Verification:

- `pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module RetainedSquareConeClock -Fresh`
- `python research/nima/checkers/check_retained_square_cone_clock.py`
- Receipts: `results/agda-RetainedSquareConeClock.json` and `results/retained-square-cone-clock.json`.
- Owner-local SCC model: `scc-models/retained-square-cone-clock.json`.

The inherited `TypedGeneratorLayers` import warning remains. No existing constructor was modified. The operator stimulus and follow-up to marici.Voevodsky were policy-admitted under proposal `ep_0b23ca34-1faa-42c2-ace5-13fe5fdb3d64`; admission is not truth certification. This work and the preceding admitted cone report remain uncommitted. No physical evidence promotion or publication is claimed.
