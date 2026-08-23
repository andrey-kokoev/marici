---
author: marici.Strominger
---
# 1920 — The A1z Correspondence: the Unique Partnerless Channel Carries the Unique Odd Determinant Line

## Question

The rung-3 cocycle arc (ledger 1915, gate K5) certified that the rational
square-root gate fails on exactly one of the six rung-3 channels,
\(A^{(1)}_z\), whose determinant line is \(uX\) with odd
\(\operatorname{val}_z=1\) — and that this is precisely the channel whose
electric partner vanishes identically, \(A^{(1)}_E=0\) (ledger 1912, R1.3).
Coincidence or correspondence — and if correspondence, what is the
mechanism?

## The verdict

Correspondence, with mechanism fully exhibited — 29/29 checks, exit 0
(`research/strominger/checkers/a1z_jacobian_correspondence_checks.py`,
packet `research/strominger/a1z-jacobian-correspondence.md`).

**The operator is a pure square (J1).** The five grounded \(S^{(2)-}\)
channels are exactly \(V^2/\mathrm{den}\) for the single leg vector field
\(V=c_{z_k}\partial_{z_k}+c_{E_k}\partial_{E_k}\) over
\(\mathrm{den}=-4E_k\omega^2(z-z_k)(\bar z-\bar z_k)/((1+u)(1+z_k\bar z_k))\).

**Partner-vanishing is a Hamiltonian collapse (J2).** \(A^{(1)}_E=0\)
\(\Leftrightarrow\) \(V(c_{E_k})=0\) \(\Leftrightarrow\) \(V\) is
Hamiltonian with respect to \(c_{E_k}\), with explicit multiplier
\(\mu=(z-z_k)(1+z_k\bar z_k)/(1+z\bar z_k)\):
\(c_{z_k}=\mu\,\partial_{E_k}c_{E_k}\), \(c_{E_k}=-\mu\,\partial_{z_k}c_{E_k}\).

**The surviving channel is a Jacobian (J3).**
\(V(c_{z_k})=\mu\,\mathrm{Jac}(c_{z_k},c_{E_k})\) — an area form, the only
channel not built as a symmetric product of soft-factor lines.

**Square-norm bookkeeping (J4).** The determinant line is the
multiplicative norm character \(D(f)=Q(\alpha f)/Q(f)\),
\(Q(f)=f\sigma(f)\). Every product-side input is square-protected:
\(D(c_{z_k})=X^2\), \(D(c_{E_k})=1\), \(D(\mathrm{den})=X^2\),
\(D(\mu)=X^2\). Evenness of the five product channels is forced, not
observed case by case.

**The Jacobian carries the unique odd character (J5).**

\[
D\big(\mathrm{Jac}(c_{z_k},c_{E_k})\big)=uX,
\qquad
\det(A^{(1)}_z)=\frac{D(\mu)D(\mathrm{Jac})}{D(\mathrm{den})}=uX .
\]

The K5 gate failure is located exactly in the Jacobian of the soft map
\((z_k,E_k)\mapsto(c_{z_k},c_{E_k})\).

**Pinning identities (J6, exact).**
\(\det(A^{(1)}_z)^2=u^2\det(A^{(2)}_z)\det(A_{zE})\) and
\(F_2(A^{(1)}_z)^2=-\bar z^2 F_2(A_{zE})F_2(A^{(2)}_z)\): the odd line is
pinned by the even lines up to \(u^2\).

## Consequence

The partner-vanishing does not numerically force oddness; it removes the
square protection. When \(A^{(1)}_E\) vanishes the surviving magnetic
first-order channel is necessarily a Jacobian — the unique object whose
norm character is not automatically a square — and the soft map's
Jacobian is computed to carry \(uX\), odd. Second cross-arc instance of an
odd \(u\)-object born at a structural locus rather than in the datum:
\(u^7\) at the readout projection grade (ledger 1917), \(uX\) at the
soft-map Jacobian (here). The datum itself is even throughout.
