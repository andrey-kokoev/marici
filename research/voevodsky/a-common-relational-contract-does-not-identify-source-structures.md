# A common relational contract does not identify source structures

## Question

Can marked-path observers, finite source/evidence protocols and polyhedral possibility interfaces share a precise observation/continuation contract without identifying their different source structures?

This is a bounded analytical result for the selected source-contract issue in tree `issue-tree:e184692f4d19e9511f700af2`. It introduces no executable backend. The SCC obligation is **forward realization** of each class into a common relational signature; any subsequent comparison of routes is **route/coherencer compatibility**. No SCC compilation or new checker run is claimed here.

## Contract

Fix a set of sorts I. For each i retain a carrier X_i, an explicitly chosen equality (or a previously justified quotient), and a readout o_i:X_i->Y_i. For each declared operation a:i->j retain a relation R_a subset X_i x X_j. An empty successor fiber means that this operation has no admitted realization at that input. If a protocol observes rejection as a self-loop, encode rejection as a separately labelled relation, not as successful admission.

Composition is relational composition with one SHARED intermediate witness:

    R_b R_a = {(x,z): exists y, R_a(x,y) and R_b(y,z)}.

A separately supplied implementation for a composite operation must prove that its relation equals this composite; the notation alone supplies no such proof. Evidence can restrict a carrier by an admitted predicate. Its truth/admission mechanism is external input, not inferred from the existence of a point satisfying it.

This signature deliberately forgets additional structure. Each instance must retain a side contract declaring its linear or module actions, filtration, topology, coefficient field, proof identity and executable resources where applicable. The forgetful relational presentation is not asserted faithful on any of those structures. Physical-time interpretation is absent unless separately supplied.

A possible-state set K subset X_i updates to R_a[K], optionally intersected with the next observed fiber. This is a semantics for possibilities, not identification of the actual source. History-conditioned interior-cut questions require the corresponding joined relation, not just its endpoint image.

## A precise descent criterion

Let q_i:X_i->Z_i be a proposed compressed representation. Define the exact set of compressed successors

    T_a(x) = {q_j(y): (x,y) in R_a}.

There exists a relation S_a on Z_i x Z_j satisfying

    S_a[q_i(x)] = T_a(x)

for every x if and only if

    q_i(x)=q_i(x') implies T_a(x)=T_a(x').

Necessity follows because the left side depends only on q_i(x). For sufficiency, assign each class the common successor set. By union over x in K,

    q_j(R_a[K]) = S_a[q_i(K)].

Induction gives exact endpoint possibility transport for every finite operation word. If the original current readout factors through q_i, current and subsequent readouts are preserved as well. Nonemptiness of the successor set then preserves admission. Separately labelled rejection must satisfy the same criterion if rejection is observable.

This criterion is stronger than merely defining the projected edge relation by existentially selecting some representative. For example, let x and x' have the same compressed value, but only x admit a. The existential projected edge admits a from the class and fabricates admission for the known input x'. This is a failure of representative independence, not an issue of solver precision.

The theorem concerns endpoint relation semantics. It proves neither equivalence of path-witness spaces nor coherence of proof transports; distinct middle witnesses and higher identities have been forgotten. Those obligations require a proof-relevant extension of the signature.

## Three instantiations and their boundaries

| Class | Carrier and operation | Available justification | Structure not recovered from the relational signature |
| --- | --- | --- | --- |
| Marked-path/filtered source | Typed source elements at fixed corners; admitted contextual linear actions, represented by their graphs | Source-action saturation preserves equality under declared actions; typed source endpoints separately control path admission | Module structure, filtration and extension classes; an ideal element is not automatically an individual execution path |
| Finite source/evidence protocol | Reachable coupled states; separately labelled accepted and rejected transitions | The existing continuation fixed-point partitions check output and successor congruence; the 70-state dependency carrier includes the origin-audit distinction | Acquisition truth, delivery guarantees and actual-origin authentication; source-only observations omit evidence state |
| Polyhedral possibility interface | Entire constrained carriers C as states; public refinement C -> C intersect L^-1(F) | L(C intersect L^-1(F)) = L(C) intersect F proves descent through q(C)=L(C) | Fine fibers, source-point identity, chosen sections and fine-audit re-exposure |

The third row uses sets C as the state carrier, not individual source points. Confusing these two levels would make the purported instantiation incorrect. Original-point witnesses live in an additional incidence relation x in C. A common section selects such witnesses; it is not the state transition itself.

For the first row, the ideal-source observer is not defined on arbitrary protocol histories. The coupling to acquisition and issuance belongs to the second row and must be supplied separately. Consequently this table gives three interpretations of one weak signature, not an equivalence of the three systems.

## Discriminating existing failures

1. The assembled source observation gives equal values on protocol states with and without acquired producer evidence. Their acquire/deliver admissions differ. It fails the criterion on the coupled protocol despite its algebraic source-action closure.
2. Two fine polyhedral histories can have equal public images but different feasibility after the same fine audit. Public-image equality satisfies the criterion for public refinement and fails for that enlarged operation language.
3. Equal composed endpoint relations can have middle fibers of different discrete cardinality; individually bijective middle transports can fail a braid. Relational descent cannot certify either witness equivalence or higher coherence.

These are already established counterexamples, not newly executed experiments. They prevent the common signature from silently promoting observation equality into source identity, operational equivalence under arbitrary extensions, or proof-path equality.

## Disposition

A common **relational semantics** and an exact compressed-successor criterion are available. A common **structure-preserving source theory** is not established. The surviving interpretation of source-relative is: every instance declares its carrier, identity, admitted operations, observations and extra structure before deriving its compression claims.

This resolves the initial definitional alternative in favor of a weak common signature with explicit, noninterchangeable structural enrichments. The selected issue remains open until the table is checked against the actual constructor interfaces and its three realization obligations are recorded in SCC. No new analytic S,A,R,C,G correspondence follows.

The next bounded check is constructor conformance: verify the actual input/output types and admission/rejection conventions in the three existing implementations, and reject any attempted implicit conversion from source points to possibility states or from source observation to evidence state. Do not start another abstract signature layer before that check.

## Evidence and nonverification

Existing premises and counterexamples:

- `the-assembled-source-observer-and-continuation-profiles-are-incomparable.md`
- `actual-continuation-admission-descends-with-the-typed-source-corner.md`
- `source-derived-bounded-dependencies-give-finite-residual-representability.md`
- `sufficient-state-is-relative-to-permitted-continuations.md`
- `commuting-saturation-does-not-imply-equivalent-filling-pencils.md`
- `pairwise-filling-equivalences-can-fail-the-three-direction-braid.md`

The descent theorem above is a direct set-theoretic proof. This packet does not rerun those checkers, authenticate source observations, provide a formal proof-assistant artifact, or certify SCC conformance.
