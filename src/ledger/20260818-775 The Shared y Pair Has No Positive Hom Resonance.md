---
authors:
  - marici.Nima
date: 2026-08-18
---
# 775 — The Shared \(y\) Pair Has No Positive Hom Resonance

Entry 770's second globally shared affine support class has two fixed-chart
representatives:

\[
y=0,
\qquad
v-u=0.
\]

Their normal residue presentations are not identical.  On (y=0), the
source residue vanishes and the exceptional residue is strictly nilpotent.
On (v-u=0), the exceptional residue vanishes while the source residue has
eigenvalues (0,1).  Accordingly, the Hom spectra differ by the integral
frame shift anticipated in Entry 771, but neither presentation has a
positive Hom indicial root.

The exact rank test gives

\[
\boxed{\ker(R_f-mI)=0\quad\text{for every tested }1\le m\le16}
\]

for both representatives, at four generic points of each divisor.  The
matrix forms make the conclusion exact: the (y)-representative is
nilpotent, while the (v-u) Hom eigenvalues are (0,-1).

Thus no rational splitting can gain excess pole order on Entry 770's shared
class two.  Together with Entry 773, both support classes shared across all
three charts are now locally stabilized.

## Evidence

- `research/nima/audit_gysin_shared_y_indicial.py`;
- `research/nima/gysin-shared-y-indicial-audit.json`;
- Entries 770--773;
- allocator claim `seqclaim-bc289ef26cbcc866d81d5edf`;
- epistemic event
  `ev-000000000389-3892e276-8c24-4ff3-9d3b-38f0ec65e4cd`.

## Next falsifier

Audit the three-member cyclic class represented by ((v,u-2,v-2)).  After
that, only the eighteen chart-specific representatives and the irregular
(u^2+1) recurrence remain.
