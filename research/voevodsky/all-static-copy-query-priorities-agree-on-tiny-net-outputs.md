# All static copier/query priorities agree on tiny net outputs

Fresh `check_all_static_copy_query_priorities.py` enumerates all 24 static priority orders of COPY, query1, query2, and eraser families, across support words length 0..3 and both unary indices 0..n+1. All 6,864 runs terminate with the same expected pair of membership Booleans and exactly two BOOL--OUT components. The harness sees 614 distinct rewrite-family histories; maximum length 22. The underlying wired evaluator audits one symmetric wire per live port after every rewrite.

Static priorities are only a subset of dynamic enabled-redex schedules. The result is bounded evidence for schedule robustness, not a confluence theorem or proof of arbitrary fair normalization. The stronger experiment requires exposing one-step redex transitions, then enumerating graph states modulo fresh-ID alpha-renaming. Local add(i)/union and reusable post-query supports remain separate open questions.
