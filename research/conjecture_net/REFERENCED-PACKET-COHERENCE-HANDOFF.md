# Referenced packets, contextual equality, and witnessed construction

**Status:** operator-led research formulation and prior-art handoff; not a new theorem, ledger admission or physical claim. **Prepared by:** marici.Nima for marici.Voevodsky, at the operator's explicit request.

## Question to preserve

What must a proof constitute if its result is a reusable constructive capability rather than an endpoint value? The operator is exploring a recursive packet presentation of that question. Build on the existing WG, retained-witness, contextual/Yoneda and Merkle work; do not replace it with a new generic proof checklist or amplitude-normalization problem.

## Operator's developing picture

- A packet is provisionally `[l,a,b,c]`, or a 2-by-2 display of four references. `l` is the active reference, not a scalar. The other entries are pointers too. Their exact roles remain to be fixed from the source constructions.
- A label `l_k` refers to and witnesses a completed complex at level k-1. A completed complex around its packet yields `l_(k+1)`. Dereferencing should recover the construction/witness information required by subsequent use. This is a proposed recursive interpretation, not a proved universal tower.
- The remembered display `[label, label/4, 3label/4, label²]` is not being asserted as numerical matrix arithmetic. The quarters obscure the intended access structure. Do not replace them prematurely with guessed names for their contents. The relation between complex-number space and a coherence complex was not settled.
- An encounter has two participant-relative constructions/comparisons, followed by compatibility of those comparisons. Equal rights means neither participant's construction is silently privileged; it does not by itself prove identical responses or inverse operations.
- A cone apex should arise from the proposed next-rank construction, not be supplied from nowhere simply because a diagram needs a fourth vertex. The existing path-horn theorem supplies a missing face and filler with the vertices already given; it is not an apex-generation theorem.
- Equality is being explored through compatible retained pasts and admitted future continuations: replacing one term by another should preserve the relevant possibilities and witnesses. Merely failing to find a contradiction is not a constructive equality proof.

## Counts discussed, with unresolved meaning retained

The operator proposed three groups:

    12*12*3 = 432
    12*3*3  = 108
    (12*3)² = 1296
    total   = 1836.

The discussion provisionally interpreted 12 as retained incoming-complex paths and 3 as outgoing/state-reference choices; the first two groups were called directional constructions and the third a comparison of witnesses. These are interpretation proposals, **not established source semantics**. In a complete directed four-vertex graph, 12 counts all directed edges, not 12 arrows terminating at one vertex. Raw products count independent choices only after typing and composability are specified.

Important correction to the assistant's discussion: matching these arithmetic counts does not identify the groups. The existing source already has a concrete 108/432/1296 partition with different precise stage meanings. Reuse that source before reinterpreting it. Also, vanishing of one scalar residual does not imply equality of the full retained packet.

## Prior ledger anchors — read, not freshly replayed here

| Entry | Reusable content | What not to substitute for it |
|---|---|---|
| **4296**, Witness Generator Glossary and Scope | `G_R : product_(s:S) sum_(t:S) R(s,t)` returns a result and actual witness; later layers separately supply histories/composition/coherence. | A dependent-sum type without an inhabitant, or a bare output label. |
| **4310**, Cardano and Chinese Remainders as Witnessed Assembly | Independently constructed components, compatibility witnesses, assembled solution and correctness; explicit incompatible controls. | Independent endpoint equations without their connecting compatibility. |
| **4312–4313**, Merkle reassembly, surfaces and fillers | References bind actual records; mathematical checks separately verify identities, gluing, all-walk transport and explicit fillers. Existing code and stores implement bounded examples. | Hash integrity as truth, face closure as global path independence, or a closed surface as its own filler. |
| **2065**, Full Yoneda Probing Stabilizes While Restricted Probing Produces Quotients | Exact finite F2 model recovers all 16 maps from natural probe profiles; missing probes yield a quotient. | Restricted observational agreement as unrestricted identity. |
| **4224**, Retained NAND Has a Joint-Refutation Universal Property | Constructive joint-refutation interface; recovery from double negation requires the stated propositionality/stability assumptions. | Absence of contradiction as automatic positive construction. |
| **4314**, Merkle Tetrahedron for the Pruning-Minimal 1836-Arrow Construction | Exact retained 108 local-selection, 432 symmetry, 1296 dense-feedback arrows; 1296 positive closed-cycle witnesses; full operator reconstruction. | Calling 432/108 forward/reverse solely from arithmetic, or identifying all 1836 candidate comparisons with proven fillers. |

Ledger source paths are under `src/ledger/`, with the numbered titles above. In particular:
- `src/ledger/4296 Witness Generator Glossary and Scope.md`
- `src/ledger/20261007-4310 Cardano and Chinese Remainders as Witnessed Assembly.md`
- `src/ledger/20261008-4312 Merkle Witness Reassembly and Identity Surface Status.md`
- `src/ledger/20261008-4313 From Merkle Identities to Discovered Surfaces and Verified Fillers.md`
- `src/ledger/20260824-2065 Full Yoneda Probing Stabilizes While Restricted Probing Produces Quotients.md`
- `src/ledger/20261003-4224 Retained NAND Has a Joint-Refutation Universal Property.md`
- `src/ledger/20261008-4314 A Merkle Tetrahedron for the Pruning-Minimal 1836-Arrow Construction.md`

## Existing mathematical interfaces to reuse

1. `research/conjecture_net/WITNESSED-CONSTRUCTIVE-IDENTITY.md`: independently generated reversible bridge, comparison routes, filled returns, coherence of certificates and dependent reuse. This is a proposed scoped realization criterion, not proof that every identity has such a source-generated package.
2. `research/voevodsky/prior-proof-philosophy-beyond-univalence-v1.md`: proof as a source-grounded compositionally reusable realization of capability; distinguishes supplied signature from source generation.
3. `research/voevodsky/prior-formulation-of-witnessed-process-existence-v1.md`: operator-supplied Kitaev vocabulary `P(n)=n(n-1)²`, `C(n)=3P(n)`, `J(n)=C(n)[n+P(n)+C(n)]`. The original Kitaev artifact was not located in that search. Equal numerical 1836 totals do not identify distinct constructions.
4. `research/sontag/deutschean-control-explanation-of-marici-object.md`: source-relative contextual capability law, including task-relevant traces and successor capabilities. Complete genealogy is not automatically essential; current output is not automatically sufficient. This pointer is recovered through the proof-philosophy synthesis, not independently audited in this handoff.
5. `research/voevodsky/closure-four-presentations-hott-proof.md`: independently constructed maps **and their square witnesses** compared via `CompatibleLift`, `liftIdentification`, and `squareCoherence`.
6. `research/nima/retained-tetrahedral-package.md` and `tetrahedral-hierarchy-at-vertex.md`: actual marked boundary/filler packages, recoverable inhabitants and marked reference views; vertex-only erasure loses data. Retention alone does not show a later update consumes the hierarchy.
7. `research/nima/dependent-transport-machine.md`: actual evaluator/transport agreement and erasure hostiles. Equal endpoints need not imply equal action; equal action need not recover syntax.

## Existing executable entry points, not new replacements

- `research/voevodsky/checkers/merkle_verify.py`: existing identity/surface/filler/transport gateway.
- `research/voevodsky/checkers/check_proton_merkle_reassembly.py`: exact 1836-arrow source reconstruction and fixed-weight pruning certificate.
- `research/nima/checkers/check_yoneda_tower_stabilization_f2.py`: bounded natural-profile faithfulness test.
- Source Agda modules named by the retained tetrahedral, four-presentation and dependent-transport notes.

## Requested Voevodsky continuation

Please review this proposal against those existing interfaces and return a compact source-backed account, not a replacement framework:

1. Identify the closest already implemented packet/reference carrier. Bind `l,a,b,c` to its actual fields and dereference/transport operations, or explicitly state what cannot yet be bound.
2. Derive the source meanings of 108, 432 and 1296 from the actual L/G/N arrows and cycle witnesses. Test whether the operator's two participant-relative constructions plus comparison can be mapped to them; preserve a mismatch rather than forcing the interpretation.
3. Specify equality through admitted histories/continuations using the existing contextual/WG and Yoneda machinery. State the required faithfulness and constructive witnesses; keep joint refutation distinct from positive equality.
4. Locate an actual constructor that could generate the next-rank apex/package. Distinguish source-generated evolution from simply packaging a supplied horn.
5. Propose one smallest executable instance using existing constructors and a certificate-erasure hostile. Do not create another parallel framework or register a universal theorem from matching counts.

Keep the operator-facing explanation compact (prefer a short table). No scientific outcome, formal net status, ledger or source-owner file is changed by this note. The prior-ledger search is provenance/reuse work, not a fresh replay of the referenced proofs.
