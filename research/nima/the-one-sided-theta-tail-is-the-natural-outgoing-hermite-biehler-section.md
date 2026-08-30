# The one-sided theta tail is the natural outgoing Hermite--Biehler section

The common determinant lift \(E\) has a direct source candidate in the one-sided theta-tail construction.

For the completed one-sided forcing \(f(q)\), Grothendieck defined
\[
G_s(q)
=
e^{-sq}\int_q^{\infty}f(v)e^{sv}\,dv,
\]
with endpoint value
\[
G_s(0)
=
\int_0^{\infty}f(v)e^{sv}\,dv.
\]

After the centered spectral rotation, this one-sided endpoint transform is the natural outgoing section:
\[
E(z)
=
\text{completed outgoing trace of }G_{\frac12-iz}.
\]
The opposite orientation supplies its reflected partner
\[
E^{\#}(z).
\]

Bilateral modular sewing should then give the completed scalar as a parity combination:
\[
A(z)
=
\frac{E(z)+E^{\#}(z)}{2},
\]
or
\[
B(z)
=
\frac{E(z)-E^{\#}(z)}{2i},
\]
with wall and archimedean endpoint corrections included before the equality is asserted.

This has the correct authority order:

\[
f
\to
\text{one-sided tail state}
\to
E
\to
E^{\#}
\to
(A,B)
\to
\xi\text{ comparison}.
\]

No zero set is used to construct the companion section.

The decisive analytic theorem is that \(E\) is outgoing and zero-free in the upper half-plane. A zero
\[
E(z_0)=0
\]
would make the one-sided tail satisfy both endpoint conditions:
\[
G(0)=0,
\qquad
G(\infty)=0.
\]
Grothendieck's zero-to-state bridge therefore turns an upper-half-plane zero of \(E\) into a nontrivial homogeneous augmented state.

A strict one-sided passivity identity should exclude exactly such a state. In centered coordinates the target is
\[
2\operatorname{Im}z\,
\|G_z\|^2
+
\mathcal D(G_z)
=
\text{input flux}
-
\text{output flux}.
\]
For a zero-output, zero-terminal state with fixed source normalization, the right side must have the sign that forces contradiction when
\[
\operatorname{Im}z>0.
\]

To obtain the Hermite--Biehler inequality, zero-freeness alone is not enough. One needs the outgoing/incoming flux comparison
\[
|E^{\#}(z)|<|E(z)|
\]
in the upper half-plane. This is precisely the scalar scattering defect of the one-sided system.

Thus the same Green identity should prove both:

- \(E(z)\neq0\) in the upper half-plane;
- \(g(z)=E^{\#}(z)/E(z)\) is strictly Schur there.

The constant source channel is again essential. Without it, \(G_s\) solves an inhomogeneous equation and \(E\) is only a scalar transform, not a characteristic output of a homogeneous system node.

The completion formula must include every non-tail term. If the actual completed \(\xi\) has polynomial, gamma, wall, or endpoint pieces, they must arise as explicit finite boundary channels in \(E\). Adding them only after forming
\[
(E+E^{\#})/2
\]
can destroy Hermite--Biehler authority.

The concrete source audit is:

1. freeze the exact completed one-sided forcing;
2. construct the homogeneous augmented tail operator;
3. define its outgoing determinant/trace section \(E\);
4. derive the reflected incoming section as \(E^{\#}\);
5. prove the one-sided flux defect
   \[
   |E|^2-|E^{\#}|^2>0
   \]
   off seam;
6. compute the even and odd parity numerators;
7. identify one numerator with the completed \(\xi\)-section in the classical Mellin domain;
8. continue both independently.

The smallest hostile uses the raw Laplace transform
\[
\int_0^\infty f(v)e^{sv}\,dv
\]
as \(E\) but omits the constant, wall, or archimedean channels. Its symmetric part matches only a truncated scalar, while the flux inequality belongs to a different system.

A second hostile proves \(E\) zero-free but not
\[
|E^{\#}|<|E|.
\]
Then the two parity spectra need not be real or interlacing.

A third hostile defines the incoming section by complex conjugation only on the seam, without an analytic reflected constructor off seam.

This is the most concrete bridge yet from the existing theta source to de Branges geometry:

> The completed one-sided theta-tail output should be the outgoing Hermite--Biehler function whose parity part is \(\xi\).
