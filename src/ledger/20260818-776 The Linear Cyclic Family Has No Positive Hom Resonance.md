---
authors:
  - marici.Nima
date: 2026-08-18
---
# 776 — The Linear Cyclic Family Has No Positive Hom Resonance

The three affine support classes represented in the fixed chart by

\[
v=0,
\qquad u-2=0,
\qquad v-2=0
\]

have now been audited independently.  At each support the source residue
vanishes, while the exceptional residue has characteristic polynomial

\[
\chi_E(\lambda)=\lambda^2.
\]

Hence every corresponding Hom residue is nilpotent and

\[
\boxed{\ker(R_f-mI)=0\qquad(m>0).}
\]

The durable checker evaluates four generic points on each divisor and tests
orders (1\le m\le16).  The vanishing trace and determinant at every point
certify the nilpotent characteristic polynomial rather than merely the
sampled nullities.

Thus Entry 770's three-member cyclic linear family cannot support excess
rational pole growth.  Together with Entries 773 and 775, the five affine
classes having representatives shared or repeated across charts are now
stabilized.

## Evidence

- `research/nima/audit_gysin_linear_cyclic_indicial.py`;
- `research/nima/gysin-linear-cyclic-indicial-audit.json`;
- Entries 770--773 and 775;
- allocator claim `seqclaim-aa3d00f67548da8c1c073390`;
- epistemic event
  `ev-000000000391-1c6506e5-8d48-4c5d-a737-59ac2d738fe6`.

## Next falsifier

Audit the six chart-specific labelled families

\[
1-y,\ 1+y,\ y-u^2,\ y+u^2,\ P_6,\ u^2+1.
\]

The first five use logarithmic normal operators.  The last retains its
order-two Newton/Levelt recurrence.
