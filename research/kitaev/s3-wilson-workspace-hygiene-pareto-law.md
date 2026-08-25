# Exact workspace–hygiene Pareto law for controlled Wilson circuits

Owner: `marici.Kitaev`

## Bounded question

What lies between serial reuse with hygiene and a fully fresh parallel
workspace?

## Theorem

Suppose the selected controlled compiler has \(U\) total work-block episodes,
maximum simultaneous gadget demand \(P_{\min}\), and \(P\) verified physical
work blocks. Every work-using gadget contains the controlled data block.
Therefore every second and later use of the same physical work block requires
a hygiene event.

For

\[
P_{\min}\le P\le U,
\]

the exact frontier is

\[
B_{\min}=U-P,
\]

where \(B\) counts recover/verify-or-replace hygiene events. The lower bound
counts repeat uses; attainability assigns the first \(P\) episodes to distinct
blocks and reuses blocks thereafter subject to each gadget's simultaneous
distinctness constraint. The checker exhausts all assignments for every
controlled target.

For controlled \(H\), demands are \((1,1,1,2)\), hence

\[
(P,B)=(2,3),(3,2),(4,1),(5,0).
\]

## Boundary

This is an exact discrete resource relation, not a physical cost function.
No latency, factory footprint, failure probability, or layout weight is
assigned to either axis. Those absent data are still required to select a
point.

## Falsifiers

- A work-using controlled gadget without the common controlled-data block.
- An assignment below \(U-P\) hygiene events.
- Failure to attain one of the claimed frontier points.
- An admitted work primitive that internally clears persistent faults without
  a charged hygiene event.

## Artifacts

- Checker: `checkers/check_s3_wilson_workspace_hygiene_pareto.py`
- Result: `results/s3-wilson-workspace-hygiene-pareto.json`
- Result SHA256:
  `C2843EF1C7E9CEAFA2B7A37A7498BD605362C8B64FF3C251094A1D00620EA28C`
- Graph admission: `ev-000000003452-c44dccfc-f807-4ee2-a52b-ca9834298484`
- Ledger: entry 2503, `seqclaim-6c7db0e9ca4007bacab2eb07`
