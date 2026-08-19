# 908 — Variance Repair Preserves the Exact Mixed-Corner Coherence Theorem

## Defect

Entries 906 and 907 used the correct abstract transition

\[
T=M_{\rm block}K_{\rm dense},
\]

but their first checkers did not respect the serialized matrix variances.

The sparse source matrix is stored as

\[
M_{\rm block}:B\times L,
\]

where \(B\) is the sparse right basis and \(L\) the common left basis. The momentum-kernel formula is serialized as

\[
\mathcal S[\gamma\mid\sigma]:D\times L,
\]

where \(D\) is the dense right basis. Its contraction matrix is

\[
K_{\rm dense}=\mathcal S^T:L\times D.
\]

Therefore the typed transition is

\[
\boxed{
T=M_{\rm block}\mathcal S^T:B\times D.
}
\]

The original numerical checker instead formed \(K_{\rm block}^{-1}\mathcal S\), and the original exact checker selected fixed dense rows rather than fixed dense right words. Those operations were dimensionally square but label-variance incorrect.

## Repair

The numerical checker now constructs the source intersection matrix directly, transposes the dense kernel, and evaluates

\[
\widehat T
=
\sin(\pi s_{235})M_{\rm block}\mathcal S^T.
\]

Across the same three generic tangential slices, the corrected first-order Richardson discrepancies are

\[
8.44\cdot10^{-5},
\qquad
1.22\cdot10^{-4},
\qquad
1.98\cdot10^{-4}.
\]

The exact checker now fixes the dense right words

\[
423,
\qquad
432,
\]

and varies the six common left words. It computes the corrected \(2\times6\) block of \(M_{\rm block}\mathcal S^T\).

## Corrected exact result

All twelve entries remain regular at

\[
X=e^{i\pi s_{23}}=1,
\qquad
Q=e^{i\pi s_{235}}=1.
\]

Both ordered specialization maps agree exactly:

\[
\boxed{
\operatorname{Sp}_{X=1}\operatorname{Sp}_{Q=1}(\widehat T)
=
\operatorname{Sp}_{Q=1}\operatorname{Sp}_{X=1}(\widehat T).
}
\]

The corrected exceptional matrix still has

\[
\operatorname{rank}=1,
\qquad
\text{row}_2=-\text{row}_1.
\]

## Disposition

The implementation defect is repaired, not suppressed. Entry 905's determinant divisor was invariant under transpose and remains unchanged. Entries 906–907 retain their substantive conclusion only through this corrected calculation.

Thus the typed narrow theorem is

\[
\boxed{
\text{the first mixed dense-to-sparse corner is strictly coherent in contraction variance.}
}
\]

## Next falsifier

Occurrence covariance may now be tested safely. Transport the corrected rank-one map through the three labelled corner charts, retaining both the sparse-right and dense-right basis permutations. Verify the signed cyclic composition; do not infer its sign from only one variance.
