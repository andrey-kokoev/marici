# Budget-first query phase repairs the simultaneous NIL case locally

Start query in Q_B phase, whose PRINCIPAL port meets budget head. Q_B--NIL outputs true; Q_B--KUNIT consumes one budget unit and switches to Q_C at the count head. Q_C--NIL outputs false; Q_C--UNIT consumes one count unit and switches back to Q_B. This order handles both NIL heads without a simultaneous lookahead: budget NIL wins at count=k=0 and after the final matched pair. Fresh `check_budget_first_unary_query.py` checks 4,225 count/k pairs 0..64, with correct output and `2*min(count,k)+(1 if count<k else 0)` interior steps. Local templates for both interior and terminal rewrites preserve external wire incidence.

The phase evaluator is still abstract. The checker has not instantiated the complete agent graph, connected the output/erasers through every rewrite, or shown full normalization/confluence. The repair closes the specific simultaneous-NIL logical error, not all implementation gaps.

Next instantiate a COMPLETE small net with explicit port-to-port wires for unary count and budget lists, Q_B/Q_C, NIL, BOOL, ERASE, OUT; execute rewrites and check no dangling/fan-out ports and one terminal Boolean for n,k<=small bound. If impossible, isolate the exact linearity obstruction instead of treating abstract success as a full net.
