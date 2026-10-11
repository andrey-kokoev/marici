---
author: marici.Voevodsky
---

# 4312 — Merkle Witness Reassembly and Identity Surface Status

## Position

Following ledger 4311, the initial CRT, Cardano and cube-boundary Merkle experiments now have six bounded extensions: global transport, polynomial proof input, gluing discovery, explicit cone fillers, scoped witness substitution and engineering support. They distinguish content integrity, local mathematical correctness, attachment transport, surface closure and a supplied filler. None establishes arbitrary dependent higher coherence or a general tetrahedral reconstruction theorem.

The working coherence tetrahedron has conceptual vertices **construction, witness, transport, and closure**. This is an organizing model, not an identified mathematical tetrahedron. Merkle hashes bind exact records and dependencies; they do not prove the identities in those records.

## Completed features

| Feature | Status | Demonstrated scope and evidence |
| --- | --- | --- |
| Typed decomposition and reassembly | Done for CRT | Lossless reconstruction; constructor sharing and modular normalization preserve four roots and four witness constraints. |
| Grammar-relative minimization | Done for CRT forward map only | Five constructors necessary and sufficient in the declared affine grammar. No whole-graph or unrestricted-language minimum. |
| Content-addressed constructions | Done in three prototypes | Domain-separated SHA-256 records bind types, ordered dependencies, boundaries and witness references. |
| Structural deduplication | Done for CRT | The 54-operation-occurrence expansion and 20-operation shared graph have the same term-content root; normalization has 16 distinct operations and a different root. Local occurrence names and duplicated storage are not retained in that term identity. |
| Content identity versus equivalence | Done in bounded languages | Separate certificates bind different hashes and invoke exact mathematical verification. Equal hashes are not the criterion for all mathematical equivalence. |
| Witness retention | Done in fixtures | Missing predicates, wrong attachments and false mathematics are distinguished from hash corruption. |
| Exact algebraic-number normalization | Done for one irreducible cubic | For x cubed minus three x minus one, complex paired contributions are represented in a degree-six cyclotomic field; outputs normalize in its degree-three real subfield. Three roots and six ordered endpoint presentations are retained. |
| Explicit attachment transport | Done for Cardano swap and scoped polynomial proofs | Cardano certificates check endpoint swap and square-root sign transport. Iteration 5 adds structural substitution of proof DAGs with explicit assumption discharge; identity and composed-route coherence tested. Neither equal values nor equal propositions silently identify distinct proof histories. |
| Identity-labelled polygon input | Prototype done | Supplied incidence structures remain supported; iteration 3 additionally accepts independent faces with only local corner indices, affine labels and polynomial identity proof roots. |
| Gluing discovery | Done in a restricted bounded grammar (iteration 3) | Searches inverse-labelled, orientation-reversing perfect port matchings; reconstructs and verifies a connected simple-edge regular surface. Reports unique labelled gluing, ambiguity, exhaustive failure within grammar, or search-limit exhaustion. |
| Closed-surface recognition | Done for the finite polygon grammar | Edge incidence and circular vertex links are checked separately; connectedness, orientability, Euler characteristic and connected orientable genus are reported. |
| Face identity checking | Done for affine rational maps | Exact coefficient arithmetic checks every face composite, hence equality for all rational inputs rather than sampled points. |
| Typed expression/proof input | Done for commutative Q-polynomials (iteration 2) | External Merkle terms and equality proofs; ring normalization, reflexivity, symmetry, transitivity, congruence and scoped assumptions. Conditional proofs cannot masquerade as unconditional theorems. Six cube faces replay through an exact endpoint-binding adapter. |
| Global path independence | Done for affine rational graph transport (iteration 1) | Spanning-forest potentials and every non-tree edge decide all graph walks; explicit signed loop witnesses retained. Cube passes; flat torus has nontrivial holonomy despite all face identities holding. Not a general symbolic or minimal fundamental-group presentation algorithm. |
| Explicit higher filler | Done in a thin affine cone model (iteration 4) | Twelve oriented tetrahedra fill the triangulated cube sphere; 18 interior triangles cancel. Original boundary restrictions and all edge/triangle transports verified. Also fills the sphere discovered in iteration 3. Not arbitrary proof-relevant higher coherence. |
| Portable saved evidence | Done | JSON object stores reverify. The surface checker also accepts an external store via `--verify FILE`; filler construction and verification have a separate CLI. |
| Unified verification gateway | Done for six schema families (iteration 6) | Dispatches polynomial proofs, surfaces, unglued faces, gluing certificates, fillers and witness transport; mathematical policies remain explicit. Legacy CRT/Cardano schemas not migrated. |
| Incremental semantic verification | Done for trusted-session polynomial caches (iteration 6) | Context- and implementation-bound cached terms/proofs; full current-object hashing and dependency closure always rechecked. One-leaf edit reuses unaffected subproofs. |
| Defensive input and measurements | Prototype done (iteration 6) | Strict gateway JSON reader, resource bounds and coefficient-growth guard. Five-run local benchmark records cold, warm and edited verification without asserting portable speed ratios. |

## Test inventory

Counts are those reported by the individual checker receipts, not a measure of independent mathematical theorems.

| Suite or control | Status | Result |
| --- | --- | --- |
| CRT edge reassembly | 9 checks passed | All four outputs and witnesses preserved over all 225 environments; witness deletion, type substitution and a wrong coefficient rejected. |
| CRT Merkle reassembly | 17 checks passed | Sharing preserves the content root; normalization changes it; a separate finite equivalence certificate verifies. Hash tampering, rehashed witness loss, attachment swaps and false mathematics rejected. |
| Cardano Merkle branches | 24 checks passed | Exact field identities, injective real embedding, all nine basis products, three distinct roots, six branch presentations and explicit reversible endpoint transport verified. |
| Cardano incompatible cube-root choice | Passed negative control | Individual cube equations remain true while uv=1 and the assembled cubic equation fail. Honest rehashing does not conceal the failure. |
| Identity-surface suite | 14 checks passed; rerun after iteration 1 | Cube boundary has 8 vertices, 12 edges, 6 faces, Euler characteristic 2, genus 0, circular vertex links and valid face identities. |
| Torus/global transport | 19 checks passed (iteration 1) | Closed genus-one 3-by-3 mesh has valid face identities but loop translations +3 and +6. All reported graph-basis loops independently replay; trivial torus, cube, noncommuting labels, frame changes, 4-by-4 mesh and CLI acceptance policies checked. |
| Polynomial expression/proof kernel | 27 checks passed (iteration 2) | Nonlinear multivariable identities, structural proof rules, assumption tracking, six face attachments, serialization and external CLI policy tested. False or unsupported identities and valid-but-unrelated face proofs rejected. |
| Gluing discovery | 20 checks passed (iteration 3) | Six independent faces reconstruct a sphere in 13 search nodes. Missing-face ports, ambiguous square attachments, search limits, local proof validity, certificate binding and external CLI replay checked. |
| Cone filler | 22 checks passed (iteration 4) | Explicit cells, boundary restriction, cancellation and flat interior transport verified. Missing/reversed tetrahedra, bad maps/types, rebound boundary, open surface and torus-as-cone-ball rejected. |
| Scoped witness transport | 21 checks passed (iteration 5) | Nonlinear proof family transported through changing contexts; used assumptions retained or explicitly discharged. Direct and two-stage substitutions produce the same final proof root; invalid and unrelated discharge proofs rejected. |
| Engineering gateway/cache | 26 checks passed (iteration 6) | Six dispatcher families, policy separation, integrity on cache hits, context/implementation invalidation, eviction, hostile JSON, coefficient growth and CLI replay tested. All ten suites freshly pass: 199 reported checks. |
| Delete a cube face | Passed negative control | Four unmatched boundary edges; surface is open despite surviving identities remaining valid. |
| Duplicate a face occurrence | Passed negative control | Four edges have three incident faces; not a surface. |
| Pinch two spheres at one vertex | Passed negative control | Every edge has two faces, but the common vertex link is disconnected; edge pairing alone is insufficient. |
| Change an edge map and rehash | Passed negative control | Topology remains a closed sphere while two face identities fail. |
| Reverse one face | Passed distinction test | Surface remains orientable; supplied orientations cease to be consistent. |
| Substitute a port type | Passed negative control | Topology unchanged; typed coherence fails. |
| Corrupt a hash or delete a witness object | Passed negative controls | Surface verifier rejects the corrupt or incomplete store. |
| Fresh external-store surface verification | Passed | Separate `--verify` invocation reproduced the successful topology and identity report. |

## Outstanding features and discriminating tests

Outstanding means not delivered by these experiments; it is not a claim that the feature is impossible or already scheduled.

| Feature | Current limit | Outstanding test or implementation |
| --- | --- | --- |
| Arbitrary identity input | External typed Q-polynomial expressions and scoped equality proofs now supported; surface edges remain affine | Extend to other types/domains, partial operations, noncommutativity and dependent/quantified propositions with explicit verification rules. Unsupported identities currently fail closed. Polynomial proof input is not yet a general reversible-map surface language. |
| Broader gluing discovery | Bounded exact inverse-label matching now implemented; unique, ambiguous, unmatched and search-limit cases tested | Extend to self-pairings, coordinate-change witnesses, nonorientable identifications and broader quotient grammars; distinguish labelled ambiguity from equivalence modulo isomorphism. |
| General CW and singular attaching maps | Surface verifier requires simple polygon boundaries | Add explicit occurrence/attachment maps and test repeated vertices, nonregular cells and self-identifications. |
| Broad topology coverage | Sphere and periodic torus fixtures now checked | Add higher-genus, nonorientable, disconnected and multiple-boundary fixtures with known invariants. |
| Broader global holonomy | All-walk criterion implemented for affine rational transport; torus falsifier complete | Extend equality/transport rules beyond this language; optionally simplify the graph cycle basis using face relations. Do not confuse local flatness with trivial holonomy. |
| Broader higher coherence and fillers | Explicit simplicial cone 3-ball with affine transport now supplied and checked | Extend beyond thin equality to proof-relevant/dependent higher witnesses; compare distinct fillings and support non-cone fillings. A closed boundary alone remains insufficient input to filler verification. |
| General dependent witness transport | Scoped Q-polynomial proof substitution now implemented, beyond Cardano; assumption transport and composed routes checked | Extend to arbitrary dependent types and proof-relevant higher comparison cells. Structural substitution is not general identity elimination or automatic proof-irrelevance. |
| Parameter-dependent radical branches | One fixed cubic | Vary coefficients around a discriminant loop and test monodromy; do not assume globally single-valued branch labels. |
| Automatic normal-form discovery | Rules and Cardano field model are hand supplied | Discover candidate rewrites/embeddings and require independently checkable certificates. |
| General minimization | Only the CRT forward grammar has a minimum proof | Declare a broader grammar and cost model, then provide lower bounds; node-count reduction alone is insufficient. |
| Broader verification caching | Trusted-process polynomial cache implemented and tested; no disk-cache trust | Extend safely to other artifact families, incremental storage/transfer and cross-process persistence; integrity checks currently remain linear in store size. |
| Unified reusable implementation | Six-family gateway implemented; specialized constructors remain separate | Migrate legacy CRT/Cardano stores if needed, stabilize interfaces and share more schema machinery without conflating policies. |
| Production input hardening | Strict gateway JSON and bounded checks implemented | Add comprehensive fuzzing and work/memory budgets across all algorithms; audit legacy API paths and deployment trust boundaries. |
| Authenticated origin and distribution | Hashes provide integrity relative to an expected root | Add signatures/trust policy if needed; test root substitution, key revocation and cross-process exchange. |
| Broader performance and storage claims | Local 128-leaf polynomial benchmark: cold 16.34 ms, warm 5.53 ms, one-leaf edit 6.14 ms (five-run medians) | Broaden workloads/platforms and measure transfer/storage costs; no portable speed guarantee. Retaining branch evidence means field-dimension reduction is not automatically total-storage reduction. |

## Durable evidence and reproduction

| Experiment | Packet | Checker | Receipt / object store |
| --- | --- | --- | --- |
| CRT source | `research/voevodsky/crt-edge-reassembly.md` | `research/voevodsky/checkers/check_crt_edge_reassembly.py` | `research/voevodsky/results/crt_edge_reassembly.json` |
| CRT Merkle | `research/voevodsky/crt-merkle-reassembly.md` | `research/voevodsky/checkers/check_crt_merkle_reassembly.py` | `research/voevodsky/results/crt_merkle_reassembly.json`; `research/voevodsky/results/crt_merkle_store.json` |
| Cardano | `research/voevodsky/cardano-merkle-branches.md` | `research/voevodsky/checkers/check_cardano_merkle_branches.py` | `research/voevodsky/results/cardano_merkle_branches.json`; `research/voevodsky/results/cardano_merkle_store.json` |
| Identity surface | `research/voevodsky/merkle-identity-surface.md` | `research/voevodsky/checkers/check_merkle_identity_surface.py` | `research/voevodsky/results/merkle_identity_surface.json`; `research/voevodsky/results/merkle_identity_surface_store.json` |

Iteration 1 adds `research/voevodsky/merkle-torus-holonomy.md`, checker `research/voevodsky/checkers/check_merkle_torus_holonomy.py`, receipt `research/voevodsky/results/merkle_torus_holonomy.json`, and store `research/voevodsky/results/merkle_torus_store.json`. The shared surface CLI accepts `--require-path-independence`; applied to the flat nontrivial torus, it intentionally exits 1.

Iteration 2 adds `research/voevodsky/merkle-identity-kernel.md`, reusable kernel `research/voevodsky/checkers/merkle_identity_kernel.py`, regression checker `research/voevodsky/checkers/check_merkle_identity_kernel.py`, receipt `research/voevodsky/results/merkle_identity_kernel.json`, and standalone polynomial/conditional/face-bridge proof stores. The kernel accepts `FILE.json --require-unconditional`.

Iteration 3 adds `research/voevodsky/merkle-gluing-search.md`, search/certificate module `research/voevodsky/checkers/merkle_gluing_search.py`, tests `research/voevodsky/checkers/check_merkle_gluing_search.py`, and receipt `research/voevodsky/results/merkle_gluing_search.json`. Independent-face input, discovered cube and ambiguous-gluing stores are linked in the packet.

Iteration 4 adds `research/voevodsky/merkle-cone-filler.md`, constructor/verifier `research/voevodsky/checkers/merkle_cone_filler.py`, tests `research/voevodsky/checkers/check_merkle_cone_filler.py`, receipt `research/voevodsky/results/merkle_cone_filler.json`, and explicit cube/discovered-sphere filler stores. The model and its limits are recorded in the packet.

Iteration 5 adds `research/voevodsky/merkle-witness-transport.md`, constructor/verifier `research/voevodsky/checkers/merkle_witness_transport.py`, tests `research/voevodsky/checkers/check_merkle_witness_transport.py`, receipt `research/voevodsky/results/merkle_witness_transport.json`, and transport/composition proof stores.

Iteration 6 adds `research/voevodsky/merkle-engineering.md`, gateway `research/voevodsky/checkers/merkle_verify.py`, tests/benchmark `research/voevodsky/checkers/check_merkle_engineering.py`, and receipt `research/voevodsky/results/merkle_engineering.json`. The gateway accepts a versioned artifact file, with optional `--require-global` or `--require-unconditional` policies.

Run the listed Python checkers, with CRT source preceding CRT Merkle. The standalone surface replay is:

```text
python research/voevodsky/checkers/check_merkle_identity_surface.py --verify research/voevodsky/results/merkle_identity_surface_store.json
```

Prior graph admissions: CRT glossary/source `ep_ed69cd6a-4db0-45b2-bac7-a48d76c73492`; CRT Merkle `ep_4b20963e-8923-44b5-8714-7485f09767a6`; Cardano `ep_fa754c21-e746-4379-a228-788ccca97fc7`. These are provenance admissions, not independent mathematical certification.

Ledger allocation: 4312, claim `seqclaim-28561e04faf2224cfb131e2f`. Website validation is reported with delivery. No Git commit or deployment is included.
