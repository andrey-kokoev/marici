# Exact pasting complex for the cyclic coherence filler

## Question

Is the common-fixture filler \(\Omega_{ABC}\) unique modulo local vertex adjustments, and is every global discrepancy fillable?

## Claim boundary

This packet constructs the oriented cellular complex of the three-cycle on the common signed-even fixture. It proves fixture-level existence and uniqueness modulo local adjustments. It does not establish higher contractibility or source-global naturality.

## Pasting complex

Let \(C^1\cong k^3\) contain adjustments at vertices \((A,B,C)\), \(C^2\cong k^3\) contain edge-cell changes \((\alpha_A,\alpha_B,\alpha_C)\), and \(C^3\cong k\) contain the global face discrepancy. With the counterclockwise orientation, define

\[
\partial_1=
\begin{pmatrix}
-1&1&0\\
0&-1&1\\
1&0&-1
\end{pmatrix},
\qquad
\partial_2=
\begin{pmatrix}1&1&1\end{pmatrix}.
\]

Then \(\partial_2\partial_1=0\). The common-fixture target discrepancy is \(D=\tau H\), and

\[
\Omega_{ABC}=(0,D,0),
\qquad
\partial_2\Omega_{ABC}=D.
\]

All other fillers of \(D\) form the affine space \(\Omega_{ABC}+\ker\partial_2\).

## Exact computation

The checker obtains

\[
\operatorname{rank}\partial_1=2,
\qquad
\dim\ker\partial_2=2,
\qquad
\operatorname{rank}\partial_2=1.
\]

Moreover, \(\operatorname{im}\partial_1=\ker\partial_2\). Therefore

\[
H^2=rac{\ker\partial_2}{\operatorname{im}\partial_1}=0,
\qquad
\operatorname{coker}\partial_2=0.
\]

Every scalar face discrepancy is fillable, and its filler is unique modulo local vertex adjustments.

## Strongest falsification attempt

Change one incidence sign while retaining the same face sum. The checker verifies that the resulting matrices no longer compose to zero. Thus orientation is load-bearing; the vanishing result does not follow from dimensions alone.

## Disposition

On the common fixture, the filler is canonical as a quotient class: alternative edge representatives differ exactly by local vertex adjustments. This proves neither literal uniqueness nor contractibility of the full filler type; higher paths and analytic naturality are absent. The next categorical target is the higher coherence of adjustment witnesses, followed by source-global extension.

## Verification

- `research/voevodsky/checkers/check_cyclic_filler_pasting_complex.py`
- `research/voevodsky/results/cyclic_filler_pasting_complex.json`
