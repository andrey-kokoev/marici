# Full detector history binding into the shared conditional carrier

## Disposition

Constructed a conditional packet for `instrument-common-source-binding` and history-coherence consumers. Their programme nodes remain open: carrier/dynamics source selection and physical preparation/clock/authority prerequisites are not supplied.

This packet covers the **entire frozen sharp-input detector history family**, not only the earlier total-N<=1 routed cavity overlap. It preserves the same Fock/memory carrier ID without silently claiming that every preparation can pass through every instrument composition.

Contract: `contracts/physics-instrument-history-binding.v1.json`.
Checker: `checkers/check_physics_instrument_history_binding.py`.

## Source-to-carrier map

For a detector input word `(n0,n1,n2)` of length at most three, each n_k is zero or one. In the ten-mode carrier, prepare a product occupation vector with n_k photons in mode `p_k=2+3k`, all other modes vacuum. These indices are fresh **detector-input roles in this presentation**, not a claim that this preparation is the cavity's transmitted output. Tensor with the same initial classical R/D memory mixture.

The full input word is prepared open-loop in labelled future-bin modes. Its total number can be three, unlike the routed single-excitation overlap. This is a conditional representation of independent sharp optical preparations, not an authorization to physically prepare them in advance or an equivalence of adaptive preparation policies.

At bin k apply each separately labelled local source Kraus operator at p_k, tensored with identity on spectators. The operated optical mode is destroyed for both click and no-click outcomes. All later optical inputs stay untouched, and detector memory is retained.

## Full source-operation square

For fixed sharp input n at the current bin, a classical unnormalized memory state `(R,D)` evolves as

```
C: (0, eta*n*R)
N: ((1-eta*n)*R+gamma*D, (1-gamma)*D).
```

The embedded source Kraus operators produce exactly these populations. Their output optical mode is vacuum; every future-bin product factor is unchanged. Summing independently labelled Kraus branches implements the same mixed memory state, without identifying their environment labels.

This proves the local preparation/instrument comparison on both memory basis states, hence on every classical mixture by linearity. Induction on k shows that the source's repeated optical preparation route and the preprepared Fock route have the same **unnormalized memory posterior and complete word probability at every prefix**. It includes zero-probability prefixes without attempting to normalize them.

The unused future-bin factors are retained in the carrier. The source sequential model does not observe them before their preparation event; this is an explicit open-loop product extension, not a claim that the source had those extra physical records already.

## Records, composition and resources

A segment has an explicit start/end bin and retains source ID, bin, port, outcome, occurrence ID and memory-retention policy. Segment composition is allowed only when bins match. It concatenates records without merging equal states or dropping N outcomes. Empty segments are identities; concatenation is associative.

Each segment's instrument map is the ordered composition of the local CP maps. Evaluating the first segment and then the next at its correct start bin gives the same labelled branch list and posterior as the concatenated word. Record associativity therefore agrees with state-map associativity, rather than only with a common numerical endpoint.

Every occupied input bin consumes its photon regardless of click/no-click. At a prefix of probability mass L, remaining optical occupation is `L*sum(future n_k)` and the current-prefix-weighted consumed ledger is `L*sum(past n_k)`. Their sum is `L*sum(initial n_k)`. Summing over the complete outcome tree gives the unconditional photon budget. Readiness is a distinct population ledger; no physical energy or clock units are inferred.

## An assembly obstruction that must not be hidden

The detector-only product domain is not invariant under arbitrary cavity maps. Prepare one photon in returning mode 0 and one in input mode 1, then apply the first passive cavity round. The resulting occupation state has probability

`23328/390625`

in the transmitted port's **two-photon sector**. The finite detector's n_port<=1 domain is violated. The checker rejects the attempted no-click instrument rather than projecting away that mass.

Thus the shared carrier permits both target embeddings, but their admissible operation domains are not interchangeable. To compose a cavity round with a detector event, establish n_port<=1 on the transformed support. The earlier total-N<=1 overlap is sufficient and stays unchanged; this packet does not extend that overlap to all three-photon preparations.

This is a genuine common-source assembly guard, not a physical measurement limitation. It remains relevant even with exact mathematical parameters.

## Verification

Fresh rational tests compare all 252 source histories over lengths one to three and three initial readiness fixtures with the Fock embedding. They verify 684 prefix memory squares, 936 segment splits, record associativity and 684 photon-resource balances. The full classical-mixture/all-word statement follows from the local linearity and induction arguments above.

History controls reject dropped no-click, memory reset, duplicate occurrences, foreign source and mismatched bin attachments. The passive-mixing two-photon guard supplies an explicit nonzero failed-domain witness. Inputs are hash-checked before and after execution.

```
python research/nima/checkers/check_physics_instrument_history_binding.py
python research/aspect/scc/scc.py check physics-programme-v18
```

Physical instrument binding, native-law selection and same-witness physical sector transport remain open. Measurement work remains parked.
