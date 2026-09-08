# v53: occurrence-linear and coherent-conductor refinements

Three supplied certificates were independently replayed: 22,304 occurrence-linear
reverse-pairing assertions, 78,779 true-obstruction-complement descent
assertions, and 226,245 coherent first-conductor assertions all passed.

`rzk/69-occurrence-linear-reverse-pairing.rzk.md` separates the valid integer
homogeneous-slice unit trace from the obstructed polynomial occurrence-linear
promotion. The latter has proper image `(X2,X4)`, primitive supported cokernel,
six transported pair ideals, and compatible principal-open traces only up to
Koszul homotopy.

`rzk/70-first-conductor-coherent-ranks.rzk.md` records component ranks
`(9,9,7,7,9,19)`, total primary-fixed rank 60, forgetful kernel/image ranks
24/36, ordinary rank 72, contractible individual components, and a
noncontractible total space. It also distinguishes the ordinary nullhomotopy of
the O02 direction from its nonzero primary-framed class.

Both new modules passed fresh transitive Rzk checks. The refined descent report
confirms and sharpens module 68: the torsor's cyclic conductor module is
`C/(tau_plus*tau_minus)` and its global lift image is `pm C` plus both localized
branch tails, still excluding the unit.

Physical status is unchanged: none of these target/coefficient computations
constructs the native source comparison, endpoint connectors, reflection
parity, or `Delta_J`.
