# The first source-side RH test is the two-translate deficit

## Rank-two projection

Fix one Gaussian width \(\sigma>0\). The source-derived translate kernel is real and even in the separation \(d\). Its two-translate Gram matrix is

\[
\begin{pmatrix}
K_\sigma(0)&K_\sigma(d)\\
K_\sigma(d)&K_\sigma(0)
\end{pmatrix}.
\]

The symmetric and antisymmetric eigenvalues are

\[
K_\sigma(0)+K_\sigma(d),
\qquad
K_\sigma(0)-K_\sigma(d).
\]

Thus the first nontrivial source-side positivity test is

\[
K_\sigma(0)\geq |K_\sigma(d)|
\]

for every real separation.

## Endpoint deficit

The crossed endpoint kernel is

\[
E_\sigma(d)=e^{\sigma/2}\cosh(d/2).
\]

Its antisymmetric contribution is

\[
E_\sigma(0)-E_\sigma(d)
=-e^{\sigma/2}(\cosh(d/2)-1),
\]

which is strictly negative away from zero. Near zero it begins as

\[
-e^{\sigma/2}\frac{d^2}{8}.
\]

Therefore the jointly regularized gamma-plus-prime contribution must compensate this exact deficit.

## Prime contribution

For a prime logarithm \(L=\log n\), imaginary-character crossing produces the paired Gaussian

\[
P_{\sigma,L}(d)
=
\frac12\left(
 e^{-(L-d)^2/(8\sigma)}
+
 e^{-(L+d)^2/(8\sigma)}
\right),
\]

with the sign and von Mangoldt weight prescribed by the explicit formula. The gamma term contributes its cosine-transform difference. Neither sector has a separately adequate positivity interpretation; they must be summed with the endpoint before testing the eigenvalues.

## Analytic target

The first concrete inequality to attack is now:

> Prove that the completed endpoint, gamma, and prime source terms jointly satisfy both rank-two eigenvalue inequalities for every positive width and every real separation.

This is necessary but not sufficient for RH. Higher translate ranks remain essential. A failure would be a direct finite-rank falsifier of the proposed positivity program.

## Relation to the channel geometry

The symmetric and antisymmetric vectors here are combinations of two translated tests. They are not the fixed and Möbius eigenlines of the coherence-channel bundle. The formulas may look identical, but no identification is made.

## Verification

```text
python research/voevodsky/checkers/check_two_translate_source_deficit_identity.py
```

Artifacts:

- `research/voevodsky/checkers/check_two_translate_source_deficit_identity.py`
- `research/voevodsky/results/two_translate_source_deficit.json`
