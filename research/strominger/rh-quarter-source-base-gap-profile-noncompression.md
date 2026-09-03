# Quarter-source base-gap profile noncompression

## Question

Does adding the ordered base-gap profile produce a nontrivial recurrence state after rank-gap-left state fails?

## Claim boundary

Let the proposed state retain the absolute left endpoint `i`, endpoint gap `j-i`, and the ordered relative base offsets `(s_1-i,...,s_r-i)`. It reconstructs every base element by `s_a=i+(s_a-i)` and reconstructs `j=i+(j-i)`. Hence it is bijectively equivalent to the full case datum `(S,i,j)`. Using consecutive ordered gaps instead gives the same conclusion once the absolute anchor is retained: cumulative sums recover the ordered offsets. This state therefore cannot explain or reduce the canonical transport recurrence; a finite lookup indexed by it merely renames the original cases.

## Disposition

Reject ordered base-gap profile as a recurrence compression without running another census. Stop this branch at the missing typed object: a source-derived recurrence map relating different full cases. Acceptance requires an explicit recurrence with source and target cases, positive coefficient law, termination measure, and an exact proof that its induced transport preserves every interlacing capacity. Do not generate further compressed-state successors from the same absence. Return to a distinct governing rival, such as the positive-real or Gram certificate backend.
