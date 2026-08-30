# Gamma-Bockstein normalization has one open naturality square

## Result

The conductor source already fixes the local scalar normalization.

The physical exponent is declared as

\[
-\frac12+\epsilon,
\]

with unit epsilon slope. Multiplication by the source normalization of order one cancels the conductor pole of order minus one. The universal local family has Milnor rank one with primitive target basis (1), and its normalized grade-zero scaling is also (1).

Thus normal-coordinate rescaling is not an admissible local freedom once the declared epsilon coordinate and Milnor generator are retained.

## Chart transport

The existing labelled residue transition fixes the ordinary Poincaré-residue orientation sign at minus one. It maps every retained relation exactly, has full transport rank, and its round trip is the identity. A separate rank calculation shows that the two conductor charts add the same single descent line.

These facts do not yet prove the derivative-level square. The residue transition was checked over ordinary coefficients, while the Bockstein lives over the dual extension in epsilon. The missing diagram is

\[
\begin{array}{ccc}
R_{12} & \xrightarrow{\beta_{12}} & L_{12}\\
\downarrow T_R && \downarrow T_L\\
R_{31} & \xrightarrow{\beta_{31}} & L_{31}.
\end{array}
\]

The remaining gate is

\[
T_L\beta_{12}=\beta_{31}T_R
\]

with the already fixed residue-orientation sign and epsilon unit.

## Deutsch disposition

The local explanation is now absolutely normalized. The global two-chart explanation is not yet closed. One exact dual-epsilon naturality calculation can close it; failure would show that the gamma-Bockstein is chart-dependent and therefore not the sought source constructor.

## Verification

```text
uv run python research/aspect/checkers/check_gamma_bockstein_normalization_authority.py
```
