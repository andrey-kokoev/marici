# What operation does the three-piece belt retain?

## Compare the same six cells

Use the common refinement already constructed, with two rows (the old tetrahedra) and three columns (the belt sectors). All six children have volume 8/9.

Give each child a real or complex amplitude. Define two explicit observations:

- Old pair summary: average the three amplitudes in each row.
- Belt summary: average the two amplitudes in each column.

These are geometric cell-field observables, not the already compiled 1836-arrow coefficient protocol and not electric charge assignments. Equal volumes justify the arithmetic means for this test.

## A mode the belt summary sees

Put the pattern (1,ω,ω²) in each row. Then

```text
old pair readout = (0,0),
belt readout     = (1,ω,ω²).
```

The actual 120-degree vertex rotation A→B→C→A fixes the two old tetrahedra setwise but cycles the three belt cells. Its pullback on the retained six amplitudes multiplies the displayed mode by ω. The conjugate mode has eigenvalue ω².

Thus the belt summary preserves a two-real-dimensional relative-contrast plane that the two-cell summary erases.

## It is not an operation exclusive to the new geometry

The rotation acts on the common refinement before either coarse summary is taken. It commutes with both averaging projectors. Thus the old description can also support the operation if its refined data are retained; only its two-number coarse summary cannot.

The six-dimensional state splits into:

```text
common mode:          1
old side contrast:    1
belt contrast:        2
mixed contrasts:     2
```

Retaining both summaries requires four dimensions. It still loses the two mixed contrasts. This is a concrete retention distinction, but selecting that additional retention obligation remains an operation to explain, not a neutron identity already derived.

## The circular adjacency does not create a topological phase defect

The three belt cells intersect pairwise on internal faces and all three intersect on the central edge. Their full intersection nerve therefore includes a filled triangle. It is contractible.

Keeping only pairwise adjacency would draw an unfilled circle and manufacture a loop by forgetting the triple-intersection witness. The checker distinguishes these two objects. The geometrical link of the central edge remains a circle; that is not the same object as the full intersection nerve.

## A more concrete primitive-operation candidate

The three-piece geometry introduces the central edge De. In the earlier fifteen-arrow receiver source, e had no outgoing arrow. Orienting the new edge as **e→D** creates

```text
A→e→D→A,
B→e→D→B,
C→e→D→C.
```

These are exactly the three internal belt-face cycles ADe, BDe, CDe. One new directed edge closes all three receiving legs. The source now has sixteen primitive arrows and fifteen new simple directed cycles in total. Every generator lies on a closed directed cycle.

The opposite orientation D→e does not close any receiver path: e remains a sink. Thus the return orientation is selected if the task is to make those incoming paths return using only the newly introduced geometric edge.

This test belongs to the **three-incoming-arrow source variant**. It does not silently add a return to the separate collective-center p→q variant. The core edge connects the apices D and e; the derived center segment is only a subsegment of that axis.

Directed closure is not yet weighted coherent closure. No coefficient weights have been assigned to the new internal cycles, and no expanded count follows from sixteen primitives. The next concrete experiment is to generate those cycles' coefficient transports and test their joint return, retaining the old source rather than completing all three belt tetrahedra into arbitrary K4 networks.

## Verification

```text
python research/voevodsky/checkers/check_belt_retained_operation.py
```

Twenty-one exact checks pass. `results/belt_retained_operation.json` records the averaging maps, cyclic mode, retention ranks, full versus graph-only nerve topology, and the primitive return-edge candidate. Existing source artifacts are unchanged.
