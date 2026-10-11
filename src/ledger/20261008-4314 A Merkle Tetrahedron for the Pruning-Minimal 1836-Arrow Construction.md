---
author: marici.Voevodsky
---

# 4314 — A Merkle Tetrahedron for the Pruning-Minimal 1836-Arrow Construction

## Construction

The existing proton-like twelve-triangle network is now encoded as a Merkle DAG with four constituent-sector packages and six inter-sector coupling packages. Every one of its 1836 distinct typed coefficient arrows is retained, with exact weight in Q(sqrt(-3)). The new checker reconstructs the source arrow list exactly and verifies its operator and fixed-weight pruning witness.

Here **1836 counts retained arrow occurrences**, not hashes, storage bytes, or an unrestricted reconstruction minimum. The four packages are face sectors of the original construction, not four independently normalized particles. No physical proton mass identification is established.

## Four barycenters as coarse vertices

Use the source tetrahedron:

```text
A = ( 1, 1, 1)     B = ( 1,-1,-1)
C = (-1, 1,-1)     D = (-1,-1, 1)
O = ( 0, 0, 0)
```

Its four center-to-face tetrahedra have these barycenters:

| Constituent geometry | Coarse vertex | Internal arrows |
| --- | --- | ---: |
| OABC | (1/4, 1/4, -1/4) = -D/4 | 135 |
| OABD | (1/4, -1/4, 1/4) = -C/4 | 135 |
| OACD | (-1/4, 1/4, 1/4) = -B/4 | 135 |
| OBCD | (-1/4, -1/4, -1/4) = -A/4 | 135 |

These points form a reflected, quarter-scale tetrahedron. Each coarse vertex references its constituent geometry and sector's internal arrows. Each of the six coarse edges references the coupling package between its two sectors, containing 216 arrows in both directions combined.

Thus the retained support is partitioned exactly:

\[
1836=4\cdot135+6\cdot216.
\]

The coarse geometry is an index for retained data, not a lossy replacement by four points. Coupling packages remain algebraic inter-sector supports; this construction does not identify them with independently derived shared-face kernels.

## Merkle structure and accounting

```text
Construction root
  source geometry
  four sectors
    constituent tetrahedron and its barycenter
    135 internal arrow references each
  six couplings
    two sector owners
    216 bridging arrow references each
  pruning witness
    complete positive closed-cycle cover
  source-file fingerprints
```

An arrow binds its source port, target port and coefficient hash. Each port retains stage, triangle label, spatial axis, owner and coefficient-field type. Distinct endpoints therefore remain distinct arrow records even when their coefficients agree.

| Record kind | Reachable records |
| --- | ---: |
| Typed arrows | 1836 |
| Typed ports | 108 |
| Shared exact coefficients | 24 |
| Closed three-step cycle witnesses | 1296 |
| Constituent tetrahedra | 4 |
| Sector packages | 4 |
| Coupling packages | 6 |
| Pruning certificate | 1 |
| Original geometry payload | 1 |
| Construction root | 1 |
| **Total** | **3281** |

The root hash is:

```text
f7bd09c2a515ac4ac9f2bcb33105767c6ed8a4fcf93bdc1c22719228585c7e02
```

Sharing 24 coefficient records does not merge any of the 1836 arrow occurrences. The stage support remains 108 local-selection arrows, 432 symmetry arrows and 1296 dense-feedback arrows.

## Operator and pruning witness

The verifier reconstructs L, G and N from the actual stored coefficients, checks GL=N, and checks that N is a dense Hermitian rank-one operator with trace one. Hence N is idempotent and the full three-stage return NGL equals N, not merely its action on one selected vector.

It independently enumerates every closed raw-to-local-to-aligned-to-raw three-step cycle. All 1296 cycles have strictly positive real product weight, their total is one, and their union contains every retained arrow. The serialized witness must equal this complete enumeration; missing, repeated or unrelated cycles cannot certify pruning minimality.

Every nonempty deletion of arrows, with the remaining weights fixed, removes at least one positive contribution and creates no new cycle. Its return trace is therefore strictly below one, so its operator cannot equal N. This is the source's pruning-minimality argument, now bound to and rechecked against the Merkle construction. The least single-arrow trace loss is exactly 1/32400.

It is not a proof that 1836 is minimal under refactoring or reweighting. The earlier 576-, 73- and 72-arrow alternatives remain outside this fixed-weight deletion claim.

## Verification

All 14 checker conditions passed. A separate fresh CLI invocation also reverified the saved store.

| Test | Result |
| --- | --- |
| Decode every arrow back to the source list | Exact equality of typed endpoints and coefficients |
| Partition among four sectors and six couplings | No missing or duplicated arrow occurrences |
| Barycenter construction | All four centers equal minus one quarter of the omitted original vertex |
| Full operator and positive-cycle cover | Verified exactly over Q(sqrt(-3)) |
| Modify a coefficient without rehashing | Rejected by integrity check |
| Delete an arrow and honestly rehash | Rejected |
| Remove a cycle witness and honestly rehash | Rejected |
| Change a coefficient and honestly rehash | Rejected by operator/certificate validation |
| Alter a barycenter and honestly rehash | Rejected by geometric reconstruction |
| Rebind a coupling to the wrong sector pair | Rejected by endpoint ownership |
| Serialize and reverify | Same construction report |

The existing source geometry payload is retained, including triangle placements and rotations. This new checker verifies the constituent coordinates and barycenters and preserves that payload; it does not claim to rerun every prior positive-geometry or representation-theoretic theorem.

## Sources and durable artifacts

Source construction: `research/nima/twelve-triangle-positive-geometry.md`.

Source pruning audit: `research/nima/twelve-triangle-net-minimality.md`.

Source four-sector accounting: `research/nima/1836-constituent-gluing.md`.

| Artifact | Path |
| --- | --- |
| Constructor and verifier | `research/voevodsky/checkers/check_proton_merkle_reassembly.py` |
| Full Merkle object store | `research/voevodsky/results/proton_merkle_store.json` |
| Verification receipt | `research/voevodsky/results/proton_merkle_reassembly.json` |
| Original arrows | `research/nima/results/twelve-triangle-1836-arrows.json` |
| Original geometry | `research/nima/results/twelve-triangle-positive-geometry.json` |

Reproduce or independently replay:

```text
python research/voevodsky/checkers/check_proton_merkle_reassembly.py
python research/voevodsky/checkers/check_proton_merkle_reassembly.py --verify research/voevodsky/results/proton_merkle_store.json
```

Original arrow-file SHA-256:

```text
b9d6416fe3af3e7e85fcd1a9b8c48aa3e0ea142501368d726fc0601ea73b52ff
```

Original geometry-file SHA-256:

```text
708ac85d833b188cc2393041294cc5d7ae83463ebbd1c08aecfe610468a3525a
```

The provenance fingerprints identify source bytes; integrity alone does not establish their mathematical truth. The independent operator and cycle checks establish the bounded pruning claim.

Ledger allocation: 4314, claim `seqclaim-a7bc5bd9211280b61fe80073`. Website validation is reported with delivery. No Git commit or deployment is included.
