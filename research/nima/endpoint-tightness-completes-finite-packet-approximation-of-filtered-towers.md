# Endpoint tightness completes finite-packet approximation of filtered towers

## Result

Depth control alone does not provide uniform finite-packet approximation. The missing condition is uniform endpoint tightness in every actual-letter source seminorm.

For a family of realized towers, finite-packet truncations converge uniformly exactly when its endpoint tails vanish uniformly at every radius. Together with boundedness, this is also the exact relative-compactness criterion. A proper corner-height moment gives an explicit sufficient tail budget, which combines with the earlier geometric depth bound.

These are source and forcing-resolved approximation results, not inverse estimates from arithmetic response noise.

## 1. Fix finite corners without changing the source

Keep S_Gamma, X_Gamma and Q_R from `uniform-actual-letter-budgets-characterize-realizable-infinite-filtered-towers.md`. The declared endpoint corners form a countable set; each has a finite marked-path basis.

Fix an increasing exhaustion F_H of that corner set by FINITE subsets, H=1,2,..., with union all corners. Write h(c) for the first H containing c. Equivalently, choose a positive integer-valued proper corner height, whose sublevel sets are finite. If using an arithmetic-height convention, finiteness must include all declared packet/background labels; a numerical endpoint alone is not silently assumed to distinguish every label.

Let P_H retain exactly the corners in F_H. It is a contraction for every Q_R. It preserves each cornerwise ideal power, hence induces compatible contractions on all the inherited filtered quotients. It need not be multiplicative for an arbitrary exhaustion; no algebra-homomorphism claim is needed.

For x in X_Gamma define

`T_(R,H)(x)=Q_R((1-P_H)x)`.

For each fixed x, T_(R,H)(x)->0 by absolute summability. This individual convergence supplies no uniform rate on a family.

## 2. The exact tightness and compactness criteria

For a subset A of X_Gamma, finite-corner truncation converges uniformly in the source topology exactly when

`sup_(x in A) T_(R,H)(x) ->0 as H->infinity`, for every R.

Call this uniform endpoint tightness. It is independent of the chosen cofinal finite exhaustion, although numerical rates depend on that exhaustion.

Moreover A is relatively compact in X_Gamma if and only if BOTH conditions hold:

1. `sup_(x in A) Q_R(x)<infinity` for every R;
2. A is uniformly endpoint tight at every R.

Proof of sufficiency: for a specified finite set of seminorms choose their largest radius R. Tightness uniformly approximates A by P_H A in Q_R. This image is a bounded subset of a finite-dimensional space, hence has a finite epsilon-net. Thus A is totally bounded in the Frechet topology. Completeness of X_Gamma makes its closure compact.

Proof of necessity: seminorms are bounded on compact sets. The contractions 1-P_H converge pointwise to zero; a finite epsilon-net in Q_R upgrades this to uniform convergence on any compact set. The same conclusion holds on its subsets.

The argument uses finite corner dimension and positive fixed Gamma weights, not a uniform positive lower bound on all letter weights.

## 3. A genuine bounded family escaping to later corners

Choose infinitely many distinct admitted two-event corners and in each take a forgotten diamond relation a_j. It has two distinct paths, coefficient magnitudes one, and Gamma=1. Put z_j=a_j/4. Then

`z_j in I`, `Q_R(z_j)=R^2` for every j.

Thus this family is bounded at EVERY source radius. Its tower budgets from the previous note are also uniformly bounded: the relation is visible already at depth one, since I^2 vanishes in a two-event corner.

Nevertheless, any finite F_H misses some of these corners, so

`sup_j T_(1,H)(z_j)=1`.

For distinct j,k, Q_1(z_j-z_k)=2. The family has no source-convergent subsequence, and no uniform finite-corner approximation. Arbitrarily large factorial/path-radius budgets cannot cure this fixed-length location escape.

The example uses existing forgotten arrows and the original relation ideal. It does not introduce new forcing letters, root states, or an arithmetic-response kernel.

## 4. An explicit sufficient location budget

For eta>0 introduce the optional PRIOR seminorm

`Q_(R,eta,h)(x)=sum_c n(c)! R^n h(c)^eta ||x_c||_Gamma`.

This is a quantitative extra hypothesis, not a redefinition of S_Gamma or of any completed source already declared. Since h(c)>H outside F_H,

`T_(R,H)(x) <= (H+1)^(-eta) Q_(R,eta,h)(x)`.

A prescribed power moment is sufficient, not necessary for tightness. The exact criterion remains section 2; it allows other uniformly vanishing endpoint-tail moduli.

## 5. Combine finite filtration depth and finite endpoint support

Suppose a compatible tower t is realized by x. Level m determines every actual corner of length n<=2m+1. Define the finite source reconstruction

`A_(m,H)(t)=P_H [x restricted to n<=2m+1]`.

This is determined by the finitely many stabilized corner coordinates of t_m in F_H. It has finite marked-path support and belongs to I. No representative of the entire quotient is chosen, and it need not lift t_m in the omitted corners.

For integer R'>R, let B_(R')(t)=Q_(R')(x), as in the bounded-limit theorem. Splitting omitted corners into long ones and the remaining endpoint tail gives

`Q_R(x-A_(m,H)(t))
 <= (R/R')^(2m+2) B_(R')(t)+T_(R,H)(x)`.

Under the extra location prior Q_(R',eta,h)(x)<=M, both terms are bounded explicitly:

`Q_R(x-A_(m,H)(t))
 <= M[(R/R')^(2m+2)+(H+1)^(-eta)]`.

Thus any prescribed positive source tolerance can be reached by finite m and H on this prior ball. This controls omission error; precision errors in the retained coefficients require their own budget.

## 6. Noisy finite-corner quotient data

Let x,y be genuine source candidates with Q_(R',eta,h)(x),Q_(R',eta,h)(y)<=M. Let d_(R,m,H) be the inherited Q_R quotient seminorm of

`P_H([x]_m-[y]_m)`.

All short corners in F_H are stabilized, so their exact source difference is bounded by d_(R,m,H). The omitted long corners and endpoint tail give

`Q_R(x-y)
 <= d_(R,m,H)
    +2M[(R/R')^(2m+2)+(H+1)^(-eta)]`.

This is a finite-corner, finite-depth stability estimate with an explicit prior. If two candidates each fit the same quotient data within epsilon in that seminorm, replace d_(R,m,H) by 2epsilon. Arbitrary noisy quotient data are not asserted to have a source lift or to satisfy exact source identities.

In particular d_(R,m,H) is NOT the labelled arithmetic response norm. The formula does not bypass the previously proved analytical inverse obstructions.

## 7. Forcing-resolved error and limits of the conclusion

For R_0=ceil(2 lambda s b), the supplied full Fox-map bound is

`||D(z)||_(F_(s,b))<=2Q_(R_0)(z)`.

Consequently, for R'>R_0 and the prior at that radius,

`||D(x)-D(A_(m,H)(t))||_(F_(s,b))
 <=2M[(R_0/R')^(2m+2)+(H+1)^(-eta)]`.

The candidate comparison in section 6 similarly acquires a factor two. Independently bounded receiver observations can be applied afterward with their declared norms.

This supplies genuinely finite source and forcing-resolved approximations, unlike length truncation alone. It does not discretize the arithmetic response fields, calibrate the attachment observer, or identify noisy vectors with cycles. Voevodsky's finite-prime attachment certificate remains a separate result in its own measurement topology.

If the old common-path source is also required, impose and track its endpoint tails and seminorms as well. Gamma-weighted approximation does not silently imply approximation in that stronger independent source requirement.

## Verification

`uv run python research/nima/checkers/check_endpoint_tightness.py`

Exact checks cover actual forgotten diamond normalization, disjoint-corner escape, and combined depth/height estimates on finite rational coefficient fixtures. The infinite compactness theorem uses the finite-net and completeness proof above, not a finite rank experiment.
