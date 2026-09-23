# A shared derivation DAG does not determine temporal proof order

From square primitive rows X:`x<=1`,Y:`y<=1`, derive shared Z:`x+y<=2`; derive W:`2x+y<=3` from Z+X and V:`x+2y<=3` from Z+Y, then T:`3x+3y<=6` from W+V. The dependency DAG has ONE Z node, even though tree-unfolding T uses Z twice. Both temporal orders (Z,W,V,T) and (Z,V,W,T) obey every dependency and yield identical exact row packets. Fresh `check_shared_square_derivation_dag.py` checks both and refuses putting T before its dependencies.

The DAG records structural support/sharing, not which independent branch was executed first. To replay a specific historical run, retain chosen linearization and event IDs in addition to typed derivation edges, row manifests and primitive roots. None of these LOCAL synthetic events authenticate a real row-source issuer. Conversely a mathematical DAG can be checked without asserting that either order actually happened.

This closes the split-deletion comparison branch's bounded distinction between row-packet retraction, kernel loss, dependency acyclicity and historical ordering. A nonredundant successor should test a partial-order trace equivalence: when two adjacent INDEPENDENT derivation events commute, specify what evidence a swap certificate must retain and why it does not authorize arbitrary swaps of dependent events. Analytic S,A,R,C,G remains deferred.
