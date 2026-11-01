# First cyclic-operadic extraction from edge-three comparison operations

## Implemented scope

This is the first bounded step toward recovering edge-five operations from the existing content-bearing structure, rather than choosing them after geometric routing. The active SCC obligation is **route/coherencer compatibility**.

`su32-cyclic-port-fragment.mjs` extracts a two-corolla fragment from the existing `compareAt` and `reconcileAt` constructors. Neither constructor was changed. They are candidate information operations already present in the repository, not an independently established physical dynamics.

The source tree is the existing comparison C followed by reconciliation R, with four external ports. All four occurrence sign bindings in `reading:0:-1` are retained.

## Colours, fibres and roots

Each actual wire has two half-incidence colours. A colour retains the wire, its endpoint, and its structural packet type (occurrence anchor, origin, record references and kind). The involution swaps the two half-incidences without modifying the packet. The local readout wire is explicitly distinguished from a shared-face wire.

This is **arc duality** in the sense of Definition 4.1 of Doherty–Hackney, not a demonstrated identification with physical P/E duality.

The fibre over a corolla profile consists of complete rows of its existing operation relation. Payloads and constructor histories live in these fibres; they are not replaced by colour labels.

Choosing a boundary arc as the output dualizes its colour. The remaining arcs become inputs. For the original reading, C's output colour then exactly equals R's corresponding input colour. For each other root, the boundary choice agrees with the existing whole-tree geometric orientation algorithm. No newly chosen payload map is needed to re-present the same decorated operation. This does not authorize a native inverse execution.

## The first Segal comparison

Let C and R denote the local operation-row sets, and E the full internal packet domain. The tested tree fibre is the matching pullback

\[
X(T)=C\times_E R.
\]

The adapter independently decomposes an actual source reconciliation output into its two local decorations, and reconstructs that output by revalidating and gluing those decorations. Both directions preserve the complete internal packet and both constructor histories.

Per sign binding, there are 8 C rows, 64 R rows, and 32 matching pairs. On these finite domains the two-sided reconstruction is exact. This is the two-vertex instance of the Segal reconstruction discussed in §4.2 of the paper; it is not a proof of all Segal or inner-horn conditions.

Cyclic reindexing acts on port presentations together with their values and colours. Composition uses the cyclic profile-splicing formula of Definition 3.2. All nine combinations of local three-port rotations give the same labelled external cyclic order, up to cyclic rotation, and retain the same source operations. This is not the previously investigated dynamical four-step return.

## Hostile: matching only content headers doubles the gluing domain

Per binding, matching only records and attachment headers admits 64 pairs rather than 32. The extra pairs disagree on the order of the internal comparison's retained children. The output on the R side contains a different actual history from the output on the C side.

Across all four bindings, **128 spurious gluings** are rejected by full packet matching. Same-polarity port gluing is also rejected. Thus structural colour compatibility and even equal observable contents do not replace equality of the retained internal fibre element.

## Verification

```sh
node research/strominger/checkers/check_su32_cyclic_port_fragment.mjs
python research/aspect/scc/scc.py validate research/strominger/scc-models/su32-cyclic-port-fragment-v1.json
```

Fresh finite checks:

- 128 two-sided source/pullback reconstructions;
- 1,152 cyclic gluing comparisons;
- 512 geometry-compatible root presentations;
- 128 rejected header-only gluings;
- 8 additional null/mixed-JSON reconstruction samples.

Receipt: `results/su32-cyclic-port-fragment-v1/verification.json`. It includes source hashes, the paper hash, a complete example, and a concrete false-gluing witness. No proof assistant was run for this fragment; sample coverage is not an unrestricted-payload theorem.

## Next exact obligation

Extend the occurrence-indexed operation fibres to edge-five and compare their restrictions on overlapping cones. The existing atlas constructor explicitly requires edge three; it has not been bypassed by relabelling an edge-five fixture. A supported extension must establish the local identifications and their compatibility, not merely copy the number of ports or use the four-block route controller.

Units, arbitrary-tree associativity/higher fillers, identification of arc and content dualities, and global edge-five descent remain unimplemented. The result establishes a concrete local operational reconstruction, not a complete cyclic infinity operad.
