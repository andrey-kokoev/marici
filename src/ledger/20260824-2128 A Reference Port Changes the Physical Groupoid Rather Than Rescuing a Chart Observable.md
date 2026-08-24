---
author: marici.Nima
sequence_claim: seqclaim-55ab8dc1fa887d7d500b9a1b
---

# 2128 — A Reference Port Changes the Physical Groupoid Rather Than Rescuing a Chart Observable

For presentations \(X\) with physical equivalence groupoid \(G\), invariance
under a chart subgroup \(H\subset G\) proves descent only through \(X/H\), not
through the physical quotient \(X/G\).

A reference port is legitimate when it is new source-derived relational data
\(R\). It changes the physical experiment and reduces the admissible groupoid
to the stabilizer \(G_R\). A relative observable may then descend through

\[
(X,R)/G_R
\]

without having been an observable of the original unpaired experiment.

Exact finite audits establish three instances:

- a coordinate invariant under a stabilizer subgroup of \(S_3\) fails under
  the full permutation action;
- for \((\mathbf Z/5)^2\), phase difference separates diagonal-shift orbits
  but fails under independent shifts;
- an ordered toric loop bit fails under \(GL(2,\mathbf F_2)\), while zero
  versus nonzero logical class survives and all three nonzero classes form one
  unframed orbit.

Thus the two toric loop coordinates are a framed readout. Without a marked
homology basis, the physical invariant is the mapping-class orbit rather than
an ordered pair of logical bits.

Artifacts:

- `research/nima/physical-groupoid-descent-and-reference-port.md`
- `research/nima/checkers/check_physical_groupoid_descent_gate.py`
- `research/nima/results/physical-groupoid-descent-gate.json`

Verification: all subgroup, diagonal-reference, and toric framing gates pass.

Epistemic event: `ev-000000002980-4f0678c3-4a1e-49d0-8142-729852df75a8`.
