# Three-Branch Log--Rees Endpoint Star and the Spatial Comparison Gate

Date: 2026-08-16  
Status: proved in the finite labelled log/Rees coefficient model. The spatial
six-functor comparison remains open. No graph admission is claimed.

For each of the three compatible labels at an endpoint, retain the states

\[
\{	ext{absent},\ 	ext{present without a circle},\
  	ext{present with a circle}\}.
\]

Their product has \(3^3=27\) states, canonically indexed by every literal
entry143 pair

\[
H\subset S\subset v_+,
\]

and similarly at \(v_-\). The source tensor differential has a radial arrow
from `absent` to `present` and a normal arrow from `circle` to `present` in
each factor. The target differential uses entry143's radial incidence sign
and normal sign \((-1)^{3-|S|+\operatorname{pos}_H(h)}\).

The checker solves the sign-naturality equations from one positive anchor.
Propagation from that anchor reaches all 27 states, proving the constraint
graph is connected and the anchored solution is unique: ten basis states
retain sign \(+1\) and seventeen receive sign \(-1\). After this
derived rebase, all 54 source arrows equal the target arrows. Both source and
target differentials square to zero on every state.

Across the two endpoints this gives 54 labelled radial rows and 54 normal
rows. Every radial row retains the exact added label and therefore the same
\(X_i/u_i\) Cech monomial after the already admitted principal-line
evaluation. The checker stores the source and target occurrence/normal
exponents separately and compares all 54 labelled radial rows. Every normal
row is a signed unit. Duplicating the complete
matrix over the two external conductor Tor grades gives 108 state-grade rows
and 216 arrow-grade rows. No differential between the spectator Tor grades
is asserted.

This closes the finite endpoint-star matrix, including the radial terms that
entry277 did not cover. It still does not construct the proper/log-excess
natural transformation identifying the normalization source sheaves with
these literal target costalks. Nor does it attach the primitive hemisphere
top to based \(q_\Sigma\). Those remain the first spatial arrows needed for
the physical mapping fibre.

## Certificate

- `research/voevodsky/check_three_branch_log_rees_endpoint_star.rs`

~~~json
{
  "claim": "The three labelled log/Rees branch factors reproduce the complete 27-state endpoint-star coefficient matrix after a uniquely derived anchored orientation rebase.",
  "status": "proved_scoped_finite_three_branch_endpoint_star_matrix",
  "states_per_endpoint": 27,
  "constraint_graph_reachable_from_anchor": 27,
  "anchored_rebase_solution_count": 1,
  "arrows_per_endpoint": 54,
  "radial_rows_both_endpoints": 54,
  "radial_label_comparisons": 54,
  "normal_rows_both_endpoints": 54,
  "orientation_rebase_positive_negative": [10, 17],
  "spectator_Tor_grade_copies": 2,
  "state_Tor_census_rows": 108,
  "arrow_Tor_census_rows": 216,
  "integer_inverted": false,
  "spatial_six_functor_comparison": "unconstructed",
  "based_qSigma_connector": "unconstructed",
  "physical_p_partial_Q": "undefined"
}
~~~
