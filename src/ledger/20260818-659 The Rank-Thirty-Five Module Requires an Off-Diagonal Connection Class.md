---
authors:
  - marici.Nima
date: 2026-08-18
---
# 659 — The Rank-Thirty-Five Module Requires an Off-Diagonal Connection Class

## Hard-to-vary claim

The rank identity \(35=15+20\) and the exact source Poincare-residue column
do not reconstruct the physical rank-thirty-five Gauss--Manin module. The
remaining datum is the off-diagonal extension class joining deletion and
residue transport.

## Fiberwise exact sequence

Entries 596 and 657 give the exact sequence of generic fibers

\[
0\longrightarrow M_{15}^{\rm del}
\longrightarrow M_{35}^{\rm phys}
\xrightarrow{\operatorname{Res}_{G_{12}}}
M_{20}^{\rm res}
\longrightarrow0.
\]

As a sequence of vector spaces over a field, it splits noncanonically. A
choice of splitting would identify

\[
M_{35}\simeq M_{15}\oplus M_{20}.
\]

But no such choice is part of the source geometry.

## Connection block

In a chosen triangular frame, the connection has schematic form

\[
\nabla_{35}
=d+
\begin{pmatrix}
A_{15}&B_{15\times20}\\
0&C_{20}
\end{pmatrix}.
\]

The diagonal blocks describe deletion and residue transport. The
off-diagonal one-form matrix \(B\) represents their extension, modulo
triangular gauge. Before flatness and symmetry constraints it contains

\[
15\cdot20=300
\]

scalar one-form entries.

The source identity

\[
\operatorname{Res}_{G_{12}}\Omega_{\rm pre}
=\Omega_{\rm phys}
\]

fixes one distinguished residue column. It does not determine the complete
off-diagonal transport block or its gauge class.

## Consequence

The proposed efficient block construction is admissible only if it retains
the extension data. Replacing the rank-thirty-five object by a direct sum

\[
M_{15}\oplus M_{20}
\]

would silently assert \(B=0\) and choose a splitting not derived from the
source.

Thus

\[
\boxed{
\text{fiber ranks + source residue column}
\ne
\text{physical Gauss--Manin extension}.
}
\]

## Relation to the localization problem

Entry 658 correctly identifies \([\Omega_{\rm phys}]\) as a source-defined
basepoint in the post-residue relative fiber. Entry 655 shows exact IBP
changes cannot alter its wall-cohomology class. Neither statement fixes the
pre-residue extension block \(B\), and neither supplies an absolute
\(\mathcal T_7\) retraction.

## Updated frontier

Construct only the source-generated horizontal saturation, rather than all
300 unconstrained entries:

1. retain the pre-residue source column and its exact residue image;
2. differentiate it in independent kinematic directions;
3. reduce deletion components in the rank-fifteen block and residue
   components in the rank-twenty block;
4. iterate until the generated submodule stabilizes;
5. test whether the resulting off-diagonal class is invariant under changes
   of block splittings.

This computes the smallest source-relevant part of \(B\) without asserting
a direct-sum decomposition.

## Evidence

- `research/benincasa/physical_rank35_extension_type_gate.py`;
- `research/benincasa/physical_five_pole_g12_residue.py`;
- Entries 596 and 655--658.

## Outcome contract

~~~json
{
  "claim": "The rank-fifteen deletion block, rank-twenty residue block, and one source residue column determine the physical rank-thirty-five connection.",
  "status": "falsified_by_extension_typing",
  "exact_sequence_ranks": [15, 35, 20],
  "fiberwise_splitting": "noncanonical",
  "connection_splitting_established": false,
  "off_diagonal_block_shape": [15, 20],
  "source_residue_column_known": true,
  "missing_datum": "off-diagonal Gauss-Manin extension class modulo triangular gauge",
  "next_experiment": "Compute the source-generated horizontal saturation across the deletion-residue extension."
}
~~~
