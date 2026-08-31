# Blow-up exceptional-cell gate for the universal p-normal lift

## Question

Does the oriented blow-up exceptional simplex of the three-wall corner satisfy the \(\tau_p\) source-map contract?

## Claim boundary

This packet tests only the exceptional Čech face supplied by the ordered blow-up direction. It does not construct the comparison morphism from that face to the logarithmic denominator class, a Bockstein class, global contour, or physical period.

## Disposition

The \(\tau_p\) contract requires a source column

\[
(1,1)
\]

in rows

\[
(\Xi_{\log},-\sigma_{123}).
\]

The ordered blow-up exceptional simplex supplies the opposite Čech face with unit coefficient, hence its column is

\[
(0,1).
\]

This is a genuine sourced leg of the contract, but it is not the full contract. The missing component is the unit leg to \(\Xi_{\log}\).

The residue differential is

\[
D=
\begin{pmatrix}
1&-1\\
-1&1\\
1&-1
\end{pmatrix}.
\]

Applying it to the exceptional column gives

\[
D(0,1)=(-1,1,-1),
\]

so the exceptional face alone is not closed in the relative residue complex. It cancels the logarithmic residue only when paired with the \(\Xi_{\log}\) leg.

Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), the exceptional column has rank \(1\), but augmenting it by the required \((1,1)\) column gives rank \(2\). Thus the exceptional simplex alone cannot factor as \(\tau_p\).

The next gate is the comparison morphism that couples the exceptional face to \(\Xi_{\log}\) with unit coefficient, or a proof that no such morphism is source-derived.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_blowup_exceptional_cell_gate.py`

Result:

- `research/voevodsky/results/cosmology_blowup_exceptional_cell_gate.json`

Command:

- `python research/voevodsky/check_cosmology_blowup_exceptional_cell_gate.py`
