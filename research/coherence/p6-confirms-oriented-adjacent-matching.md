# Rank six confirms the oriented adjacent-matching law

## Construction

For six oriented axes, form the Pfaffian expansion over all fifteen perfect matchings. For each matching

\[
M=\{(i_1,j_1),(i_2,j_2),(i_3,j_3)\},
\]

compose the three two-cochain operators \(\mathcal F_{i_kj_k}\) in all six orders. Sum those compositions, then combine the fifteen matching terms with their Pfaffian signs.

This is the operator-valued symmetric three-cup appropriate to even-degree two-cochains. No preferred matching is supplied.

## Result

For six distinct positive lengths with order statistics

\[
a_{(0)}<a_{(1)}<\cdots<a_{(5)},
\]

the endpoint expression again reduces to exactly one evaluation:

\[
\boxed{
\rho_0(\operatorname{Pf}_6\mathcal F)
=
\operatorname{or}(a_0,\ldots,a_5)
\operatorname{ev}_{L_6},
}
\]

where

\[
L_6
=(a_{(1)}-a_{(0)})
+(a_{(3)}-a_{(2)})
+(a_{(5)}-a_{(4)}).
\]

The coefficient is exactly \(\pm1\), despite summing six operator orders for each of fifteen matchings.

The checker verifies 763 oriented frames across two rational metric chambers. Every output has one term, and every term matches the adjacent-pair cost with the orientation sign.

## Consequence

Rank four was not exceptional. It is the first nontrivial member of an even-rank boundary-Pfaffian law:

\[
L_{2m}
=
\sum_{r=0}^{m-1}
(a_{(2r+1)}-a_{(2r)}).
\]

This is the minimum perfect-matching cost for \(2m\) points on a line. The operator Pfaffian contains every matching, but half-line support and alternating cancellation retain only the adjacent matching.

The structure resembles a boundary version of fermionic Gaussian elimination:

- the antisymmetric two-cochain supplies pair amplitudes;
- the Pfaffian supplies all complete pairings with orientation;
- the ordered boundary selects the noncrossing nearest-neighbor pairing;
- endpoint readout returns its total displacement.

No external minimization operator is present.

## Implication for the power hierarchy

The even ranks appear to be observational closures:

\[
P^{2m}
=
\text{oriented complete pairing of }2m\text{ primitive positions}.
\]

Odd ranks carry compatibility of the corresponding partial pairings. In particular, \(P^4\) is not an isolated terminal dimension; it is the first level at which two observer pairs close. Rank six closes three observer pairs.

This modifies the idea that four alone is universally privileged. Four is minimal for comparison between two binary observations, while the same law extends to higher even arity.

## Verification

Run:

```text
python research/coherence/check_p6_pfaffian_matching.py
```

Artifacts:

- `check_p6_pfaffian_matching.py`
- `p6-pfaffian-matching.v1.json`
