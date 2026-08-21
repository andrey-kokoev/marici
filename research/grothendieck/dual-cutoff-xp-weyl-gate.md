# Dual-cutoff dilation has the right leading zeta-zero density

Epistemic-graph event: 1396.

## Minimal phase-space enlargement

The compact-circle boundary of Ledger 1367 has only linear Weyl growth.  The
smallest classical dilation phase space with growing volume uses

`H(x,p)=xp`

in the positive quadrant, with dual cutoffs

`x>=ell_x`, `p>=ell_p`, and `xp<=E`.

Its exact area is

`A(E)=integral_(ell_x)^(E/ell_p)(E/x-ell_p)dx`

`=E log(E/(ell_x ell_p))-E+ell_x ell_p`.

Dividing by one Planck cell `2 pi hbar` and imposing the self-dual product

`ell_x ell_p=2 pi hbar`

gives

`N_xp(E)=E/(2 pi hbar)(log(E/(2 pi hbar))-1)+1`.

For `hbar=1`, the two growing terms agree exactly with the smooth
Riemann--von Mangoldt count

`N_zeta(E)=E/(2 pi)log(E/(2 pi))-E/(2 pi)+7/8+S(E)+O(1/E)`.

The raw phase-volume constant is `1`, not `7/8`; the discrepancy is `1/8`.
Neither the fluctuating term `S(E)` nor individual zero ordinates follows
from phase volume.

## Quantum typing

The symmetric quantization is the Mellin dilation operator

`H_hat=(xp+px)/2=-i hbar(x d/dx+1/2)`.

The position cutoff alone is a local boundary, but the momentum cutoff is
nonlocal in the position representation.  A self-adjoint realization of both
requires a Fourier-dual boundary operator, not merely a compact interval or
the Mobius sign local system.

## Carrier audit

The paired coefficient--Betti system supplies a bilinear evaluation pairing
and adjoint pull--push legs.  It does not currently supply:

1. a real symplectic form with Heisenberg commutator `[x,p]=i hbar`;
2. positive half-line coordinates `x,p`;
3. a source-normalized Planck cell;
4. dual cutoff projectors with product `2 pi hbar`; or
5. a self-adjoint boundary law implementing both cutoffs.

Thus the `xp` region is the first candidate with the correct spectral growth,
but it is not yet source-derived from Marici.  Matching the leading count is
a necessary-shape result, not evidence that the zeros are its spectrum.

## Hostile gate

The next candidate must derive the dual cutoff operators and their product
normalization before inspecting zeros.  A boundary fitted using the Riemann--
Siegel phase, `xi`, or zero data is circular and rejected.

## Primary comparison

This audit uses the established `xp` regularization framework discussed in
G. Sierra, *A quantum mechanical model of the Riemann zeros*,
arXiv:0712.0705, and G. Sierra--J. Rodriguez-Laguna, *The H=xp model
revisited and the Riemann zeros*, arXiv:1102.5356.  The area calculation and
Carrier typing above are independent derivations.

## Scope

No quantized dual-cutoff operator, determinant `xi`, Riemann hypothesis, or
physical Carrier realization is asserted.
