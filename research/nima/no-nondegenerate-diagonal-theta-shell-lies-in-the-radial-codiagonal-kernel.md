# No nondegenerate diagonal theta shell lies in the radial codiagonal kernel

## Question

Does the balanced endpoint–Wronskian kernel of the minimal radial graph intersect the actual diagonal completed-theta shell range?

## Claim boundary

No for any nondegenerate diagonal shell, and no for a same-sign positive loading of such shells. Kernel membership would force the diagonal autocorrelation to vanish identically, while its wall value is the strictly positive shell square norm. Signed or complex cross-shell combinations remain a separate question.

## Diagonal shell

Fix a real completed-theta label \(n\) and a nontrivial shell \([a,b]\). Its autocorrelation is

\[
\rho_n(t)
=
\int_a^b\Phi_n(u)\Phi_n(u+t)\,du.
\]

The exact radial Stokes identity is

\[
\rho_n'(t)
=e_n(t)-\frac12w_n(t),
\]

where \(e_n\) is the directed endpoint source and \(w_n\) is the ordered Wronskian current.

## Kernel contradiction

Membership in the codiagonal kernel requires the complete function-valued identity

\[
e_n(t)=\frac12w_n(t)
\]

on each oriented half-line. Hence

\[
\rho_n'(t)=0.
\]

Rapid exterior decay forces

\[
\rho_n(t)=0
\]

on both orientations and therefore at the wall.

But

\[
\rho_n(0)
=
\int_a^b\Phi_n(u)^2\,du.
\]

The real analytic completed-theta atom is not identically zero on a nontrivial shell. Its square is nonnegative and positive on an open subset, so

\[
\rho_n(0)>0.
\]

This contradicts kernel membership. Therefore

\[
J_{{\rm or},n}^{[a,b]}
\notin\ker D
\]

for every nondegenerate diagonal shell.

## Same-sign diagonal loading

Let a finite or absolutely convergent diagonal loading have real coefficients \(\omega_\lambda\ge0\), not all zero. Its wall value is

\[
\rho_{\omega}(0)
=
\sum_\lambda\omega_\lambda
\int_{a_\lambda}^{b_\lambda}
\Phi_\lambda(u)^2\,du.
\]

Every nonzero term is positive, so

\[
\rho_{\omega}(0)>0.
\]

The loaded packet therefore cannot lie in the balanced codiagonal kernel. This conclusion uses same-sign loading and does not extend to signed or complex coefficients by positivity alone.

## What remains open

Three larger source classes require separate audits:

1. signed diagonal combinations whose wall norms can cancel;
2. ordered off-diagonal label pairs, where \(\rho_{nm}(0)\) is not a square norm;
3. post-codiagonal common-history combinations with cross-prime metric coupling.

For those classes, one must use label recovery, Fourier faithfulness, or a direct function-valued endpoint–Wronskian independence theorem. A nonzero wall value is a sufficient obstruction, not the only possible one.

## G4 consequence

If G4 uses the radial codiagonal as a quotient feature, its balanced radical does not remove any individual diagonal theta shell or any same-sign positive diagonal assembly. A claimed diagonal gauge nullity would contradict the positive wall square unless G4 changes the metric, introduces signed coupling, or applies another quotient.

Thus candidate-one diagonal information survives the minimal codiagonal. Any actual G4 radical affecting it must be sourced later in the architecture.

## Direction rescore

- Individual diagonal-shell intersection with the codiagonal kernel: excluded.
- Same-sign positive diagonal loading: excluded.
- Signed diagonal loading: 7/10; requires independence beyond wall positivity.
- Ordered off-diagonal packets: 7/10.
- G4 radical comparison: interface-blocked.

## Disposition

The minimal codiagonal kernel is real but does not contain the nondegenerate diagonal completed-theta source. The diagonal radial feature therefore survives codiagonalization at source level. Remaining kernel questions concern signed, off-diagonal, or G4-coupled assemblies, not individual diagonal shells. No RH conclusion is authorized.
