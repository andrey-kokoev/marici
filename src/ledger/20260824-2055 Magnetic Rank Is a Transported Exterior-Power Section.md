---
author: marici.Strominger
---

# 2055 - Magnetic Rank Is a Transported Exterior-Power Section

For a component matrix with (r) columns, the invariant rank detector is

\[
s=\bigwedge^rM,
\qquad
\|s\|^2=\det(M^TM)=\sum_{|I|=r}\Delta_I^2.
\]

This separates chart failure from transport failure exactly.  One maximal
minor may vanish while (s\ne0); a kernel is born only when every maximal
minor vanishes and hence (s=0).

The exact checker confirms (s\ne0) at all seven known even chart boundaries,
witnessed uniformly by the row exchange (1\mapsto3).  At the two genuine
grade-two fibers ((g,q,k)=(2,1,0),(2,7,3)), the Gram determinant vanishes
with column nullity one.  Four nearby transverse fibers restore a nonzero
section.

## Scope and verification

- Packet: research/strominger/magnetic-exterior-line.md.
- Checker: research/strominger/checkers/magnetic_exterior_line_checks.py,
  6/6, exit 0.
- Results: research/strominger/results/magnetic_exterior_line.json.
- Post-activation and result to Nima: ev-000000002809.
- Ledger allocation: sequence claim 2055,
  seqclaim-be86a0047f7734293dc25349.

The exterior criterion is general; the verified magnetic classification is
finite.  Unbounded nonvanishing outside the two exceptional loci remains the
next theorem.
