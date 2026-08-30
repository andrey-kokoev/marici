# The first adelic Green gate is a linear-to-quadratic polarization lift

The source-level correction does not yet produce a Green form. It exposes a
representation mismatch inside the theta source.

Poisson sewing is linear on the signed density labels \(\phi_n\). Positivity
of the labelled seam form is obtained after passing to amplitudes
\(\psi_n=\sqrt{\phi_n}\) and taking Gram overlaps. These operations do not
commute:

\[
\sqrt{\phi+\chi}\ne \sqrt{\phi}+\sqrt{\chi},
\]

and Fourier transformation does not canonically act on the pointwise square
roots. Therefore a positive amplitude Gram cannot simply be declared
Poisson-covariant.

There is an exact finite obstruction. Suppose a lift \(L\) is both additive
on positive densities and rank one:

\[
L(\phi)=|\psi_\phi\rangle\langle\psi_\phi|,
\qquad
L(\phi+\chi)=L(\phi)+L(\chi).
\]

If \(\psi_\phi\) and \(\psi_\chi\) are linearly independent, the right side has
rank two while the left side has rank one. If they are collinear, the lift has
already collapsed the two density directions. Thus no faithful additive
rank-one lift exists on a cone containing two independent theta densities.

The canonical linear positive alternative is the multiplication
representation

\[
\phi\longmapsto M_\phi.
\]

It preserves positivity and transports Poisson-linear identities, but it does
not reproduce the Hellinger Gram:

\[
M_\phi M_\chi=M_{\phi\chi},
\qquad
\langle\sqrt{\phi},\sqrt{\chi}\rangle
=\int\sqrt{\phi\chi}.
\]

Hence the source-level doubled Green theorem must choose which quadratic
functor is authorized, or enlarge the carrier so that both shadows are
projections of one object.

The smallest viable target is an operator-valued polarization
\(\Gamma(\phi,\chi)\) satisfying:

1. sesquilinearity before diagonal restriction;
2. \(\Gamma(\phi,\phi)\ge0\);
3. Poisson covariance under the source Fourier action;
4. recovery of the theta density on a declared scalar port;
5. recovery of the positive interval Green form on a different port;
6. retention of the external five-cell boundary coordinates;
7. faithfulness on the mixed source-observer directions used by the RH
   defect.

This is not automatically a completely positive lift of a scalar density.
Complete positivity alone permits the multiplication model and therefore does
not select the needed mixed Green geometry. The polarization and its ports
must be source-derived.

The decisive two-label hostile is a pair \(\phi,\chi\) for which Poisson
linearity fixes \(\phi+\chi\), while the proposed amplitude lift either
creates unauthorized cross terms

\[
|\sqrt\phi\rangle\langle\sqrt\chi|
+
|\sqrt\chi\rangle\langle\sqrt\phi|
\]

or deletes the mixed Green coordinate entirely. Scalar theta summation cannot
distinguish these outcomes.

Thus the earliest theorem is narrower than the full doubled adelic Green
identity:

> Construct a source-authorized operator-valued polarization of the linear
> theta density representation that is Poisson-covariant and whose Green and
> boundary ports are jointly faithful.

Only after this bridge exists can the exterior boundary observer be attached
and the five projected currents computed.
