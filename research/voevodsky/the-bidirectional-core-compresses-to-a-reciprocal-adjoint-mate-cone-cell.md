# The bidirectional core compresses to a reciprocal adjoint-mate cone cell

## Oriented systems

Let

\[
D_+:X_+\to Y_+,
\qquad
D_-:X_-\to Y_-
\]

be the two oriented forward operators. Let

\[
R_X:X_+\to X_-,
\qquad
R_Y:Y_+\to Y_-
\]

be reciprocal unitary involutions.

The forward reciprocal cell is

\[
R_YD_+
=
D_-R_X.
\]

The backward Green maps are

\[
D_+^*:Y_+\to X_+,
\qquad
D_-^*:Y_-\to X_-.
\]

Taking the adjoint mate of the forward cell gives

\[
R_XD_+^*
=
D_-^*R_Y.
\]

Thus the backward square is determined as the mate of the forward square once the reciprocal transports are unitary and the adjoints are independently admitted.

## Cone compression

Each orientation has a two-term cone

\[
\mathcal C_+
=
[ X_+\to Y_+ ],
\qquad
\mathcal C_-
=
[ X_-\to Y_- ].
\]

The reciprocal cone map is

\[
R_{\mathcal C}
=
R_Y\oplus R_X[1].
\]

The forward square is exactly the condition that this is a chain map:

\[
R_{\mathcal C}
\delta_+
=
\delta_-R_{\mathcal C}.
\]

Since the reciprocal maps are involutions,

\[
R_{\mathcal C}^2=I.
\]

## Hodge enhancement

The cone Hodge operators are

\[
Q_+
=
\delta_++
\delta_+^*,
\]

\[
Q_-
=
\delta_-+
\delta_-^*.
\]

Forward coherence together with its adjoint mate gives

\[
R_{\mathcal C}Q_+
=
Q_-R_{\mathcal C}.
\]

Thus reciprocal transport preserves the complete fixed/possible package: forward compression, backward response, cone defect, and Hodge energy.

## Exact finite fixture

Checker:

`research/voevodsky/checkers/check_bidirectional_adjoint_mate_cone_cell.py`

Result:

`research/voevodsky/results/bidirectional-adjoint-mate-cone-cell.json`

The checker verifies exactly:

1. the forward reciprocal square;
2. the backward adjoint square;
3. the induced reciprocal cone chain map;
4. involutivity of the cone transport;
5. covariance of the Hodge operator.

## Analytic instantiation

For the theta system, the intended assignments are:

- \(X_\pm\): oriented source/history graph carriers;
- \(Y_\pm\): oriented source--endpoint port carriers;
- \(D_\pm\): upper and lower chart source-to-output operators;
- \(R_X\): history reflection with source orientation;
- \(R_Y\): reciprocal exchange of Clark ports;
- \(D_\pm^*\): independently constructed Green return maps.

The local oriented resolvent charts already supply candidate \(D_\pm\), and seam reflection supplies candidate reciprocal maps. The remaining analytic obligation is equality of the independently constructed Green returns with the adjoint mates on one common closed domain.

## Higher compression

This bidirectional cell is the atomic input to the octahedral tower. Composable bidirectional cells can be cone-compressed while preserving their reciprocal Hodge covariance.

The next coherence level compares two orders:

1. compose oriented systems, then form the reciprocal cone;
2. form reciprocal cones, then compose their correspondences.

Their comparison is the completion-level Beck--Chevalley cell.

## Disposition

The fixed data and compatible possibilities are now packaged symmetrically in both directions. Their reciprocal exchange, cone compression, and Hodge enhancement form one exact finite coherence cell and one precise analytic constructor contract.
