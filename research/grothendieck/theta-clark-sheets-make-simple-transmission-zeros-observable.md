# Theta Clark sheets make simple transmission zeros observable

## Single endpoint port

On one finite interval, the integrating-factor state is the pair ((Y,c)).
The endpoint output has row

\[
 O_F=\begin{pmatrix}1&F\end{pmatrix},
\]

where (F) is the interval transfer coefficient. Its Gramian is

\[
 W_F=O_F^*O_F
 =\begin{pmatrix}
 1&F\\
 \overline F&|F|^2
 \end{pmatrix}.
\]

This Gramian has rank one. At a transmission zero, it becomes

\[
 W_0=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

The source-input direction is then unobservable through the single endpoint
port. The off-diagonal incidence derived from the ordinary shear collapses
precisely when it is needed.

## Clark-differentiated ports

The source-native Clark sheets supply

\[
 H_+=F+iaF',
 \qquad
 H_-=F-iaF',
\]

with nonzero real (a). Retain both endpoint rows

\[
 O_+=\begin{pmatrix}1&H_+\end{pmatrix},
 \qquad
 O_-=\begin{pmatrix}1&H_-\end{pmatrix}.
\]

Their joint Gramian is

\[
 W_a=O_+^*O_++O_-^*O_-
 =2\begin{pmatrix}
 1&F\\
 \overline F&|F|^2+a^2|F'|^2
 \end{pmatrix}.
\]

Therefore

\[
 \det W_a=4a^2|F'|^2.
\]

At a simple transmission zero, (F=0) and (F'\ne0), so (W_a) is positive
definite. The full state remains observable even though the undifferentiated
scalar channel is silent.

## Minimality and meaning

The two sheets are not an arbitrary extra sensor. Their opposite first-jet
terms arise from the source sheet involution (a\mapsto-a). The common scalar
component retains (F), while the antisymmetric component retains (F').

This realizes the proposed distinction exactly:

- a scalar zero is loss of the grade-zero transmission meaning;
- the full two-sheet relationship survives through its transverse first jet;
  and
- a simple zero is a rank transfer between scalar and antisymmetric channels,
  not disappearance of the source state.

## Multiplicity boundary

If

\[
 F=F'=0,
\]

the two-sheet Gramian is again singular. Higher-multiplicity zeros require
higher source-authorized jet channels. One may not assume simplicity of the
Riemann zeros to close this gap.

The natural extension is a jet observability tower whose first nonzero
derivative restores rank. Its source authority and completion stability must
be established independently.

## Relation to RH orientation

Clark observability proves that scalar silence does not erase the full state.
It does not constrain where silence can occur. The same Gramian formula holds
for hostile sources with off-seam simple zeros.

The remaining orientation theorem must couple this now-faithful jet Gramian
to the typed dynamic boundary supply. The relevant state is no longer merely
((Y,c_+,c_-)), but the common endpoint coordinate together with the symmetric
and antisymmetric Clark source channels.

## Falsifier

The simple-zero observability claim fails if the Clark sheet coefficients are
not exactly opposite, if their common endpoint rows do not inhabit one source
module, or if (F'\ne0) while the displayed determinant vanishes. Any RH claim
from this Gramian alone is falsified by a hostile source with an off-seam
simple zero.

## Scope

This proves that the source-native two-sheet observation is faithful at every
simple transmission zero. It does not prove zero simplicity, completion-
stable observability, a boundary-supply orientation law, or RH.
