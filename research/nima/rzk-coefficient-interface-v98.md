# v98: three supported detector coordinates

`rzk/126-three-supported-detector-coordinates.rzk.md` carries the primary,
reciprocal, and relation detector frame into the amplitude construction. The
three integer-valued functionals assemble canonically into the coordinate map
`Supported -> (a,b,c)`.

A pointwise residue law for these detectors produces the supported-coordinate
factorization and therefore the full physical amplitude bridge after
precomposition with Gysin. The coefficient fixture supplies all three detector
maps and the law judgmentally, and again induces the canonical bridge.

This separates two facts that the Agda interface also distinguishes: joint
detection of the supported object does not itself prove the amplitude residue
formula. For the physical model we still need concrete primary, reciprocal,
and relation functionals and their oriented residue identity.

The transitive closure contains eleven files. A fresh combined Rzk check passes
all 180 declarations (192 checker steps including parameter/assumption
commands). The target module adds no `#assume` declarations.
