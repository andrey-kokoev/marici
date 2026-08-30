# Complete blocks still fail when cell identity is fixed to block position

Every block may contain all 32 cells and still confound the reset if it repeats one fixed order. Position-dependent warm-up, cavity clearance, detector recovery, or thermal relaxation then becomes a cell-specific offset.

The exact hostile has no predecessor memory. Reset predecessors occupy positions with equal response, while the four control predecessors occupy positions carrying offsets `0`, `1/10`, `2/10`, and `3/10`. Every block is complete. The reset spread is zero and the control spread is `3/10`, so the complete-block contract falsely qualifies the reset.

The repair is position balance across blocks. Start with one sealed 32-cell permutation and use its 32 cyclic rotations. Across a rotation superblock, every cell occupies every position exactly once. Arbitrary additive position effects then become a common offset for every cell. In the hostile, both spreads become zero and qualification correctly fails its memory-sensitivity gate.

The acquisition analyzer now requires uniform position multiplicity for every cell. One million trials per cell is compatible with the 32-position cycle because one million is divisible by 32.

Executable witness: `checkers/check_within_block_position_confounder.py`.
