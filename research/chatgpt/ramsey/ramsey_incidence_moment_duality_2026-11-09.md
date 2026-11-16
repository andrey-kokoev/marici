# The order of Ramsey incidence obstruction and its moment-dual alternative

Date: 2026-11-09. Status: one general finite-dimensional alternative theorem; a complete *catalogue-dependent* calculation of the minimum incidence order for the 39 relevant `R(3,6;16)` residual graphs; one exact restriction on coefficient locality. **No classification-independent existence proof for pair potentials is claimed.**

## 1. Ramsey residual setup

Adopt graph edges as red. A putative 23-vertex triangle-free graph with no independent seven-set reduces, using `R(3,6)=18` and the seven classified 17-vertex `(3,6)` graphs, to a 6-regular graph. Removing a vertex and its six neighbors gives a 16-vertex triangle-free residual graph `H` with 33 edges, independence number five, and degree between two and five. Its six port neighborhoods are independent 5-sets `T_1,...,T_6` in `H`.

Write `F = I_5(H)`. Each independent five-set `I` must meet at least five of the ports: otherwise `I` and two untouched ports would be an independent seven-set. Equivalently,

    sum_{j=1}^6 1[I cap T_j = empty] <= 1  for every I in F.

Let `D` be the symmetric matrix with `D[I,T]=1` when `I cap T` is empty.

## 2. Incidence hierarchy

For `r=0,1,2`, define `P_r[I,A]=1[A subset I]` for `I in F` and independent r-subsets `A` of `V(H)`. A certificate of order r is any *signed* coefficient vector `c` whose induced weights `z=P_r c` satisfy

    z >= 0,   m = min_T (Dz)_T > 0,   sum_I z_I < 6*m.

The elementary double-counting proof excludes the six port neighborhoods: each port accumulates at least `m`; each five-set can be disjoint from at most one port, so the combined accumulation is at most `sum z <6m`.

The hierarchy is nested. Each independent five-set has five vertices and ten pairs. In particular, any vertex-additive weight `z(I)=sum_{u in I} a_u` is also a pair-additive weight by setting `c_{uv}=(a_u+a_v)/4` on all nonedges `uv`; for an independent five-set `I`, each vertex appears in exactly four such pairs. Uniform weights are vertex-additive with `a_u=constant/5`.

## 3. Complete exact finite calculation

Using the independently SHA-256-verified catalogue `r36_16.g6.gz`, there are exactly 39 graphs with 33 edges out of 2,576 records. For those 39 graphs:

| Certificate order | Classes certified | Classes proved unable to support such a certificate |
|---|---:|---:|
| `r=0`, uniform weights | 0 | 39 |
| `r=1`, arbitrary signed vertex coefficients | 19 | 20 |
| `r=2`, arbitrary signed nonedge-pair coefficients | 39 | 0 |

The `r=0` impossibilities are direct integer inequalities `|F|>=6 min_T degree_D(T)`.

The `r=1` successes have explicit signed integer coefficient vectors. For each of the other 20 classes, an exact dual nonnegative rational certificate `lambda,eta` has been reconstructed symbolically and independently checked by integer arithmetic: `B_1^T lambda + P_1^T eta = P_1^T 1`, with `sum lambda >= 6` and `B_1 = D P_1`. Consequently no signed vertex-additive certificate can reach total mass less than six after unit-coverage normalization.

The `r=2` successes have the previously verified integer pair coefficients, each inducing nonnegative five-set weights and a strict `6m-W>0` margin. There is no need to assume individual pair coefficients are nonnegative.

**Conclusion (conditional on catalogue completeness):** uniform weights never suffice; degree-one signed incidence suffices in exactly 19 of the 39 residual isomorphism classes; degree-two signed incidence is essential in the remaining 20 and sufficient in all 39. This concerns the *degree of the certificate polynomial*, not the radius or amount of graph information needed to obtain its coefficients.

## 4. General moment-dual alternative

For any finite family `F` of equally sized sets, with disjointness matrix `D`, fix a subset-incidence matrix `P` (for example `P_r`) and a positive integer `d`. Define

    A = (d D - J) P, where J is the all-ones square matrix.

Then *exactly one* of the following alternatives holds:

**Primal:** there is a real coefficient vector `c` with `P c >= 0` and `A c > 0` componentwise.

**Dual:** there exist a probability vector `lambda >=0` on `F` (`sum lambda=1`) and a nonnegative slack vector `eta >=0` on `F` such that

    P^T (d D lambda + eta) = P^T 1.

Proof: the primal asks whether the polyhedral cone `{A c : P c >=0}` intersects the strictly positive orthant. If it does not, the separating-hyperplane/Motzkin alternative supplies `lambda >=0`, `lambda != 0`, `eta >=0` with `A^T lambda + P^T eta =0`. Normalizing `lambda` to sum one and using symmetry of `D` gives the displayed dual. Conversely, for any primal `c` and dual `lambda,eta`, `lambda^T A c = -eta^T P c <=0`, while `A c>0` and `lambda` nonzero imply `lambda^T A c >0`, contradiction.

**Interpretation:** the dual is an adversarial distribution of putative port neighborhoods whose disjointness exposure can be completed by nonnegative slack so as to match **all selected r-subset marginals** of the uniform five-set measure. For `r=2`, it matches the totals associated to every nonedge vertex pair. Such a balanced pseudo-distribution is the exact obstruction to the existence of a signed pair certificate.

This is a general elementary linear-algebraic alternative, not a newly established universal Ramsey-number formula. It identifies exactly what a classification-independent proof of order-two sufficiency must rule out.

## 5. Sharp boundary controls at 34 edges

Two explicit 16-vertex `(3,6)` graphs with 34 edges have six pairwise compatible independent five-sets `T_1,...,T_6` (provided in `ramsey_boundary_k6_witnesses.json`). Put `lambda` equal to `1/6` on each port; for every independent five-set `I`,

    d(D lambda)_I = # { j : I cap T_j = empty } in {0,1}.

Consequently `eta_I=1-6(Dlambda)_I` is nonnegative, and the **stronger pointwise relation** `6 Dlambda + eta = 1` holds. Hence the pair-moment dual holds for every incidence order, and no fractional certificate of any order can have total mass below six on these controls.

The 33-to-34 transition is real and cannot be explained merely by the size of the five-set universe.

## 6. Exact obstruction to coarse pair-local rules

On catalogue graph 1253 (`OQ?GOKaCQAOOPHaEad\`Ow`), group nonedge pairs by the four-tuple

    (min degree of endpoints, max degree of endpoints,
     number of common neighbors, number of independent five-sets containing the pair).

There are 21 pair types. Even allowing a signed coefficient for each type, the optimal mass is **at least**

    157135/24654 = 6.373610773... > 6.

A separate exact dual with 12 nonzero coverage entries and eight nonzero five-set-positivity entries verifies this lower bound by integer arithmetic. Yet unrestricted signed pair coefficients succeed on the same graph with mass below six.

Thus the pairwise *interaction order* suffices, but coefficients cannot always be chosen as functions of these four coarse pair statistics. This is an exact finite no-go result for that source-local ansatz, not a theorem about every possible notion of locality.

## 7. Strongest remaining target

Eliminate the need for catalogue-based coefficient selection by proving directly from `|V(H)|=16`, `|E(H)|=33`, triangle-freeness and `alpha(H)=5` that **no** probability distribution `lambda` and slack `eta >=0` can satisfy

    P_2^T (6 D lambda + eta) = P_2^T 1.

Equivalently, prove the existence of a signed pair potential `c` with `P_2 c >=0` and `(6D-J)P_2 c>0`.

The hierarchy results constrain the method: a first-order or uniform-marginal argument cannot work across the entire class; and the simple endpoint-degree/codegree/five-frequency pair-local ansatz also fails on graph 1253. The desired theorem needs an additional source of second-order information, a transport rule for that information, or a more intrinsic extremal inequality.

## 8. Reproducible verification

The following run without NumPy, SciPy, or a solver:

- `python ramsey_incidence_order_exact_verify.py`: checks the entire 39-graph uniform/vertex/pair hierarchy with exact integer arithmetic, including all 20 rational dual lower bounds.
- `python ramsey_pairtype_dual_1253_verify.py`: checks the 21-type no-go dual exactly.
- `python ramsey_moment_balance_boundary_verify.py`: checks the explicit pointwise moment dual on both 34-edge controls.

Data:

- `r36_16.g6.gz`: user-supplied 2,576-record catalogue.
- `ramsey_incidence_order_exact_certificates.json`: the 19 first-order successes, 20 first-order dual impossibilities, and all 39 uniform degree checks.
- `ramsey_pair_conservation_certificates.json`: the 39 pairwise successes.
- `ramsey_pairtype_dual_1253.json`: the 21-type no-go dual.
- `ramsey_boundary_k6_witnesses.json`: the two 34-edge counterexamples.

The numerical discovery scripts are separate: `ramsey_incidence_order_exact_generate.py` and `ramsey_pairtype_dual_1253_generate.py`.
