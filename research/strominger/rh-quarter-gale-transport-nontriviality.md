# Fixed-eight Gale-comparability transport is nontrivial

## Question

Is the successful comparability flow merely a complete-graph restatement of total positivity?

## Claim boundary

No. Comparability is incomplete in 3,291 of 3,584 terminal cases. Of 1,048,580 positive-negative label pairs, 304,735 are Gale-incomparable; the minimum observed comparable-edge density is `230/380`. Nevertheless every negative singleton neighborhood has strictly positive exact supply slack, with no zero singleton inequalities. Together with the prior exact max-flow result, this shows a genuine restricted-network certificate at fixed size eight. The audit has not computed a symbolic all-subset Hall proof or a canonical flow.

## Disposition

Retain Gale comparability as nontrivial bounded structure. The all-order obligation is now explicit: prove weighted Hall inequalities for every negative-label subset from the source minors. Before requesting that theorem, test whether a deterministic label-and-magnitude greedy flow succeeds across the bounded census, which would provide a candidate canonical construction rather than casewise max-flow existence.
