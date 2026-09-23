# A signed difference between valid proofs needs a common exact target

On the unit square, x<=2 from x-upper plus surplus 1 and 0<=1 from x-lower+x-upper both validate individually. Their multiplier delta is nonzero but a SAME-TARGET comparison rejects their differing target normals/bounds. Even x<=2 and x<=1 via the SAME x-upper multiplier give zero multiplier delta; their different exact target bounds still force rejection. Fresh `check_comparison_target_scope.py` accepts the same-target control only.

A signed vector can always be formed algebraically; an edge with a prescribed SAME-TARGET meaning cannot treat that vector as sufficient evidence of that meaning. A genuine cross-target transformation would require a distinct rule, explicitly bound targets, proof, and provenance. None is established here. Source issuer unknown; analytic S,A,R,C,G deferred.

The bounded nonnegative proof gate branch is resolved: equation equality, multiplier/surplus signs, endpoint validity and exact target equality were tested. Next investigate a distinct cross-target weakening rule: from a proven x<=1 to x<=2 one may increase nonnegative surplus by 1, but must issue a new target-bound packet and cannot relabel the original proof event.
