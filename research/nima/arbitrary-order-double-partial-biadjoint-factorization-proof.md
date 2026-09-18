# Arbitrary-order double-partial biadjoint factorization

## Theorem

Let `alpha` and `beta` be arbitrary cyclic orders on the same `n>=4` labels. Let `G(alpha,beta)` be the set of cubic trees planar in both orders, and define the unit-coefficient common-tree function

$$
m_n(\alpha\mid\beta)
=
\sum_{g\in G(\alpha,\beta)}
\prod_{e\in g}\frac1{X_e}.
$$

Fix a nontrivial split `S | S^c`. If `S` is a cyclic interval in both `alpha` and `beta`, then `X_S` is a common physical channel and

$$
\operatorname{Res}_{X_S=0}m_n(\alpha\mid\beta)
=
m_L(\alpha_L\mid\beta_L)
 \,m_R(\alpha_R\mid\beta_R),
$$

where each induced order is obtained by restricting its parent cyclic order to one side and inserting one internal cut label `I` at the cut. If `S` is not a cyclic interval in either order, no common planar tree contains that channel and the residue is zero.

This statement concerns the unit-coefficient common-tree convention. Any separate convention-dependent overall signs of color-ordered double-partial amplitudes must be restored consistently on both sides.

## Common-channel criterion

An internal edge of a planar cubic tree separates the external labels into two cyclic intervals in the embedding order. Therefore a channel can occur in an `alpha`-planar tree only if one side of its split is an `alpha` interval. The same condition holds for `beta`.

Hence `X_S` can occur in a common tree only if `S` (equivalently `S^c`) is an interval in both cyclic orders. Conversely, if it is an interval in both, choose arbitrary planar trees on each cut side and glue them at the internal leaf. The glued tree is planar in both orders, so the common channel occurs.

## Restriction map

Let

$$
G_S(\alpha,\beta)
=
\{g\in G(\alpha,\beta):S\in g\}.
$$

Cutting the edge `S` of `g` produces two cubic trees `g_L` and `g_R`, each with a new leaf `I`. Because the original embedding is planar in `alpha`, these trees are planar in the induced orders `alpha_L` and `alpha_R`. Planarity in `beta` similarly gives planarity in `beta_L` and `beta_R`. Thus cutting defines

$$
\Phi:G_S(\alpha,\beta)
\longrightarrow
G(\alpha_L,\beta_L)\times
G(\alpha_R,\beta_R).
$$

## Gluing inverse

Given a pair `(g_L,g_R)` in the product, identify their two leaves labelled `I` and replace them by one internal edge. The induced cyclic orders place `I` at exactly the two cut positions in both `alpha` and `beta`; consequently the glued tree is planar in both parent orders. Cutting its distinguished edge recovers the original pair.

Cutting and gluing are inverse operations, so `Phi` is a bijection for arbitrary orders and arbitrary multiplicity.

## Residue factorization

Multiplying by `X_S` and setting `X_S=0` retains exactly the common trees containing the cut edge. Under the bijection, every remaining propagator belongs to exactly one cut side, so its monomial splits:

$$
\prod_{e\in g\setminus\{S\}}X_e^{-1}
=
\left(\prod_{e\in g_L}X_e^{-1}\right)
\left(\prod_{e\in g_R}X_e^{-1}\right).
$$

Therefore

$$
\begin{aligned}
\operatorname{Res}_{X_S=0}m_n(\alpha\mid\beta)
&=
\sum_{g\in G_S(\alpha,\beta)}
\prod_{e\ne S}X_e^{-1}\\
&=
\sum_{g_L,g_R}
\left(\prod_{e\in g_L}X_e^{-1}\right)
\left(\prod_{e\in g_R}X_e^{-1}\right)\\
&=
m_L(\alpha_L\mid\beta_L)
  m_R(\alpha_R\mid\beta_R).
\end{aligned}
$$

## Arbitrary-order symmetries

The same common-tree definition proves, without finite enumeration,

$$
m_n(\alpha\mid\beta)=m_n(\beta\mid\alpha).
$$

Indeed, `G(alpha,beta)` is the intersection of the two planar-tree sets, and set intersection is symmetric.

Rotating or reversing the written representative of either cyclic order does not change which abstract trees admit a planar embedding in that order. Therefore `m_n` is independently invariant under the dihedral presentation changes

$$
(\alpha,\beta)
\longmapsto
(g\alpha,h\beta),
\qquad g,h\in D_n,
$$

when `g` and `h` act only by choosing an equivalent rotation or reversal of the same labelled cyclic order. These are presentation symmetries, not arbitrary permutations of labels in one order.

Finally, every simultaneous relabelling permutation `pi` induces a bijection

$$
G(\alpha,\beta)
\longrightarrow
G(\pi\alpha,\pi\beta),
$$

and sends each channel variable `X_S` to `X_(pi S)`. Hence the function is covariant under simultaneous relabelling. These symmetries commute with the cut-and-glue factorization bijection.

## Consequences

- Every common physical pole is simple.
- The residue support is exactly a Cartesian product of the two side supports.
- The number of residue terms is the product of the two lower common-tree counts.
- No channel incompatible with either cyclic order appears.
- Exchange symmetry, independent cyclic/reversal presentation invariance, and simultaneous relabelling hold for arbitrary orders.

## Relation to executable evidence

`check_double_partial_biadjoint_factorization.py` tests selected order pairs for `4<=n<=9` and verifies 542 channel factorizations. `check_exhaustive_double_partial_biadjoint_factorization.py` exhausts all cyclic orders modulo rotation and reversal through seven points: 66,894 unordered order pairs and 205,149 common-channel factorizations, all with exact Cartesian-product support. The arbitrary-order theorem follows from the cut-and-glue bijection rather than either finite range.

## Claim boundary

This proves support and unit-coefficient factorization for tree-level double-partial biadjoint functions. It does not fix convention-dependent signs between arbitrary orderings, construct a positive geometry for every order pair, or address loop-level and color-dressed amplitudes.
