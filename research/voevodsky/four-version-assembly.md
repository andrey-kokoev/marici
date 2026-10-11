# Reconstruction wrapper for four existing recipes — not a derived common construction

## Correction of the claim

The operator requested a shared construction explaining the four versions and independently justified procedures connecting them. This implementation does not establish that result. It packages existing endpoint-specific choices into one record and rebuilds the selected recipe. Route agreement is substantially imposed by that organization.

The passing checks establish faithful reconstruction and implementation consistency only. They must not be cited as discovery of a common origin or completion of the requested meta-tetrahedron. The earlier statement that this answered the operator's construction-level question is withdrawn.

A substantive completion would need a common generating operation and connecting procedures justified from it without choosing which endpoint recipe to rebuild. Those procedures would then be frozen and tested against the four constructions. No such independently justified generating operation is supplied here.

## What was requested

Find a common starting construction and actual procedures connecting its four versions, then check that taking different routes gives the same result.

The earlier investigations substituted comparisons of compressed coefficient states. This test instead acts on complete construction records and executes the geometric and carrier-building procedures. Its active obligations are forward realization and route compatibility.

## What is being tested

The shared starting record is `contracts/four-version-assembly-seed.json`: a labelled regular tetrahedron, its cyclic generators, the retained placement/frame convention, belt gap 7/10, adjacent-pair rule, circulation rule and signed spinor rule. These are supplied choices from the existing constructors, not consequences of an unmarked center point.

Operation B makes opposed base copies, translates and stitches them into the belt, assigns the retained alternating circulation, and rebuilds whichever carrier is present. Operation S replaces the cyclic-mode carrier by face-normal spinor projections and recomputes their frame normalization, retaining the geometry and circulation signs.

The conjecture is that S(B(P)) and B(S(P)) produce the same complete fourth construction, with the intermediate records reproducing N and E respectively. Rivals are merely relabelled records, copying expected coefficients, erasing the belt signs, or copying the electron normalization after changing geometry.

The checker builds both routes without access to the reference coefficient stores. Only after construction does the test harness open those stores and compare the full labelled coefficients. Sign erasure and stale normalization are deliberate failure controls; a compressed state-only input must be rejected.

## What was constructed

The executable assembly family is:

| Geometry | Cyclic triangle-mode assembly | Spinor face assembly |
|---|---|---|
| Tetrahedron | Proton construction P | Electron candidate E |
| Signed, paired belt | Neutron candidate N | Fourth candidate X |

The cyclic column uses one weighted local-mode / alignment / return assembler. Its inputs are twelve transported three-coordinate modes for P and three transported twelve-coordinate modes for N. The geometry routines construct those inputs, including the original plane coordinates and circulation signs. The spinor column uses one face-projector / frame-normalization assembler for both geometries.

No reference endpoint coefficients enter these constructors. They are loaded only after both routes have executed, to check the results.

### Operation B: rebuild on the belt

1. Apply the recorded seed-to-display placement convention.
2. Select the tetrahedral base, create its opposed copy and place them at gap 7/10.
3. Stitch nearest vertices into six outward-oriented panels.
4. Assign the recorded alternating circulation; for cyclic assembly, form the first C3-invariant adjacent pairing and its intrinsic plane coordinates.
5. Reassemble using the current local carrier rule.

B does not merely deform existing coefficient arrays. It reconstructs them from the new geometry. The display placement in the retained coordinate conventions is explicitly orientation reversing; neither a proper spinor rotation nor an unnoticed relabelling is substituted for it.

### Operation S: change the local assembly rule

1. Keep the current geometry, face ordering and circulation signs.
2. Compute its outward Euclidean face normals.
3. Replace the cyclic-mode rule by P_i=(I−chi_i n_i·sigma)/2.
4. Compute the actual sum of projectors and its inverse; use them to build the new local, alignment and return matrices.

This normalization is computed afresh. The tetrahedral value cannot be carried unchanged onto the belt.

## What passed

The actual intermediate constructions match their retained protocols coefficient for coefficient:

| Rebuilt construction | Matched nonzero transfers |
|---|---:|
| P | 1836 |
| N | 1836 |
| E | 144 |
| X | 312 |

The N comparison also checks every intrinsic coordinate, metric factor, selected mode numerator and branch sign. The generated belt vertices and ordered faces match the source geometry.

Both routes

```text
P → B → N → S → X
P → S → E → B → X
```

produce exactly equal construction content: retained seed, geometry, labels, signs, carrier, normalization and all coefficients. Their common endpoint content hash is

```text
d8dcc6c117d483f4f0e3589148cf04f3677ac14cc622e95176dd6545ec4e95e6
```

The route histories themselves remain different; the test does not erase or identify them.

## The other comparisons and all four faces

Because the full seed and recipes are retained, a reverse edit can restore the tetrahedral geometry or the cyclic assembly rule and rebuild. These are explicit recipe operations, not recovery of information from a compressed state. The diagonal N-to-E procedure, for example, restores the seed tetrahedron and applies S.

All six pairwise recipe comparisons and their reverse edits were executed. Each rebuilds the expected endpoint. The four triangular route tests pass:

| | |
|---|---|
| **PNE:** P → N → E equals P → E | **PNX:** P → N → X equals P → X |
| **PEX:** P → E → X equals P → X | **NEX:** N → E → X equals N → X |

The diagonals are composite recipe edits, not independently derived physical interactions. The comparison is at this frozen seed and its declared parameters, not a theorem about arbitrary states or every possible assembly family.

## Failure controls and the earlier obstruction

Erasing the neutron circulation signs when applying S produces the different 264-transfer construction, so it fails the intended route comparison. Copying the electron frame normalization onto the belt produces a non-idempotent return. Supplying only a final coefficient/state record without its seed and geometry is rejected.

The earlier rank and local-channel obstructions remain true for state-preserving or face-local maps. They do not obstruct these reconstruction procedures: the latter retain the construction recipe and rebuild a different carrier rather than compressing a two-component input into a one-component state. No arbitrary scalar functional is inserted here.

## Disposition and limits

**A reconstruction wrapper has been built and checked; the requested common construction remains unestablished.** The six comparisons are recipe-selection/rebuilding operations, not independently justified connections discovered between the constructions.

Its shared starting record still supplies the labelled tetrahedron, placement/frame conventions, gap, adjacent-pair selection, circulation rule, cyclic generators and spinor rule. The test establishes that the four existing protocols fit this common recipe and that the implemented edits commute. It does not derive those choices uniquely, establish a physical transformation between particles, or identify the fourth candidate.

Fourteen exact checks pass. The shared-assembler version was frozen at `5b714c6e0d1709d5` before its full run. Existing source artifacts and viewers were not modified.

## Reproduction and artifacts

```text
python research/aspect/scc/scc.py check voevodsky-four-version-assembly
python research/aspect/scc/scc.py categorical research/voevodsky/contracts/four-version-assembly-diagram.json
```

- Common starting record: `research/voevodsky/contracts/four-version-assembly-seed.json`
- Procedures and checker: `research/voevodsky/checkers/check_four_version_assembly.py`
- Comparison report: `research/voevodsky/results/four_version_assembly.json`
- Reconstructed full records: `research/voevodsky/results/four_version_assembly_records.json`
- Instantiated route diagram: `research/voevodsky/contracts/four-version-assembly-diagram.json`

SCC compares the result tokens of already executed routes at the declared inputs. Its report does not replace the source checker or establish arbitrary-state transport, uniqueness or physical identity.
