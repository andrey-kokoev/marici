# Prior-research clues for the E/P reader obstruction

Connection: `joint44-native-source-selection` and the `face-chart-transition-descent` reader/overlap obligation.

## Main finding

**The prior research already warned against freezing bindings and projector component matrices across changes of coefficient frame.** Our latest obstruction is consistent with that warning. We imposed equality of the compressed five-coordinate L/G/N matrices while changing the five-coordinate interpretation.

A fresh small calculation now confirms the relevance: the reader-natural body-carrying comparison preserves the unchanged full native operators, with their compressed matrices related to the earlier ones by an exact coefficient-frame conjugation. Thus its failure of literal five-matrix equality is not, by itself, failure of the physical/raw operator law.

This does not invalidate the kernel obstruction: the proposed fixed-named-matrix U(2) family really is not reader-natural. It identifies the extra premise responsible for that family and suggests revising that premise rather than inventing a new reader generator.

## Ranked prior clues

### 1. A fixed-projector obstruction was already proved

`research/strominger/full-field-path-coherence-v1.md` and its checker construct the order-five comparison of two actual retained native histories. The full-field lift works, while fixed L/G/N commutation fails.

For the declared A4-equivariant coefficient model, the fixed-G obstruction is independent of the chosen embedding: injectivity would force a nonzero commutator to vanish. The paper's alternative transports component operators and readers with the frame.

**Relevance:** requiring one numerical projector pattern in every presentation can be an inconsistent extra condition, not an owning native law. The old result concerns a full-field frame change; our new bridge below is specifically its compressed five-coordinate analogue, keeping the full native operators unchanged.

### 2. Phase-only and endpoint-only bindings were already rejected

`research/strominger/five-coefficient-field-binding-v1.md` proves that a fixed N binding in the identity co-moving field convention has rank at most3. Phase-dependent bindings preserve all five coefficients. It explicitly does not derive five-dimensional L/G operators from that construction.

`research/strominger/window-combination-coherence-v1.md` records equal geometric/absolute-origin endpoints with different coefficient permutations. The concrete relative comparison has order5. The full packet history must therefore remain in the binding.

**Relevance:** independently valid seed-level presentations do not automatically supply a common reader interpretation on native histories.

### 3. There is an existing positive history-aware sewing construction

`research/strominger/joint-field-assembly-sewing-v1.md` uses

    B_h = F_h B0 Pi_h^-1,
    R_h = B_h^sharp.

Its18 actual interfaces satisfy full44 binding and readout squares. Freezing the canonical binding fails at11 of14 packet presentations.

Our own `ramsey-arbitrary-assembly-coherence-v1.md`, sections3–4, already carries this construction to the declared unbounded candidate. Its theorem keeps Pi_h even when the chart/frame agrees.

**Relevance:** we did not lack a mechanism for transporting interpretations. We should have checked the local E/P proposal against that mechanism before treating its fixed compressed projectors as globally meaningful.

### 4. Full-source covariance includes readers, not only projectors

`research/strominger/packet-handoff-naturality-10-v1.md`, section4, gives the simultaneous transport of field operators, native actions, metric, geometric reader and the antilinear reversal attachment. It checks complete raw-reader squares and shows that leaving the reversal attachment fixed produces spurious results.

**Relevance:** a repair must carry the entire interpretation consistently. Calling a changed matrix a gauge is insufficient if an independently fixed readout is silently left behind.

### 5. Geometry/line data do not uniquely select the full reader

Iterations9–10 of the same programme exhibit geometric neutron grouping and phase rivals with matching coarse invariants but different complete readers. They also distinguish capacity-based M/C conventions from independently supplied physical carrier-relative grading and observation origin.

**Relevance:** equality of a convenient reduced projector pattern is not automatically a source derivation of the named occurrence readout. Conversely, covariance alone cannot authorize an arbitrary choice of physical reader.

The eight-sector interface supplies an additional useful warning: a complete comparison can transport native channels correctly while enlarging their geometric support. That matches our three-edge repair, not a claim of recovered single-edge locality.

## Fresh exact bridge to the current counterexample

Use the two previously tested coefficient conventions:

    T_ref  x = (x3,x4,x2,x0,x1),
    T_body x = (x3,x4,x1,x2,x0).

The first belongs to the fixed-named-projector family and fails reader naturality. The second is reader-natural.

Their P coefficient change is

    D_P = T_body T_ref* = permutation[0,1,4,2,3].

Under the unchanged PN permutation,

    D_N = Pi_PN D_P Pi_PN* = permutation[2,1,4,3,0].

For each of the actual unchanged full neutron operators A = L,G,N, let A_ref and A_body be its compressions in the two moving bindings. The fresh check establishes

    A_body = D_N A_ref D_N*,
    A_body != A_ref.

It also rechecks

    P_P T_body = T_body P_E.

No full native operator was altered. These two moving bindings describe the same moving preparation subspace with different coefficient frames. The earlier difference between that moving subspace and the original fixed preparation remains; this calculation does not erase it.

Thus the earlier fork was too crude: 'reader-natural but violates native projectors' should be read as **reader-natural, with covariant rather than identical compressed projector matrices**.

This is not yet a proof that every named geometric occurrence reader is independently source-selected, or that the full four-facet semantic descent follows. It is a concrete reason to revisit the extra fixed-five-matrix requirement.

## Recommended next experiment

Start from T_body and the existing retained-history formula. Carry the compressed operator interpretation, named readouts and actual history together through the reader-prefixed PN interfaces. Test those actual squares rather than reimposing the canonical seed matrix at every context.

Keep separate:

1. unchanged full native operators;
2. their history/frame-dependent five-coordinate matrices;
3. independently required occurrence observations.

A mismatch in item3 would be substantive. A mismatch only between coordinate matrices in different frames is not sufficient to reject the interpretation.

## Evidence status

Six prior receipts were inspected. Their direct source-pin counts are4,4,4,10,109,115; all246 comparisons match the current files. Counts include repeated dependencies. The old scientific suites were **not replayed** in this search.

The coefficient-frame bridge above was freshly checked exactly:

    python research/voevodsky/checkers/check_ramsey_reader_prior_clues.py

Receipt: `results/ramsey-reader-prior-clues-v1.json`. It records the prior pin audits, note hashes, exact permutations and all three conjugacy checks. No owner source, old receipt or net outcome was changed.
