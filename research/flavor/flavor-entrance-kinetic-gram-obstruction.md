# Entrance kinetic-Gram obstruction

## Bounded question

Can the canonical kinetic normalization used by the connector source be
treated entirely as a field-coordinate convention, or does the pair of
identically represented entrance doublets contain an undeclared physical
alignment coordinate?

## Field-rescaling quotient

For an isolated field with positive kinetic coefficient \(Z\), the change to
a canonical field rescales its masses and couplings together. Pole masses and
canonically normalized vertices descend under this presentation quotient.
WP508 already declares the canonical scalar and gauge field-space metric used
in the heavy-pole calculation. The vectorlike messenger stages carry distinct
row or port representations, so their individual positive wavefunction
factors can likewise be absorbed into the corresponding running couplings.

The entrance pair is different. Both \(H^u_\alpha\) and \(H^d_\alpha\) are
complex \((1,2,1/2)\) scalars and vectors of the same \(SO(3)_E\). Gauge
symmetry therefore permits

\[
\mathcal L_{\rm kin}=(D_\mu H^a)^\dagger K_{ab}(D^\mu H^b),
\qquad K=K^\dagger>0,
\]

with a general two-by-two Hermitian Gram. Canonicalization by
\(H=K^{-1/2}H_c\) transports the two declared Yukawa entrance covectors.
Their canonically normalized overlap is

\[
\rho={e_u^\dagger K^{-1}e_d\over
\sqrt{(e_u^\dagger K^{-1}e_u)(e_d^\dagger K^{-1}e_d)}}.
\]

It vanishes exactly only when the off-diagonal kinetic entry vanishes.

## Exact hostile pair

The canonical packet \(K_0=I_2\) gives \(\rho=0\). The equally positive and
gauge-authorized packet

\[
K_1=\begin{pmatrix}2&1\\1&2\end{pmatrix}
\]

has determinant three and gives \(\rho=-1/2\). Thus both packets have healthy
kinetic terms and the same field representations, but they induce inequivalent
relative up/down entrance geometry after canonicalization.

A common field redefinition cannot set \(K=I\) and simultaneously restore two
orthogonal fixed Yukawa axes unless the full interaction tensors are
transformed and admitted. Calling the canonical choice a convention while
retaining the old axis-aligned vertices silently drops the kinetic mixing
coordinate.

## Disposition

Kinetic normalization is not a global blocker for the connector theory. Its
only currently proved obstruction is the identical-representation entrance
doublet multiplicity. The existing gauge symmetry does not forbid the mixing.
The smallest repair is an independently declared source symmetry whose two
one-dimensional characters distinguish \(H^u\) from \(H^d\), or else an
enlarged coupling registry containing the complete two-family kinetic and
Yukawa tensors and their beta functions.

This operation neither descends to a numerical selector on `physical16` nor
creates a detector instrument. It identifies the first nonfaithful arrow in a
premature canonical-model export: deletion of the off-diagonal entrance
kinetic Gram.

## Reproduction

Run:

    python research/flavor/checkers/wp628_entrance_kinetic_gram_obstruction.py

The generated result is
`research/flavor/results/wp628_entrance_kinetic_gram_obstruction.json`.

