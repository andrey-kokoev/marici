# Deeper theta audit: Krein charge is exactly the framed Herglotz quotient

## Status

Exact spectral-measure identity and circularity audit. The neutral-mode picture
is physically faithful, but its unrestricted positivity theorem is exactly the
Herglotz property of the ordered theta transfer. Consequently constrained
Krein language does not become an RH explanation unless a source-local theorem
controls the signed spectral measure before resolvent or zero inspection.

## Signed spectral measure of the framed channel

Let \(A=A^*\), let \(K=K^*\) commute with \(A\), and suppose

\[
Kb=\alpha c,
\qquad
\alpha\in\mathbb R\setminus\{0\}.
\]

Let \(E_A\) be the spectral measure of \(A\). Define the signed measure

\[
d\mu(t)
=
\alpha^{-1}
d\langle b,KE_A(t)b\rangle.
\]

Then the ordered transfer is

\[
F(z)
=
c^*(A-zI)^{-1}b
=
\int_{\mathbb R}
\frac{d\mu(t)}{t-z}.
\]

The port mismatch has become the sign structure of one spectral measure.

## Exact resolvent-charge identity

Define the endpoint-resolvent state

\[
x_z
=
(A-zI)^{-1}b.
\]

Its modular charge is

\[
\langle x_z,Kx_z\rangle
=
\alpha
\int_{\mathbb R}
\frac{d\mu(t)}{|t-z|^2}.
\]

On the other hand,

\[
\operatorname{Im}F(z)
=
\operatorname{Im}(z)
\int_{\mathbb R}
\frac{d\mu(t)}{|t-z|^2}.
\]

Therefore

\[
\langle x_z,Kx_z\rangle
=
\alpha
\frac{\operatorname{Im}F(z)}{\operatorname{Im}z}
\]

for every nonreal \(z\) in the resolvent domain.

This is the exact bridge between the physical Krein energy and the analytic
Pick/Herglotz kernel.

## First consequence: neutrality at a zero

If

\[
F(z_0)=0,
\qquad
\operatorname{Im}z_0\ne0,
\]

then

\[
\langle x_{z_0},Kx_{z_0}\rangle=0.
\]

This recovers the neutral invisible constructor theorem.

## Second consequence: global positivity is Herglotz

Suppose \(\alpha>0\). The assertion

\[
\langle x_z,Kx_z\rangle>0
\]

throughout one open half-plane is equivalent to

\[
\frac{\operatorname{Im}F(z)}{\operatorname{Im}z}>0.
\]

That is precisely the Herglotz orientation of the framed scalar transfer.

Therefore a proposed proof that begins by declaring positive modular charge on
every resolvent state has assumed the analytic condition carrying the RH
burden. The physical vocabulary does not remove the circularity.

## Third consequence: positive spectral measure is sufficient but too strong

If

\[
d\mu\geq0,
\]

then \(F\) is Herglotz and has no zeros in either open half-plane. In finite
dimension this means every spectral residue

\[
w_j
=
\alpha^{-1}
\langle P_jb,KP_jb\rangle
\]

has one sign.

For the native theta transfer, proving that sign law is exactly the missing
orientation problem. Positive prime grammar in source coordinates does not
imply positivity after the oscillatory spectral transform.

## Two real equations at an off-seam zero

Write

\[
z=x+iy,
\qquad
y\ne0.
\]

The equation \(F(z)=0\) is equivalent to the simultaneous signed cancellations

\[
\int
\frac{t-x}{(t-x)^2+y^2}
\,d\mu(t)
=
0
\]

and

\[
\int
\frac{1}{(t-x)^2+y^2}
\,d\mu(t)
=
0.
\]

The second equation is modular-charge neutrality. The first is the vanishing
of the conjugate energy moment. An indefinite signed measure can satisfy both.

Thus the physical collision requires two tuned cancellations, not merely a
mixed signature.

## Exact hostile measure

Take three carrier poles

\[
-1,
\qquad
0,
\qquad
1
\]

with signed weights

\[
1,
\qquad
-1,
\qquad
1.
\]

Then

\[
F(z)
=
\frac{1}{-1-z}
-
\frac{1}{-z}
+
\frac{1}{1-z}
\]

has zeros at \(z=\pm i\). Both signed Poisson-type moments vanish there.

This finite measure is the spectral form of the three-state Krein hostile.

## What would be independently explanatory

The source theorem must precede the resolvent. Viable forms include:

1. a labelled incidence factorization expressing \(d\mu\) as the pushforward
   of a positive source measure through a sign-preserving map;
2. a variation-diminishing theorem forbidding the two simultaneous signed
   cancellations;
3. a source grading that pairs every negative spectral contribution with a
   boundary channel before scalar projection;
4. a total-positivity or sign-regularity theorem for the ordered port kernel;
5. a completed conservation law that is definite only on the full constrained
   zero-dynamics relation and is derived without reference to \(F\).

The first four are falsified immediately if hostile source perturbations
preserve the proposed source law while changing the signed spectral weights.

## Why seam augmentation remains meaningful

Adding the seam as an independent state can produce a positive full-system
energy. But full-system positivity governs the full multiport determinant. It
does not orient the cross transfer unless a source-derived incidence identity
ties the seam energy to the signed measure \(\mu\) of the ordered channel.

Therefore augmentation helps only if it proves a new framed identity. Merely
adding positive energy to invisible channels returns to the wrong-divisor
problem.

## Completion audit

For finite cutoffs \(X\), let \(F_X\), \(K_X\), and \(x_{X,z}\) satisfy the
same identity. A uniform constrained charge bound is equivalent to a uniform
lower bound on the imaginary-part quotient along the admitted state family.

If the admitted family is defined by the vanishing of \(F_X\), the statement
is circular. It becomes independent only when the state class is specified by
source incidence, transport, boundary, and residue equations that do not use
the scalar transfer value.

This is the categorical role of the complete constructor tree: it must define
admissibility before the zero readout is evaluated.

## Decisive conclusion

The physical Krein picture gives an exact explanation of what an off-seam zero
would physically be: a neutral invisible state. It does not yet explain why
that state is impossible. Whole-resolvent charge positivity is exactly the
RH-bearing Herglotz property in another coordinate.

The only noncircular next move is to derive a sign or no-cancellation law for
the ordered spectral measure from labelled theta/Tate incidence before forming
the resolvent transfer.
