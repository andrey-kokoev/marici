# Iteration3: actual relation packets and the minimum nontrivial balanced cut

## Fresh net task and a necessary correction

Read the current34-node/v10-pin net. Its recommended task was `relation-layer-wg-binding`: retain an actual nonzero four-event product and compare balanced seam factorizations as WG packages.

The four-event packet has only a2+2 product cut because each relation consumes at least two events. A nonidentity balancing action (as) tensor b = a tensor (sb) with a one-event s needs FIVE events, with cuts3+2 and2+3. Two genuinely different nonminimal cuts cannot be manufactured inside the four-event cutoff. We keep the four-event attachment witness and add the smallest five-event extension for balancing; the four-event result is not replaced or relabelled.

## Reused source, not an invented algebra

The new checker imports the guarded definitions from `research/nima/checkers/check_seven_event_factorization_descent.py`: relation, multiply, record, feature and derivative. It does not rerun the large seven-event global presentation or alter it.

Relations are signed combinations of marked paths with explicit initial/final vertex bitmasks. A wrapper verifies that paths do not repeat an event and have one common endpoint, and rejects noncomposable operands. Source equality means equality of full marked-path coefficient vectors, not equality under terminal recording.

## Four-event attachment retained

Take the singly retained relation a on events0,1 and the forgotten relation b on events2,3. Their product v=ab has eight nonzero signed terms from vertex0 to15. The actual terminal recorder kills a,b,v, while a selected path coefficient detects v with value1.

The local source action is computed by actual typed right multiplication by b on the basis (a,b,v). Its only nonzero matrix entry is a->v. Endpoint typing kills b*b and v*b. Splitting into unrelated first-relation and product-layer coordinates and dropping the cross-layer action gives the zero matrix instead.

This finite hostile detects exactly the attachment feature required by the existing nonsplitting proof: q(a)b=0 in I/I^2 but ab is nonzero in I. It does not newly compute the entire458-dimensional ideal or classify every possible module extension. The full nonsplitting theorem remains the cited source result.

## Five-event balancing packets

Use a on events0,1, one marked/unmarked event s=2, and b on events3,4. For all eight choices of the two local relation kinds and the middle event mark, construct:

    left packet:  (a*s, b), cut after event3
    right packet: (a, s*b), cut after event2.

Both products are exactly the same nonzero source vector asb. Each factor is recorder-invisible. Their two seam images BEFORE balancing differ because the cut labels differ. A two-factor specialization of the owner's buffer-merging normal form identifies them. The result is nonzero and its balanced seam boundary vanishes.

This is not equality obtained by dropping all witnesses. The reconciled Answer keeps both FactorPackets, each containing:

- both complete typed source factors;
- their full product vector;
- their unbalanced cut-labelled seam data;
- the balanced seam normal form.

It also retains the Request(a,s,b) and an actual nonzero source-coordinate detector. The verifier reconstructs both packets from that request and checks their products and balanced equality independently. Original factors and different factorization histories remain available after reconciliation.

These finite Python packages follow the complete-input/result/witness discipline. They are NOT yet encoded as actual native `WholePackageSigmaPi.Complete` values, nor is their generator compiled as a Layer1 WG. That is the next binding task, not something established by calling a Python dataclass a WG.

## Tests and boundaries

Executed `python research/strominger/checkers/check_relation_wg_packets.py` successfully. Nine positive checks pass, including all eight five-event balancing cases. Four controls reject wrong endpoints, raw-cut equality before balancing, an unrelated graded direct sum substituted for the source action, and a zeroed product detector.

Receipt: `research/strominger/results/relation-wg-packets-v1.json`.

The action matrix is computed from actual path products and reconstructed from basis coordinates; it is not merely a hard-coded expected matrix. The two-factor seam calculation reuses the owner's derivatives and independently checks its boundary.

No new Agda verification, completed analytic descent,137-record comparison, full source reconstruction or identification of Ph2S2 with I^2 is claimed.

## Next executable obligation

Bind this exact finite Request/Answer/action data to the existing native complete-package interface, retaining both cuts and the source action. The input now has explicit generated vectors and witnesses; do not rebuild another abstract relation model. The parent `relation-layer-wg-binding` remains open until this native interface is supplied at its claimed scope.
