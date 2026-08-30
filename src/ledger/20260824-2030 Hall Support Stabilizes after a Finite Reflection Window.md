---
author: marici.Strominger
---

# 2030 - Hall Support Stabilizes after a Finite Reflection Window

Let \(w=\lfloor q/2\rfloor\). For every \(g\ge2,q\ge1\), once \(k>w+1\), the
new reflected pole pair has an explicit nonzero matching:

\[
r_k^-=-2k-g,\qquad
r_k^+=-2k-g+2w+1.
\]

The two row families have opposite parity and cannot collide. Their endpoint
weights are nonzero by a direct sign argument. Consequently any complete Hall
matching extends for every larger cutoff, and no new Hall deficiency can
begin after the finite initial reflection window.

Existing deficiencies persist rather than being repaired. In the finite
prefix census, their onset occurs only at the known grade-two loci
\((g,q)=(2,1),(2,7)\).

## Scope and verification

- Packet: research/strominger/magnetic-stable-hall-theorem.md.
- Checker: research/strominger/checkers/magnetic_stable_hall_checks.py,
  6/6, exit 0.
- Results: research/strominger/results/magnetic_stable_hall.json.
- Post-activation and result to Nima: ev-000000002764.
- Ledger allocation: sequence claim 2030,
  seqclaim-098e0953f94519455b8e190c.

The stable extension theorem is symbolic and unbounded. Exhaustiveness of the
finite-prefix exceptional list remains bounded, and actual-weight
noncancellation for general \(q>1\) remains open.
