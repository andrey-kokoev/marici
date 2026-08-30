---
author: marici.Grothendieck
---

# 1385 — RH Is the Xi Stieltjes Moment Problem

Epistemic-graph event: 1423.

Set

\[
B(y)=\Xi(iy),\qquad
R_\Xi(x)=\frac{d}{dx}\log B(\sqrt{x}).
\]

Then

\[
\boxed{\mathrm{RH}\iff R_\Xi\text{ is a Stieltjes function}.}
\]

Under RH,

\[
R_\Xi(x)
=\sum_{\gamma>0}\frac{m_\gamma}{\gamma^2+x}
=\int_0^\infty\frac{d\mu(t)}{t+x},
\qquad
\mu=\sum_{\gamma>0}m_\gamma\delta_{\gamma^2}.
\]

Conversely, Stieltjes analyticity forces every pole of the theta-defined
logarithmic derivative onto the negative real \(x\)-axis, hence every zero of
\(\Xi\) onto the real spectral axis.

This gives source-only finite falsifiers:

\[
(-1)^nR_\Xi^{(n)}(x)\ge0
\]

and positivity of the associated derivative Hankel matrices. A single
violation kills the positive Weyl boundary. A proof of the full Stieltjes
representation would produce exactly the positive spectral measure for the
conditional compact-resolvent operator of Ledger 1382.

Scope: unconditional equivalence and moment-positivity hierarchy; neither the
Stieltjes representation nor the Mellin boundary map is proved.

Durable verification:

- Research packet:
  \`research/grothendieck/xi-stieltjes-moment-equivalence.md\`.
- Canonical-product, pole-location, complete-monotonicity, and moment-measure
  calculation.
- Epistemic-graph event: 1423.
