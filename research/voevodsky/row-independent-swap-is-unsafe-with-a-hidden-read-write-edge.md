# Row-independent swap is unsafe with a hidden read-write edge

The square derivation DAG treats W and V as incomparable children of Z, so its row-only trace policy would swap them. In a SYNTHETIC effect overlay, W writes slot=1 and V reads slot. Executing W,V makes V observe 1; executing V,W makes it observe 0, although both mathematical derived rows and final square proof packets are unchanged. Fresh `check_effect_sensitive_trace_swap.py` checks these observations, refuses the W/V swap as `EFFECT_CONFLICT`, and still permits swaps with a branch U whose read set is disjoint. Row dependency Z/W remains independently forbidden.

A valid swap certificate therefore needs typed read/write or other effect evidence as well as row-derivation predecessors and manifests. Missing effect declarations cannot safely mean 'no effect' when the intended equivalence preserves observations. This is a model counterexample, NOT an assertion that actual Farkas computations touched a slot or that any actor issued a row grant. It isolates the precise information hidden by a purely mathematical dependency DAG.

Next test UNKNOWN effect footprints: define a fail-closed swap policy, distinguish certified pure events from undeclared events, and record what evidence would justify adding an independence edge without claiming authority from graph admission. Analytic S,A,R,C,G mapping remains deferred.
