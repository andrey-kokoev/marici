# Equal treatment counts do not protect the associator from route memory

The crossed hardware design algebraically separates the logical associator from a static hardware offset. It still fails if the apparatus remembers the preceding route and the schedule balances only current treatment counts.

Label the four crossed cells `L1`, `R2`, `L2`, and `R1`. Give every cell four trials. A grouped cyclic schedule has equal cell counts, yet its ordered transitions are unequal. If an observation acquires an additive carryover depending only on the previous cell, with carryover `3/5` after `L1` and zero otherwise, the true-zero associator is reported as `3/20`.

A cyclic de Bruijn schedule of order two over the four cells has sixteen trials and contains every ordered pair exactly once. Consequently every current cell sees the same empirical distribution of preceding cells. Any additive first-order carryover becomes a common offset and disappears from the crossed contrast. In the hostile above, the recovered associator is exactly zero.

This adds a design condition, not another measured observable: balance the ordered treatment transitions inside each calibration epoch and record both the previous route and the transition block. Trial-level randomization and equal treatment counts are insufficient certificates.

The result is exact but sharply scoped. It removes arbitrary additive memory of the immediately preceding treatment. Transition-specific interactions and memory extending two or more trials do not descend through this quotient; they require higher-order history balance or an independently validated memory model.

Executable witness: `checkers/check_transition_balanced_associator_falsifier.py`.
