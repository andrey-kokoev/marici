# The global radial--odd packet is assembled, but C34 has no source-derived arithmetic loading map

## Question

Does the completed relative `C34` feature already select the arithmetic
coefficient that couples finite radial loading to the archimedean odd packet?

## Claim boundary

No. The retained radial packet has a convergent source-derived assembly, but
the `C34` feature is typed on a Mellin observer space and contains no map from
prime-labelled arithmetic loading into that observer space.

For each prime, the retained packet

\[
X_p=(-\rho_p(0),E_{p,+},W_{p,+};
+\rho_p(0),E_{p,-},W_{p,-})
\]

admits the oriented codiagonal

\[
C_pX_p=E_{p,+}+E_{p,-}
-\frac12(W_{p,+}+W_{p,-}).
\]

Two coefficient families satisfy the required prime majorants:

\[
\omega_p^{\rm mix}(\sigma)=\frac12p^{-3/2-\sigma}
\]

and the source-derived theta coefficient

\[
c_p=2(\log p)\sum_{k\ge1}p^{-k/2}\Phi'(k\log p).
\]

Their convergence proves two admissible assemblies; it does not identify their
roles.

The relative feature instead has observer representation

\[
\rho(g)=M_{m_g}
\]

and signed cross form determined by `Q^T-Q^0`. Its category-level construction
does not specify a coefficient `omega_p`, a prime return structure, or a map
from the retained arithmetic packet to a Mellin observer `g`.

## First missing typed object

The comparison requires a source-derived loading map of the form

\[
\Lambda_{\rm ar}:D_{\rm ret}^{\rm ar}
\longrightarrow E_{C34}
\]

or an equivalent common-source span, satisfying

\[
\rho(\Lambda_{\rm ar}X^{\rm ar})=M_{m_{X^{\rm ar}}}
\]

with declared primitive, square, endpoint, and archimedean coordinates. No
such map is present in the `C34` datum.

## Disposition

The global radial--odd assembly and its convergence are closed. Canonical
loading selection is blocked at `Lambda_ar`; choosing `omega_mix`, `c_p`, or a
fitted combination from the desired bulk equality would reverse the analytical
form-finding order. Defer this branch until a source formula for `Lambda_ar` is
materialized.