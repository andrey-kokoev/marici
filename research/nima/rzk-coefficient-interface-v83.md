# v83: primitive conormal replay and input audit

The recovered standalone checker was independently replayed and passed 80,087
exact assertions.

`rzk/109-primitive-conormal-replay-audit.rzk.md` records the target-side
primitive conormal column `(0,1)` and the intrinsic target Ext calculation
through degree six. Native ranks are `(1,6,24,92,354,1362,5240)`. The reported
`C/(beta)` summands double the displayed ranks at `beta=0`; inverting `beta`
removes those torsion summands.

The replay constructs only the target-side column. The complete framed physical
source, its covectors, and physical control cohomology remain unset. Therefore
no physical `b` map or first-jet obstruction is instantiated by this result.

The Rzk module passes a fresh check.
