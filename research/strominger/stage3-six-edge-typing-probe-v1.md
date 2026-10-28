# Stage-3 six-edge-first typing probe

## Question and explicit approximation

Operator proposal: retain the stage-1 P and stage-2 P,N,E,E pattern, grow all six tetrahedral edges first, then fill the remainder of stage3. Test whether shared constraints force the types.

This first probe uses the existing primitive geometry and two complete-face growth rounds from its seed. It does NOT yet identify those rounds with the proposed successive unit-length tetrahedral layers. The six edge groups consist of new cells incident to each of the six seed edges; this is an edge-fan ordering, not a newly derived boundary-edge growth law.

Unlike the preceding occupied-body probe, it does not import forbidden particle contacts. It imports only the C/M vertex roles of the actual ordered P,N,E templates from windowProtocol. Each has two C vertices and two M vertices. Source-indexed marks and execution provenance are not inferred from these binary roles.

## Procedure

1. Keep the central seed's existing C/M marks.
2. Construct the four complete-face neighbors and their next-round neighbors from LocalPrimitiveGeometry.
3. Require each cell to have exactly two C and two M vertices. Shared vertices have one global mark. Propagate a mark when the cell's remaining quota forces it.
4. Process the six seed-edge fans first. Repeat to closure; compare with reversed and ordinary cell orders.
5. For each resulting cell enumerate all bijections from each actual ordered P/N/E template to its vertices that preserve C/M roles.

Stage2's assigned P,N,E,E labels are compatible with this necessary role test. Because all three templates have the same C/M multiset, those labels alone add no ordering or trajectory constraints to it. No independent choice of template frame is promoted to an admitted native history.

## Result

Fresh execution of `node research/strominger/checkers/check_stage3_six_edge_probe.mjs` passes its assertions and reports:

- 1 central cell, 4 first-shell cells and 10 second-shell cells;
- all 10 second-shell cells belong to the six seed-edge fans; this approximation has no remaining second-shell cell after those fans;
- 12 additional vertex marks are forced;
- all three processing orders give the same complete mark assignment;
- each of the 10 second-shell cells admits P, N and E, with four role-preserving template frames for each type;
- hence 3^10=59049 type assignments satisfy this role-only model, before trajectory/frame and native-admission constraints.

The factor four is 2! ways to place the C labels times 2! ways to place the M labels. It is not four additional physical modes.

## Interpretation

Edge-first processing is consistent in this approximation and does force vertex-role data. C/M role data alone do not force P/N/E typing, because that distinction also uses the ordered active window, continuation and retained source frame.

Two limitations prevent treating this as a decisive test of the operator's proposal:

1. The model has edge-adjacent fans rather than a verified unit-length shell with edge paths followed by a nonempty remainder.
2. It omits precisely the ordered trajectory/interface data that may supply the proposed additional constraints.

No claim that the full six-edge construction fails or succeeds follows. The next implementation needs the actual directed edge-path extension and transport of its ordered windows, on an explicit identification of the intended stage3 geometry. A guessed type schedule would conceal rather than test that requirement.

No net, viewer or production rule was changed. The new checker is a standalone exploratory probe, not a physical result or a proof of native assembly.
