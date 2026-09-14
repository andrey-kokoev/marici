# Parity folding does not close on the translate-rung family

## Identification tested

For a three-point translation packet,

\[
G_3=
\begin{pmatrix}
K_0&K_1&K_2\\
K_1&K_0&K_1\\
K_2&K_1&K_0
\end{pmatrix},
\]

use the orthonormal reversal-even basis

\[
e_+=\frac{e_1+e_3}{\sqrt2},
\qquad e_2.
\]

The even compression is

\[
G_+=
\begin{pmatrix}
K_0+K_2&\sqrt2K_1\\
\sqrt2K_1&K_0
\end{pmatrix}.
\]

The odd compression is the rank-one value

\[
G_-=K_0-K_2.
\]

## Failure of lower-rung closure

A standard two-translate rung has equal diagonal entries \(K_0,K_0\). The even fold has diagonals \(K_0+K_2,K_0\), so canonical identification requires

\[
K_2=0.
\]

Likewise, the odd fold equals the standard rank-one base value only if \(K_2=0\).

For the Gaussian Weil kernel, no such vanishing identity is available. Therefore the proposed source identification with an earlier translate rung fails generically.

An exact positive fixture

\[
K_0=1,
\qquad K_1=1/2,
\qquad K_2=1/4
\]

already exhibits the mismatch while its rank-three determinant remains positive.

## Correct interpretation

Parity folding really propagates negativity to lower **dimension**, but not backward within the same translate-rung family. It produces new packet types:

\[
T_{-h}g+T_hg,
\qquad
T_{-h}g-T_hg,
\]

rather than individual Gaussian translates.

Closing the coherence system under these folds creates a multitype wavelet-packet hierarchy. But positivity of its rank-one leaves is exactly positivity of Weil evaluations on those linear combinations; it is not implied by positivity of the original single-translate base rung.

Hence an iteration down to rank one does not yet contradict known base positivity. The negative information survives inside the newly generated leaf.

## Disposition

The simple backward-descent proof is blocked:

\[
\text{reversal fold}
\not\cong
\text{earlier translate rung}.
\]

A successful repair would need an independent source theorem making all terminal folded leaves positive. Without that theorem, the fold hierarchy reorganizes the original all-test positivity problem rather than proving it.

## Verification

```text
python research/voevodsky/checkers/check_parity_fold_lower_rung_identification_no_go.py
```

Artifacts:

- `research/voevodsky/checkers/check_parity_fold_lower_rung_identification_no_go.py`
- `research/voevodsky/results/parity_fold_lower_rung_identification_no_go.json`
