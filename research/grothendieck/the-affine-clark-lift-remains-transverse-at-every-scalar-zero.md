# The Affine Clark Lift Remains Transverse at Every Scalar Zero

## Scope correction

The first version identified the one-sided endpoint \(G_s(0)\) with the
completed scalar readout. That is not the correct RH typing. The completed
readout is assembled from reciprocal endpoint ports, and its zero can be a
cross-port cancellation while neither endpoint vanishes. The corrected
statement below works on that actual zero domain.

## The missing channel is visible at the completed endpoint

Let

\[
G_s(q)=e^{-sq}\int_q^\infty f(v)e^{sv}\,dv,
\qquad
F(s)=G_s(0).
\]

Let \(U\) and \(V\) denote the reciprocal endpoint amplitudes in their common
completed source frame. The completed scalar readout has the form

\[
X=U+V.
\]

Its zero condition is \(V=-U\), not \(U=V=0\). Retain the common affine
forcing value \(f_0=f(0)\). The two forced endpoint features then contain

\[
Y_U=U+f_0,
\qquad
Y_V=V+f_0.
\]

On the completed zero domain, the parallelogram law gives

\[
|Y_U|^2+|Y_V|^2
=|U+f_0|^2+|-U+f_0|^2
=2|U|^2+2|f_0|^2.
\]

For the completed theta source, \(f_0>0\). Consequently the reciprocal affine
endpoint packet is strictly nonzero at every completed scalar zero. Any Clark
derivative squares add further nonnegative terms, but are not needed for this
endpoint transversality.

## Interpretation

A scalar zero is not loss of meaning in the full source object. It is loss of
the grade-zero transform projection. The affine forcing coordinate retains a
canonical source witness precisely where the homogeneous value--tangent
carrier can vanish.

This is the capability absent from both failed repairs:

1. orthogonal reciprocal doubling merely duplicates squared invariants;
2. homogeneous Clark shearing changes the frame but leaves a negative radial
   direction;
3. affine Clark lifting adds the independent source coordinate \(f(0)\), so
   the lifted state cannot disappear with the scalar readout.

The result also sharpens the geometric-algebra picture. The scalar projection
\(U+V\) can vanish while the augmented reciprocal vector

\[
\widetilde V=(U+f_0,V+f_0)
\]

remains nonzero. Meaning was not destroyed in the source; it was erased by the
augmentation that added the two ports and forgot their common forcing channel.

## Scope boundary

Endpoint transversality is not RH. It proves strictness only after the two
reciprocal ports have been placed in a common source frame with the same
forcing value. Establishing that common-frame identification is part of the
Fourier--Tate sewing theorem. The remaining global conservation statement must
connect this lifted state to the coefficient
\(2\operatorname{Re}(s-1/2)\) without a typed residual or escape at infinity.

The next exact target is therefore not another positivity search. It is to
pull the doubled Green current back to this affine endpoint lift and determine
whether every non-bulk term is an incidence boundary of the retained source
ports.
