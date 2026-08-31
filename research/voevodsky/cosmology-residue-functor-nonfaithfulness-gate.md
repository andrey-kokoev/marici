# Residue functor nonfaithfulness gate for the p-normal lift

## Question

Does the residue-level monic comparison construct the pre-residue chain map required for \(\tau_p\)?

## Claim boundary

This packet tests the logical reverse step from residue equality to a source morphism. It does not construct a section of the residue exact sequence, a resolved/Rees exceptional generator with kernel data, a Cayley--Menger face cone, a Bockstein class, global contour, or physical period.

## Disposition

The residue comparison proves

\[
\operatorname{Res}(\Xi_{\log})=(1,-1,1)
\]

and identifies the opposite exceptional boundary with its negative. This fixes the visible coefficient.

It does not invert the residue functor. A minimal pre-residue model has basis

\[
(\Xi_{\log}^{\rm vis},k)
\]

and residue matrix

\[
\begin{pmatrix}
1&0\\
-1&0\\
1&0
\end{pmatrix}.
\]

The vector \((0,1)\) is invisible to residues. Therefore \((1,0)\) and \((1,1)\) have the same pair-face residue column \((1,-1,1)\). Equality after applying residue cannot select the pre-residue kernel component and cannot construct a source chain map.

Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), the pre-residue rank is \(2\), the residue image rank is \(1\), and the kernel rank is \(1\). Thus the residue functor is not faithful on the required lifting problem.

The remaining datum is a source-derived lift through the residue exact sequence that specifies the kernel component and proves total-differential compatibility. The local tests are now exhausted: Laurent primitive search, double residue, pair-face residues, ordered Čech residue cone, relative residue cocycle, universal \(\tau_p\) classifier, exceptional Čech leg, unit forcing, residue-level monic comparison, and the nonfaithfulness of residue as a reverse construction.

Further progress requires source data: a logarithmic Čech--de Rham residue exact sequence with a section on this class, a resolved/Rees exceptional generator with pre-residue kernel component, or a Cayley--Menger face cone supplying that kernel datum.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_residue_functor_nonfaithfulness_gate.py`

Result:

- `research/voevodsky/results/cosmology_residue_functor_nonfaithfulness_gate.json`

Command:

- `python research/voevodsky/check_cosmology_residue_functor_nonfaithfulness_gate.py`
