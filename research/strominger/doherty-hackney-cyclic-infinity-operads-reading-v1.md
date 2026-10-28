# Reading: Doherty–Hackney, arXiv:2506.15622v2

Read the supplied 41-page PDF `references/2506.15622v2.pdf` in full, including its technical sections and appendix, through text extraction. Some mathematical glyphs and overbars are lost in extraction; formulas below are stated using explicit duality notation rather than copying damaged displays.

Brandon Doherty and Philip Hackney, *Models for cyclic infinity operads*, July 14, 2025.

## Main results

The paper constructs and compares homotopy theories of cyclic operads:

- **Theorem A / 6.5:** a model structure on cyclic dendroidal sets, with normal monomorphisms as cofibrations and cyclic quasi-operads as fibrant objects. The latter fill all inner horns indexed by unrooted trees.
- **Theorem B / 7.14:** homotopy-coherent nerve and rigidification give a Quillen equivalence with simplicial cyclic operads.
- **Theorems C–D / 8.2–8.4:** complete cyclic dendroidal Segal spaces provide another equivalent model.
- **Theorem E / section 9:** analogous comparisons hold for planar versions, obtained using slices over associative operads/presheaves of planar structures. This supplies the missing model-categorical foundation for Walde's connection between cyclic 2-Segal spaces and invertible planar cyclic infinity-operads.

These are comparison/existence theorems for mathematical model structures, not algorithms that identify native operations from a cell-incidence graph.

## 1. Cyclic composition is not a circle bundle

An ordinary operad distinguishes an operation's output from its inputs. A cyclic operad treats its boundary slots without a permanently distinguished output. Its colors carry an involution; composition glues a specified pair of dual-compatible slots from two operations (Definition 3.2, pp. 6–7).

The symmetric cyclic theory does **not** require a chosen cyclic ordering of the slots: it has the full symmetric action on all slots. Planar cyclic operads replace that action with cyclic actions and use locally cyclically ordered tree structures (section 9).

This must be separated from Mnev's simplicial set of circular orders whose realization is K(Z,2). A cyclic-operad structure does not, merely by its name, provide a circle fiber, a first Chern class, or a map into Mnev's SC.

For Su-32, input/output-neutral port composition might be relevant to dual presentations even if no canonical planar order exists. But our directional signs are not automatically the required color involution, and the four record labels are not automatically the operation's four boundary ports.

## 2. Trees separate local operations from composite realizations

The shape category uses unrooted trees with oriented arcs, a fixed-point-free involution on those arcs, vertex neighborhoods and boundary arcs (Definitions 4.1–4.10, pp. 8–10). A root is a chosen boundary arc.

Inner faces contract internal edges; outer faces restrict to appropriate subtrees. Thus a tree-shaped coherence problem does not require treating each three-record comparison as a triangular simplex.

The **Segal core** retains the vertex operations and their shared edge data. In the set-valued setting (Definition 4.28, p. 13), the Segal condition is the bijection

```
X(T) -> lim_{vertices and edges U of T} X(U).
```

In the Reedy-fibrant space-valued version, the corresponding map is a weak homotopy equivalence. This expresses that compatible local operation data determine a composite realization up to the specified coherent notion of equivalence. It is stronger than agreement of the final payload readout.

For two vertices joined along one edge, this gives a concrete first gluing test. More vertices test compatibility of composition orders. The inner-horn formulation supplies another way to encode the compositional and higher coherence requirements.

## 3. Changing roots is constrained by the operation structure

The root-elision functor from rooted to unrooted tree shapes is a discrete fibration (Proposition 4.12). It is also a discrete opfibration on active maps (Proposition 4.16). These are precise compatibility statements about how roots behave under tree maps, not permission to choose arbitrary reference changes.

The paper analyzes adjoint strings for forgetting cyclic structure and forgetting roots. Free cyclic enlargement and cofree constructions are available mathematically, but adding formal structure is not the same as finding it in the source system.

Our new central-N packet only changes an active E-reference view while keeping the current central boundary fixed. **It has not been shown to change the output root of a multi-input operation.** Calling its E+ / E- selector a cyclic re-rooting would therefore be premature.

## 4. Coherence has explicit composition-shape parameters

The rigidification construction in section 7 associates to a suitable subtree S the nerve of the poset of edge subsets containing its boundary. Its varying choices are the internal edges, producing a cube of dimension equal to the number of internal edges (pp. 18–20).

Composition is induced by gluing subtrees along one compatible edge and taking unions of the corresponding subsets. This realizes a cyclic version of the Boardman–Vogt construction.

This is relevant to retained comparison histories: different stages/orders can be encoded with explicit coherence data rather than identifying their raw syntax. But the paper does not construct a native interpretation of those parameters for Su-32. Freely completing a presheaf to a fibrant object can add fillers; it cannot certify that those fillers were supplied by the existing native rules.

The Beck–Chevalley argument in section 7 concerns the functors between these model categories. It should not be substituted for a source-specific interchange theorem between two Su-32 operations.

## 5. Important limitations for Su-32

1. **Matching interfaces are required.** Record-support overlap is not automatically a compatible operadic gluing edge. Define port types, their duals, and the actual identification law first.
2. **No automatic reversal of processes.** Cyclic symmetry of slots is not a theorem that a physical operation is invertible. Anti-involution is distinguished from inversion; the paper treats anti-involutive categories as a special case.
3. **Trees do not include arbitrary loop contractions.** If the proposed composition itself glues into cycles or self-contractions, a tree-based cyclic operad may not suffice. The paper explicitly lists modular infinity-operad model structures as future work. Cycles in the ambient physical carrier alone do not establish that such composition shapes are necessary.
4. **Shared record reuse needs a declared treatment.** Unfolding a retained DAG as a tree must not turn one shared record into independent inputs. If a proposed port model cannot retain that constraint, it is the wrong adapter.
5. **Planarity is additional data.** A planar cyclic model requires compatible cyclic orders at vertices (Definition 9.1). Do not insert lexical order or infer it from the tetrahedral support count.
6. **Homotopy coherence must have an actual target.** An AST log is not already a simplicial operation space. Conversely, equality of decoded states is not automatically a specified path between operation histories.

## Most useful consequence for the present work

This paper suggests a compositional question closer to our actual construction than an immediate K(Z,2) calculation:

> Do the retained comparison operations admit a root-independent, dual-port composition law, and do compatible local operations determine coherent global composites?

A bounded first test would:

1. Specify a corolla for one existing comparison: its actual ports, port colors/duals, operation state and retained provenance. Do not derive arity just from the number of record labels.
2. Specify one genuinely admissible two-vertex gluing, with full shared record/occurrence constraints.
3. Compare the proposed whole-composite state with its vertex-and-edge restrictions. Determine whether the Segal-style map has no extension, one extension, or additional retained choices.
4. Test a three-vertex composition and any independently justified re-rooting, retaining an explicit witness if orders are compared only up to equivalence.

Our complete-core selector supplies a possible information-preserving view operation, but none of the required multiport gluing or cyclic actions is yet established. The test must not declare the Segal condition true by defining the whole composite to be exactly its list of local decorations and then claim a native theorem.

The benefit is conceptual: **comparison contexts can be organized by operation trees before they are organized by ordinary simplices.** This avoids the unsupported step from three-record supports to tetrahedral faces. It does not resolve the native operation-selection problem by itself.

No model implementation or scientific admission status was changed by this reading.
