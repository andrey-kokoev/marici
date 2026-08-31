# Relative residue cocycle after adjoining the ordered Čech face

## Question

After the ordered Čech 2-simplex cancels the pair-face residue vector, is there a closed relative object at residue level?

## Claim boundary

This packet constructs a residue-level relative cocycle. It does not construct a logarithmic primitive, a full logarithmic Čech--de Rham total differential, resolved/Rees compatibility, a Cayley--Menger face cone, ideal-dual evaluation, a global contour, or a physical period.

## Disposition

Let \(\Xi_{\log}\) denote the logarithmic denominator class with pair-face residue vector

\[
(1,-1,1)
\]

in the ordered basis

\[
(q_1q_2,q_1q_3,q_2q_3).
\]

Let \(-\sigma_{123}\) be the oppositely oriented ordered Čech face. Its boundary vector is

\[
(-1,1,-1).
\]

The residue-level differential from generators \((\Xi_{\log},-\sigma_{123})\) to ordered pair-face residues is

\[
\begin{pmatrix}
1&-1\\
-1&1\\
1&-1
\end{pmatrix}.
\]

Therefore

\[
\Xi_{\log}+(-\sigma_{123})
\]

has zero residue differential. The next differential is zero by the Čech boundary identity, so \(d^2=0\).

There are no incoming boundaries in this minimal residue complex: the ordinary logarithmic denominator carrier has no one-form primitive for \(\Xi_{\log}\), and the three-wall Čech nerve has no 3-simplex. Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), the relative differential has rank \(1\), the incoming-boundary rank is \(0\), and the cocycle remains nonzero.

Thus the obstruction has been retyped. In the ordinary denominator carrier, \(p\eta\) is a residue obstruction. After adjoining the ordered Čech face, the combination of the logarithmic class with the opposite Čech 2-simplex is a closed nonboundary residue-level relative class.

The remaining gate is no longer residue cancellation. It is the construction of a source-derived total chain-level lift of this residue cocycle into the logarithmic Čech--de Rham or resolved/Rees carrier.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_relative_residue_cocycle.py`

Result:

- `research/voevodsky/results/cosmology_relative_residue_cocycle.json`

Command:

- `python research/voevodsky/check_cosmology_relative_residue_cocycle.py`
