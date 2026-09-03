# The equivariant zero-trace projection has an exact intertwiner residual

## Question

When does the canonical zero-trace projection preserve reciprocal and prime-label actions, and what fails when the source maps are not equivariant?

## Projection

Let endpoint recovery and harmonic lift satisfy

\[
T:H\to E,
\qquad
P:E\to H,
\qquad
TP=I_E.
\]

Define

\[
A=I_H-PT.
\]

Then

\[
A^2=A,
\qquad
TA=0,
\qquad
A|_{\ker T}=I.
\]

Thus \(A\) is the split projection onto \(\ker T\).

## Equivariance

Let \(U_H\) and \(U_E\) be a reciprocal reflection or one prime-label action on history and endpoint spaces. Define the intertwiner defects

\[
\delta_P=U_HP-PU_E,
\qquad
\delta_T=U_ET-TU_H.
\]

Direct expansion gives the exact residual

\[
U_HA-AU_H
=-\delta_PT-P\delta_T.
\]

Hence the typed identities

\[
U_HP=PU_E,
\qquad
U_ET=TU_H
\]

are sufficient for \(A\) to preserve the action. The formula also localizes any failure: covariance can be lost through the harmonic lift, endpoint recovery, or a cancellation between their defects.

## Labelwise family

For prime and grade projections \(L_\lambda\), the same formula applies with \(U=L_\lambda\). If \(P\) and \(T\) are label diagonal, \(A\) is label diagonal and regularization occurs independently in every source sector. Without those intertwiners, zero-trace subtraction may mix labels even though \(TA=0\).

## Hostile

A projection can be exactly zero-trace while failing reciprocal covariance. Therefore endpoint cancellation alone does not preserve the odd source character. The nonzero commutator above is the exact convention residual; it must not be absorbed into a changed parity assignment.

## Verification

`research/aspect/checkers/check_equivariant_zero_trace_projection.py` checks idempotence, zero trace, equivariance, the exact defect formula, and a failed-intertwiner hostile using rational matrices.

## Disposition

The reciprocal- and label-equivariant zero-trace projection is constructed conditionally on two explicit source intertwiners. The next gate is to audit the actual harmonic lift and endpoint recovery on the theta forcing skew product against these identities before applying the projection to any tail/PV candidate.
