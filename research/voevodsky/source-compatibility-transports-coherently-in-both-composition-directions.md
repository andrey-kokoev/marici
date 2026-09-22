# Source compatibility transports coherently in both composition directions

## Object and orientation

The independently generated 70-state source-bound carriers, across all 52 field decompositions, supply actual transition pairs. For each of eighteen labels retain separate accepted and rejected relations; rejection is observable and has an unchanged state.

Each relation has two presentations. Forward presentation lists compatible successors. Its transpose lists compatible predecessors. The latter retains the original edge's source/evidence lineage and acceptance stratum; it supplies a backward compatibility query, not an authorization to execute acquisition or delivery in reverse.

## Coherence theorem

For relations f and g, transpose satisfies

    (g composed with f)^op = f^op composed with g^op,
    (f^op)^op = f.

The source-coordinate isomorphisms F_DE act on both endpoints of every relation. Direct checking establishes

    transport(F_DE, f^op) = transport(F_DE, f)^op.

The already checked strict composition F_EG F_DE = F_DG therefore also holds in the opposite presentations. Boundary regrouping and orientation reversal commute. The identity follows from relational composition and bijective endpoint transport; the finite checks bind it to the actual carriers rather than proposing new physical laws.

## Exact checks

After a fresh run of the decomposition constructor:

- 1,872 double-transpose checks;
- 67,392 composition-reversal checks;
- 97,344 decomposition/reversal naturality checks;
- 46,656 generator associativity checks on the reference carrier.

All other carriers are related to that reference by checked bijections. The relational identities and generator checks extend by composition to arbitrary finite words. Vertex outputs and source-coordinate bindings are preserved by the decomposition comparisons.

Some opposite relations have two successors. Thus the backward presentation naturally retains multiple possible predecessors even though the forward protocol is deterministic. No arbitrary inverse branch is selected.

## Structural result

The same source-compatible relation supports histories and possibilities in either logical orientation. Decomposition changes its presentation; transpose exchanges which endpoint is read as given and which as possible. Both operations preserve the compositional relation with strict coherence in this finite model.

This establishes the direction-independent version at the level of relational compatibility. It does not establish a direction-blind fixed observer, an internally executable reverse-time protocol, or equivalence of forward and backward deterministic dynamics. The earlier fixed-label orientation distinction remains valid.

## Reproduction

    python research/voevodsky/checkers/check_unoriented_decomposition_transport.py

Artifact: `results/unoriented-decomposition-transport.json`.

The checker reads the freshly generated actual carriers and independently performs set-relation composition and transpose. It relies on the owning source/evidence and expression-semantics certificates for the meaning of their transition pairs.
