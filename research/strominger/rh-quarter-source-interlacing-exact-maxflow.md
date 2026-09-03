# Quarter source interlacing exact max-flow

## Question

Can interlacing edges transport all negatively oriented Jacobi--Cauchy--Binet source mass into positive source capacity?

## Claim boundary

Exact rational max-flow proves feasibility for all 769 upper interval-avoiding order-eight cases. This is a finite weighted certificate, not an all-order construction or proof of the required Hall inequalities.

## Disposition

Every case admits a capacity-respecting flow from each negative source term to positive terms whose index sets interlace it. Thus the 108 greedy failures were allocation-order artifacts, not cut obstructions. Interlacing is the first local relation found that supports all bounded cancellations. The next leaf is `quarter-source-interlacing-hall-inequalities`, seeking source-minor inequalities that verify every weighted Hall cut at arbitrary Hurwitz size and thereby convert max-flow existence into a theorem.
