# First retained mixed-face comparison gate: F006

## Actual interface

F006 has vertices V001,V008,V036, composite edge route E004 then E037, and direct edge E006. It is H234 in T000 and H123 in T003. These references come from the explicit prototype bridge, not a toy replacement face.

The [finite exact comparison gate](checkers/esd7_retained_face_comparison.py) is implemented and its12 checks pass. **The actual F006 analytical comparison remains blocked by missing source-bound operator/domain data.** Passing implementation controls is not reported as a verified face.

## What the gate checks

For two finite linear presentations and vertex comparison frames C, every edge must satisfy

    C_target L_edge = R_edge C_source.

The two retained endpoint rows obey

    E_right C_vertex = B_vertex E_left,

with invertible C and B and rank-two endpoint readouts. It computes and retains the full face residual

    Delta = edge_vw edge_uv - edge_uw

and checks its transported square. A nonzero residual is not erased or renamed a homotopy. Even a passing residual comparison does not supply a chain homotopy, analytical filler or native field equation.

The gate is a finite-packet implementation interface. An actual analytical binding may instead require an operator-level proof on an admitted graph domain; this finite matrix checker does not settle that domain problem.

## Controls, not fabricated source operators

The positive control uses explicitly synthetic exact rational matrices, noncommuting edges, nontrivial presentation/endpoint frames and a nonzero retained residual. It checks the implementation, not F006.

A mutation confined to an endpoint direction passes a regular-row-only check but fails the full edge and residual squares. Dropping an endpoint, using a singular comparison, swapping dependent edge maps and supplying floating-point entries are also rejected.

No identity matrices or synthetic operators are installed as defaults for the real face.

## Why the real comparison is still open

The inspected sources provide:

- a schematic typed tetrahedral pasting equation;
- recovery of H234 by faithful whiskering **on an admitted observer-generated geometric subcategory**;
- cutoff exponent/decay-order bookkeeping, explicitly conditional on the source analytical estimate.

The prototype registry attaches those roles and budgets, but supplies no edge operators, comparison frames or endpoint readouts for E004/E037/E006 in these two generated presentations. The source faithful-whiskering argument cannot be applied merely because a generated face is labelled H123 or H234. Its carrier, represented maps and recovery operation must first be bound.

This is a missing binding in the inspected interface, not a claim that the analytical source programme is false or that no comparison can exist. The two retained analytical endpoint coordinates are not automatically identified with the native E-window readout either.

## Next precise input

Bind E004, E037 and E006 in both local presentations, including their admitted carriers/domains, the three presentation frames and endpoint transport. Supply actual analytical homotopies or the source-faithful whiskering recovery data. Then run the full retained comparison rather than only the regular projection.

The114-record convention and full-complex field transport remain separate open gates.

```sh
python research/strominger/checkers/check_esd7_retained_face_comparison.py
```

[Receipt with synthetic controls, actual face references and explicit missing inputs](results/esd7-retained-face-comparison.json).
