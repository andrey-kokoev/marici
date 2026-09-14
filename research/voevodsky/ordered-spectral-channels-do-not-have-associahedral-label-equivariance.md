# Ordered spectral channels do not have associahedral label equivariance

The proposed dictionary identifies \(X_{13},X_{24}\) with the two eigenvalues of the primitive/prime-prime Schwarz square.

A quadrilateral rotation exchanges the channel labels

\[
X_{13}\longleftrightarrow X_{24}.
\]

But exchanging the two primitive basis vectors conjugates the observation square by

\[
P=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

which leaves its ordered eigenvalue pair unchanged.

For example,

\[
S=\operatorname{diag}(3,1)
\]

has ordered spectrum \((3,1)\). After basis exchange,

\[
PSP=\operatorname{diag}(1,3),
\]

but its ordered spectrum is still \((3,1)\), whereas associahedral covariance requires the labeled pair \((1,3)\).

Therefore ordered eigenvalues cannot supply an equivariant identification with the labeled channels \(X_{13},X_{24}\).

The unordered spectrum does satisfy the trace/product dictionary:

\[
\{X_{13},X_{24}\}=\operatorname{Spec}(S),
\]

but it forgets precisely the cyclic channel labels and oriented incidence needed by the positive geometry.

A labeled comparison requires additional source data: an eigenline or branch orientation that exchanges under cyclic relabelling. Such a branch must remain coherent through eigenvalue collisions and cannot be selected after assuming positivity.

Thus the corrected frontier is not merely spectral equality. It is a source-derived **oriented spectral cover** of the Schwarz observation square.

## Verification

```text
python research/voevodsky/checkers/check_associahedral_spectral_channel_equivariance_no_go.py
```

Artifacts:

- `research/voevodsky/checkers/check_associahedral_spectral_channel_equivariance_no_go.py`
- `research/voevodsky/results/associahedral_spectral_channel_equivariance_no_go.json`
