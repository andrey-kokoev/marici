# Cyclic local realizations and global pasting gate

## Question

Can every remaining local constructor and edge cell be realized, and do their interfaces already compose into the global cycle cell?

## Claim boundary

All local realizations below are fixture-level typed constructions. They establish existence and non-vacuity of the declared constructor classes, not source-global natural transformations. The global cycle is tested only after packet-interface compatibility.

## Realized local data

- \(G_C:P_C\to O_C^{\rm raw}\): the heat-jet, Gram, and shifted-Gaussian charts are generated from one atomic entire kernel.
- \(C_A:O_A\to R_A\): normalization, continuation, cutoff, and completion residues form a tagged sum; exact input gives certified zero and a perturbed normalization is detected.
- \(T_A:R_A\to P_B\): residue tags map injectively to matching arithmetic parameter tags.
- \(\alpha_B\): truncated raw probe evaluation differs from full evaluation by the exact tail \(\tau\), represented as an enclosure cell.
- \(\alpha_A\): transporting a normalization residue corrects \((4+\delta)E+4G+4P\) to \(4(E+G+P)\).
- \(\Phi_C^{\rm def}\) and \(\alpha_C^{\rm def}\): realized on the signed atomic deformation fixture; constant transport is rejected.
- Each symbolic local constructor tested commutes with the halving substitution defining the completed deformation family.

## Global pasting gate

The three edge cells use different fixtures and interface descriptors:

1. \(\alpha_A\): sector scalars and normalization residue;
2. \(\alpha_B\): completed-versus-truncated probe with tail enclosure;
3. \(\alpha_C^{\rm def}\): signed atomic obstruction and analytic deformation.

Equal notation does not construct their pullback. The first missing typed object is one common fixture/interface descriptor agreeing on coefficient convention, support, chart, residue type, and completion map. Without it, pasting them into \(\Omega_{ABC}\) would be a transport defect.

## Common-interface repair

`cyclic-common-interface.json` supplies one signed-even two-frequency kernel

\[
K=e^{-ta^2}\cos(az)-\varepsilon e^{-tb^2}\cos(bz)
\]

carrying normalization residue \(\delta\), tail enclosure \(\tau H\), raw probe charts, signed obstruction \(\varepsilon\), and gauge deformation on one parameter tuple. The sector split \((1/4,1/4,1/2)K\) reconstructs \(K\); omitting the prime sector is a deliberate nonzero failure.

On this pullback the three edge witnesses paste to the lax filler

\[
\Omega_{ABC}=(0,\tau H,0).
\]

The halving completion commutes with the sector and deformation cells. Neither uniqueness, contractibility, nor source-global naturality is asserted.

## Disposition

Every declared constructor, edge-cell class, and the global lax filler now has an explicit compatible fixture. Fixture-level categorical realization is complete. The remaining strength gap is source-global naturality: extending the common-interface filler from this signed-even kernel family to the full RH-model objects.

## Verification

- `research/voevodsky/cyclic-local-realizations.json`
- `research/voevodsky/checkers/check_cyclic_local_realizations.py`
- `research/voevodsky/results/cyclic_local_realizations.json`
