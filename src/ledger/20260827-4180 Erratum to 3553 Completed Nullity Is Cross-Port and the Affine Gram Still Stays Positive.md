# 4180 — Erratum to 3553: Completed Nullity Is Cross-Port and the Affine Gram Still Stays Positive

Ledger 3553 incorrectly identified the one-sided endpoint \(G_s(0)\) with the
completed scalar readout. The RH-relevant readout is assembled from reciprocal
ports:

\[
X=U+V.
\]

Thus \(X=0\) means \(V=-U\), not that either port vanishes. The corrected
affine endpoint theorem is

\[
|U+f_0|^2+|V+f_0|^2
=2|U|^2+2|f_0|^2>0
\]

on the completed zero domain, provided Fourier--Tate sewing places both ports
in the same source frame with common \(f_0=f(0)>0\).

The main interpretation survives in stronger, correctly typed form: a scalar
zero is loss of the augmentation projection, while the reciprocal
source-forced packet remains nonzero. The newly explicit gate is the common
source-frame mate.

Corrected checker result: `18/18`.