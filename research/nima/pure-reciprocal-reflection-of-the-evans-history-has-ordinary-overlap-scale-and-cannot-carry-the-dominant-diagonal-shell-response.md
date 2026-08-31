# Pure reciprocal reflection of the Evans history has ordinary-overlap scale and cannot carry the dominant diagonal shell response

## Question

Can the already constructed unitary reflection port supply the dominant
\((1,1)\) late-shell reciprocal response?

## Claim boundary

No, if the reciprocal shell value is only the reflected-history overlap. Evenness
of the completed theta forcing identifies that overlap with the ordinary shell
at parameter \(-z\), up to orientation sign. It therefore has ordinary
\(\Lambda^{-2}\) scale, not endpoint \(\Lambda^{-1}\) scale. A complete
diagonal reciprocal response requires an additional endpoint or constitutive
component with source-fixed normalization.

## Exact reflection identity

The completed forcing is even:

\[
 \Phi(-q)=\Phi(q).
\]

The stable histories are

\[
 u_-(q;z)=\int_{-\infty}^q e^{z(q-r)}\Phi(r)\,dr,
\]

and

\[
 u_+(q;z)=-\int_q^\infty e^{z(q-r)}\Phi(r)\,dr.
\]

For \(q>0\), substitute \(s=-r\) to obtain

\[
 u_-(-q;z)
 =\int_q^\infty e^{z(s-q)}\Phi(s)\,ds
 =-u_+(q;-z).
\]

At a Xi zero, the glued Evans state uses these two stable branches, so its
reflected positive-shell value obeys the same relation.

## Reflected overlap

Let

\[
 I_{a,b}^{(0)}(z)
 =\int_a^b\Phi(q)u_+(q;z)\,dq.
\]

A pure reflected-history pairing is

\[
 I_{a,b}^{({\rm refl})}(z)
 =\int_a^b\Phi(q)u_-(-q;z)\,dq.
\]

Therefore

\[
 I_{a,b}^{({\rm refl})}(z)
 =-I_{a,b}^{(0)}(-z).
\]

Any reciprocal orientation sign can only multiply this exact identity by a
fixed unit; it cannot change its asymptotic order.

## Late-shell scale

For \(a\to\infty\),

\[
 I_{a,b}^{(0)}(-z)
 =-\frac{\Phi(a)^2}{2\Lambda(a)^2}
 \left(1+O(\Lambda(a)^{-1})\right).
\]

Hence

\[
 I_{a,b}^{({\rm refl})}(z)
 =O\!\left(\frac{\Phi(a)^2}{\Lambda(a)^2}\right).
\]

The diagonal response required after endpoint totalization has scale

\[
 \frac{\Phi(a)^2}{\Lambda(a)}.
\]

Their ratio tends to zero.

## Consequence for the reciprocal block

Unitary reflection proves domain stability and norm preservation, but a shell
value defined only by reflected overlap cannot cancel the dominant endpoint
term. The full reciprocal block must contain a separately derived component,
such as:

- transported endpoint response;
- an arithmetic constitutive loading acting on the wall--jump return;
- a diagonal source current from the polarized Green identity.

Its coefficient and sign must be fixed before Xi zeros are inspected.

## Relation to the two-by-two return

The existing reciprocal shift realization constructs

\[
 G_{\rm wj}(z)
 =\begin{pmatrix}a(z)&b(z)\\b(z)&a(z)\end{pmatrix},
\]

but explicitly leaves the arithmetic constitutive matrix
\(C_{\rm arith}(z)\) open. The missing diagonal shell strength can only enter
through that source law or an equivalent retained endpoint attachment; it is
not supplied by reflection itself.

## Multiplicity

Parameter differentiation preserves

\[
 \partial_z^jI^{({\rm refl})}(z)
 =(-1)^{j+1}\partial_z^jI^{(0)}(-z).
\]

Every reflected jet remains one inverse decay rate smaller than the required
endpoint jet. The mismatch persists throughout the multiplicity chain.

## Disposition

Pure reciprocal reflection is eliminated as the dominant diagonal response
mechanism. Candidate one now requires the source-derived diagonal constitutive
or endpoint component of the reciprocal block. That component remains absent
from corrected SCC v2. No RH conclusion is authorized.
