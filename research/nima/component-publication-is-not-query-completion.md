# Component publication is not query completion

Adapted the attributed four-cell query net to distinguish a published answer from completion. Each READC has separate answer and acknowledgment boundaries. VALUE--READC publishes ANSWER and creates an explicit CLEAN--TICKET obligation; only consuming that pair places DONE at ACK. Every component channel has its own acknowledgment. Global completion means all acknowledgments are present.

The public observer returns an immutable tuple of named answers (None while pending), per-channel completion flags, and a global flag. Numeric zero is a published value, not a pending marker. Observation performs no reductions.

A deliberate schedule publishes all four component answers while withholding all four cleanup reductions. Every answer is then available but completion remains false. Completing cleanup leaves all answers unchanged. One hundred randomized schedules (1,000 transitions) preserve the live meanings, immutable observations and final snapshot. Final topology contains only OUT/ANSWER and ACK/DONE pairs.

These cleanup tokens are explicit protocol obligations introduced by this prototype. They are NOT evidence that all geometric/source obligations have been discharged, and no source-return discipline or successor-release gate is implemented yet. The model remains an attributed net with primitive payload arithmetic, not a physical contour derivation. A next operation must eventually be wired to actual completion, not merely to answer visibility; this file does not claim that sequencing has already been implemented.

Implementation: `research/nima/checkers/four_cell_ack_query_net.py`.
Checker: `research/nima/checkers/check_four_cell_ack_query_net.py`.
Result: `research/nima/results/four-cell-ack-query-net.json`.
