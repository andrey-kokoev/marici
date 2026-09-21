# The ordinary middle-history observation descends

## Finite source-coordinate result

A concrete candidate resolves the middle-lift gate from `ordinary-middle-quotient-paired-descent-gate.md` without a section or fitted quotient metric:

    F(a tensor w tensor c) = D(a) tensor rho_middle(w) tensor D(c).

Here D denotes the actual local seam derivative, and rho_middle is the terminal history receiver, not another seam derivative. Keep the ordered pair partition, both intermediate vertices, and one common root state as external labels/factors.

For a two-event block the terminal record has rank six on its eight endpoint paths. Both middle relations lie in its kernel: the forgotten routes have the same vacuum record, and the singly retained sums agree by telescoping the event features. Their independence makes the kernel exactly R2. Hence rho_middle induces an injection of B2=E2/R2 into the typed terminal history carrier.

Each outer D is injective on its two-dimensional relation space. Therefore F factors through R1 tensor B2 tensor R3 and is injective there. Its rank is 2*6*2=24 per partition and 2160 over 90 distinct labels. This is an exact source-coordinate rank, not a spectral sample rank.

Changing w by either middle relation leaves F unchanged. Pairing F against any admitted ambient observer is consequently independent of the middle lift, with no need to infer that the source relation is Green-radical. Under the existing faithful function-valued history transfer, the same identities persist pointwise and in the admitted finite carrier. This transfer remains relative to that carrier's domain and tensor/direct-sum declarations.

The candidate target is two outer seam factors with a middle history factor. It is NOT the three-seam shifted target. This map is not asserted to extend the already constructed shifted chain observation into one common target complex.

## What this does not close

This constructs a common ordinary observation, not the independently prescribed coarse observations on all 6300 ordinary coordinates. Equality of parenthesizations of this tensor is not proof that the existing left and right coarse Green forms restrict to its form.

The next comparison must specify coarse maps on C4 tensor R2 and R2 tensor C4 and prove that their pullbacks along f_L and f_R equal this F, with compatible ambient pairings. Alternatively it must exhibit the obstruction to those extensions. Abstract linear extensions from the common subspace do not establish canonical analytical or source-equivariant extensions.

No claim of positivity, restricted nondegeneracy, uniform completion, or a new boundary sewing identity follows.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_ordinary_middle_history_observation.py`

Checks all 90 partitions in the actual vertex-potential record model: 180 middle relations killed, 1440 lift changes, middle record rank six, and outer seam ranks two. The 2160 rank follows by tensor products and retained direct-sum labels.

Source definitions are imported from `../grothendieck/checkers/check_six_prime_derived_block_associativity.py`; that checker's source comparison is rerun as a dependency. This is not an independent verification of those source definitions or an evaluation of Clark traces.
