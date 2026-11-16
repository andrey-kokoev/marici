# Integer defect diffusion on Ramsey independent-set disjointness graphs

Date: 2026-11-09  
Scope: R(3,7), classification-dependent finite verification and a graph-equivariant certificate-generation rule.  
Status: A single integer-only recurrence generates an exact fractional obstruction certificate on all 39 possible 33-edge, 16-vertex residual graphs. It has **not** been proved analytically that it must succeed independently of the known exhaustive graph catalogue.

## 1. Mathematical object

Let `H` be a triangle-free 16-vertex graph with no independent six-set. Write

`F(H) = {I ⊆ V(H) : |I|=5 and I is independent}`.

Construct the symmetric 0/1 *disjointness* matrix `D` indexed by `F(H)`:

`D[T,I] = 1` if `T∩I=∅`, and `0` otherwise.

The graph with adjacency `D` is an induced subgraph of the Kneser graph `KG(16,5)`, restricted to the independent five-sets of `H`. The fractional certificate sought is a nonnegative vector `y` with

`D y >= 1` and `sum(y) < 6`.

This is the fractional total domination inequality for that disjointness graph, with strict target six. The standard concept of fractional total domination is not novel; the specific graph family, threshold test, and integer generator below are the present subject.

### Why it rules out six ports

If `H` is the residual graph of a hypothetical 23-vertex 6-regular triangle-free graph of independence number at most six, its six independent port neighborhoods `T_1,...,T_6` are members of `F(H)`. Each independent five-set `I` is disjoint from **at most one** `T_j`: otherwise `I` together with two unmatched ports forms an independent seven-set.

If `Dy >= 1`, then `6 <= sum_j (Dy)[T_j] <= sum_I y[I]`. Therefore `sum(y) < 6` is a contradiction. This argument does not require the port degree-cover equations once the candidate neighborhoods are known to be independent five-sets.

Equivalently, any such `y` induces a probability distribution `mu(I)=y[I]/sum(y)`, satisfying `min_T P_{I~mu}[I∩T=∅] > 1/6`.

## 2. The source-generated recurrence

The parameters depend only on `n=|V(H)|`, not on which catalogue graph is supplied:

- `Q=n^5` (integer scale);
- `λ=1/n` (weight penalty);
- `N=n^3` (number of updates);
- `Δ=max_T sum_I D[T,I]` and `L=Δ^2` (incidence-dependent safe step denominator).

Start from the zero integer vector `z_0=0`. For `t=0,...,N-1`, compute all entries with **integer arithmetic**:

`r_t(T) = max(0, Q - sum_{I disjoint T} z_t(I))`

`z_{t+1}(I) = max(0, z_t(I) + floor((sum_{T disjoint I} r_t(T) - Q/n)/L))`.

At the end set

`m = min_T sum_{I disjoint T} z_N(I)` and `W = sum_I z_N(I)`.

The output certificate is simply `y(I)=z_N(I)/m`, provided `m>0` and `W<6m`. There is no rounding of a numerical LP solution: `z_N`, `m`, `W`, and all checks are integers. `mu(I)=z_N(I)/W` is the generated probability distribution.

### Why this counts as a single generative operation

The update at an independent set depends only on its neighbors in the disjointness graph and on each neighbor's current coverage deficit. No catalogue index, isomorphism type, optimal LP coefficients, global graph invariant, or desired certificate support is used to select its next value.

The process is **equivariant under graph relabeling**: a vertex permutation induces a permutation of `F(H)`, conjugates `D` by its permutation matrix, and correspondingly permutes every `z_t`. The scalar parameters and `Δ` are invariant. It therefore produces a canonical, label-covariant output for a fixed graph and specified parameters.

The rule is local on the *disjointness graph* of five-sets, not local on the original 16-vertex graph: constructing the graph of all independent five-sets is global combinatorial preprocessing. The number of iterations and the penalty `1/n` were selected after finite experimentation and **are not yet consequences of a structural Ramsey theorem**.

### Variational interpretation

Without integer rounding, the rule is projected gradient descent for the convex penalty

`E(y) = (1/2) sum_T (max(0,1-(D y)[T]))^2 + (1/n) sum_I y[I]`.

Its gradient is `-D(1-Dy)_+ + (1/n) 1`. As `D` is symmetric and has maximum row sum `Δ`, `||D||_2<=Δ`, so the gradient has Lipschitz constant at most `Δ^2`. The integer floor is a fixed discretization of that flow. This variational identification explains the repair dynamics and guarantees equivariance, but **does not prove** its finite-step threshold for the Ramsey graph class.

## 3. Exact exhaustive results

The uploaded `r36_16.g6.gz` has SHA-256:

`5fd4e68d880e1d4ed05337b97cba0ce15387e1f545744aed80b91bb4b2186f25`.

It contains 2,576 graph6 records. Exactly 39 have 33 edges; their maximum degrees, independent-set restrictions, and graph identities are checked by the independent verification code. For every one of those 39 graphs, the above single integer rule (`n=16`, `Q=1,048,576`, `N=4,096`) yields `m>0` and `W<6m`.

| Quantity | Exhaustive 33-edge result |
|---|---:|
| Graphs | 39 |
| Generated certificates passing integer verification | 39 |
| Failed certificates | 0 |
| Maximum exact mass `W/m` (decimal) | 5.939933085574381 |
| Maximum exact mass as a reduced fraction | 608956/102519 |
| Attaining graph's source-record index (1-based) | 1253 |
| Its integer `W`, `m`, and slack `6m-W` | 6,089,560; 1,025,190; 61,580 |
| Earliest successful updates, across all 39 | 10 through 3,193 |
| Median first successful update | 149 |

For the hardest final certificate, the avoidance probability is at least `m/W ≈ 0.1683520648454`, exceeding `1/6` by approximately `0.00168539817874`.

The independent *standard-library-only verifier* recomputes all independent five-sets from the original source graph6 file and checks each of the 39 generated integer certificates; it does not run the gradient generator, trust floating-point arithmetic, or invoke LP optimization. The generator itself uses `numpy` with signed 64-bit integer operations only; all numerical quantities in the 16-vertex instance are safely below overflow bounds.

**Proof status:** This is an exhaustive verified finite-generation theorem *conditional on the external catalogue's completeness*. It is not a catalogue-free proof of the generating law.

## 4. Sharpness and attempted falsification

The 16-vertex catalogue also contains five 32-edge graphs and 200 34-edge graphs. The same unaccelerated integer recurrence succeeds on all five 32-edge graphs and on 197 of the 200 34-edge graphs.

Two of the three 34-edge failures are genuine obstructions to `sum(y)<6`, not failures of the algorithm. The graphs with graph6 strings

- `O?Sp@A?CgK@Lc_PDgLSQo`
- `O@GWOIAOWccKPBaBIOLAD`

have explicit collections of **six independent five-sets** `T_1,...,T_6` whose neighborhoods in the disjointness graph are pairwise disjoint. Consequently any fractional cover `Dy>=1` has `sum(y)>=6` by exact dual counting. The six-set witnesses and a standard-library verifier are provided separately.

One additional 34-edge graph, `OoCOWODC@IgUGKOoe?iOT`, did not pass this particular integer recurrence in 4,096 steps although a numerical LP found mass `17/3≈5.666667`. Thus nontermination of this generator at a fixed step bound does **not** imply nonexistence of a fractional certificate.

In particular, the strict six-bound is **not valid for all** 16-vertex (3,6)-graphs with 34 or more edges. Its structural proof must use finer hypotheses than just triangle-freeness and independence number five; the 33-edge incidence constraint is one essential discriminator.

## 5. General degree-saturation theorem and the origin of symmetry

The square, self-adjoint disjointness operator is **not an arbitrary geometric choice**. Its two index roles coincide for a structural reason.

**Degree-saturation theorem.** Let `G` be a triangle-free, `(k−1)`-regular graph with `alpha(G)<=k−1`. Choose `v`; set `S=N(v)` and `H=G−N[v]`. The `k−1` neighbors of `v` are mutually nonadjacent, and each has exactly `k−2` neighbors inside `H`. Each port neighborhood `T_s=N_G(s)∩H` is therefore an independent `(k−2)`-set. For every independent `(k−2)`-set `I` of `H`, at most one of these `k−1` neighborhoods is disjoint from `I`, since two avoided ports together with `I` would make an independent `k`-set. Therefore, if the square disjointness matrix `D` on independent `(k−2)`-sets satisfies `Dy>=1` with nonnegative `y` and `sum(y)<k−1`, **no such `G` can exist**.

This proof is independent of any graph catalogue and works for every `k` satisfying its assumptions. In a hypothetical `(k−1)`-regular graph of order `N`, the residual graph has

`|V(H)| = N−k`, and `|E(H)| = (k−1)(N−2k+2)/2`.

For `(N,k)=(23,7)`, these specialize to 16 vertices and 33 edges. The **self-duality** is the equality of the port-neighborhood size `k−2` and the size of the independent witnesses `k−2`. Without degree saturation, the natural incidence matrix is generally rectangular, with different types of ports and witnesses.

This theorem explains why a symmetric `D=D^T` and a two-way deficit/weight diffusion arise naturally in the `R(3,7)` calculation. It does **not** force degree saturation in other Ramsey problems; that step requires a separate argument.

## 6. The next theorem worth proving

For every triangle-free `H` on 16 vertices with `e(H)=33` and `alpha(H)=5`, can one derive from its incidence structure, without classification, that the above integer flow necessarily reaches `W<6m` by `n^3` steps?

A weaker but cleaner first target is the existence of a fractional total dominating vector with mass strictly less than six, independent of its construction. A stronger target would derive a *combinatorial lower bound on the final coverage-margin function* `J(z)=6 min(Dz)-sum(z)` in terms of degree, independent-set extension, or overlap counts. The observed existence of positive `J(z)` for all 39 graphs is exact; a structural estimate is missing.

The general `R(3,k)` problem would replace independent five-sets by independent `(k-2)`-sets and six ports by `d` ports. A nonnegative measure on those sets with minimum disjointness probability greater than `1/d` forbids the port configuration. No universal choice of the diffusion parameters or threshold for arbitrary `k` has been proved.

## 7. Reproduction

- `ramsey_integer_diffusion_generator.py`: uniformly builds all 39 integer witnesses without LP solvers, writes `ramsey_integer_diffusion_certificates.json`.
- `ramsey_integer_diffusion_verify.py`: independently verifies all integer inequalities against the source graph6 catalogue (standard library only).
- `ramsey_boundary_k6_witnesses.json` and `ramsey_boundary_k6_verify.py`: independently check six-neighborhood witnesses on the two 34-edge controls.
- Source file `r36_16.g6.gz`, checksum above.

For the existing complete six-port proof (including exclusion of degree-five vertices), see `ramsey_r37_complete_six_port_obstruction_2026-11-09.md`. The present result replaces the 39 per-graph LP certificate **generation** operations with a single uniformly defined integer process; it does not remove the use of the complete catalogue in proving the process succeeds for all admissible residual graphs.
