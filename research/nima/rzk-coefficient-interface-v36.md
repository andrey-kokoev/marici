# v36: actual repeated-normal excess source

**Rees-resonance update:** [`rzk-coefficient-interface-v37.md`](rzk-coefficient-interface-v37.md)
retains the two annihilating primitives of the D03 filling variation and proves
their secondary compatibility cycle is detected as a nonboundary.

`rzk/46-repeated-normal-excess-source.rzk.md` internalizes the smallest source
feature that the branch-excess obstruction requires.

The branch and D03-pair copies of the shared normal are distinct basis states,
but both have differential `u3` to the same base state. Their oriented
difference

    eta = h3_plus - h3_pair

is therefore a checked cycle. Rzk proves square-zero on arbitrary finite
integral `Z[u3]` expressions, defines an excess detector that vanishes on every
boundary, evaluates eta to one, and shows that an asserted boundary for eta
would imply `0_Z=1_Z`.

A fresh 71-file headless closure passed in 29.98 seconds. Evidence:
`results/46-repeated-normal-excess-source.typecheck.json`.

This prevents our formal model from replacing the external excess channel by
an internal target-normal multiple. It supplies the source-side Tor-one
summand needed to state the new obstruction correctly. The full 32-generator
Koszul tensor, Koszul-to-Cech endpoint residue, and 220-generator critical Hom
complex remain certificate-level calculations.
