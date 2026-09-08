# v55: supported occurrence trace and descent duality

Independent replays passed 35,051 assertions for the occurrence-supported
conductor trace and 50,010 assertions for endpoint-complete descent duality.

`rzk/72-occurrence-supported-conductor-trace.rzk.md` records that replacing the
polynomial output by `H^2_(X2,X4)(A)` changes the reverse map from proper-ideal
image to an isomorphism, without making the residue a scalar unit. In its fixed
ordered occurrence frame the primitive trace fibre is contractible. The free
generic residue morphism specializes to zero at the conductor, while the whole
occurrence Koszul/Gysin morphism retains a primitive bottom component and its
codimension-two conormal determinant.

`rzk/73-endpoint-complete-descent-duality.rzk.md` restores all fourteen boundary
families. Base-defined scalar pushouts retain only three mixed-pole classes and
have a nonzero joint blind kernel. The relative dualizing complex has branch
cohomology in degree `-3` and an odd conductor term in degree `-1`; their
attachment is nonsplit. Supported duality retains the complete cyclic descent
obstruction with its `T`-conormal shift.

Both fresh transitive Rzk checks passed. This sharpens the physical gate: scalar
pairings are provably insufficient, but the coefficient-supported Gysin and
dualizing constructions are still not identified with the native spatial
source, endpoint connector 2-cells, reflection parity, or `Delta_J`.
