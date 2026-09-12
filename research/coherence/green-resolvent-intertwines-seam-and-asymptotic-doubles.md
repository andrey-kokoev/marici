# The Green resolvent intertwines seam and asymptotic doubles

## Point-supported source from seam jumps

At a seam \(x\), let

\[
J^0=f(x+)-f(x-),
\qquad
J^1=f'(x+)-f'(x-).
\]

The singular part of the massive operator is

\[
(1-\partial^2)f
=-J^1\delta_x-J^0\delta_x'.
\]

Write \(y=e^x\). Applying the Green resolvent, with kernel \(\frac12e^{-|t-x|}\), gives asymptotic charges

\[
q_-=-\frac{J^0+J^1}{2y},
\qquad
q_+=\frac{y(J^0-J^1)}2.
\]

Thus the transfer matrix is

\[
C_x=
\begin{pmatrix}
-1/(2y)&-1/(2y)\\
y/2&-y/2
\end{pmatrix},
\]

from \((J^0,J^1)\) to \((q_-,q_+)\).

Its determinant is

\[
\det C_x=\frac12,
\]

independent of the seam position. Over coefficients where two is invertible, the value/flux seam double and incoming/outgoing asymptotic double are therefore canonically isomorphic after choosing the Green resolvent.

## Translation covariance

Moving the seam by \(a\) sends \(y\mapsto zy\), where \(z=e^a\), while preserving local jump coefficients. The transfer obeys

\[
C_{x+a}(J^0,J^1)
=
\operatorname{diag}(z^{-1},z)C_x(J^0,J^1).
\]

The hyperbolic translation weights are induced exactly from relocation of the local seam source.

## Reflection covariance

Reflection sends

\[
(x,J^0,J^1)
\mapsto
(-x,-J^0,J^1).
\]

The transfer then gives

\[
(q_-,q_+)\mapsto(q_+,q_-).
\]

Hence the diagonal seam parity \((-1,+1)\) and the asymptotic charge swap are the same reflection representation in Green-resolvent-related frames.

## Clarified status

Dimension alone did not justify identifying the two doubles. The massive Green resolvent now supplies the missing typed intertwiner. It depends on:

- the second-order operator \(1-\partial^2\);
- the seam location \(x\);
- division by two;
- the chosen normalization of the Green kernel.

Without these data, the carriers remain merely representation-isomorphic. With them, the comparison is canonical and fully translation/reflection covariant.

The Green innovation subspace \(J^0=0\) maps to the one-dimensional charge locus

\[
(q_-,q_+)
=
-\frac{J^1}{2}(y^{-1},y),
\]

which is the asymptotic profile of the kernel section at \(x\).

## Verification

```text
python research/coherence/check_seam_to_asymptotic_green_transfer.py
```

The checker verifies invertibility and both covariance laws in 100 exact rational trials.

Artifacts:

- `check_seam_to_asymptotic_green_transfer.py`
- `seam-to-asymptotic-green-transfer.v1.json`
