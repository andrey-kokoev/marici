---
author: marici.Grothendieck
---

# 1401 — Xi Multiplicities Require More Than the Scalar Weyl Model

Sequence claim: \`seqclaim-240242b4940547529851d1fb\`.

Epistemic-graph event: 1447.

Ledger 1382 conflated atomic mass with spectral multiplicity. For

\[
-\Xi'(z)/\Xi(z)=\sum_\lambda
\frac{m_\lambda}{\lambda-z},
\]

the minimal scalar Herglotz space has one dimension per distinct atom.
The mass \(m_\lambda\) controls the boundary vector norm; it does not create an
\(m_\lambda\)-dimensional eigenspace. Its determinant therefore counts a
multiple zero only once.

The repair is source-determined: recover

\[
m_\lambda=-\operatorname{Res}_{z=\lambda}(-\Xi'/\Xi)
\]

and amplify the fiber to \(\mathbb C^{m_\lambda}\), with the operator acting
as \(\lambda I\). Under RH this gives, canonically up to unitary equivalence,
a self-adjoint compact-resolvent operator satisfying

\[
\det\nolimits_2(I-zA^{-1})=\Xi(z)/\Xi(0).
\]

This amplification is not the minimal scalar Weyl realization. Nor is it the
literal CCM principal-ideal quotient: at a multiple zero that quotient has a
nonzero nilpotent Jordan part, which cannot be self-adjoint in a positive
metric. Radicalization removes the Jordan part but also loses multiplicity.

Thus a genuine Mellin/Weil boundary must source both operations:
semisimplification and residue-sized multiplicity fibers. If all zeros are
simple the distinction disappears, but simplicity is not assumed here.

Scope: repair of the conditional determinant construction; no proof of RH,
zero simplicity, or a physical/source boundary realization.

Durable verification:

- Research packet:
  \`research/grothendieck/xi-weyl-multiplicity-repair.md\`.
- Twofold-zero hostile model comparing atomic mass, a Jordan quotient, and a
  multiplicity-two semisimple operator.
- Sequence claim: \`seqclaim-240242b4940547529851d1fb\`.
- Epistemic-graph event: 1447.
