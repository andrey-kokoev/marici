# Pair-incidence conservation and the minimum order of the Ramsey obstruction

Date: 2026-11-09

## 1. Status

An exact finite theorem, conditional on the completeness of the supplied 2,576-graph `R(3,6;16)` classification: **every one of the 39 relevant 33-edge residual graphs has a six-port fractional obstruction that is induced by signed vertex-pair coefficients.** In six of the 39 cases, **nonnegative pair coefficients cannot yield any such obstruction**. For one explicit residual graph, an exact dual certificate additionally proves that **even signed vertex-additive coefficients cannot work**. Thus the obstruction has a provably essential signed pairwise component in a natural incidence-polynomial hierarchy.

This does **not** derive the pair coefficients from a universal local formula, and it does **not** independently classify the relevant graphs. It identifies the smallest necessary order in the tested hierarchy and isolates the role of cancellation.

## 2. Six-port setting

Let `H` be a triangle-free graph on 16 vertices, with 33 edges and independence number 5. Let `F` be its family of independent 5-subsets. In the hypothetical 23-vertex `(3,7)` graph previously reduced to 6-regularity, every neighbor of a fixed vertex would supply a port neighborhood `T_i in F`, for six ports `i=1,...,6`.

For every `I in F`, at most one `T_i` can avoid `I`: otherwise two ports together with `I` would form an independent 7-set.

Define the disjointness matrix `D_{T,I}=1[I cap T = empty]`.

## 3. Pair-incidence conservation identity

Index `e={u,v}` over the 87 *nonedges* of `H`. Define

`P[I,e] = 1[e subset I]`,

`B = D P`, so `B[T,e]` is the number of independent 5-sets containing `e` and disjoint from `T`, and

`r = P^T 1`, so `r[e]` is the number of independent 5-sets containing `e`.

For any **signed** integer pair potential `c=(c_e)`, set

`z_I = (P c)_I = sum_{e subset I} c_e`.

Assume the resulting 5-set weights, not necessarily each individual pair coefficient, satisfy `z_I >= 0`. Set

`m = min_{T in F} (B c)_T`,  `W = r^T c = sum_{I in F} z_I`.

**Pair-conservation theorem.** If `m>0` and `6m>W`, then six port neighborhoods cannot satisfy the independent-seven condition.

**Proof.** Any six port neighborhoods `T_1,...,T_6` have

`sum_i (B c)[T_i] >= 6m`.

But reversing the summation over the independent 5-set witnesses gives

`sum_i (B c)[T_i] = sum_{I in F} z_I * #{i: T_i cap I = empty} <= sum_I z_I = W`,

using `z_I>=0` and the fact that each `I` can avoid at most one port. If `6m>W`, these inequalities contradict one another. QED.

Equivalently, the signed pair conservation margin is

`J(c)=min_{T in F} [ sum_e c_e*(6 B[T,e]-r[e]) ]`.

A *positive* margin combined with `Pc>=0` is an exact obstruction certificate. Note that `c_e` can have both signs even though every `z_I` is nonnegative. Positive and negative contributions cancel on the ten pairs inside each 5-set.

## 4. Complete 39-class verification

The input catalogue is `/mnt/data/r36_16.g6.gz` with SHA-256

`5fd4e68d880e1d4ed05337b97cba0ce15387e1f545744aed80b91bb4b2186f25`.

Of 2,576 graph6 records, exactly 39 have 33 edges. For each such graph, a numerical LP found candidate signed pair coefficients. These were scaled by `10^7`, independently rounded to integers, and shifted by `+1` per pair to make every resulting five-set weight strictly positive. A **separate, standard-library-only checker** regenerated every independent 5-set, computed the pair sums and coverages with integer arithmetic, and verified:

* `z_I >= 0` for all `I`;
* `m = min_T sum_{I disjoint T} z_I > 0`;
* `6m - sum_I z_I > 0`.

Result: **39/39** pass. The largest exact generated ratio `W/m` is approximately `5.8728677662`, strictly below six. The smallest integer gap `6m-W` in the generated records is `1,271,332`.

The LP is a *discovery tool* only: the strict finite theorem depends on the integer checker and on catalogue completeness, not on floating-point solver correctness.

## 5. Why unsigned pair weights are insufficient

Suppose instead that all `c_e>=0`. Then we can omit `Pc>=0` because it follows automatically.

For a fixed `H`, consider any nonnegative vector `lambda_T` with

`sum_T lambda_T B[T,e] <= r[e]` for every nonedge pair `e`.

For any nonnegative `c` with `B c>=1`, it follows that

`sum_T lambda_T <= lambda^T Bc <= r^T c = W`.

Thus if `sum_T lambda_T >=6`, **no nonnegative pair potential can produce mass below six**.

The uploaded data contain exact *integer-scaled dual witnesses* with `sum_T lambda_T>6` for the six catalogue source indices:

| 1-based source index | Exact rational dual lower bound (decimal display) |
|---:|---:|
| 412 | 6.009738 |
| 927 | 6.125378 |
| 972 | 6.078803 |
| 973 | 6.367786 |
| 1253 | 6.406301 |
| 1813 | 6.064043 |

All pair inequalities of these duals were checked exactly with integers, without LP. The dual witnesses rule out **all possible** nonnegative pair coefficients on these six graphs, not merely coefficients returned by a particular search algorithm.

Consequently, the signed pair potential is genuinely stronger than a positive mixture of pair-incidence indicators within this model.

## 6. Why vertex-additive potentials are also insufficient

Take catalogue source graph 1253, graph6 `OQ?GOKaCQAOOPHaEad\`Ow`. A vertex-additive candidate has the form

`z_I = sum_{v in I} a_v`,

with arbitrary **signed** coefficients `a_v`. An additional constant term is already included: because every `I` has five vertices, a constant equals a uniform contribution of one-fifth at each vertex.

Let `P1[I,v]=1[v in I]`, `B1=D P1` and `r1=P1^T 1`. Any vertex-additive feasible candidate has `P1 a>=0` and `B1 a>=1` after normalizing minimum coverage to one.

There are exact nonnegative rational dual vectors `lambda_T`, `eta_I` satisfying

`B1^T lambda + P1^T eta = r1`,

with

`sum_T lambda_T = 38484/5127 = 7.5061439438268...`.

Hence every vertex-additive candidate has mass

`r1^T a = lambda^T B1 a + eta^T P1 a >= sum_T lambda_T = 38484/5127 >6`.

The dual equality was reconstructed with exact rational linear algebra and independently checked with integer arithmetic. This proves that a one-body additive ansatz cannot explain the obstruction for this graph, **even with signed vertex coefficients**.

For comparison on the same graph:

| Model | Best LP value or verified bound |
|---|---:|
| Unrestricted five-set weights | `75/13 = 5.7692307692...` (previous exact primal/dual) |
| Signed pair-induced five-set weights | exact generated rational ratio `<5.873` |
| Nonnegative pair-induced weights | exact dual lower bound `>=6.406301` |
| Arbitrary signed vertex-additive weights | exact dual lower bound `>=38484/5127>7.506` |

Therefore **second-order signed incidence is necessary and sufficient for an obstruction in this additive hierarchy**, on graph 1253; and signed second-order incidence is sufficient across all 39 classes.

## 7. What this does not prove

The pair coefficients were obtained through graph-specific linear optimization, then exactly certified. Therefore no classification-independent theorem has yet established `J(c)>0` from 16 vertices, 33 edges, triangle-freeness, and `alpha(H)=5` alone. The number of pair variables is 87, which is not a universal constant; the simplification is in **interaction order**, not in the number of unknown coefficients.

A fixed globally shared linear combination of basic degree and pair-codegree features did not work in the exploratory optimisation. Thus the next question is **which graph-local transport/comparison operation generates a signed pair potential `c` lying in the five-set-positivity cone `Pc>=0` and with `J(c)>0`**.

The precise classification-independent target is a theorem asserting, under the same graph hypotheses,

`exists c in R^(nonedges(H)): P c >=0 and (6 B - 1 r^T)c > 0`.

This statement isolates the sought coherence law as a separation of two incidence cones. It does not require an `esd7` representation, and tests the lowest interaction order shown necessary by the exact dual obstruction.

## 8. Reproduction

Run from the directory with the supplied catalogue:

`python ramsey_pair_conservation_verify.py`

This requires only Python's standard library and these files:

* `r36_16.g6.gz` (uploaded user catalogue)
* `ramsey_pair_conservation_certificates.json` (all 39 signed-pair potentials and six nonnegative-pair duals)
* `ramsey_vertex_affine_dual_1253.json` (exact one-body failure dual)
* `ramsey_r37_full_catalogue_audit.py` (only its graph6 decoder and independent-set enumeration functions; no SciPy functions called)

Optional generation script requiring NumPy and SciPy:

`python ramsey_pair_conservation_build.py`.

The verifier checks the SHA-256 and verifies all inequalities, including all six duals and the one-body dual, using integer arithmetic.
