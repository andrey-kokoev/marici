# Four-channel completion needs a linear join barrier

The four per-channel release boundaries now feed a binary tree of three JOIN agents. READY--JOIN consumes its first token and becomes HOLD, whose principal port faces the second input. READY--HOLD consumes the second token and emits one READY to its parent. No readiness token is copied. The final BARRIER root sees READY only after all four channel gates have released.

The delayed-channel test publishes every answer, withholds exactly one CLEAN transition, and drains every other enabled transition. The global barrier stays blocked even though three channels finish. Releasing the withheld cleanup then permits one final READY token. Terminal nodes are only four ANSWER--OUT pairs and one READY--BARRIER pair.

One hundred randomized schedules (2,000 transitions) preserve live component meanings and produce the same final observation. Prefix instrumentation confirms that global readiness implies all four cleanup steps and all four channel releases occurred. Observations are immutable and do not schedule work.

This is a fixed four-input join, not an arbitrary programming language or a completed geometric continuation. Completion accounts for introduced model tokens only. The successor body, reusable source-return protocol and correspondence of these tokens to actual source/form obligations remain unimplemented.

Implementation: `research/nima/checkers/four_cell_completion_barrier_net.py`.
Checker: `research/nima/checkers/check_four_cell_completion_barrier_net.py`.
Result: `research/nima/results/four-cell-completion-barrier-net.json`.
