# Relative Čech–de Rham interferometer SCC model

## Question

Can a simulation-only phase-sensitive instrument distinguish residue cancellation from a genuine total-complex lift without manufacturing the missing cosmological constructor?

## Claim boundary

This model classifies finite linear-algebra signatures in the basis \((\Xi_{\log},-\sigma_{123})\). It does not realize an optical apparatus, construct a cosmological exceptional generator, authorize a contour, or define a physical period.

## Construction

The residue differential is

\[
D_{\rm res}=\begin{pmatrix}1&-1\\-1&1\\1&-1\end{pmatrix},
\]

so the relative vector \(v=(1,1)^T\) is closed. A scalar dark-port row \((1,-1)\) sees only cancellation and has rank one. The complementary phase-sensitive probe family

\[
P=\begin{pmatrix}1&-1\\1&1\end{pmatrix}
\]

has rank two over the audited fields and separates the cancellation coordinate from the coherent common coordinate.

Four regimes are tested:

1. residue cancellation with no incoming total differential: closed nonboundary;
2. a hypothetical source-authorized exceptional column \((1,1)^T\): algebraically sufficient but not currently sourced;
3. a circuit quotient that forces the target to zero: rejected as tautological;
4. incoherent intensity post-selection: rejected because it does not implement the signed amplitude relation.

## Disposition

The checker passes over \(\mathbf F_{101}\) and \(\mathbf F_{103}\). Its positive result is classifier adequacy: complementary probes distinguish the four regimes. It leaves the exceptional constructor and total lift unconstructed.

The next admissible constructor must be a source-derived chain map from a resolved/Rees exceptional generator or Cayley–Menger face cone into the logarithmic Čech–de Rham total complex, with image \((\Xi_{\log},-\sigma_{123})\). SCC must reject an abstract ancillary route lacking that source map.

## Reproducibility

- Contract: `research/aspect/contracts/relative-cech-de-rham-interferometer.v1.json`
- Checker: `research/aspect/checkers/check_relative_cech_de_rham_interferometer.py`
- Result: `research/aspect/results/relative_cech_de_rham_interferometer.json`
