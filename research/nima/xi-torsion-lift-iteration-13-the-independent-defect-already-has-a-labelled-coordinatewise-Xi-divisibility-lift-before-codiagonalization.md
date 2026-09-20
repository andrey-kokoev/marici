# Xi-torsion lift iteration 13: the independent defect already has a labelled coordinatewise Xi-divisibility lift before codiagonalization

## Return to the shellwise theorem

The independent crossing theorem is stronger than the assembled scalar formula.
For every shell and seam it proves

\[
\Delta_{a,b,c}(z)
=
\tau(z)H_{a,b,c}(z),
\]

where

\[
H_{a,b,c}(z)
=
T_{PB}^{\rm rig}(e^{z\cdot}\otimes K_{1,c}).
\]

This equality holds in the complete bordered packet before prime loading,
cutoff summation, or scalar codiagonalization.

## Central labelled module

Let `Lambda` be the prime-power shell labels and define the weighted labelled
analytic module

\[
\mathscr B_{\rm lab}(U)
=
\left\{(F_\lambda)_\lambda:
F_\lambda\in\mathcal O(U;B_\lambda),
\text{ with the declared prime majorant}\right\}.
\]

The local ring `O(U)` acts coordinatewise. Prime cutoffs are coordinate
projections, and the spectral connection acts coordinatewise on the
holomorphic packet.

Define

\[
H^{\rm lab}(z)
=(\omega_\lambda H_\lambda(z))_\lambda,
\qquad
\Delta^{\rm lab}(z)
=(\omega_\lambda\Delta_\lambda(z))_\lambda.
\]

The established majorant places both packets in the labelled module on every
admitted compact spectral chart. Shellwise equality gives the genuine
vector-valued identity

\[
\boxed{\Delta^{\rm lab}=\tau H^{\rm lab}.}
\]

No inversion of the scalar codiagonal is involved.

## Torsion-freeness

Each coordinate module `O(U;B_lambda)` is torsion-free over the scalar
holomorphic ring: if `tau F_lambda=0` and `tau` is not identically zero, then
`F_lambda=0` on the open complement of its discrete divisor and hence
identically by analytic continuation.

The weighted labelled product is therefore torsion-free coordinatewise:

\[
\tau F=0
\Longrightarrow F=0.
\]

This conclusion requires neither Bohr recovery nor an `O`-linear scalar
codiagonal.

## Relationship to the scalar codiagonal

The scalar assembly

\[
\Sigma:\mathscr B_{\rm lab}\to B_{\rm border}
\]

is useful and is recoverable on the constant-coefficient source slice by the
four-chart/Bohr observers. It is not injective after full `O`-module saturation,
as iteration 12 showed.

That failure does not affect the labelled identity because divisibility was
proved before applying `Sigma`.

Accordingly, the logically correct statements are:

1. strict horizontal scalar codiagonal on the constant-coefficient analytic
   Köthe/Bohr source range;
2. canonical membership and recoverability of `H_border` on that range;
3. Xi-torsion-freeness in the central labelled analytic module, not as a
   consequence of scalar codiagonal injectivity.

## Cokernel qualification

If “bordered cokernel” means the scalar quotient after codiagonalization, its
Xi-torsion can still be nonzero because `Sigma` is not `O`-injective. If it
means the quotient of the labelled source construction before assembly, the
relevant `H` class is already zero/lifted and the ambient module is
torsion-free.

Thus the claimed equivalence depends on which cokernel is intended. The source
supports the labelled interpretation and rejects the saturated scalar one.

## RH boundary

The coordinatewise identity concerns labelled bordered Evans packets. It still
does not identify any coordinate with the Hermitian relative-Haar energy

\[
(1-p^{-2\operatorname{Re}z})E_p(b_z).
\]

A prime-diagonal metric localization map remains necessary for that step.

## Next audit

Trace the notation “bordered cokernel sector” to its declared interface. If it
is scalar, exhibit its finite-support holomorphic kernel explicitly and reject
the equivalence. If it is labelled, record objectives 1--3 as closed for the
Evans sector and move to the metric localization gate.