# Photon-count preservation does not certify coherent reset transport

Complete dephasing preserves the computational photon-count responses of `0` and `1` exactly. It destroys the `X` and `Y` quadratures, the phase-bearing entries needed by a complex Bargmann invariant, and the `000–111` coherence.

In Pauli-transfer coordinates `(I,X,Y,Z)`, the identity reset has diagonal `(1,1,1,1)` and rank four. The hostile has diagonal `(1,0,0,1)` and rank two. Both give identical outputs on computational count probes. For input three-wing coherence `3/5`, the identity returns `3/5` and the hostile returns zero.

The reset must be qualified as a coherent process on an informationally complete spanning family. Required coordinates include both phase quadratures, the complex triad invariant, and the actual three-wing carrier. Population tomography is not enough.

Executable witness: `checkers/check_coherence_preservation_falsifier.py`.
