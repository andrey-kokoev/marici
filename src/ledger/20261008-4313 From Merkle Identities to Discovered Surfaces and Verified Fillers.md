---
author: marici.Voevodsky
---

# 4313 — From Merkle Identities to Discovered Surfaces and Verified Fillers

## Disposition

The six-iteration continuation of ledger 4312 delivers bounded executable prototypes for identity input, gluing discovery, global transport, explicit fillers, witness transport and verification infrastructure. All ten associated suites passed, reporting 199 checks. These are computational checks within declared mathematical models, not 199 independent theorems or a general higher-coherence engine.

The central distinction is now executable: **valid local identities, a closed surface, trivial global transport, and an explicitly supplied filler are different obligations**. Content hashes bind each construction and its witnesses; dedicated verifiers check the mathematics.

## Six iterations

| Iteration | Delivered | Decisive result | Checks |
| --- | --- | --- | ---: |
| 1 — Global transport | Spanning-forest cycle witnesses for exact affine rational maps | A closed torus has valid face identities but loop translations +3 and +6. The cube passes the stronger all-walk path-independence criterion. | 19 |
| 2 — Identity input | Typed multivariable Q-polynomial expressions and equality-proof DAGs | Ring normalization and structural proof rules verify nonlinear identities. Used assumptions remain explicit; unrelated valid theorems cannot replace face witnesses. | 27 |
| 3 — Gluing discovery | Bounded matching of independently witnessed local face boundaries | Six separated faces reconstruct a sphere with 8 vertices, 12 edges and 6 faces in 13 search nodes. Ambiguity, unmatched ports and budget exhaustion receive distinct reports. | 20 |
| 4 — Explicit filler | Merkle-addressed simplicial cone with affine transport | Twelve tetrahedra fill the triangulated cube sphere; 18 interior triangles cancel. Boundary restrictions and all triangle transport identities verify. | 22 |
| 5 — Witness transport | Structural proof substitution with explicit assumption discharge | Sequential and direct substitutions yield the same final judgment hash. Required assumptions cannot silently disappear; distinct proof histories remain distinct. | 21 |
| 6 — Engineering | Six-schema gateway, trusted-session proof cache, strict input checks and benchmark | Cache hits cannot hide missing dependencies, modified objects or changed assumptions. Policies for local coherence, global independence and unconditional proof stay separate. | 26 |

The six iterations contribute 135 checks. The preceding cube-surface suite contributes 14, and the CRT/Cardano suites contribute 50: 199 across ten suites in total.

## What the construction now does

The expression kernel accepts declared variables, canonical rational constants, addition, multiplication and negation. Equality proofs use ring normalization, reflexivity, symmetry, transitivity, congruence and explicitly scoped assumptions. It does not execute arbitrary code or assume unsupported mathematical identities.

The gluing input consists of separate face cycles, local corners, affine map labels and polynomial proof roots. No shared vertex IDs or edge pairing is supplied. Candidate edges must carry inverse affine labels, and endpoint identification reverses orientation. A gluing certificate binds source packet, complete pairing and output surface. Reconstruction verifies the quotient independently.

The unique cube fixture deliberately uses distinct potential differences as labels. Its uniqueness is therefore a constrained positive result, not a general solution to ambiguous assembly. Uniqueness refers to labelled port pairings, not homeomorphism classes. A negative result is qualified by the search grammar and budget.

The filler is explicitly typed `thin-affine-Q-cone-v1`. It retains the original boundary root, face subdivision, oriented tetrahedra and interior transport. Its 9 vertices, 26 edges, 30 triangles and 12 tetrahedra have Euler characteristic one. Ball topology follows from the verified cone-over-sphere construction, not from Euler characteristic alone. A torus is rejected by this ball constructor even when its transport is trivial.

The transport module moves a proof family such as x*x=y*y under h:x=y to substituted contexts. Every used source assumption needs a target proof with the substituted endpoints. Legitimate discharge to an unconditional equality is allowed when an explicit proof is supplied. Equality of endpoint values alone does not identify proof histories.

## Negative controls that matter

| Tempting shortcut | Counterexample or rejection |
| --- | --- |
| Every face commutes, therefore every loop is trivial | Flat torus with nontrivial generating-loop transport |
| Every edge has two faces, therefore it is a surface | Two spheres pinched at one vertex have a disconnected vertex link |
| A valid identity can fill any face | Exact endpoint binding rejects an unrelated valid polynomial theorem |
| Failure to find a gluing proves none exists | Search-limit exhaustion is distinct from exhaustive failure within the grammar |
| A closed boundary already supplies its filler | The filler verifier requires explicit cells, boundary restriction and interior transports |
| A torus can be coned to an ordinary ball | The apex link is not a sphere; this constructor refuses it |
| Substitution may silently drop hypotheses | Every used source assumption requires a checked target discharge proof |
| Equal propositions imply identical proof histories | A symmetry-twice alternative remains a distinct proof DAG |
| A cached success makes current premises unnecessary | Missing or altered dependencies are rejected before reuse |

## Measured engineering result

A balanced proof DAG combines 128 independently witnessed leaves, with 1,026 supplied objects and 266,483 bytes in the measured JSON encoding. Five local runs gave:

| Verification mode | Median | Semantic cache misses |
| --- | ---: | ---: |
| Cold | 16.34 ms | 1,024 |
| Unchanged warm | 5.53 ms | 0 |
| One edited leaf | 6.14 ms | 26 |

The edited run reused 24 cached terms/subproofs. All runs still hash the supplied objects and validate the current dependency closure. These timings are local observations, not portable speed guarantees. The cache is bounded, context- and implementation-bound, and trusted only within a running process; no remote or disk cache is accepted as evidence.

The gateway rejects duplicate JSON keys, nonfinite and floating-point scalars, excessive nesting or object sizes, and unsupported schemas or policies. Polynomial coefficient growth is bounded. This is defensive prototype work, not a production security audit.

## Remaining scope

| Area | Still outstanding |
| --- | --- |
| Mathematical language | Other coefficient domains, noncommutativity, partial functions, quantified and dependent propositions |
| Gluing | Coordinate-change witnesses, self-pairings, nonorientable identification, parallel/singular cells and uniqueness modulo isomorphism |
| Topology | Broader positive and negative fixtures beyond the current sphere/torus grammar |
| Fillers | Non-cone fillings, comparison between fillings and proof-relevant higher coherence |
| Witness transport | General dependent-type transport and automatic discovery of discharge proofs |
| Infrastructure | Caching for other artifact families, authenticated roots, cross-process persistence, full fuzzing and comprehensive resource budgets |
| Performance | Broader workloads/platforms, storage/transfer benchmarks and scaling analysis |

There is no unrestricted tetrahedral reconstruction theorem, arbitrary-identity solver, canonical minimal filling, or production-readiness claim.

## Evidence and entry point

| Area | Research packet | Test receipt under `research/voevodsky/results/` |
| --- | --- | --- |
| Global transport | `research/voevodsky/merkle-torus-holonomy.md` | `merkle_torus_holonomy.json` |
| Identity kernel | `research/voevodsky/merkle-identity-kernel.md` | `merkle_identity_kernel.json` |
| Gluing | `research/voevodsky/merkle-gluing-search.md` | `merkle_gluing_search.json` |
| Filler | `research/voevodsky/merkle-cone-filler.md` | `merkle_cone_filler.json` |
| Transport | `research/voevodsky/merkle-witness-transport.md` | `merkle_witness_transport.json` |
| Engineering | `research/voevodsky/merkle-engineering.md` | `merkle_engineering.json` |

The packets contain constructor APIs, reproduction commands, serialized artifacts and scope qualifications. The unified gateway is `research/voevodsky/checkers/merkle_verify.py`. For example:

```text
python research/voevodsky/checkers/merkle_verify.py research/voevodsky/results/merkle_cube_cone_filler.json
python research/voevodsky/checkers/merkle_verify.py research/voevodsky/results/merkle_engineering_proof.json --require-unconditional
```

Ledger 4312 remains the detailed feature/status inventory; this entry records the six-iteration outcome. Allocation: 4313, claim `seqclaim-6c1480415fbfdd3a5f1c5704`. Website validation is reported with delivery. No Git commit or deployment is included.
