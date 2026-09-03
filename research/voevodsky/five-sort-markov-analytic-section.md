# Five-sort Markov analytic section

## Question

Do the accumulated Markov constructors now realize every object sort and coherence class of the integrated computad on one connected restricted domain?

## Claim boundary

The section is restricted to finite or uniformly completable metric-transition Markov paths and finite rooted trees, with framed presentations and admitted gauge actions. It is not a global section for arbitrary Carriers or other physical sectors.

## Sort realization

The five computad sorts are realized as follows:

- `carrier`: typed Markov paths or rooted trees with contraction transfers;
- `gauge_presentation`: framed Markov data \((R_i,A_i)\);
- `finite_green`: finite positive path or rooted-tree covariance kernels;
- `quotient_form`: metric-transition coordinates \((M_i,C_i)\) modulo orthogonal frame changes;
- `closed_form`: uniformly contractive bounded operators on the Hilbert direct sum.

The incidence routes are:

\[
	exttt{gauge_presentation}
\to
	exttt{carrier}
\to
	exttt{finite_green},
\]

followed by the partial completion/descent hyperedge connecting `finite_green`, `quotient_form`, and `closed_form`.

## Cell realization

All six declared cell classes have restricted realizations:

- associator: identity for ordered amalgamation or rooted branch union;
- left and right unitors: empty extension and identity gauge;
- interchange: compatible vertex-gauge telescoping;
- Beck–Chevalley: identity for ordered-subset or rooted-subtree restriction;
- completion comparison: identity on finite compressions and metric-transition descent.

## Law realization

The five declared law classes hold on the admitted domain:

- pentagon by associativity of ordered products or branch union;
- triangle by strict units;
- interchange hexagon by compatible gauge composition;
- pasting by nested restriction;
- completion pasting by exact principal compressions and frame-independent descent.

Companions and conjoints exist for the admitted orthogonal gauge groupoid and for bounded GL frame changes in the framed-metric extension.

## Section status

This is a genuine connected analytic section of the five-sort presentation. Its domain predicates are essential:

- typed Markov incidence;
- contraction/positivity;
- seam or rooted-branch compatibility;
- quotient frame descent;
- uniform completion bounds;
- bounded gauge and inverse where completed.

Removing these predicates does not enlarge the theorem; it makes constructors undefined.

## Cross-sector boundary

The section does not realize:

- arbitrary Carrier geometry;
- `R_zeta` or `U_G4`;
- Kitaev's physical controlled-cycle constructor;
- general cyclic graph amalgamation;
- physical readout maps;
- cross-sector mixed horns.

## Disposition

The original five-sort computad now has a genuine restricted global analytic section on the Markov domain, including all declared cell and law classes. The remaining global objective is cross-sector extension and gluing, not completion of the Markov section itself.

## Verification

- `research/voevodsky/checkers/check_five_sort_markov_analytic_section.py`
- `research/voevodsky/results/five_sort_markov_analytic_section.json`
