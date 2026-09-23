# Retained defect transport makes two-refinement retirement coherent

## Return to the structural question

The earlier architecture compared presentations through a retained base and required actual compatible face data before a cone could be filled. The retirement lane now has a small explicit counterpart: a comparison between direct and staged fine continuation, with the information needed to authorize that comparison carried throughout.

This is NOT yet an identification with the earlier residue jet, four-simplex or five-dimensional cone. It is a checked comparison cell on which such an identification would have to rest.

## Objects and the retained package

Let E be one of the owning m=4 fine histories. Its retirement exposes public observations and a shared lifting contract. To permit stronger fine continuations, retain a package

    D_E=(original fine archive, source chart, event/context binding,
         actual-history authority, checked continuation path).

Our executable package is deliberately sufficient rather than minimal: it retains the complete fine rows. It does not identify a smallest residue invariant. Authority comes from an explicitly trusted pre-retirement vault; a packet containing the same digest is not independently authorized.

The live shared summary does not by itself contain D_E. A fair total-retention account includes the vault and its history selector. The event/root binding remains unchanged along authorized refinement paths.

## The comparison square

For a fine predicate F, compare

    E ----------------retire----------------> R_C(E)
    |                                           |
    | intersect F                               | continue using D_E
    v                                           v
    E intersect F ------present-------------> I(E intersect F).

The lower-right interface I presents exact public admission and admissible fine witnesses of the refined relation. Its representation need not be the old common section. The right arrow is a resource-relative operation: it reconstructs the authorized fine relation, intersects it with F, then presents the successor.

Without D_E or equivalent retained information/authority, the right arrow may not exist. The already checked A/B obstruction proves that for the fine bound h<=1/2: the same public point has different admission answers. Thus this is not a formal square obtained by defining a missing arrow from a chosen lift.

## Two-refinement cell

For predicates F and G, the semantic comparison is

    Theta_(F,G): Continue_G(Continue_F(R_C(E);D_E))
                    ==> Continue_(F intersect G)(R_C(E);D_E).

Both routes must present exactly E intersect F intersect G. In the fixed chart, fine evidence consists of rational affine inequalities. The checker validates each edge against its expected predecessor, exact operation batch and immutable archive root. It then compares canonical row sets of the terminal states.

Canonicalization here normalizes rational strings, sorts rows and removes exact duplicates. It does not solve general polyhedral equivalence or remove all redundant inequalities. Equality of the resulting full row systems is a sufficient certificate of equality of the complete fine relations, and therefore of their public images and their admissible fine-lift relations at EVERY public point.

The direct and staged proof tips are different hashes. The comparison does not identify execution traces or authorization histories. It identifies their declared semantic outcomes while preserving their path-specific proof bindings.

## An elementary composition law

At the semantic level the relevant algebra is conjunction:

    (E intersect F) intersect G = E intersect (F intersect G).

In this row presentation, all finite parenthesizations normalize to the same union of original and appended rows; the statement follows by induction on the sequence length. Permuting pure conjunctive refinements also leaves the fine relation unchanged.

This gives coherence of the semantic normal form for this class, NOT a general commuting law for arbitrary operations. Projection, history erasure, authority revocation, policy changes and source edits do not automatically commute. Nor do canonical semantic forms provide all higher proof-path homotopies required by the earlier analytic cone architecture.

## Checked owning realization

The test uses the real owning m=4 moment-curve source chart with n=18 and either history A or B. Apply

    F: h<=1/2,
    G: h>=1/4.

It constructs and checks:

1. direct continuation by the two-row batch;
2. staged continuation by F then G;
3. permuted continuation by G then F.

For both histories, the direct/staged and staged/permuted terminal fine relations agree. The public endpoint (1,1) survives only for B; the first public vertex survives only for A. Hence the comparison preserves actual history rather than collapsing the two branches to one convenient witness.

Point controls recheck the returned source-chart witness against the terminal fine rows. They supplement, but do not replace, the whole-domain equality certificate given by identical row systems.

The defect transport controls retain the same full archive and authority root while updating path commitments. Substituting the other history's archive is rejected even when the coarse family context is identical. Twelve refusal controls include missing fine rows, omitted earlier operations, broken predecessor binding, history substitution, altered retained archive and self-asserted authority.

## What is—and is not—implemented

These are replayable comparison certificates, not two simultaneously published successors of one linear checkpoint. The checker invokes the explicit trusted vault boundary to obtain its root; it does not simulate external authentication. Fine archive construction and verification share the established envelope kernel. No separately implemented general geometric equivalence prover is claimed.

The archive root and path binding model a retained base. The additional fine rows and identity are a candidate retained defect PACKAGE, not an established residue jet. We have not proved injective residue transport, found a minimal defect, assigned the old five presentation roles to today's objects or filled a literal four-simplex/five-cone.

The concrete advance is narrower and structural: a required comparison cell now has explicit premises, an exact semantic equality certificate, nontrivial history-dependent controls and a stated failure when identity authority is absent. This is preferable to naming an abstract cone whose missing faces are still unauthorized.

## Reproduction

    python research/voevodsky/checkers/check_continuation_coherence.py

Implementation: `checkers/continuation_coherence.py`.

Artifact: `results/continuation-coherence.json`.

Result: two histories, four terminal semantic comparisons, twelve refused invalid certificates.
