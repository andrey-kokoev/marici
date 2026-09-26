# Completion tokens gate channel successor release

The acknowledged query net now connects each completion boundary to a real GATE agent. Only the principal pair DONE--GATE releases a READY witness at that channel's NEXT root. Answer publication cannot activate this rule. The completion token and gate are consumed once; other pending channels remain blocked.

A deliberate prefix publishes all four answers while withholding cleanup: all NEXT roots remain unreleased. Completing exactly one cleanup enables exactly one gate. Before the gate fires, that channel is complete but not released; after it fires, the completion remains observable through READY even though DONE has been consumed. Replaying the consumed pair is rejected.

One hundred randomized schedules (1,400 transitions) preserve live component meanings and monotone publication/completion/release flags. Terminal graphs contain only ANSWER--OUT and READY--NEXT pairs. Public observation is read-only.

Scope: this is per-channel release, not an all-channel barrier. READY witnesses eligibility to start an operation; it does not implement a geometric successor body, retain reusable source support, or certify physical obligations. Those require a further contract rather than treating published answers as sufficient authority.

Implementation: `research/nima/checkers/four_cell_completion_gate_net.py`.
Checker: `research/nima/checkers/check_four_cell_completion_gate_net.py`.
Result: `research/nima/results/four-cell-completion-gate-net.json`.
