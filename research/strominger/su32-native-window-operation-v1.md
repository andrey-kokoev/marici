# Native boundary operation with integer lifts retained

## Question and disposition

Can the edge-five native boundary be read from the existing global fibration without inventing a seam, deleting incidences, or confusing a comparison programme with wire transport?

**Yes, as an open-window operation.** The construction retains every physical cell and derives all 200 boundary continuations. It does not construct a closed 80-independent-fibre carrier. Its state domain must distinguish arbitrary sections of the lifted bundle from pullbacks of states on the old periodic base.

## Global source operation

Start with the source period-labelled graph in `sulfur-32-wiring.mjs`, not the local comparison motifs. Its lattice has generators

\[
g_i=(1,1,1,1)-4e_i,
\qquad g_0+g_1+g_2+g_3=0.
\]

The first three are a basis. A period translation has the exact coordinates

\[
a_i(t)=\frac{t_3-t_i}{4},\qquad
L(a)=\sum_{i=0}^2 a_i g_i.
\]

Define the global integer-indexed graph by retaining every port `(p,a)`, with `a` in the integer lattice. A source edge with translation `t` joins

\[
(p,a)\longleftrightarrow(q,a+a(t)).
\]

No finite sheet reduction or new period lattice is chosen. The actual geometry of a lifted port is its representative face translated by `-L(a)`.

This rule preserves shared faces for every integer coordinate: the source equality `F_q=F_p+t` gives

\[
F_q-L(a+a(t))=F_p-L(a).
\]

N opposite-face continuity stays in the same lifted cell. These identities define the global family algebraically; the executable checks use bounded integer coordinates, not finite samples as a proof of an infinite physical object. No physical interpretation of an infinite universe is asserted.

The inverse geometry map reconstructs each physical cell from its base cell and integer coordinate. The checker verifies all 245 window cells individually and checks all sixteen residue types of each native cell shape. Thus physical occurrence identity is retained rather than inferred from a cell count.

## Restrict the global family to the actual window

Only after defining the global wire family do we retain wires meeting the edge-five window. Complete their P–N–E segments using the source translations. This produces:

| Quantity | Count |
|---|---:|
| Physical window cells, all distinct | 245 |
| Complete wires meeting the window | 420 |
| P–N–E passages wholly inside | 220 |
| Internal P cell views, four slots each | 80 |
| Internal E cell views, four slots each | 80 |
| External input wire slots | 100 |
| External output wire slots | 100 |

All completed ports and edges are independently found in the larger radius-four native sector. The 200 cut faces agree exactly with the earlier open-bulk boundary. Exterior observations do not replace or clip whole window cells; the global family retains the unobserved exterior slots as well.

For an arbitrary opaque wire-content type `X`, the operation is a labelled regrouping

\[
(X^4)^{80}\times X^{100}
\longrightarrow
(X^4)^{80}\times X^{100}.
\]

Its inputs and outputs refer to different endpoint and boundary slots, with their wire identities retained. The inverse reverses the presentation. No numerical mixing, comparison-packet constructor, or history deletion is introduced.

Implementation: `native-window-operation.mjs`. `applyNativeWindowOperation` validates the input cell/axis labels and all boundary values, reconstructs the wire assignment, and presents it at the other endpoints. Missing boundary rows and exchanged axis slots are rejected.

## Two state domains, not one

A section of a pulled-back bundle is not necessarily the pullback of a section.

### Unrestricted lifted sections

Distinct integer translates may have different contents. The window observes 420 wire values. Each of the 100 external inputs can vary while every internal P cell view stays fixed, changing an internal E slot. The checker executes this counterexample for each external input, and for the reverse presentation: 200 independence checks.

The external inputs therefore cannot be omitted on this domain. This enlarges the state domain relative to states pulled back from the old periodic model; it is not silently asserted as a physical state law.

### Canonical pullbacks of periodic base sections

The old model has 64 wire contents. Pulling one such state back makes contents agree on all integer translates of a base wire. Both the 80 internal P views and the 80 internal E views observe every base wire, so either presentation recovers those 64 contents and determines the exterior values.

`completePeriodicWindowProfile` implements this restricted completion, checks repeated contents for equality, and preserves all original records. A changed repeated content is rejected rather than averaged or overwritten. The completed profiles agree with direct pullback in both presentations.

This gives an invertible change of internal views **on the periodic image**, not a closed graph with 80 independently assignable fibres. It removes unknown boundary values only by retaining the old state restriction.

## Discriminating rival: five-sheeted period covers

The geometric projection has exactly five physical P occurrences and five E occurrences over each corresponding base cell. That multiplicity does not imply a five-sheeted fundamental domain.

Every index-five subgroup of the rank-three source period lattice is the kernel of a nonzero covector over the field with five elements, modulo nonzero scalar multiplication. There are exactly 31 such kernels. `sulfur-period-covers.mjs` constructs all their global graphs from the existing translation labels, without selecting one as physical.

Each cover has 80 P, N and E fibres and 320 wires. All native window edges map correctly into every cover: 27,900 edge checks. Both payload presentations round-trip in all covers: 62 checks. But none preserves all 80 distinct physical P/E cells as distinct cover fibres:

| Distinct P / N / E images | Covers |
|---|---:|
| 36 / 36 / 36 | 6 |
| 48 / 48 / 48 | 3 |
| 54 / 56 / 54 | 12 |
| 64 / 66 / 64 | 6 |
| 69 / 72 / 69 | 4 |

Even the best cases distinguish only 69 P and 69 E cells. Each receipt retains an actual same-axis port collision and two incompatible contents at that shared image. This explicitly realizes the failure predicted by the preceding capacity bound; it is not a new independent proof that every possible fibration fails.

## Remaining construction

The native open operation and its periodic-state restriction are now explicit. A closed 80-independent-fibre realization, an independently justified exterior state law, and the identification of signed comparison records with a sufficient native boundary profile remain unconstructed. The finite-cover realization branch is rejected; it is not repaired by changing the physical cell inventory.

## Reproduction and evidence boundary

```sh
node research/strominger/checkers/check_su32_native_window_operation.mjs
node research/strominger/checkers/check_su32_five_period_cover.mjs
python research/aspect/scc/scc.py check strominger-su32-native-window-operation-v1
```

The SCC wrapper freshly runs both Node checkers. Contracts are `contracts/su32-native-window-operation-v1.json` and `contracts/su32-five-period-cover-v1.json`. Receipts are `results/su32-native-window-operation-v1/verification.json` and `results/su32-five-period-cover-v1/verification.json`.

The first retains all 420 completed wires, the boundary attachment map, both full profiles, state-domain distinctions and an independence witness. The second retains the exact physical projection and all 31 collision cases. Existing source geometry and wiring were unchanged; no proof assistant was run.
