# The first equally spaced rank-three source packet is positive numerically

## Packet

Fix

\[
\sigma=0.005
\]

and take Gaussian translates centered at

\[
-0.25,
\qquad0,
\qquad0.25.
\]

The source-side kernel values are approximately

\[
K(0)=0.1496980,
\qquad
K(0.25)=-0.1171689,
\qquad
K(0.5)=0.0922235.
\]

They produce the symmetric Toeplitz matrix

\[
\begin{pmatrix}
K(0)&K(0.25)&K(0.5)\\
K(0.25)&K(0)&K(0.25)\\
K(0.5)&K(0.25)&K(0)
\end{pmatrix}.
\]

## Reflection decomposition

The reflection-odd vector has eigenvalue

\[
K(0)-K(0.5)
\approx0.0574746.
\]

The remaining reflection-even block has determinant

\[
0.0087581.
\]

The three numerical eigenvalues are approximately

\[
0.0574746,
\qquad
0.0238115,
\qquad
0.3678080.
\]

Thus the packet is numerically positive definite. Its determinant is approximately

\[
5.03\times10^{-4}.
\]

## Significance

Rank-two positivity does not automatically imply rank-three positivity. This calculation passes the first higher-rank test and exhibits a nontrivial negative nearest-neighbor kernel entry compensated by the full matrix structure.

No zero locations enter the evaluation; the kernel values come from the endpoint, gamma, and prime source formula.

## Scope

This is a floating scout, not an analytic enclosure. A rank-three certificate can reuse the scalar enclosures for \(K(0)-K(0.5)\) and must additionally bound the reflection-even determinant away from zero.

## Verification

```text
python research/voevodsky/checkers/scout_three_translate_source_gram.py
```

Artifacts:

- `research/voevodsky/checkers/scout_three_translate_source_gram.py`
- `research/voevodsky/results/three_translate_source_gram_scout.json`
