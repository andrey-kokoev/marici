# Cycle reduction is a derived view pinned to the original path

Fresh `check_nondestructive_cycle_reduction.py` takes a synthetic four-edge S->P->Q->P->T path. Removing the exact P->Q->P cycle produces a separate two-edge S->P->T DERIVED VIEW referencing both the original full-path digest and removed-segment digest; the original four edges stay intact. Changing the return edge Q->R fails `NO_EXACT_CYCLE` instead of being discarded. The view is marked `observed_replacement=False`.

This is structural path rewriting, not verification that comparison endpoints have correct Farkas packets or that any event happened. The row issuer and analytic S,A,R,C,G role map remain unknown/deferred.

Next test an OVERLAPPING-CYCLE ambiguity: if a path contains multiple reducible cycles, reductions in different orders may yield the same endpoint math but different intermediate views; preserve each selected segment and original digest rather than asserting unique historical normal form.
