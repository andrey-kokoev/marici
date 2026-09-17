# Arbitrary-n double-partial biadjoint tree amplitudes

## Definition

Let `alpha` and `beta` be cyclic orders on the same finite label set `L`, with `|L|=n`. A channel is a proper bipartition `S | (L\S)`, identified with its complement. It is planar in a cyclic order when one side is a cyclic interval. A cubic tree is planar in an order precisely when all of its `n-3` channels are planar in that order.

Define

\[
m_n[\alpha\mid\beta]
=\sum_{T\in\mathcal T(\alpha)\cap\mathcal T(\beta)}
 \prod_{e\in T}\frac1{X_e}.
\]

The sum is finite because a cyclic order has only `C_{n-2}` planar cubic trees.

## Theorem

For every finite `n>=3` and every pair of cyclic orders:

1. `m_n[alpha|beta]=m_n[beta|alpha]`.
2. Simultaneous relabelling of both orders and channel variables leaves the amplitude unchanged.
3. The amplitude vanishes exactly when the two orders admit no common planar cubic tree.
4. Every pole is a simple channel planar in both orders.
5. On every common channel `d=S|(L\S)`, the residue factors as

   \[
   \operatorname{Res}_{X_d=0}m_n[\alpha\mid\beta]
   =m_{S\cup\{*\}}[\alpha_L\mid\beta_L]\,
    m_{(L\setminus S)\cup\{*\}}[\alpha_R\mid\beta_R],
   \]

   where `*` is the cut leg and each induced order is obtained by collapsing the opposite interval to `*`.

## Proof

Claims 1 and 2 follow because intersection and relabelling commute:

\[
\mathcal T(\alpha)\cap\mathcal T(\beta)
=\mathcal T(\beta)\cap\mathcal T(\alpha),
\qquad
g(\mathcal T(\alpha)\cap\mathcal T(\beta))
=\mathcal T(g\alpha)\cap\mathcal T(g\beta).
\]

Claim 3 is immediate from the finite defining sum with unit coefficients.

Each tree is a set of channels, so a channel variable occurs at exponent zero or minus one in every term. This proves simplicity. A pole can occur only when its channel belongs to a tree in both planar-tree sets, hence is planar in both orders. Conversely, every channel in a common tree occurs in the amplitude.

Fix a common channel `d`. Cutting any common tree `T` along `d` produces two cubic trees `T_L,T_R`. Planarity of `T` in `alpha` implies planarity of each restriction in the induced orders `alpha_L,alpha_R`; the same statement holds for `beta`. Thus cutting defines

\[
\{T\in\mathcal T(\alpha)\cap\mathcal T(\beta):d\in T\}
\longrightarrow
(\mathcal T(\alpha_L)\cap\mathcal T(\beta_L))
\times
(\mathcal T(\alpha_R)\cap\mathcal T(\beta_R)).
\]

This map is injective because the original channel set is recovered as `T_L union {d} union T_R`. It is surjective because gluing any pair of common-planar side trees along `*` yields a cubic tree whose channels are noncrossing in both original cyclic orders. Therefore it is a bijection.

After multiplying by `X_d` and setting `X_d=0`, only trees containing `d` remain. Under the cut bijection their propagator monomials split into the product of left and right monomials. Distributing the finite sum over the Cartesian product proves the residue formula.

All arguments apply to every finite label set and do not depend on a multiplicity bound.

## Executable instances

- `check_double_partial_biadjoint_common_trees.py` enumerates common trees for selected order pairs at `4<=n<=9`.
- `check_double_partial_biadjoint_factorization.py` exhausts 542 common-channel factorizations and verifies the Cartesian-product support identity.

The enumeration checks the implementation; the cut/glue bijection supplies the arbitrary-n proof.

## Boundary

This proves tree-level double-partial support, symmetry, pole simplicity, vanishing, and factorization. It does not yet establish CHY localization, inverse KLT relations, loop amplitudes, or amplitudes with non-unit numerators.
