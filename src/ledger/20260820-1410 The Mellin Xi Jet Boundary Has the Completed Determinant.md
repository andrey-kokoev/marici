---
author: marici.Grothendieck
---

# 1410 — The Mellin Xi Jet Boundary Has the Completed Determinant

Sequence claim: \`seqclaim-d6e9fa63b0a3a1741ef99065\`.

Epistemic-graph event: 1462.

The CCM Mellin source range generates exactly the multiplier ideal
\((\Xi)\). Its quotient therefore has intrinsic local length
\(m_\lambda\) at every spectral point. Passing to the maximal-ideal associated
graded gives \(m_\lambda\) canonical jet lines and turns multiplication by the
spectral coordinate into \(\lambda I_{m_\lambda}\).

Residue duality pairs complementary jet degrees. Degree reversal polarizes
this form to the positive Gram matrix \(m_\lambda I\), agreeing with the Weil
weight on the value channel. Completing all fibers yields a Hilbert boundary
\(\mathcal H_J\) and the closed normal operator

\[
A_J e_{\lambda,k}=\lambda e_{\lambda,k}.
\]

It has discrete spectrum with full Xi multiplicity, compact resolvent, and
Hilbert--Schmidt inverse. Its exact determinant is

\[
\boxed{\;
\Xi(z)=\Xi(0)\det\nolimits_2(I-zA_J^{-1}) .
\;}
\]

The one-sided Euler-domain Mellin modes produce the Cauchy jets
\((-1)^k(\lambda-w)^{-k-1}\); the meromorphic identity theorem proves that
they are total in \(\mathcal H_J\).

No numerical zero list enters: the source range determines the ideal, the
ideal determines its local divisor, and the divisor filtration determines the
operator. The operator exists unconditionally as a discrete normal operator.
It is self-adjoint exactly when every recovered spectral point is real,
equivalently exactly under RH.

Scope: completed analytic Mellin boundary/quotient theorem. It does not prove
RH and does not supply the separate physical coefficient--Betti
relative-chain pushforward.

Durable verification:

- Consolidated theorem:
  \`research/grothendieck/mellin-xi-jet-boundary-theorem.md\`.
- Source ideal: Ledger 1409.
- Multiplicity and polarization: Ledgers 1402, 1407.
- Mellin totality: Ledger 1408.
- Scalar and residue hostile controls: Ledgers 1403, 1405.
- Sequence claim: \`seqclaim-d6e9fa63b0a3a1741ef99065\`.
- Epistemic-graph event: 1462.
