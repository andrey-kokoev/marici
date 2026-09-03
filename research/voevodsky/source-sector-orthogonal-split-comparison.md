# Comparison of sourced sectors with the orthogonal-split realization

## Question

Do the current enlarged Green, gauge quotient, or closed-form source sectors admit structure-preserving comparison with the orthogonal-split analytic partial equipment?

## Claim boundary

This packet tests the declared cyclic/auxiliary decomposition of the enlarged Green block exactly and audits the source data needed for gauge and closed-form comparisons. It does not prohibit unstructured diagonalization of a positive matrix.

## Enlarged Green obstruction

Use the exact scalar block already materialized in the variance audit:

\[
G=\begin{pmatrix}2&1/2\\1/2&1\end{pmatrix}.
\]

Its Schur complement is \(7/4>0\), so the form is positive. The orthogonal-split realization, however, requires zero cross pairing between the declared cyclic and auxiliary tags.

A decomposition-preserving invertible change of coordinates has block form

\[
T=\operatorname{diag}(a,b),
\qquad a,b\ne0.
\]

The transformed cross entry is

\[
(T^{\mathsf T}GT)_{12}=\frac{ab}{2},
\]

which cannot vanish. Therefore no comparison preserving the declared cyclic and auxiliary summands maps this Green block into the orthogonal-split model.

A general shear can diagonalize the form, but it mixes the typed summands and changes the embedding/port structure. Equal positive dimension therefore does not construct a structure-preserving comparison.

## Gauge quotient gate

The completed gauge exact sequence splits as plain vector spaces, but the source supplies no canonical gauge section or pointwise kernel framing. A comparison to the canonical split realization would require that additional presentation data. Its existence as an arbitrary linear choice is not source authority.

## Closed-form gate

The unbounded radial target does not yet supply the common-core intertwiner \(R_\zeta\). Hence no closed-form comparison with the finite orthogonal-split realization is currently defined.

## Disposition

The current sourced sectors do not map into the orthogonal-split realization with their declared structure:

- enlarged Green fails by a nonzero invariant cross block under decomposition-preserving maps;
- gauge comparison is blocked by absent canonical splitting data;
- closed-form comparison is blocked by the absent independently derived intertwiner.

The orthogonal-split model remains a consistency witness, not a model of the sourced architecture. The next executable branch is a broader nonorthogonal Gram-certified realization retaining full cross-pairing data and testing its coherence under composition.

## Verification

- `research/voevodsky/checkers/check_source_sector_orthogonal_split_comparison.py`
- `research/voevodsky/results/source_sector_orthogonal_split_comparison.json`
- `research/voevodsky/green-extension-variance-audit.md`
- `research/voevodsky/gauge-quotient-over-extension-audit.md`
- `research/voevodsky/unbounded-r-zeta-identity-typing-audit.md`
