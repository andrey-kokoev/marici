# Three-Operator Gram-Loop Purity Selector

## Question

Does the minimal odd incidence cycle remove WP816's operator-sign ambiguity,
and does that structure pass Aspect's germ tester?

## Exact ternary carrier

For three independently marked real operators, normalize the diagonal residues
to one and take a common off-diagonal magnitude \(r\geq0\). Independent sign
changes of the operators act by \(R\mapsto SRS\), with diagonal
\(S_{ii}=\pm1\). An individual cross residue is not invariant, but

\[
\chi=\operatorname{sgn}(R_{12}R_{23}R_{31})
\]

is invariant: every sign change reverses exactly two incident edges. The two
sign classes have representatives

\[
R_+(r)=\begin{pmatrix}1&r&r\\r&1&r\\r&r&1\end{pmatrix},
\qquad
R_-(r)=\begin{pmatrix}1&r&-r\\r&1&r\\-r&r&1\end{pmatrix}.
\]

Their spectra are respectively

\[
\{1+2r,1-r,1-r\},
\qquad
\{1-2r,1+r,1+r\}.
\]

Positivity alone does not select the sign: both matrices are positive at
\(r=1/4\). Rank-one purity changes the conclusion. The positive class reaches
rank one at \(r=1\), whereas the negative class is positive only for
\(0\leq r\leq1/2\) and has rank two at its boundary. More generally, every
real rank-one Gram matrix \(R=vv^T\) obeys

\[
R_{12}R_{23}R_{31}=(v_1v_2v_3)^2>0
\]

when all three incidences are nonzero. With unit diagonal, purity also fixes
all three normalized magnitudes to one.

This is an intrinsic invariant of the marked three-operator sign groupoid. It
is not the nine-link texture phase and no claim is made that it already
descends under the full flavor weak-basis groupoid.

## Aspect germ-tester audit

The minimal object is natively ternary:

```text
ThreeOperatorGramLoopGerm
  operator_germs: O1, O2, O3
  primitive_attachments: C12, C23, C31
  common_state_and_pole_germ
  rank_one_purity_authority
  marked_line_threshold_protection
  three_cross_channel_calibration
  physical16_descent
```

The comparison must be formed before quotienting any operator by its local
sign. Reducing it to pairwise endpoint facts loses the cycle product. Thus the
native-arity, primitive-attachment, fiber, and constructor-order gates pass.

Three gates remain open. Flavor has not supplied the source law that makes the
rank-one three-line carrier unavoidable. The marked operator triangle has not
been proven to descend to `physical16`. No common calibrated three-cross-channel
detector has been admitted. The germ tester therefore classifies this as a
valid ternary conditional selector, not an authorized physical selector.

## Threshold and instrument typing

Positive diagonal transport \(R\mapsto ZRZ\) preserves every normalized edge
and the positive loop sign. More strongly, real congruence preserves rank-one
positivity and cannot create a negative nonzero triangle: the transported
matrix remains \(ww^T\). Nonaligned mixing can nevertheless make a component
of \(w\) vanish and erase two primitive attachments. Threshold survival thus
requires nonvanishing protection of the three marked lines, not diagonal
transport specifically.

A calibrated record \((R_{12},R_{23},R_{31})\) is faithful on the three cross
residues. Positive detector gains preserve the sign of their product, but
uncalibrated gains leave a three-dimensional magnitude kernel. This is a
formal instrument design, not evidence that the required flavor detector
exists.

## Classification and falsifiers

Conditional on a nonzero real rank-one three-operator Gram carrier, the
operation is both a normalized-magnitude selector and an intrinsic loop-sign
selector. Without purity it is neither: \(R_+(1/4)\) and \(R_-(1/4)\) are the
smallest rational hostile pair. The smallest negative-loop purity obstruction
is \(R_-(1/2)\), whose rank is two rather than one.

The physical claim is falsified if any of the following occurs:

1. the source permits a positive rank-one carrier with negative triangle
   product;
2. one primitive attachment is absent or reconstructed from the desired
   result;
3. a full weak-basis transformation changes the proposed `physical16` target;
4. admitted threshold mixing erases one of the marked incidences;
5. the calibrated three-channel response has rank below three;
6. detector gain signs or common-frame calibration are not independently
   fixed.

## Deutschian appraisal

The new explanation is structural: odd incidence plus purity makes one sign
class impossible, rather than merely assigning it a worse fit. This answers
why two-operator purity was sign-blind. It does not yet answer why nature must
instantiate this particular pure triangle or how its loop character becomes
the asymmetric flavor portal. The next source candidate must derive the three
marked incidences and rank-one carrier together, then exhibit a weak-basis
invariant map into `physical16` and a calibrated common-frame detector.

## Disposition

Progressive conditional theorem, incomplete physical authority. Aspect's
structural germ gates pass; its source-authority, quotient-descent, and
instrument gates remain open.
