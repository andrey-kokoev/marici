# Entry 1242 — The Five-Site Compatible Pair Landau Census Closes Without a New Divisor

## Final seven representatives

Use Entry 1241's exact four-focus ideal for each of the seven remaining disjoint-cut connected-region pair orbits:

\[
I=(C_{\rm real},M_{12},M_{13},M_{23}),
\]

where the \(M_{ij}\) are the three labelled collinearity minors.

## Staged exact certificate

For each minor define

\[
R_i(c,t,z)
=
\operatorname{Res}_b(C_{\rm real},M_i).
\]

Then compute all three pairwise second resultants

\[
S_{ij}(t,z)
=
\operatorname{Res}_c(R_i,R_j).
\]

For every one of the seven source representatives,

\[
\boxed{
S_{12}=S_{13}=S_{23}=1
}
\]

over \(\mathbb Q(z,t)\), before imposing \(z^2=5\).

Already one unit \(S_{ij}\) excludes a common solution of \(C_{\rm real},M_i,M_j\); hence the complete four-generator ideal has no solution. The quadratic specialization cannot undo a unit identity.

## Independent modular replication

The same staged calculation was repeated at

\[
p=1009,
\qquad
p=1021,
\]

using both roots of \(z^2=5\) in each field. All

\[
7\times2\times2\times3=84
\]

modular second resultants are units.

## Complete pair classification

The 49 compatible pair orbits from Entry 1236 now divide as follows:

\[
\begin{array}{c|c}
\text{class}&\text{number of free }C_5\text{-orbits}\\
\hline
\text{confined to }t=0&7\\
\text{projects to existing one-wall thresholds}&8\\
\text{unit stationarity ideal}&34
\end{array}
\]

Therefore

\[
\boxed{
\text{the complete source-compatible pair Landau census adds no new divisor.}
}
\]

## Interpretation

This closes pair pinches on the frozen cyclic five-site family. It does not close the 242 compatible triple orbits, and it does not prove a Picard–Fuchs theorem for the full period.

The result is evidence that the one-wall energy/incidence carrier already contains the projected pair support. It does not identify every pair contribution with a nonzero physical cycle.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_four_focus_staged_modp.rs`
- `research/benincasa/marici-gm/src/bin/five_site_four_focus_staged_exact.rs`
- `research/benincasa/results/five-site-four-focus-staged-modp.json`
- `research/benincasa/results/five-site-four-focus-staged-exact.json`
- `research/benincasa/results/five-site-four-focus-elimination-summary.json`

## Next falsifier

Begin the compatible triple census with the source-derived classes containing \(G=5t\), repeated cut supports, or an already unit pair subideal. Eliminate these inheritance classes before constructing any genuinely three-wall stationarity system.
