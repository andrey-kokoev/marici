# Physical mixed-variance mate acceptance boundary

`agda/DGPyramidMixedVarianceMate.agda` defines the strict acceptance contract for the comparison still missing from the Marici pyramid.

`PhysicalMixedVarianceMateSpecification Partial` declares a mate type and eleven separately inspectable predicates covering the ten conceptual gates (the final boundary/framing gate is split): ordinary source-equivalence compatibility; positive and negative physical endpoint identification; genuine full-Q contraction compatibility; corrected Morse-disk compatibility; marked-normal omega placement; its lower-support transgression; Cartier/Rees duality; dihedral orientation and endpoint swap; physical q/e/h_M/H_C identification; and discrepancy framing.

`PhysicalMixedVarianceMate Spec` requires one candidate and a witness for every predicate. `PreservesAllMateCoherences` exposes the full nested conjunction, and `mateCoherences` derives it without merging failure sites.

`MateWithAdmissibleFiller` keeps the final distinction explicit: even a fully coherent mate does not provide K, delta(K)=Delta, or the four filler witnesses. An `AdmissibleFiller` must still be supplied independently.

No mate or filler inhabitant is constructed from current coefficient, carrier, support, or marked-normal certificates. Predicate definitions must precede candidate selection, preventing retrospective acceptance of a chosen scalar or parity.

The new module is publicly imported by `DGPyramidArchitecture.agda`. Agda 2.8.0.1/Cubical 0.9 accepted a fresh aggregate build under `--safe --cubical --guardedness`, exit0 without warnings. No holes, postulates, Git operations, or physical claims.
