# Residue-level monic comparison for the exceptional face

## Question

After the exceptional-face comparison coefficient is forced, what part of the comparison is actually constructed by the current residue data?

## Claim boundary

This packet constructs only the residue/Gysin shadow. It does not construct a pre-residue chain map, a Čech--de Rham total differential, a relative p-normal Bockstein, a global contour, or a physical period.

## Disposition

The logarithmic class has ordered pair-face residue column

\[
\operatorname{Res}(\Xi_{\log})=(1,-1,1).
\]

The oppositely oriented exceptional boundary has column

\[
\partial(-\sigma_{123})=(-1,1,-1).
\]

Their sum is zero. Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), each column has rank \(1\), their span has rank \(1\), and the paired sum has rank \(0\).

Therefore the residue map is monic on the one-dimensional \(\Xi_{\log}\) line, and the exceptional-to-logarithmic comparison is unique after choosing orientation. This is exactly the residue-level comparison required by the previous unit gate.

The monicity is only a residue-sheaf statement on the \(\Xi_{\log}\) line. It is not a monomorphism of the full logarithmic denominator complex and does not supply a primitive.

The remaining gate is to lift this residue comparison through the residue exact sequence: construct a preimage of the comparison in the logarithmic Čech--de Rham total complex or in a resolved/Rees carrier.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_residue_monic_comparison.py`

Result:

- `research/voevodsky/results/cosmology_residue_monic_comparison.json`

Command:

- `python research/voevodsky/check_cosmology_residue_monic_comparison.py`
