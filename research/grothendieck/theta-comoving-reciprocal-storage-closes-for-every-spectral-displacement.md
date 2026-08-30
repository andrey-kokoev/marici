# Theta comoving reciprocal storage closes for every spectral displacement

## Smallest doubled carrier

Fix (L>0) and define the remaining source-tail energy

\[
 T(q)=\int_q^L|f(v)|^2\,dv.
\]

On the two reciprocal Mellin channels, use the generator

\[
 A_\delta=\begin{pmatrix}-\delta&0\\0&\delta\end{pmatrix}.
\]

Define the positive endpoint storage and seam observation row by

\[
 P_\delta(q)
 =T(q)
 \begin{pmatrix}e^{2\delta q}&0\\0&e^{-2\delta q}\end{pmatrix},
\]

\[
 C_\delta(q)
 =|f(q)|
 \begin{pmatrix}e^{\delta q}&0\\0&e^{-\delta q}\end{pmatrix}.
\]

The Clark quadrature port tensors this carrier with an identity factor. It
does not change the calculation.

## Exact infinitesimal residual

Since

\[
 T'(q)=-|f(q)|^2,
\]

direct differentiation gives

\[
 P_\delta'
 +A_\delta^*P_\delta
 +P_\delta A_\delta
 +C_\delta^*C_\delta
 =0.
\]

The spectral derivative terms in (P_\delta') cancel exactly against the
reciprocal dilation generator. The remaining loss of tail storage is exactly
the positive seam observation density.

Thus Nima's dynamic residual vanishes with no additional boundary supply on
this minimal tail--seam carrier:

\[
 \mathcal R_\delta(q)=0
\]

for every real (\delta), every cutoff, and every square-integrable source.

## Meaning of the cosh growth

Packet 202 measured both reciprocal components in one fixed Euclidean frame
and obtained

\[
 2\cosh(2\delta q)\|f\|_2^2.
\]

The identity above measures storage in the co-moving positive metric naturally
transported by the reciprocal dilation. In that metric, the same tail--seam
exchange is lossless for every (\delta).

Therefore fixed-frame cosh growth is real, but it is not by itself an
invariant obstruction to admissibility. It records the mismatch between a
fixed frame and nonunitary reciprocal transport. A proof cannot declare the
fixed Euclidean frame physical merely because its bounded trajectories select
the critical seam.

## Relation to the endpoint shear

The storage and seam sensor above act on the reciprocal forcing port. They do
not couple to the endpoint displacement coordinate (Y) whose shear
coefficient is (F_L(s)). Hence their exact residual contains no information
about transmission zeros.

At a silent endpoint shear, the positive path Gramian remains nonzero and the
co-moving storage identity still closes. This is consistent with Kitaev's
identity-loop theorem: positive path energy is a separate cocycle, not an
endpoint-storage function.

## Revised source target

The primitive, prime-square, archimedean, or mixed-seam incidence must create
a source-derived coupling between the reciprocal forcing port and the
endpoint displacement port. Without such an off-diagonal incidence, the
dynamic storage law is universal and non-orienting.

The smallest next residual should therefore be computed on the enlarged state

\[
 (Y,c_+,c_-)
\]

or its Clark-quadrature realification, with every off-diagonal storage and
supply entry derived before scalar compression. A diagonal direct sum of the
shear and reciprocal Gramian cannot constrain their coincidence.

## Falsifier

Any claim that fixed-frame cosh growth alone forbids off-seam states is
falsified by the positive co-moving storage identity above. A proposed
RH-bearing dynamic residual fails if its endpoint-displacement and reciprocal
forcing blocks remain uncoupled, because then it decomposes into two
independent universal identities.

## Scope

This proves exact dynamic storage closure for the minimal reciprocal
tail--seam carrier at every spectral displacement. It corrects the invariant
interpretation of packet 202. It does not derive the required off-diagonal
arithmetic incidence, orient transmission zeros, or prove RH.
