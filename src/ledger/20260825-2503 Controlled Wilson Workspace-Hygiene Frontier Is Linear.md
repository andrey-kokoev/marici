---
author: marici.Kitaev
sequence_claim: seqclaim-6c7db0e9ca4007bacab2eb07
---

# 2503 — Controlled Wilson Workspace–Hygiene Frontier Is Linear

## Exact Pareto law

Let \(U\) be the total number of work-block episodes in a controlled Wilson
compiler, \(P_{\min}\) its maximum simultaneous gadget demand, and \(P\) the
number of provisioned verified work blocks. Since every work-using gadget
overlaps on the controlled data block, every reuse of a physical work block
requires hygiene.

For \(P_{\min}\le P\le U\), exhaustive assignment gives

\[
B_{\min}=U-P,
\]

where \(B\) counts recover/verify-or-replace events.

For controlled \(H\), work demands are \((1,1,1,2)\), and the complete
frontier is

\[
(P,B)=(2,3),(3,2),(4,1),(5,0).
\]

## Boundary

This is a schedule-independent resource relation, not a physical optimum.
Neither verified-block preparation nor hygiene has an admitted latency,
failure probability, or footprint weight, so no frontier point is preferred.

## Verification

- Packet: `research/kitaev/s3-wilson-workspace-hygiene-pareto-law.md`.
- Checker: `python research/kitaev/checkers/check_s3_wilson_workspace_hygiene_pareto.py`.
- Result SHA256:
  `C2843EF1C7E9CEAFA2B7A37A7498BD605362C8B64FF3C251094A1D00620EA28C`.
- Graph admission: `ev-000000003452-c44dccfc-f807-4ee2-a52b-ca9834298484`.
- Ledger allocation: `seqclaim-6c7db0e9ca4007bacab2eb07`.
