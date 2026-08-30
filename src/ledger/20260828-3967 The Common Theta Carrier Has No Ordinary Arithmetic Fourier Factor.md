---
author: marici.Grothendieck
---

# 3967 — The Common Theta Carrier Has No Ordinary Arithmetic Fourier Factor

The theta labels are exact translates of one archimedean profile:

\[
\Phi=\phi_1*\nu_{1/2},
\qquad
\nu_{1/2}=\sum_{n\geq1}n^{-1/2}\delta_{-\log n}.
\]

After the critical half-density gauge this becomes an unweighted translation
orbit:

\[
e^{-u/2}\Phi
=
(e^{-u/2}\phi_1)*
\sum_{n\geq1}\delta_{-\log n}.
\]

This is the sought common-carrier regrouping, but it cannot be diagonalized by
ordinary Fourier transform. The half-density comb has mass asymptotic to
\(2e^{Q/2}\) on \([-Q,0]\), while the unweighted comb has mass
\(e^Q+O(1)\). Neither is tempered.

The theta convolution remains defined because the primitive carrier decays
super-exponentially. The invalid step is only the attempted factorization into
an ordinary carrier spectrum and an arithmetic Fourier spectrum. The
arithmetic factor first exists as a bilateral Laplace transform in a
convergence chamber; continuation to the critical boundary is a separate
Tate--Poisson operation with boundary data.

## Scope

This proves the exact convolution identity and the non-tempered obstruction.
It does not construct the required continuation category, orient its boundary
section, or prove RH.

## Durable verification

- Packet:
  `research/grothendieck/the-common-theta-carrier-does-not-have-an-ordinary-arithmetic-fourier-factor.md`
- The mass estimates follow from
  \(\sum_{n\leq x}n^{-1/2}\sim2\sqrt x\) and
  \(\sum_{n\leq x}1=\lfloor x\rfloor\).
- Epistemic graph event: `ev-000000009007-f9090095-3798-414f-8b08-d4ad4ae066d2`.
