# The Evans-to-conservative-Green chain map already contains the RH confinement step

## Exact Evans state

The theta Koszul section has the two-sided history lift

\[
C_{\rm match}(z)i_{\rm Ev}(z)=w\tau(z).
\]

At every Xi zero \(z_0\), this supplies a nonzero two-ended forced history
\(u_{z_0}\) with zero seam mismatch.

## Proposed conservative promotion

A chain map to the paired maximal-isotropic Green pencil would require

\[
C_{\rm FP}(z)i(z)=w_{\rm FP}(z)\tau(z).
\]

At \(\tau(z_0)=0\), the image would be a nonzero Green-kernel state with
vanishing endpoint flux and all adjoint source equations satisfied.

## Off-seam Green identity

For the natural forced history,

\[
(\partial_q-a)u=c\Phi,
\]

the exact Green identity under zero endpoint flux is

\[
2a\|u\|^2
=
-2\operatorname{Re}
\bigl(c\langle u,\Phi\rangle\bigr).
\]

The conservative paired kernel cancels the forcing pairing through its lower
source equation. Consequently

\[
a\|u\|^2=0.
\]

For a nonzero promoted state, this forces

\[
a=0.
\]

Thus a completed chain map carrying every Xi residue to the conservative
Green kernel immediately confines every Xi zero to the critical seam.

## Logical strength

The statement

\[
\tau(z_0)=0
\Longrightarrow
0\ne i(z_0)\in\ker C_{\rm FP}(z_0)
\]

is not a routine determinant-factorization lemma. Together with the already
closed Green identity, it proves the RH confinement conclusion.

Moreover, RH alone would not automatically prove this chain map: seam zeros
must still satisfy the full complex adjoint residual and maximal-isotropic
domain conditions. The chain-map theorem is at least RH-strength and may be
strictly stronger than RH.

## Consequence for gate placement

The following objects must remain distinct:

1. **G4 divisor compiler:** the triangular stabilization
   \(K_\tau\oplus Q_U\), preserving determinant line and multiplicity;
2. **Evans lift:** the exact zero-to-two-ended-history map;
3. **RH-bearing promotion:** the chain map from the Evans/Koszul residue to the
   conservative Green kernel;
4. **confinement:** the Green identity applied to that promoted state.

Items 3 and 4 compose directly to RH. Calling item 3 a preliminary
constructor closure would hide the main theorem inside G4.

## Current residual

The three-port first row is

\[
(A-z)u=Vc+B_\Sigma x.
\]

The unchanged Evans history has \(c=1\) and already satisfies

\[
(A-z)u_z=V1.
\]

The successor packet
`distinct-seam-walls-make-the-centered-incidence-injective-and-exclude-an-exact-theta-lift.md`
proves \(\ker B_\Sigma=0\), so its arithmetic coordinate must be \(x=0\).
Promotion therefore requires the two lower residuals

\[
V^\dagger u_z=0,
\qquad
B_\Sigma^\dagger u_z=0.
\]

The arithmetic law \(D_U\) cannot cancel either residual for the unchanged
Evans state. A nonzero \(x\) necessarily changes the history and its seam
mismatch, requiring a new divisor-preserving chain comparison.

## Audit rule

Any proposed proof of the chain square must be checked for one of these hidden
insertions:

- defining \(D_U\) from the desired residual;
- dividing by \(\tau\);
- assuming all zeros already lie on the seam;
- replacing closure of \(\operatorname{ran}B_\Sigma\) by exact range;
- dropping the lower adjoint equation;
- using scalar determinant equality in place of a domain-preserving state
  map.

Each insertion assumes or bypasses the confinement theorem.

## Disposition

The triangular divisor compiler and analytic Evans lift are legitimate G4
objects. Promotion to the conservative maximal-isotropic kernel is the
RH-bearing theorem itself, not an administrative completion step. It remains
open at exact forcing lift, adjoint residual, seam domain, and multiplicity
transport. No RH conclusion is authorized.
