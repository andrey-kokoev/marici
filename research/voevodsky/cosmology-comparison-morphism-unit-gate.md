# Unit gate for the exceptional-face comparison morphism

## Question

If a comparison morphism couples the ordered blow-up exceptional face to \(\Xi_{\log}\), is its coefficient free or forced?

## Claim boundary

This packet proves a conditional unit-forcing statement. It does not construct the geometric comparison morphism, a logarithmic primitive, a Bockstein class, a global contour, or a physical period.

## Disposition

The residue differential is

\[
D=
\begin{pmatrix}
1&-1\\
-1&1\\
1&-1
\end{pmatrix}
\]

with columns ordered as

\[
(\Xi_{\log},-\sigma_{123}).
\]

The ordered blow-up exceptional simplex already supplies the \(-\sigma_{123}\) leg with unit coefficient. A possible comparison column therefore has form

\[
(\lambda,1).
\]

The chain-map condition is

\[
D(\lambda,1)=0.
\]

This holds exactly when

\[
\lambda=1.
\]

The opposite orientation gives the simultaneous sign reversal \((-1,-1)\). No other scalar is compatible with the residue differential.

The checker tests \(\lambda=-3,\ldots,3\) over \(\mathbb Z\) and solves the same condition over \(\mathbb F_{101}\) and \(\mathbb F_{103}\). In both finite fields the unique coefficient with exceptional leg fixed to \(1\) is \(\lambda=1\).

Thus any sourced comparison morphism from the blow-up exceptional face to \(\Xi_{\log}\) has no scalar-fitting freedom: it must be the unit map, up to simultaneous orientation reversal. The missing datum is existence of the geometric residue/Gysin comparison, not normalization.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_comparison_morphism_unit_gate.py`

Result:

- `research/voevodsky/results/cosmology_comparison_morphism_unit_gate.json`

Command:

- `python research/voevodsky/check_cosmology_comparison_morphism_unit_gate.py`
