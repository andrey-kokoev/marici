# Su-32 layer-4 comparison and central reconciliation

## Frozen question

Test the actual layer-4 operands without a spinor encoding. At shared E+, the operands retain `(P+,E+)` and `(P-,E+)`; analogously for the other three central comparison cells. What information can a lossless comparison retain, and do the two orders of reconciliation recover the same four-record input?

Prior-source audit: `internal-source-comparison-and-interchange-v1.md` requires a whole-carrier port law, an equivalence and a selected-value witness. `canonical-comparison-synthesis-v1.md` derives such witnesses only in its classified Fragment. Neither theorem supplies an equivalence between arbitrary independently valued P+ and P- records. `native-reader-comparison-v1.md` likewise distinguishes full retained information from an insufficient active reader. No fresh Agda proof or import of their admission theorem is claimed here.

Candidate: the comparison is a retained fiber product over the shared labelled record. Reconciliation is joining compatible three-record comparisons over their two-record overlap. This operation is derived from preserving both input projections and identifying only their shared record. It is a candidate interpretation of the specified comparison sites, not a claim that the physical interaction is this join.

Rivals: identifying the two whole operands; retaining only the common reference; inventing a spinor phase; identifying the two construction orders as literal histories. Tests: all Boolean assignments of four independent records, all cone/readings and sign bindings; mismatching reference/payload controls; recovery of both operands and all four records; distinct retained histories for equal final records.

SCC obligation: route/coherencer compatibility on this finite set-valued candidate, with physical/native comparison admission and cross-cone transport left separate. All cones are tested as restrictions against the already fixed whole-carrier fixture; no local routing is generated.

## Constructed operation at the actual cells

For independent payload types A+, A− and B+, comparison at shared E+ has carrier

```
(A+ × B+) ×_(B+) (A− × B+)  ≅  A+ × A− × B+.
```

The map takes two operands with the same labelled E+ record to their three-record union. Its two projections recover the original operands. Conversely a triple determines exactly that compatible pair. This proves the set-level fiber-product description for arbitrary payload sets, not just the Boolean test fixture.

The implementation checks the native joint-N input identities, shared-reference cell and comparison location. It rejects different E+ payloads or different reference identities even when the other data agree. Neither P record is changed or discarded. The constructor receives only those two operand views and their incidence layout; it cannot recover an unprovided fourth record from a hidden root packet.

The other three comparisons give:

| Shared reference | Retained records |
|---|---|
| E+ | P+, P−, E+ |
| E− | P+, P−, E− |
| P+ | P+, E+, E− |
| P− | P−, E+, E− |

The code retains both operand nodes in each comparison, not just the union. Payload snapshots with the same label are checked for equality; they are not independent new inputs.

## Central-N reconciliation

The two E-reference comparisons overlap in P+,P−. Joining them recovers all four records. The two P-reference comparisons overlap in E+,E− and recover the same four records. Both pairs are checked to meet the actual central N identified by the native cone.

This supplies a data-level interchange:

```
join(compare_at_E+, compare_at_E−)
          same retained record assignment as
join(compare_at_P+, compare_at_P−).
```

The resulting construction trees are unequal and both are retained in the comparison certificate. Equality of decoded records does not erase their order or become a native higher filler. The stored `nativeFiller` remains null.

The gluing succeeds because the overlap values agree. It does not require all records, phases or path comparisons to become equal. A family of independently supplied local operands with conflicting shared values is rejected.

## Decisive failures of stronger interpretations

### Shared reference does not recover the other operand

Take two full inputs differing only at P−. Their `(P+,E+)` views are identical; their `(P−,E+)` views differ. Therefore the actual right operand cannot be reconstructed from the left view alone.

For Boolean payloads, the compatible-pair carrier at fixed shared-reference type has eight triples. Imposing P+=P− leaves only four. The graph of any fixed equivalence between the four-element operand carriers likewise has four elements, not all eight compatible pairs.

This does not say abstract equivalences between those carriers cannot exist. A state-dependent equivalence could be supplied, but its choice is extra comparison data. The existing Agda compiler's Fragment input and whole-carrier/selected-point conditions have not been constructed for these Su-32 operands.

### No phase or spin lift is forced by this operation

The same joins work on Boolean values, structured JSON and complex-amplitude examples. They commute with any consistently applied per-record payload maps, including both common and independent phase rotations. All supplied phases survive because all four records survive; no U(1) quotient or transport prescription is selected.

Thus the required reference comparisons and their two-order reconciliation already have a lossless set-valued model. An assertion that their incidence or recoverability alone forces a Hopf bundle is false. A phase-sensitive physical comparison could add structure, but its additional equation is not present in this join.

## Fresh tests

All tests passed on all 36 cone/readings and four alternative sign bindings per chart:

- 2,304 cases, exhausting 16 independent Boolean assignments per chart/binding;
- 9,216 three-record comparisons, each retaining its two inputs;
- both reconciliation orders recover the original four records, including serialization;
- 3,072 checks that the eight outer entry-branch views remain unchanged;
- 144 phase-fixture comparisons showing common and independent rotations both remain compatible;
- seven hostile controls: incompatible shared payloads, wrong reference identity, dropped operand, erased history, altered result, wrong central N and wrong reading.

Each local test is a restriction of the fixed incidence fixture. These cases do not constitute a single simultaneous global payload assignment across all cones. The full boundary geometry remains unchanged.

## Disposition

We now have an executable candidate for what a layer-4 comparison retains and how central reconciliation preserves all records in either order. It is a reference-gluing law, not an inferred amplitude transformation. Its counterexamples prevent replacing shared-reference compatibility with whole-operand equivalence or erasing one derivation after the final data agree.

The Hopf investigation has a sharper discriminator: an actual layer-4 law must supply a phase-sensitive relation or frame transport that differs from this set-valued baseline. The previously derived five-slot doublets do not answer that question without an operand/operation adapter.

## Replay

```sh
node research/strominger/checkers/check_su32_layer4_comparison.mjs --record
python research/aspect/scc/scc.py validate research/strominger/scc-models/su32-layer4-comparison-v1.json
python research/aspect/scc/scc.py check su32-layer4-comparison-v1
```

Implementation: `su32-layer4-comparison.mjs`. Receipt: `results/su32-layer4-comparison-v1/verification.json`, including actual-cell example derivations, the separating input pair, counts and source hashes. Initial execution: `structured_command_execution:e_29164_1793123082566524100_25`. The SCC entrypoint executes the Node checker afresh. No formal proof backend or renderer was changed or run.
