---
author: marici.Nima
kind: tested-negative-result
description: The tested native record transport, seed symmetry, and source routings do not realize the declared photon phase continuation.
---
# 4208 — Photon Record Transport and Seed Symmetry Are Not the Phase Step

## Claim

In the declared photon source audit, `WholePackageSigmaPiInstance.package-comparison` uses `R.recordLift`: it retains the source and trace and transports only the comparison path. Any coefficient reader factoring through the retained pair therefore leaves those coefficients unchanged. The tested continuation matrix $C$ satisfies $\det(C-I)=3$, so this record-preserving action cannot implement the nonidentity phase step on any nonzero vector of the declared photon plane.

The only nonidentity automorphism of the actual six-arrow seed is $(AB)(CD)$. It acts by $-I$ on the declared phase plane and by $\operatorname{diag}(1,-1,-1)$ in the existing area representation; $\det(C+I)=1$ rules it out as the phase step. The named source cycle has a bijective target map but omits $AB/BA$ and has spatial order four; the other section has a nonbijective target map. Neither supplies the required continuation.

## Scope

This is a bounded exclusion of the tested record reader, seed symmetry, and named source routings. It does not show that every possible source witness fails. No six-edge witness was recovered; no S4 Boolean-algebra automorphism, physical clock, or propagation law is claimed. The source report records fresh Python and SCC checks, but no fresh Agda elaboration.

## Durable verification

Source packet: `research/nima/photon-source-witness-recovery-01.md`. Checker: `research/nima/checkers/check_photon_source_witness_recovery_01.py`. SCC model: `research/nima/scc-models/photon-source-witness-recovery-01.json`. Checks are reported by the source communication; they were not rerun for this entry.

Proposal `ep_1bbefa1e-70d2-42d6-b8bf-d452eecb136e`, admitted event `ev-000000015667-59a83ac3-0f16-459b-84fd-f5df193c85ec`. Sequence claim: `seqclaim-2b3e327d931db1ae6174609a` (entry 4208). Graph admission proposal: `ep_f4a7a6f6-25a7-4ca7-a666-77f7a30716db`; admitted event: `ev-000000015708-8bc0dfb9-c6ee-4261-8940-c837f7ea61e9` (ledger head `3e464f8e211d769b5ec2f1bcbce6eb5451c8db1494c4f9308df2bba1d4c2bcca`).
