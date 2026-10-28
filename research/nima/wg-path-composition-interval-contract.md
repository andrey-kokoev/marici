# WG-I5: interval extension by the existing path-composition specialization

## Question and fixed candidate

Does the endpoint-compatible labelled-span composition operation already implemented as `compose(left,right)` in `research/nima/checkers/check_indexed_path_synthesis.py`, instantiated on a declared oriented line, realize both full-record interval extensions?

This selects PATH COMPOSITION, not fibration/reindexing and not repeated self-composition. The existing code's four-vertex complete graph is a fixture, not identified with the line. Only the endpoint-matching composition algorithm is reused. The line carrier is explicitly supplied for this candidate; its physical or native-source selection is NOT claimed.

Active SCC obligation: source forward realization and full-record operation/composition compatibility. This is a specification, not a new proof or executed test.

## Domain and codomain

For every n>=6, put m=n-5. Supply the directed line with vertices 1,...,m+1 and generating edges e_k=(k,k+1), 1<=k<=m. Its nonempty directed paths have their complete ordered edge words retained.

For 1<=i<=j<=m write

    p_ij = (e_i,e_(i+1),...,e_j).

The target source-record type is H_n from `wg-interval-operation-bridge.md`, i.e. the actual compiled selected NNMHV histories, with full prefixes and boundary replacement payloads. The candidate decoder is

    D_n(p_ij) = h_n(j+4,i+4).

The interval projection is F_n(D_n(p_ij))=(i,j). Inputs must be consecutive forward line paths; arbitrary complete-graph paths, empty paths and loops are outside this decoder domain. An empty execution history at a nonempty path is allowed and must not be confused with an empty path object.

## Precisely claimed operations

Let composition concatenate two edge words exactly when their endpoints match. Use singleton path families when invoking the current set-valued implementation.

    A_L(p_ij) = e_(i-1) concatenated with p_ij, provided i>1;
    A_R(p_ij) = p_ij concatenated with e_(j+1), provided j<m.

The selected edge is fixed by the current endpoint. BOTH admitted operations are available where both guards hold. No schedule choosing between them is asserted.

WG-I5 conjectures that D_n is a bijection between these path objects and H_n and that, for every n and every admitted input,

    D_n(A_L(p)) = L(D_n(p)),
    D_n(A_R(p)) = R(D_n(p)).

Equality is on full compiler records, not just endpoints. The operations must rebuild the correct prefix and remove obsolete upper replacements. Extend the map to labelled execution histories, preserving intermediate path objects, move tags and record witnesses. Sequential execution composition must be preserved; LR and RL execution histories must remain distinct even when they produce the same final path object.

This does not identify adjacent-path concatenation itself with interval extension: extension is the specified left/right singleton-edge action of that composition operation. Reindexing alone is a deliberate negative control, since it preserves the edge word. Self-composition, which doubles length when admitted, is a separate negative control rather than the claimed successor.

## Acceptance, falsifiers and scope

Acceptance requires a written all-n proof plus independent regression against the actual history compiler and the inspected composition operation. Freeze the operation's source identity; do not replace it by a new endpoint-edit function and call that verification. Test boundary guards, full payload recovery and retained execution history, and reject arbitrary non-line paths.

A legal line input with unequal output records refutes this fixed candidate. An ill-typed composition, incorrect payload or inability of the existing operation to implement the specified edge action is also a candidate failure. Failure does not refute generic WG generation or every common source.

No autonomous generator, unique L/R schedule, carrier selection, rung assignment, metric, time, continuum limit or physical geometry is included. A proof establishes an explicit representation-level specialization, not that the oriented line is derived from the original four-point carrier or a physical source.

## Separate scheduling question

Autonomous scheduling is deferred and is NOT a dependency of this geometric operation-realization route. A future scheduling conjecture must separately name its controller state, law, choice policy, boundary behavior and physical need. Until those are supplied there is no well-defined scheduling proposition to rank or prove.

## Replacement policy

This contract supersedes the vague `native-law-selection` planning task, not the previously proved controlled-WG bridge. The old task is administratively retired, not refuted. The repaired local assembly requires this scoped operation witness plus scale and causal witnesses on compatible source domains; no global source-selection claim follows from it.
