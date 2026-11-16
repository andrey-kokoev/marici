# Ramsey Circuit Cover and Latent-Mode Formation

**Date:** 2026-11-08  
**Scope:** Exact local-to-global characterization of simultaneous vertex extensions for triangle-free graphs, including the sharp distinction between maximum and maximal independent sets. Self-contained proofs and a standard-library checker. No general formula for `R(3,k)` is asserted.

## 1. Source problem

Represent a red/blue edge coloring of a complete graph by the red graph `G`. Ramsey-admissibility at parameter `k` is

\[
 G\text{ triangle-free},\qquad \alpha(G)\le k-1.
\]

Take such a red graph `G`, and adjoin new vertices `W={v_1,...,v_m}`. Let `H` be the red subgraph on `W`; let `S_i⊆V(G)` be the red neighbors of `v_i` inside `G`. Write `S(J)=⋃_{i∈J}S_i`.

The enlarged graph `F` is triangle-free **if and only if**:

1. Every `S_i` is independent in `G`.
2. `H` is triangle-free.
3. If `ij∈E(H)`, then `S_i∩S_j=∅`.

Every independent subset of `F` decomposes uniquely as an independent subset `J` of `H` plus an independent subset of `G-S(J)`. Thus

\[
\boxed{\alpha(F)=\max_{J\in\operatorname{Ind}(H)} \bigl(|J|+\alpha(G-S(J))\bigr).}\tag{1}
\]

This is the complete simultaneous-extension theorem; there is no assumption that the new vertices are mutually blue.

## 2. Why *all maximal* old independent sets matter

Let `MaxInd(G)` denote **inclusion-maximal** independent sets (which need not have cardinality `α(G)`). For every `U⊆V(G)`:

\[
\alpha(G-U)=\max_{I\in\operatorname{MaxInd}(G)}|I\setminus U|.\tag{2}
\]

Proof: each independent set of `G-U` extends to an inclusion-maximal independent set of `G`, without decreasing the number of surviving vertices.

For each `I∈MaxInd(G)`, define the slack `b_I=k-1-|I|≥0`. The independence condition (1) is equivalent to

\[
\boxed{|J|-|I\cap S(J)|\le b_I\quad
\text{for every }I\in\operatorname{MaxInd}(G),\ J\in\operatorname{Ind}(H).}\tag{3}
\]

Checking only maximum old independent sets is sufficient for **one** new vertex, but generally insufficient for **several** new vertices.

## 3. Transversal-matroid circuit-cover theorem

For each `I∈MaxInd(G)`, form a bipartite graph `B_I`:

- left vertices: the prospective new vertices `W`;
- right vertices: the old elements of `I`, plus `b_I` distinguishable dummy capacity slots;
- `v_i` meets `x∈I` exactly when `x∈S_i`;
- every `v_i` meets every dummy slot.

The subsets of `W` admitting injections/matchings into the right side form a **transversal matroid** `M_I`.

**Theorem (circuit-cover characterization).** Assuming the three triangle conditions in §1, the complete extension `F` is Ramsey-admissible if and only if

\[
\boxed{\operatorname{Ind}(H)\subseteq
\bigcap_{I\in\operatorname{MaxInd}(G)}\operatorname{Ind}(M_I).}\tag{4}
\]

Equivalently, every circuit `C` of every `M_I` must contain a red edge of `H`:

\[
\boxed{\forall I\ \forall C\in\operatorname{Circ}(M_I),\quad E(H[C])\ne\varnothing.}\tag{5}
\]

**Proof:** Hall's marriage theorem for `B_I` says `J⊆W` is matchable precisely when, for every `T⊆J`,

\[
 |T|\le |I\cap S(T)|+b_I.
\]

If `J` is independent in `H`, so is every `T⊆J`. Therefore (3) for every independent `T` is equivalent to `J` being independent in each `M_I`. A subset is matroid-dependent iff it contains a circuit. An `H`-independent subset cannot contain a circuit exactly when every circuit contains an `H`-edge. This proves (4)–(5).

**No common matching is imposed across different `I`.** A matching is a certificate of a numerical capacity inequality for that particular old independent set, not a physical assignment that must be consistent between alternative old independent sets. Demanding a simultaneous matching would introduce an unjustified extra condition.

### 3.1 A direct edge-cover reformulation

For fixed `G` and fixed independent neighborhoods `S_i`, an admissible red graph `H` on the new vertices exists exactly when there is a triangle-free graph `H` satisfying:

- Every red edge `ij` in `H` is allowed by `S_i∩S_j=∅`.
- For every circuit `C` in the union of all `Circ(M_I)`, at least one pair in `C` is chosen as a red `H`-edge.

This is a constrained **circuit edge-cover** problem. Pairwise compatibility matrices capture only the two-vertex shadow; larger circuits are the exact missing higher-arity requirements.

## 4. An exact successor law in k: matching nullity

Remove the dummy slots temporarily. Let `ν_I(J)` be the largest matching size from `J` to the actual old vertices in `I`, and define the matching nullity

\[
 h_I(J)=|J|-\nu_I(J).
\]

Adding `b_I` universally available dummy slots makes `J` matchable exactly when

\[
\boxed{h_I(J)\le b_I=k-1-|I|.}\tag{6}
\]

This is equivalent to (3) when tested over all `H`-independent `J` (via Hall's theorem).

At fixed `G`, fixed `H`, and fixed `S_i`, raising `k` to `k+1` increases every `b_I` by one. In other words, the relevant matroid is the **one-step elongation** of the previous transversal matroid. A family with nullity exactly `b_I+1` becomes matchable at the successor parameter. Other families with larger nullity can remain obstructed.

This is an exact algebraic successor of the *local constraint field*, not a claim that the entire extremal graph family at `k+1` is obtained by elongating one preferred graph at `k`.

Because a transversal matroid on these ports has rank at most `k-1`, every circuit has size at most `k`. This upper bound is sharp: minimal obstruction arities `2,3,...,k` are constructible.

## 5. Minimal incompatible sets have zero private incidence

For a fixed old maximal independent set `I`, let

\[
 d_I(J)=|J|-|I\cap S(J)|-b_I.
\]

Suppose `J` is inclusion-minimal among sets with `d_I(J)>0` (with no need to assume H is blue-complete). For each `i∈J`, let

\[
 p_i=\bigl| (S_i\cap I)\setminus\bigcup_{j\in J\setminus\{i\}}S_j\bigr|.
\]

Then

\[
 d_I(J)-d_I(J\setminus\{i\})=1-p_i.
\]

Minimality forces `d_I(J)=1`, `d_I(J\setminus\{i\})=0`, and `p_i=0` for every `i`.

Thus a minimal Hall-deficient family has **exactly one unit of deficit** and **no member carries private old capacity** relative to the full deficient family. Its constraints depend on collective overlap or on auxiliary slack rather than a private resource.

## 6. Two different origins of higher-order failure

### Example A: repeated use of the same capacity

Let `k=4`, let `G` be the empty graph on `{a,b,c}`, and add three mutually blue vertices `u,v,w`, all with identical red neighborhood `{a,b}`.

The only old maximal independent set is `{a,b,c}` (size three, zero slack). Each of `u,v,w` has the same two eligible old sites `a,b`.

- Any one or two new vertices have a matching and produce a Ramsey-valid graph.
- All three cannot match into just two sites: the three-element set `{u,v,w}` is a matroid circuit.
- A red edge between any pair of new vertices would create a red triangle through `a` or `b`, so **the circuit is unrepairable** by choosing red edges among new vertices.

### Example B: latent smaller maximal independent set becomes critical

Let `k=4`, let `G` be the three-leaf star with center `c` and leaves `a,b,d`. Add mutually blue vertices `u,v,w` with neighborhoods `{a}`, `{b}`, `{d}` respectively.

The two inclusion-maximal old independent sets are:

- `{a,b,d}` (size 3, slack 0). The matching of `u,v,w` to `a,b,d` is **perfect**, so this maximum independent set does not obstruct the triple.
- `{c}` (size 1, slack 2). No new vertex has any red neighbor in `{c}`. Three new vertices demand three units against two dummy slots: the triple is a circuit of the **latent smaller mode**.

The maximal independent set containing the center evolves as follows:

| Number of added vertices | Latent maximal independent set | Size |
|---:|---|---:|
| 0 | `{c}` | 1 |
| 1 | `{c,u}` | 2 |
| 2 | `{c,u,v}` | 3 |
| 3 | `{c,u,v,w}` | 4, forbidden |

Every proper subassembly is valid for `k=4`. Unlike Example A, adding a red edge `uv` **repairs** the obstruction because `{a}∩{b}=∅`: the final graph remains triangle-free and its independence number returns to at most three.

This is a concrete mechanism by which the previous stage's apparently subcritical independent-set mode grows into the obstruction.

### Arbitrarily high minimal arity

For `k≥3` and any `2≤t≤k`, take `G` empty on `k-1` old vertices, choose the same `t-1` old vertices as red neighborhood of each of `t` mutually blue new vertices.

For `m≤t` new vertices:

\[
\alpha_m=\max(k-1,\ k-t+m).
\]

Thus every `m<t` subassembly is valid, but the complete `t`-vertex assembly violates the Ramsey bound. Its minimal obstruction circuit has size exactly `t`. No fixed universal pairwise/triplewise test suffices for all `k`.

## 7. An exact recurrence for maximal independent sets

Take a single valid vertex extension `G'=G+v_S`. Inclusion-maximal independent sets update as

\[
\boxed{
\operatorname{MaxInd}(G')=
\{I\in\operatorname{MaxInd}(G):I\cap S\ne\varnothing\}
\ \cup\
\{\{v\}\cup J:J\in\operatorname{MaxInd}(G-S)\}.
}\tag{7}
\]

Here the two parts are distinct because the latter contains `v`.

**Proof:** an old independent set is maximal in `G'` precisely when it was maximal in `G` and cannot be augmented by `v`, i.e. it intersects `S`. An independent set containing `v` is maximal precisely when its remaining members form a maximal independent set of `G-S`.

This is a complete update rule for the old independent-set modes that parameterize the new circuit-cover system. It explains why retaining only maximum independent sets loses relevant data after further extensions.

## 8. Verification

The companion standard-library script is `ramsey_transversal_matroid_circuits.py`.

It independently evaluates each proposed extension by constructing the whole red graph, directly checking red triangles and independence number, and comparing with both the original family inequalities and the transversal-matroid circuit criterion.

Executed results:

```text
Exhaustive equivalence cases: 37101
Triangle-free labeled bases: 10
Maximal-independent-set update tests: 50
Matching-nullity/elongation checks: 73552
Latent mode sizes: [1, 2, 3, 4]
PASS
```

Exhaustive domain: every labeled triangle-free graph on one, two, or three old vertices; `k` from `α(G)+1` through 5; every independent choice of up to three new red neighborhoods (with repetitions allowed); every red graph on those new vertices. Additional direct controls include the three-leaf star and all sharp obstruction arities through `k=9`.

These finite checks are regressions for the separately proved all-finite theorem, not a proof of Ramsey thresholds.

## 9. Next mathematical target

The full simultaneous extension problem is now reduced to:

1. maintain all inclusion-maximal independent sets under (7);
2. construct the induced matching matroids for prospective new neighborhoods;
3. cover every matroid circuit by allowed red edges among new vertices, without creating red triangles;
4. determine whether the resulting **circuit-cover state** has an invariant or finite compression that preserves future extensions.

In particular, the test should distinguish:

- **overlap exhaustion**: multiple new vertices share too few old neighbor sites;
- **latent-mode promotion**: a smaller inclusion-maximal old independent set has unspent slack but no new coverage, and grows until forbidden;
- **edge repair incompatibility**: a circuit requires an internal red edge, but all such choices may be forbidden by overlaps or by other red edges.

All three mechanisms are consequences of the same exact theorem. A connection between their circuit orbit statistics and the values of `R(3,k)` remains to be demonstrated; no symmetry group such as `S_5` or `M_24` is inferred from the existence of a circuit of corresponding size.
