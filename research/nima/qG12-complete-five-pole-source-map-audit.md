# `q_G12` complete five-pole source-map audit

## Question

Do the frozen artifacts construct the rank-35 five-pole presentation, its rank-20 residue quotient, and the base-change map to the shared-wall cocycle?

## Established structure

Each occurrence family has five denominators and homogeneous rank 35. Deletion along `q_G12` gives the exact rank pattern

\[
0\longrightarrow M_{15}\longrightarrow M_{35}\longrightarrow R_{20}\longrightarrow0.
\]

The prescribed physical source is the unsplit sum of the `q_g23` and `q_g31` occurrence columns. Its normalized residue has three generically nonzero shared-wall components and zero mixed-occurrence component. Hence its class is nonzero in `R20` and does not lie in the deletion submodule. This proves complete-source occupancy without a full five-axis pivot lattice.

## Missing construction

The artifacts do not provide retained bases or reduction matrices for `M35`, `M15`, or `R20`. Only one source Poincaré-residue column is known. The rank-35 extension type gate records that a connection-level reconstruction additionally requires a `15×20` off-diagonal Gauss–Manin block, containing 300 scalar entries before constraints, modulo triangular gauge. Rank data plus one source column do not determine this horizontal extension class.

The generic base-change checker establishes ranks `34+26=60` away from homogeneous specialization and the homogeneous Euler split `15+20=35`. It does not construct the derived base-change maps; its companion artifact states that these maps and their compatibility with connecting morphisms remain conditional.

## Consequence

The source residue column already proves nonzero occupancy and Čech closure, but there is no chain-level map carrying the complete five-pole presentation to the shared-three-wall presentation. Therefore the requested lower-graph factorization square cannot be upgraded from one distinguished source column to a morphism of coefficient systems.

## First missing datum

The first missing datum is the retained block presentation

\[
(d_{15},d_{20},E_{15,20})
\]

with source-labelled bases, where `E15,20` represents the horizontal extension class. It must induce the known unsplit source residue column and commute with the deletion–restriction connecting morphisms. A fiberwise noncanonical splitting is insufficient.

## Strongest falsification attempt

Reconstruct `M35` as the direct sum `M15⊕R20` from the rank identity. This reproduces dimension 35 but sets the horizontal extension block to zero by choice. The type gate explicitly shows that no connection splitting is established, so the direct sum is not a source-derived presentation.

## Acceptance test

1. freeze ordered retained bases and pivots for `M15` and `R20`;
2. construct the off-diagonal connection block modulo triangular gauge;
3. verify flatness and deletion–restriction compatibility;
4. recover the unsplit source residue column and all three oriented wall components;
5. compare with a held-out kinematic direction;
6. set the extension block to zero as a deliberate failure unless exact splitting is proved.

## Disposition

Complete-source occupancy is proved, but the complete source map is not constructed. The branch stops at the missing horizontal extension class and retained block matrices, not at the already-settled nonvanishing question.

## Evidence

- `src/ledger/20260818-656 Entry 653 Tests a Three-Pole Subpacket Not the Complete Physical Source.md`
- `src/ledger/20260818-657 The Complete Physical Source Occupies the Rank-Twenty Residue Quotient.md`
- `research/benincasa/physical_rank35_extension_type_gate.py`
- `research/benincasa/physical_five_pole_residue_occupancy_gate.py`
- `research/benincasa/check_generic_five_pole_base_change_rank.py`
- `research/benincasa/deletion_restriction_base_change_split.json`
