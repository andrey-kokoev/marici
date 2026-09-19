# The jet--Volterra incidence is prime diagonal on the faithful valuation tensor carrier

Let

\[
\mathcal L=\ell^2\{(p,k)\},\qquad
\mathcal K_{\rm jet}=\mathcal L\widehat\otimes\mathcal X_{\rm jet},
\]

where `X_jet` is the augmented boundary-plus-bulk theta-jet graph.  Retain the
source idempotents

\[
P_{p,k}=|e_{p,k}\rangle\langle e_{p,k}|\otimes I.
\]

For the source-derived local column `b_(p,k)(t)`, define the assembled forward
incidence by the orthogonal direct sum

\[
\widetilde B_{\rm jet}
=\bigoplus_{p,k} b_{p,k}.
\]

Equivalently, each translated cut lift is placed between its own source
idempotents. Therefore

\[
P_{q,\ell}\widetilde B_{\rm jet}P_{p,k}=0
\quad\text{for }(q,\ell)\ne(p,k).
\]

This is exact carrier-level label preservation, not an inference from scalar
Mellin orthogonality.  Fourier acts as `I_L tensor F`, so saturation also
commutes with every `P_(p,k)`.  Adams transport obeys

\[
A_2P_{p,k}=P_{p,2k}A_2.
\]

Together with the cutoff-uniform local estimate and
`|a_(p,k)|<=2^(-1/2)`, the direct-sum jet incidence is bounded in the weighted
arithmetic norm.

This closes local prime/grade diagonality and the all-label incidence assembly.
It does not exclude separately authorized cross-prime Green kernels. Such
kernels are different assembly arrows and must be applied before the terminal
scalar augmentation; they cannot be hidden inside `B_jet`.
