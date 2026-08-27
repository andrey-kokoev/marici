# Raw acquisition boundary for the five-bin reset

The physical run consists of 32 cells: two arms, four adversarial predecessors, and four targets. The reset arm literally inserts five empty bins. The control arm inserts none. Each cell requires one million attempted trials. Every acquisition block contains all 32 cells exactly once. A sealed base permutation is executed through all 32 cyclic rotations so every cell occupies every position once per rotation superblock.

Every attempted trial is one CSV row. Reset failure is an outcome column, never an exclusion key. The analyzer streams raw rows, requires unique trial keys, one qualification epoch, one sealed schedule, exact 32-cell block completeness, and uniform position multiplicity for every cell, reconstructs all cell proportions, and applies the frozen predecessor-spread gates.

The no-reset arm must display predecessor sensitivity of at least `1/10`. The reset arm must reduce both target-response and reset-monitor predecessor spread to at most `1/20`. This makes a passing result a comparison between an instrument known to expose memory and the proposed erasing intervention.

Run the physical record through:

```text
python research/aspect/checkers/analyze_reset_qualification_run.py RAW.csv --output RESET_RESULT.json
```

No physical result exists until that command receives apparatus records satisfying `contracts/reset-qualification-acquisition.v1.json`.
