# The contour transform is faithful on cohomology, not on local principal parts

## Green and curl stage

Let `F` be a finite-order puncture distribution with vanishing total sphere
mode. The normalized scalar Green operator solves

\[
 \Delta\Phi=F,\qquad \int_{S^2}\Phi=0.
\]

Equivalently, its kernel obeys

\[
 \partial_\xi\partial_{\bar\xi}\log S
 =2\pi\delta_\xi-\frac12\gamma_{\xi\bar\xi}.
\]

The subtraction is forced: the Laplacian image has zero integral. The inverse
is unique modulo the constant mode. For the spin-two potential reconstruction,
the additional scalar kernel of `D_z^2` consists of the `l=0,1` harmonics,
because its squared multiplier is

\[
 (l-1)l(l+1)(l+2).
\]

## Contour stage

On `X=S^2-P`, let `A` be the reconstructed one-form. For every contour `C`
avoiding `P`, the physical period is

\[
 \mathcal I_C(A)=\oint_C A.
\]

Stokes gives `I_C(A)=<dA,chi_Sigma>` for a regularized region cutoff. Around
one puncture, a meromorphic local presentation

\[
 A=\sum_{k=1}^{N}a_{i,k}\frac{dz}{(z-\xi_i)^k}+dX+\text{regular}
\]

has period

\[
 \boxed{\oint_{C_i}A=2\pi i\,a_{i,1}.}
\]

All `k>=2` terms are local derivatives and have zero period. Exact shifts
`dX` also vanish. Therefore the contour transform factors through de Rham
cohomology:

\[
 \Omega^1(X)\longrightarrow H^1_{\rm dR}(X)
 \xrightarrow{\rm periods}\mathbb C^{|P|-1}.
\]

The second arrow is faithful for the complete contour basis. The first is the
nonfaithful quotient.

## Boundary relation

For small positively oriented loops around all punctures,

\[
 \sum_i[C_i]=0,
 \qquad \sum_i\operatorname{Res}_{\xi_i}A=0.
\]

Thus `|P|-1` periods are independent. In a one-chart presentation the missing
relation appears as the boundary period at infinity; it is not an additional
source record. Omitting that boundary port can falsely make the finite
puncture residues appear unconstrained.

## Distribution jets

Under the Cauchy boundary identity, a simple pole produces a delta mass and a
nonzero period. Higher Cauchy powers produce derivatives of delta. A contour
whose boundary avoids the puncture pairs with a cutoff constant near the
puncture, so these derivative jets have zero unweighted period. They remain
visible to local test-function ports but not to the ordinary contour family.

Hence the joint readout

\[
 (\text{local coefficient ports},\text{period ports})
\]

is strictly finer than periods alone. The latter deliberately retain only
the global cohomology class.

## First-nonfaithful-arrow classification

1. Green inversion loses the constant mode, and spin-two reconstruction loses
   the declared `l<=1` scalar modes.
2. Passage from one-forms to periods loses exact forms and higher-pole local
   derivatives.
3. The complete period basis loses nothing further on `H^1(X)`.
4. Selecting only one contour introduces an additional linear projection
   kernel among the residue coordinates.

This is the physical combinatorial shadow of rational exactness: contractible
principal-part data are removed, while cycles survive as boundary periods.

## Evidence

`checkers/completed_local_to_contour_transform_checks.py` verifies the residue
period law, exactness of higher poles, the global residue relation, complete
period rank, single-contour deficiency, Green zero modes, and delta-jet
visibility.
