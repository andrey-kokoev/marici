# Cokernel obstruction for current sourced p-normal fillers

## Question

What is the obstruction group after keeping only the source columns currently constructed?

## Claim boundary

This packet computes the cokernel obstruction of current sourced candidates against the formal \(\tau_p\) horn. It does not construct a new source object, Bockstein class, global contour, or physical period.

## Disposition

The ambient pair module has basis

\[
(\Xi_{\log},-\sigma_{123}).
\]

The required filler column is

\[
(1,1).
\]

The only current sourced column is the ordered blow-up exceptional face

\[
(0,1).
\]

Therefore the obstruction lies in

\[
\mathbb Z\langle \Xi_{\log},-\sigma_{123}\rangle
/\mathbb Z\langle -\sigma_{123}\rangle
\cong
\mathbb Z\langle \Xi_{\log}\rangle.
\]

The obstruction vector is

\[
(1,0),
\]

the primitive \(\Xi_{\log}\) coordinate. Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), the sourced span has rank \(1\), while adjoining the required \((1,1)\) column gives rank \(2\). The obstruction remains nonzero.

Thus the missing object is exactly a sourced \(\Xi_{\log}\) unit leg modulo the exceptional Čech face. More copies of the exceptional face, residue equality without pre-residue lift, nonunit \(\Xi_{\log}\) multiples, and the two-chart fixed-fiber gradient-pivot restriction do not kill this obstruction.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_tau_obstruction_cokernel.py`

Result:

- `research/voevodsky/results/cosmology_tau_obstruction_cokernel.json`

Command:

- `python research/voevodsky/check_cosmology_tau_obstruction_cokernel.py`
