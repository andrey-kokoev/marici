# Resolution Net v1 — separate experimental calculus

Status: finite immutable reference syntax implemented in `reference.py`; bounded laws and negative tests pass via `python research/voevodsky/resolution-net-v1/check_reference.py`. Results: `results/reference.json`. A tree-port prototype now implements three local substitution schemas in `local_net.py`; run `check_local_net.py` for bounded schedule simulation. See `local-substitution.md` for the five agent signatures and limitations. Python models only finite explicit packages/witnesses, not the arbitrary type-valued Agda signature.

Dedicated issue tree: `issue-tree:eaac890b531559a26d4086ec`.
Initial selected issue: `issue-tree:eaac890b531559a26d4086ec:root:v1`.
Created under the user's explicit request; graph admission records coordination, not mathematical certification. This tree is separate from the existing interaction-net/amplitude tree.

## Current verified checkpoint

See `trust-surface-audit.md` and `results/trust-surface-audit.json`: a fresh 29-stage audit passes, including all nine live Agda modules. The abstract calculus has checked semantic preservation and all-schedule termination; resource-indexed signatures have checked per-token accounting. Concrete wire certificates are finite and still trust Python reification/export. No performance advantage, global authority, or universal concrete port refinement is claimed. Reproduce with `python research/voevodsky/resolution-net-v1/check_trust_surface.py`.

## Decision

Develop resolution-as-primitive as a separate version of interaction-net machinery. Do not replace, migrate, or change the semantics of the existing net implementations. No compatibility is presumed. Compare versions through explicit examples and translations, not shared mutable runtime state.

Semantic reference: `research/nima/coherence-resolution-closure.md` and `research/nima/agda/CoherenceResolutionClosure.agda`. The source was inspected for this design; its formal checks were not rerun here.

## Primitive proposal

There is one semantic operation: witness-bearing resolution of complete packages. Individual domain operations are supplied as typed rule witnesses, not introduced as independent operational primitives. A resolved history can itself serve as a seed. Substitution/flattening composes these layers and retains every rule occurrence and its premise histories.

Initially use exactly the reference signature: seeds, one-premise rules U(p,q), and two-premise rules V(p,q,r). These are constructors/data of the resolution signature, not yet a claim that a single interaction-net agent implements them. Do not hide an arbitrary legacy evaluator behind a Resolve callback.

The implementation experiment must determine how much structural machinery local execution actually needs. One semantic operator does NOT imply one agent symbol, one port, or one rewrite rule. Report these counts separately.

## Laws and boundaries

* Retain complete package data and actual rule witnesses; endpoint equality is not derivation equality.
* Flattening obeys left/right units and associativity.
* Flattening is not assumed injective or an equivalence. Distinct placements of a rule inside/outside a seed may flatten to the same history.
* Reachability truncation, if exposed, is a separate observer, not the execution carrier.
* Comparisons and higher coherence require supplied witnesses; do not manufacture them from successful execution.
* An executable finite representation does not implement all arbitrary type-valued signatures supported by the semantic reference.

## First implementation gate

1. Give a small immutable reference syntax for finite witnessed resolutions and layered seeds.
2. Specify ports, wire ownership, and local rewrite rules implementing substitution. Start with tree-shaped inputs; any graph sharing, duplication or erasure needs an explicit extension rather than implicit Python aliasing.
3. Prove or test semantic simulation against reference flattening, retaining rule identities and premise order.
4. Exercise unit/associativity examples and the noninjective-flattening regression from the source.
5. Enumerate finite competing schedules and compare reconstructed histories. Do not equate schedule agreement with a general confluence theorem.
6. Only then translate a small existing net example and measure actual simplification: agent families, rewrite schemas, invariants, and retained evidence.

The seven-point amplitude comparison may later be a package-level fixture. Its numeric/symbolic certificates are not automatically Agda proof inhabitants, and amplitude computation is not required for the first local-rewrite test.

## Isolation

All new prototype code, tests, and results belong under `research/voevodsky/resolution-net-v1/`. Legacy nets and the Nima Agda reference remain unchanged. No graph transition, publication, or replacement of existing machinery is implied by this experiment.
