# Correction: the published tail integral solves the opposite-signed flow equation

## Audited formulas

The current source packet states both

\[
G_z(q)=-\int_q^\infty e^{z(q-r)}\Phi(r)\,dr
\]

and

\[
(\partial_q+z)G_z=-\Phi.
\]

These formulas are not compatible under the ordinary derivative convention.

Set

\[
I_z(q)=\int_q^\infty e^{z(q-r)}\Phi(r)\,dr,
\qquad G_z=-I_z.
\]

Leibniz differentiation gives

\[
I_z'(q)=-\Phi(q)+zI_z(q),
\]

hence

\[
G_z'(q)=\Phi(q)+zG_z(q).
\]

Therefore the displayed integral satisfies

\[
\boxed{(\partial_q-z)G_z=\Phi},
\]

not \((\partial_q+z)G_z=-\Phi\).

## Two consistent repairs

One may retain the integral and replace the flow equation by

\[
(\partial_q-z)G_z=\Phi.
\]

Alternatively, to retain \((\partial_q+z)G_z=-\Phi\), one must use

\[
G_z(q)=\int_q^\infty e^{z(r-q)}\Phi(r)\,dr,
\]

in the half-plane where this terminal integral converges. These alternatives have different stability half-planes and Green boundary signs; they cannot be interchanged silently.

## Effect on the Green face

For the published integral convention,

\[
G_z'=zG_z+\Phi,
\qquad
\overline{G_w'}=\bar w\,\overline{G_w}+\overline{\Phi}.
\]

Thus

\[
\partial_q(\overline{G_w}G_z)
=(z+\bar w)\overline{G_w}G_z
+\overline{\Phi}G_z
+\overline{G_w}\Phi.
\]

After integration and decay at infinity,

\[
(z+\bar w)\langle G_w,G_z\rangle
=-\overline{G_w(0)}G_z(0)
-\langle\Phi,G_z\rangle
-\langle G_w,\Phi\rangle.
\]

This has the opposite endpoint sign from the previously quoted positive Green identity.

## Lattice consequence

The abstract sum/difference Gram factorization of the forcing reservoir remains algebraically valid. However, the claim that it combines with the endpoint trace to produce the stated positive tail Green face depends on selecting and freezing one consistent flow convention.

Accordingly, the prior coordinate \(g=1\) must be refined:

- \(g_{\rm alg}=1\): forcing reservoir has a sum/difference Gram factorization;
- \(g_{\rm oriented}=0\): the published integral, flow equation, and endpoint orientation have not yet been reconciled.

The corrected local coordinates are therefore

\[
(t,g_{\rm alg},g_{\rm oriented})=(1,1,0).
\]

## Acceptance gate

Freeze exactly one of the two consistent repairs, state its stability half-plane, rerun the polarized integration by parts, and propagate the selected sign through the doubled reciprocal sewing and Krein metric. Until then, the positive Green face is not analytically certified with the published tail integral.

## Claim boundary

This is a sign/type correction. It does not reject existence of a consistently oriented positive tail model; it rejects simultaneous use of the currently displayed integral and flow equation.
