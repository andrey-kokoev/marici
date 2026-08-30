# Entry 1243 — Every Compatible Five-Site Triple Inherits a Closed Pair

## Frozen census

Entry 1236 supplies

\[
1210
\]

compatible labelled triples, forming

\[
242
\]

free \(C_5\)-orbits.

Each triple contains three source-compatible labelled pairs. Classify those subpairs using the exact outcomes of Entries 1237–1242:

- `unit`: the pair stationarity ideal is the unit ideal;
- `t_zero`: the pair equations force \(t=0\);
- `old_threshold`: the pair projects only to an existing one-wall threshold.

## Exact inheritance census

The 242 triple orbits divide as

\[
\begin{array}{c|c}
\text{inherited pair content}&\text{triple orbits}\\
\hline
\text{unit subpair only}&172\\
\text{unit and }t=0\text{ subpairs}&56\\
t=0\text{ subpair only}&14
\end{array}
\]

There is no unresolved orbit.

Equivalently, 228 triple orbits contain a unit pair ideal. Their three-wall stationarity ideals are therefore units without further elimination. The remaining 14 orbits inherit total-energy support from a \(t=0\)-forcing pair.

## Result

\[
\boxed{
\text{no compatible triple requires a new three-wall stationarity calculation.}
}
\]

Since every orbit is free under \(C_5\), the corresponding labelled counts are

\[
860,
\qquad
280,
\qquad
70,
\]

respectively, summing to 1210.

Thus the complete source-compatible pair-and-triple Landau census on the frozen cyclic family adds no divisor beyond total-energy and the existing one-wall supports.

## Scope

This is an inheritance theorem for the pair/triple subsets occurring in the frozen 180-term OFPT packet. It does not classify active sets of four or more walls, nor does it prove that the scalar period's minimal Picard–Fuchs operator has no apparent singularities.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_triple_landau_inheritance.rs`
- `research/benincasa/results/five-site-triple-landau-inheritance.json`

## Next falsifier

No additional hypergraph census is required. Every compatible active set of size at least four contains a compatible triple, and every compatible triple contains a closed pair by this entry. Record the hereditary closure for all active-set sizes, then return to the scalar period problem: determine whether the resulting one-wall support bound controls a derived differential equation or only its genuine Landau divisor.
