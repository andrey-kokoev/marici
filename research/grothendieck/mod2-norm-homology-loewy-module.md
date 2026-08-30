# Residual norm homology is the augmentation ideal modulo its socle

Epistemic-graph event: 1362.

## Module identification

For a collapsed branch set `B` of size `k`, let

`A_B=F_2[epsilon_i:i in B]/(epsilon_i^2)`

and let `I_B=(epsilon_i:i in B)` be its augmentation ideal.  The socle of
`A_B` is the one-dimensional top line

`Soc(A_B)=F_2 epsilon_B`.

The square-zero norm homology from Ledger 1341 is canonically

`H(A,N_B) congruent (I_B/Soc(A_B)) tensor A_(B^c)`.

The kernel of multiplication by `epsilon_B` is `I_B tensor A_(B^c)`, and its
image is `Soc(A_B) tensor A_(B^c)`, proving the identification.

## Loewy theorem

For `k>=2`, viewed under the collapsed-kernel augmentation ideal, this module
has Loewy length `k-1`.  Its successive layers have ranks

`binomial(k,1), binomial(k,2), ..., binomial(k,k-1)`

times the spectator module `A_(B^c)`.  Equivalently, layer `r` is represented
by collapsed monomials of degree `r+1`, for `0<=r<=k-2`.

For `k=1` the module is zero.  For `k=2` it is already semisimple under the
collapsed kernel, with two degree-one generators.  For `k=5` its Loewy layers
have dimensions `5,10,10,5`.

## Interpretation

The residual bad-prime information is not an unstructured rank defect.  It
is the entire proper part of the Boolean augmentation module: the unit is
excluded by the kernel condition and the top socle is killed as norm image.
Successive kernel actions climb the remaining subset lattice until the
removed top class forces zero.

This is formal deck-module structure.  It neither proves geometric support
for all branch intersections nor supplies physical relative chains.
