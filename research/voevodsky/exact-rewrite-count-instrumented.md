# Exact rewrite count instrumented

Fresh `check_exact_normalization_count.py` subclasses the tagged production engine and checks P=3O+C immediately before/after every rewrite. For all bit words n<=4, both indices through n+2, and four distinct family-priority schedules, every edge decreases P by exactly one. All 4,852 runs terminate with P=0, correct Boolean answers, and exactly 3n+i+j+5 steps; 101,676 individual delta checks pass. This is a count of interaction-net reductions, not Python runtime or output-availability latency.

The test supports the previous rule arithmetic independently of the lexicographic rank assertions. It does not establish universal structural closure, and the four priorities do not enumerate arbitrary dynamic schedules. No new confluence claim is made.

Next close the structural-proof integration gap rather than further increasing small samples: express each active-pair replacement as a finite forest with typed boundary slots, prove the generic gluing/forest lemma, and explicitly track rooted components when replacements split. This is the missing general context argument connecting the fifteen-case ledger and validator to all finite constructor inputs. The unit potential then supplies termination immediately.
