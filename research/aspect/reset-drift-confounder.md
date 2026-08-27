# Grouped acquisition can certify a reset when no memory exists

Suppose neither arm has predecessor memory and every true target response is `1/5`. Let four successive acquisition regions carry additive drifts `0`, `1/10`, `2/10`, and `3/10`.

Acquire the reset arm in one stable region and group the no-reset arm by predecessor across the four drifting regions. The reset predecessor spread is zero. The control predecessor spread is `3/10`. Both gates pass, so the naive run certifies a memory-erasing reset even though the apparatus exhibited no memory to erase.

The repair is exact complete-block acquisition. Every block contains each of the 32 arm-predecessor-target cells once, in sealed randomized order. Any block-common drift then enters every cell equally. In the hostile, both predecessor spreads become zero and the no-reset sensitivity gate correctly rejects qualification.

Random ordering without exact within-block incidence balance is not enough. The raw record must carry `acquisition_block`, `within_block_position`, and `sealed_schedule_key`, and every block must realize the complete 32-cell alphabet exactly once.

Executable witness: `checkers/check_reset_drift_confounder.py`.
