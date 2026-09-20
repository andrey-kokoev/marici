# Xi-torsion lift iteration 12: O-module saturation destroys label injectivity because distinct exponentials are dependent over holomorphic germs

## Proposed jet enlargement

To repair iteration 11, one might enlarge the constant-coefficient exponential
source to

\[
K_O=O_{z_0}\widehat\otimes K,
\]

with synthesis

\[
J_O((a_\lambda))(z)
=
\sum_\lambda a_\lambda(z)e^{\lambda z}.
\]

This source is closed under multiplication by every holomorphic germ,
including `tau`, and under the spectral connection after the usual frequency
term is included.

## Finite-support kernel

The enlargement immediately destroys label injectivity. For any two distinct
frequencies `lambda_1,lambda_2`, take

\[
a_{\lambda_1}(z)=e^{(\lambda_2-\lambda_1)z},
\qquad
a_{\lambda_2}(z)=-1.
\]

Then

\[
a_{\lambda_1}(z)e^{\lambda_1z}
+a_{\lambda_2}(z)e^{\lambda_2z}=0
\]

identically. This hostile has finite label support and satisfies every Köthe,
Silva, and local analytic bound.

Thus exponentials are linearly independent over constants but maximally
dependent over holomorphic germs: each `e^(lambda z)` is a unit in `O_(z_0)`.
No topology can make `J_O` injective without restricting the coefficient ring
or retaining labels in the target.

## Polynomial jets do not solve the full problem

A finite polynomial-jet enlargement avoids the displayed exponential germ at a
fixed degree, but it is not closed under multiplication by a general `tau`.
Completing all polynomial degrees to analytic germs restores `O`-module closure
and restores the kernel above.

On the Fourier side, the same phenomenon appears as adjoining all derivatives
of point masses and then allowing analytic infinite-order combinations.

## Structural incompatibility

For an unlabelled scalar common history, the following three properties cannot
hold simultaneously:

1. continuous recovery of independent prime labels;
2. closure under the full local holomorphic ring `O_(z_0)`;
3. synthesis by scalar exponential atoms `e^(lambda z)`.

Bohr recovery achieves 1 and 3 by keeping coefficients constant in `z`.
Divisor torsion requires 2. Saturating to obtain 2 destroys 1.

This explains why objectives 1--2 do not become equivalent to objective 3 in
the scalar codiagonal category.

## Valid labelled alternative

In the central labelled module

\[
\prod_\lambda O_{z_0}e_\lambda,
\]

`O` acts diagonally and labels remain independent. It is torsion-free
coordinatewise. But the scalar codiagonal to holomorphic germs is not
`O`-injective. To use this alternative, the bordered identity itself must lift
to a labelled `O`-module identity before codiagonalization.

That is precisely the vector-valued defect lift identified in topology
iterations 39--42; it cannot be recovered from scalar Xi-divisibility.

## Consequence for H-border

The source construction gives a labelled constant-coefficient lift of
`H_border`, and Bohr topology recovers it. It does not imply that every
holomorphic multiple or divisor relation in the scalar bordered target lifts
labelwise. In particular,

\[
\Delta_{\rm border}=\tau H_{\rm border}
\]

remains one scalar module relation, not a coordinatewise Haar identity.

## Next direction

The only nonhostile continuation is to seek a source-derived **labelled
bordered identity** in the central module, or a metric localization map that is
already diagonal in prime labels. Further scalar-topology refinement cannot
simultaneously provide label recovery and full Xi-divisor module structure.