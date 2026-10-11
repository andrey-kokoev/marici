# Six comparisons and four faces of the proposed meta-tetrahedron

## Question and claim boundary

The operator requests constructing the missing comparisons and checking agreement of the routes among proton, neutron candidate, electron candidate and the unnamed fourth candidate.

The active obligation is **route/comparison compatibility**, restricted first to the retained coefficient protocols. A comparison of their complete geometry/construction records is a separate, stronger obligation.

- **Problem:** Can six nonzero state comparisons close all four triangular faces while retaining the original source protocols?
- **Conjecture:** Explicit source-bound encoders permit a directed tetrahedron after declaring one common scalar functional on the two-component input. This construction will expose, rather than remove, the full-state obstruction.
- **Rivals:** Four-way full-state equivalence; a unique completion or fourth protocol forced by state coherence; or independent scalar views at the proton and neutron endpoints that still factor through each other.
- **Risky consequences:** All four encoders must recover the actual stored returns and intertwine their stages. All four faces and six common-input squares must commute. Different scalar views must expose a route residual. No unrecorded state enlargement is permitted.
- **Falsification attempt:** Test three different common functionals, then independently change one nuclear functional; test the reverse route and compute the Gram determinant of a general complex row as an exact polynomial. Strengthen the test by substituting the known wrong-sign 264-transfer control and checking the complete three-step composite.
- **Disposition:** Six factorized comparisons close all four faces and the three-step composite, conditional on one extra common functional. The reverse route loses a component; three different choices pass; even the wrong-sign fourth control admits the same abstract coherence. Thus a directed selected-state tetrahedron is constructed, but the requested source-derived meta-tetrahedron of complete construction procedures is not established.

## Source-bound encoders

Write P, N, E and X for the four retained constructions. The normalized embeddings into their actual raw coefficient spaces are

\[
J_P:\mathbb C\to H_P,
\quad J_N:\mathbb C\to H_N,
\quad J_E:\mathbb C^2\to H_E,
\quad J_X:\mathbb C^2\to H_X.
\]

The raw dimensions are 36, 36, 8 and 12. These are coefficient carriers, not physical particle state-count claims.

The checker reconstructs the proton vector from its original labelled triangle geometry, with squared norm 80. It reconstructs the neutron candidate's selected numerator vector z using its retained metric diag(1/d_i); its squared norm is the exact sum of |z_i|²/d_i. Both normalized outer products match their full stored returns. The E and X encoders are independently checked against their stored operators and the earlier E–X bridge.

Let sharp denote the appropriate metric adjoint. For every corner,

\[
J_i^\sharp J_i=I,
\qquad J_iJ_i^\sharp=\mathcal N_i.
\]

Each original L, G and return stage is self-adjoint in that corner's metric and fixes J_i. These checks bind the comparison to the source modes rather than identifying states from equal dimensions alone.

## Six explicit comparisons

Choose a unit-norm scalar functional

\[
\ell:\mathbb C^2\longrightarrow\mathbb C.
\]

This is the added datum. No existing source instruction selects it. Orient the tetrahedron E, X, N, P and define logical maps

\[
B_{EX}=I_2,
\qquad B_{NP}=1,
\qquad
B_{EN}=B_{EP}=B_{XN}=B_{XP}=\ell.
\]

The actual raw-space comparisons are the exact factored matrices

\[
T_{ab}=J_b B_{ab}J_a^\sharp.
\]

Their numerators, positive normalization factors, metrics and logical matrices are retained in `results/meta_tetrahedron_comparison_store.json`. No floating-point dense matrix substitutes for these factors.

All four triangular faces close:

\[
\begin{aligned}
T_{XN}T_{EX}&=T_{EN}, & T_{XP}T_{EX}&=T_{EP},\\
T_{NP}T_{EN}&=T_{EP}, & T_{NP}T_{XN}&=T_{XP}.
\end{aligned}
\]

The three-step composite satisfies

\[
(T_{NP}T_{XN})T_{EX}
=T_{NP}(T_{XN}T_{EX})
=T_{EP}.
\]

These follow by contracting the independently checked middle factors J_i-sharp J_i and comparing the logical matrices. The checker also verifies all six common-input squares, with preparations J_E and J_X from the two-component input and J_N ell, J_P ell at the one-component corners.

The maps intertwine each retained stage because the encoders are fixed by it. However, they annihilate every source component orthogonal to the selected return. This does not construct maps of individual primitive arrows, geometric faces or complete assembly instructions.

## What the falsifiers reveal

### Coherence does not choose the scalar view

The three choices

\[
\ell_0=(1,0),\qquad
\ell_1=(0,1),\qquad
\ell_2=(3/5,4/5)
\]

all pass every face and common-input check with the same frozen source encoders and input basis. They give different P and N records for the same input. The symbolic construction works for any common unit functional, since its logical identities reduce to multiplication by identity maps.

Giving P the view ell_0 and N the independent view ell_1 preserves EXN and EXP but breaks ENP and XNP. More generally, if the N-to-P scalar comparison is c, coherence requires ell_P=c ell_N. Thus a comparison between the endpoints alone forces their scalar views to be proportional; it cannot recover an independent component.

### A reverse route cannot recover the full input

For ell_0, the spinor-to-scalar-to-spinor route acts on the shared input as

\[
\ell_0^\sharp\ell_0=
\begin{pmatrix}1&0\\0&0\end{pmatrix},
\]

rather than I_2. Its defect is diag(0,1). The second component is genuinely absent from the scalar record.

This obstruction is not special to the chosen row: for every complex ell, the checker expands the polynomial identity

\[
\det(\ell^\sharp\ell)=0,
\]

whereas det(I_2)=1. Hence there is no reversible complex-linear equivalence between the current one- and two-component selected returns.

Reversing all six comparisons gives a commuting tetrahedron of isometric inclusions. That version covers only one chosen line in the E and X spaces when prepared from a one-component root; it does not identify their complete two-component states with P or N.

### The wrong-sign fourth also passes state coherence

Replace the signed face projectors by the previously tested all-same-sign control. Its frame sum is 3I, so it has an isometric two-component encoder and a different 264-transfer return. The same logical comparison matrices close all four faces with this replacement as well.

That control is **not admissible under the retained neutron-sign requirement**. Its role is to show that selected-state coherence alone cannot enforce that requirement or select the 312-transfer candidate. Geometry and signed attachment transport must remain independent gates.

## Exact boundary and reproduction

| Claim | Disposition |
|---|---|
| Directed selected-state tetrahedron with a declared scalar view | Constructed; all faces and the three-step composite checked |
| Unique scalar view or fourth candidate selected by state coherence | Refuted by the alternative views and wrong-sign control |
| Reversible full-state equivalence at the current selected ranks | Excluded by the singular Gram matrix |
| Coherent comparison of all four complete construction procedures | Not established |

The first missing constructor is a comparison functional derived from the common construction record, rather than chosen to close the diagram. Its acceptance test must retain the actual geometry and signs as well as the coefficient states. The present data do not supply it; no source carrier has been enlarged to conceal that absence.

```text
python research/aspect/scc/scc.py check voevodsky-meta-tetrahedron-comparisons
python research/aspect/scc/scc.py categorical research/voevodsky/contracts/meta-tetrahedron-comparisons.json
python research/aspect/scc/scc.py inverse research/voevodsky/contracts/meta-tetrahedron-comparisons.json source_derived_meta_tetrahedron
```

Fifteen exact conditions pass. The initial test plan was frozen at d1bdf160d0c4681b; the strengthened plan, adding the wrong-sign control and explicit three-step check, was frozen at 11024d13545abae5 before execution. The SCC word-token backend compares hashes of already materialized logical composites; the source checker supplies the matrix and metric evidence. Its complete-construction comparison remains unsupported.

Results: `results/meta_tetrahedron_comparisons.json` and `results/meta_tetrahedron_comparison_store.json`. Existing source records and viewers are unchanged. No physical particle identification, commit or deployment is claimed.
