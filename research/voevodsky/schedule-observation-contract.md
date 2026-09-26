# Scheduling: final agreement versus publication timing

The reachable-family confluence proof in `reachable-concurrency-confluence.md` establishes a unique normal form modulo fresh internal names, fixing public roots, under the existing constructor/phase/freshness premises. It does not establish identical intermediate observations after a fixed number of rewrites.

## Observation invariant

Each public slot starts at a gate or passive phase auxiliary. Publication attaches one TRUE/FALSE or FOUND/EXHAUSTED principal leaf directly to its fixed OUT root. No rule consumes that isolated pair. Hence a published value and its peer identity remain immutable; slot types and root order never change. Strict instruction boundaries imply ready slots form an initial segment of the ordered observation list: an instruction cannot publish before any earlier observing instruction has completed, which includes its publication. Nonobserving instructions do not affect this argument.

Final ACK cannot occur with enabled work: each operation forwards completion only after its owned work is exhausted, and every earlier gate is already consumed. Conversely, in a reachable finite-program net with pending instructions or an active incomplete operation, the phase progress argument supplies an enabled rewrite. Thus complete iff no enabled rewrite in this constructor-reachable domain. This is not a definition for malformed imported graphs. The facade still exposes the word only at final completion.

## Concrete timing distinction

The all-schedule checker now validates the invariant at every reachable state/edge, including exact published peer preservation. For member(0) on (1,0), the Boolean can be published after4,5 or6 rewrites, depending on COPY/query scheduling, although every terminal execution has8 rewrites and the same result. This is a direct counterexample to fixed-step trace equality, not to confluence. Reading a pending value at one step bound is not evidence that another schedule must also be pending.

Five complete fixture searches cover641 raw states709 edges, with one terminal observation per fixture. No cap is reached. The prior115 local diamonds remain in the closure as a separate check, not a replacement for the phase proof. All18 fresh closure suites pass after adding schedule-independence tests.

Next highest-value theoretical obligation is root-fixed confluence evidence beyond the current written phase classification: make the classification executable as a reachable-state invariant across the wider mixed corpus, and explicitly validate no outside-to-outside splice participates in a concurrent pair. Keep theorem premises visible. This is a targeted bridge between the general argument and production rule dispatch, not another promise of formal certification.
