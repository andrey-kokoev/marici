# `q_G12` rank-35 flatness-extension audit

## Question

Do frozen rank-15 and rank-20 connection data plus the known unsplit source residue column determine or constrain the missing `15×20` extension block?

## Block equation

For a filtration-preserving rank-35 connection written in a retained splitting as

\[
A_{35}=\begin{pmatrix}A_{15}&E\\0&A_{20}\end{pmatrix},
\]

flatness requires the diagonal blocks to be flat and the off-diagonal block to satisfy

\[
dE+A_{15}\wedge E+E\wedge A_{20}=0
\]

up to the sign convention fixed by covariant versus contravariant transport. A triangular gauge changes `E` by the corresponding covariant coboundary. Thus flatness constrains an extension class only after `A15`, `A20`, their common parameter basis, and a gauge convention are materialized.

## Frozen-data audit

No source-labelled rank-15 deletion connection matrix was found. No source-labelled rank-20 residue connection matrix for this homogeneous five-pole deletion–restriction sequence was found. The available rank-20 interacting/soft systems concern different filtrations and cannot be substituted without an interface map.

The rank-35 type gate provides only ranks and one source Poincaré-residue column. It counts 300 scalar entries in `E` before constraints but supplies neither diagonal block nor derivatives of the source column. Therefore the flatness equation cannot be instantiated, and no residual dimension modulo gauge can be computed.

A frozen two-dimensional corner no-go establishes a further restriction: block-diagonal occurrence relabelling has diagonal gauge term and cannot create an off-diagonal extension entry. A source-derived triangular shear or the actual extension block is necessary. Hence cyclic coefficient dlogs cannot fill the missing block.

## Strongest falsification attempt

Set `E=0` and infer flatness from separately flat diagonal blocks. This constructs a split connection, but no source theorem establishes such a horizontal splitting. Moreover, the diagonal blocks themselves are absent for the required five-pole sequence. The zero choice is gauge-dependent presentation, not a derived extension.

## First missing objects

The first missing objects, in order, are:

1. source-labelled retained bases and parameter conventions for `M15` and `R20`;
2. exact connection matrices `A15` and `A20` in those bases;
3. the source residue column and its covariant derivatives in every declared parameter direction;
4. a triangular-gauge convention for representatives of `E`.

Only then is the linear flatness complex for `E` defined.

## Acceptance test

Construct the covariant differential on `Hom(R20,M15)`, compute its first cohomology or a gauge-fixed kernel, impose the known source column inhomogeneously, and report the exact residual dimension. Include `E=0` as a deliberate failure if it does not transport the unsplit source horizontally.

## Disposition

Flatness does not presently reduce the 300-entry extension problem because the two diagonal connection blocks needed to state its equations are absent. Block-diagonal symmetry transport is proved incapable of generating the missing extension.

## Evidence

- `research/benincasa/physical_rank35_extension_type_gate.py`
- `research/benincasa/checkers/audit_block_diagonal_descent_extension_no_go.py`
- `research/benincasa/results/block_diagonal_descent_extension_no_go.json`
- `research/benincasa/deletion_restriction_base_change_split.json`
