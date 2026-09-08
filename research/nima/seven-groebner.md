# Seven-point local Groebner certificate

## Question

Do the 63 local quadrics require higher-degree generators in a declared Groebner completion?

## Claim boundary

Use lexicographic order x_0 > ... > x_41 in the triangulation ordering of results/seven_point_fibers.json. Caps were 300 basis elements, 50000 pairs, and 200000 monomial reductions. A capped run would not certify completion.

The exact binomial Buchberger checker processes all 1953 pairs. Relatively prime leading monomials use the product criterion; other S-pairs reduce by replacing divisible monomials with the corresponding trailing monomial. Each replacement strictly decreases lexicographic order. Both S-pair monomials reduce to the same monomial in all cases. The run uses 266 reductions and adds no generators.

Thus the original 63 quadrics form a Groebner basis. Their minimal leading generators are squarefree, so the initial ideal and consequently the local ideal are radical. Reductions are monic binomial identities over the integers, and the same certificate applies over every field, including characteristic two.

## Disposition

The proposed need for higher-degree Groebner generators in this order is refuted. Radicality is proved, not primeness or equality with the triangle toric ideal. A radical ideal may still contain additional boundary components. The complete exponent-pair basis is recorded for a separate saturation test; no degree cutoff is being promoted to a generating theorem, because all Buchberger pairs were discharged.
