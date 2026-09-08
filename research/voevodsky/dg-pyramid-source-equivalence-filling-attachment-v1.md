# Source equivalence and Q-filling attachment interfaces

Added two safe Cubical Agda certificate boundaries following the latest complete-source calculations.

`agda/DGPyramidSupportEquivalence.agda` records the ordinary pulled-back-normal to cellular comparison, inverse, homotopy/contraction witness, endpoint and short-boundary restrictions, induced Q comparison, corrected Morse evaluation, and occurrence/normal/Rees homogeneity. It explicitly does not identify this model with the native-normal source or physical supported dual.

`agda/DGPyramidQFillingAttachment.agda` separates fillings, filling chains, variation classes, and lower attachments. It records the three closed zeta variations and diagonal relation, two-coordinate detection of the zero variation, the three concrete attachment representatives, injectivity of lower attachment, and the seven-triangle/eight-triangle comparison bounded by a six-tetrahedron chain. Theorems `preservingAttachmentForcesTrivialVariation` and `sameAttachmentForcesSameFillingClass` expose the computed rigidity: fixing lower support kills every nontrivial ordinary Q-filling variation.

`PartialMariciPacket` now requires both certificates and explicit compatibility predicates relating each to its Q-support certificate. The physical completion gates are unchanged.

A preliminary combined shell command checked the support module but used an incorrectly shell-expanded PowerShell status variable before invoking the second module. The second module was then checked directly. A fresh aggregate rebuild subsequently checked both modules and the updated partial adapter successfully.

Agda 2.8.0.1/Cubical 0.9 accepted `DGPyramidArchitecture.agda` under `--safe --cubical --guardedness`, exit0 without warnings. No holes, postulates, concrete matrix-import claims, Git operations, or physical filler claims.
