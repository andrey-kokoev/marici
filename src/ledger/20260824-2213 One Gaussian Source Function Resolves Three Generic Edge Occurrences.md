---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2213 — One Gaussian Source Function Resolves Three Generic Edge Occurrences

## Functional evaluation map

A translationally invariant boundary state supplies one function
\(\kappa(y)=\delta\log K(y)\), not three arbitrary edge-labelled constants.
Its action on the triangle is the evaluation map

\[
\kappa
\longmapsto
(\kappa(y_{12}),\kappa(y_{23}),\kappa(y_{31})).
\]

On the predeclared polynomial jet basis \((1,y,y^2)\), the determinant is

\[
\boxed{
(y_{23}-y_{12})(y_{31}-y_{12})(y_{31}-y_{23}).
}
\]

Hence the evaluation rank is:

\[
\begin{array}{c|c}
\text{edge energies}&\text{rank}\\
\hline
\text{pairwise distinct}&3\\
\text{exactly two equal}&2\\
\text{all equal}&1.
\end{array}
\]

## Consequence

At generic edge energies, one source function has enough local jets to
realize the full regular-\(C_3\) detector required by Entry 2200. No
edge-labelled violation of translational invariance is needed.

On equal-energy loci the physical source map loses rank. The unresolved
cyclotomic directions persist algebraically but cannot be selected by a
momentum-only Gaussian deformation. Any activation there requires higher
occurrence data or another independently derived source.

Thus the coincidence divisor is an existing coefficient/readout support for
rank loss, not a new Carrier stratum.

## Evidence

- Entries 2200 and 2211–2212
- `research/benincasa/checkers/gaussian_functional_evaluation_rank.rs`
