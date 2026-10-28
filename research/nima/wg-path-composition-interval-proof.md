# WG-I5: oriented-line path composition realizes full-record interval extension

## Scope

This proves the frozen representation-level claim in `wg-path-composition-interval-contract.md`. Active SCC obligation: forward realization and full-record operation/composition compatibility. The directed line is a supplied carrier. No autonomous schedule, physical selection of the line, metric or spacetime interpretation follows.

The existing operation is `compose(left,right)` in `checkers/check_indexed_path_synthesis.py`: concatenate p and q when target(p)=source(q). The independent history source is `nnmhv_coherence_paths.py`. The earlier endpoint-edit construction supplies the comparison target, not the path operation.

## All-n proof

Fix n>=6 and m=n-5. Give vertices 1,...,m+1 the edges e_k=(k,k+1). Every nonempty directed path is uniquely

    p_ij=(e_i,e_(i+1),...,e_j),  1<=i<=j<=m.

Proof: its first edge fixes i, and every successive edge is forced by the matching endpoint; the last edge fixes j. Conversely each displayed word is a legal path.

The compiler's selected histories are exactly h_n(b1,b2) with 5<=b2<=b1<=n-1, retaining outer pair (2,b1), inner pair (3,b2), left-nested branch, prefix (b1,2), and an upper replacement (2,b1) precisely when b1=b2. Therefore

    D_n(p_ij)=h_n(j+4,i+4),
    E_n(h_n(b1,b2))=p_(b2-4,b1-4)

are mutually inverse on COMPLETE objects, including boundary payloads. This uses the compiler formula proved in `wg-interval-operation-bridge.md`, not a claim that endpoints recover arbitrary histories.

### Left operation

For i>1, target(e_(i-1))=i=source(p_ij). The actual composition rule returns exactly the singleton {p_(i-1,j)}. Thus

    D_n(e_(i-1) ; p_ij)=h_n(j+4,i+3)=L(D_n(p_ij)).

The guard i>1 is equivalent to b2>5. At i=1 no preceding line edge exists; it is not an admissible operation.

### Right operation

For j<m, target(p_ij)=j+1=source(e_(j+1)). Composition returns exactly {p_(i,j+1)}. Consequently

    D_n(p_ij ; e_(j+1))=h_n(j+5,i+4)=R(D_n(p_ij)).

The guard j<m is equivalent to b1<n-1. At j=m no succeeding line edge exists.

On diagonal paths i=j the original record has an upper replacement. Either extension moves off the diagonal and must remove it; a right extension also changes the prefix. These follow from the complete decoder, rather than being discarded comparison coordinates.

### Composition and histories

A labelled execution is a path object together with a finite admissible L/R word and every intermediate path. Applying D_n to each state and retaining each operation tag gives a corresponding full-record execution. The inverse applies E_n statewise and retains the same tags. Induction on word length using the two operation equations proves that these maps are mutually inverse on executions and preserve endpoint matching, empty executions and concatenation. Associativity is ordinary concatenation of execution sequences.

Where both moves are admitted, L then R and R then L give the same final path p_(i-1,j+1), hence the same complete source record. They are distinct executions: their tags and intermediate path objects differ. Thus the operation graph and its free execution-path category are faithfully realized; its endpoint quotient is not a faithful execution representation. No cancellation, preferred ordering or conflation with the thin containment poset is made.

The underlying compose operation itself is associative because endpoint-compatible tuple concatenation is associative. Left and right singleton-edge actions are its explicitly selected actions. Reindexing alone preserves path words and cannot implement either extension. Self-composition of a nonempty forward line path is inadmissible because its final vertex differs from its initial vertex; the earlier length-doubling fixture is not this extension law.

## Exact independent regression

`checkers/check_wg_path_composition_interval.py` loads the actual existing source script, runs its original fixture checks, and uses its unmodified compose/source/target functions. It independently enumerates selected records with the NNMHV compiler; the decoder looks up complete compiler records and checks the inverse. It compares actual path-composition outputs against the separately implemented endpoint source edits.

Finite tests cover every object and admitted extension for n=6..15 and all admissible executions for n=6..10, including every binary split and triple split of execution words. Controls reject non-line words, empty objects, boundary extensions, stale prefixes and upper replacements; they distinguish reindexing, self-composition and erased execution order. The general theorem is the argument above, not extrapolation from finite enumeration.

No fresh Agda formalization is claimed. The checker and SCC receipt establish bounded software regression, not physical source selection.

## Disposition

WG-I5 is constructed/proved at its frozen mathematical scope: an existing path-composition specialization realizes the selected interval edits and retained execution composition. This is stronger than merely declaring a new endpoint-edit WG, but does not derive the supplied oriented line from the original four-point carrier.

WG-I1, WG-I2, WG-I3, WG-I4-v2, WG-G1/G2, C2/C3 and M0 remain open. In particular, the metric-scale counterexample and distinct-causal-realization obligations are unchanged. No downstream proof is inferred from equal interval endpoints.
