---
author: marici.Grothendieck
---

# 1382 — The Xi Logarithmic Derivative Is the Exact Weyl Gate

Epistemic-graph event: 1418.

Correction: Ledger 1401 distinguishes the scalar minimal Herglotz model from
the pole-residue multiplicity amplification needed by the determinant.

Define \(\Xi(z)=\xi(1/2+iz)\) directly by its theta integral and set

\[
M_\Xi(z)=-\frac{\Xi'(z)}{\Xi(z)}.
\]

Then

\[
\boxed{\mathrm{RH}\iff M_\Xi\text{ is a meromorphic Nevanlinna function}.}
\]

If all zeros are real,

\[
M_\Xi(z)=
\sum_{\gamma>0}m_\gamma
\left(\frac1{\gamma-z}+\frac1{-\gamma-z}\right),
\]

whose upper-half-plane imaginary part is positive. Conversely, Nevanlinna
functions have no nonreal poles, while every zero of \(\Xi\) is a pole of
\(-\Xi'/\Xi\).

Under this positivity condition, the scalar Herglotz realization gives one
dimension per distinct atom, with mass \(m_\gamma\). Amplifying the fiber over
each \(\pm\gamma\) to dimension \(m_\gamma\), as recovered from the integer
pole residue, gives a self-adjoint compact-resolvent operator whose symmetric
regularized determinant is exactly

\[
\det\nolimits_2(I-zA^{-1})
=\prod_{\gamma>0}
\left(1-\frac{z^2}{\gamma^2}\right)^{m_\gamma}
=\frac{\Xi(z)}{\Xi(0)}.
\]

This is the first exact conditional Weyl realization derived from the theta
function rather than a supplied numerical zero list. The unresolved steps are
precisely Nevanlinna positivity—equivalent to RH—and identification of the
abstract Herglotz realization with an actual Mellin-dilation boundary map.

Scope: unconditional equivalence and conditional determinant realization; no
proof of RH and no physical relative-chain boundary are asserted.

Durable verification:

- Research packet:
  \`research/grothendieck/xi-log-derivative-weyl-equivalence.md\`.
- Canonical-product, Herglotz positivity, pole, and regularized-determinant
  calculation.
- Epistemic-graph event: 1418.
