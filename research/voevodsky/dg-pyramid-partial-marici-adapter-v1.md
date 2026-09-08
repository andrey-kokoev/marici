# Partial Marici pyramid adapter boundary

`agda/DGPyramidPartialMariciAdapter.agda` packages all presently formalizable inputs without asserting that the external finite certificates have already been imported as Agda inhabitants.

`PartialMariciPacket P` bundles:

- full Q-support/contraction and seven-triangle certificate;
- carrier endpoint certificate and coefficient obstruction;
- marked-normal Q certificate;
- explicit homological-to-Hom degree shift into a typed candidate boundary P;
- bridge through the existing `GenericQComparisonCell` gate;
- explicit carrier-Q and marked-Q compatibility witnesses.

The parameter P is only a degree/sign-correct candidate boundary. Its algebraic `e` and `H_C` fields do not become physical by being present.

`PhysicalCompletionSpecification Partial` names exactly the unavailable constructions and independently defines their validity predicates. `PhysicalCompletionGates Spec` then requires:

- a valid mixed-variance mate;
- both valid physical endpoint connectors and their identifications with the carrier construction through that mate;
- physical e and H_C comparisons, their validity, and identification with the typed boundary cells;
- Cartier/Rees compatibility.

Even a future inhabitant of these gates does not produce `AdmissibleFiller`: the candidate K, boundary equation, support, endpoint, Q, and Rees/Cartier frame witnesses remain in the separate filler fibre.

This is an interface-level partial packet, not an inhabitant backed by rechecked Python matrices. Importing the concrete 2,338-state and target certificates remains a distinct generation/verification task.

Agda 2.8.0.1/Cubical 0.9 accepted the new module and the aggregate architecture under `--safe --cubical --guardedness`, exit0 without warnings. No holes, postulates, Git operations, or physical claims.
