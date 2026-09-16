# The completed Clark pair is a fixed codiagonal sewing of four oriented resolvent cross-entries

## Upper and lower oriented charts

Let the upper-chart source-to-endpoint entries be

\[
M_0^+(z)
=
i
\int_0^\infty
\Phi(u)e^{izu}
\,du
=
iF(-iz),
\]

\[
M_1^+(z)
=
i
\int_0^\infty
u
e^{izu}
\Phi(u)
\,du.
\]

The reciprocal lower-chart entries are

\[
M_0^-(z)
=-i
\int_0^\infty
\Phi(u)e^{-izu}
\,du
=
-iF(iz),
\]

\[
M_1^-(z)
=-i
\int_0^\infty
u
e^{-izu}
\Phi(u)
\,du.
\]

Each pair is realized by the full-line translation resolvent in its natural half-plane orientation.

## Completed even transform

Put

\[
s=-iz.
\]

Then

\[
F(s)=-iM_0^+(z),
\qquad
F(-s)=iM_0^-(z).
\]

Therefore

\[
X(z)
=
\frac12
\left[
F(s)+F(-s)
\right]
=
\frac{i}{2}
\left[
M_0^-(z)-M_0^+(z)
\right].
\]

Thus Xi is the oriented codiagonal difference of the two zeroth-moment resolvent entries.

## Completed Clark pair

The moment identities give

\[
E(z)
=
X(z)+iX'(z)
=
\frac{i}{2}
\left[
-M_0^+(z)+M_0^-(z)
+M_1^+(z)+M_1^-(z)
\right],
\]

\[
E^*(z)
=
X(z)-iX'(z)
=
\frac{i}{2}
\left[
-M_0^+(z)+M_0^-(z)
-M_1^+(z)-M_1^-(z)
\right].
\]

Equivalently,

\[
\begin{pmatrix}
E\\
E^*
\end{pmatrix}
=
\frac{i}{2}
\begin{pmatrix}
-1&1&1&1\\
-1&1&-1&-1
\end{pmatrix}
\begin{pmatrix}
M_0^+\\
M_0^-\\
M_1^+\\
M_1^-
\end{pmatrix}.
\]

This sewing matrix is constant and source-independent.

## What this closes

The following pieces are now explicit:

1. the upper oriented selfadjoint resolvent chart;
2. the lower reciprocal chart;
3. zeroth- and first-moment source ports;
4. reciprocal reflection between the charts;
5. the exact fixed codiagonal producing \(X,E,E^*\).

No zero data or fitted coefficients occur.

## Control interpretation

The four resolvent entries are local transfer coordinates. The fixed two-by-four matrix is the reciprocal output interconnection producing the physical incoming and outgoing Clark ports.

The local chart systems are conservative Weyl systems. The global physical transfer is obtained only after their codiagonal interconnection.

## Remaining gate

A fixed output interconnection of two conservative systems need not be passive. The sewing matrix has an indefinite Clark signature, and passivity requires positivity of

\[
E(z)
\overline{E(w)}
-
E^*(z)
\overline{E^*(w)}.
\]

Therefore the remaining problem is exactly whether this codiagonal maps the direct sum of the two local Weyl kernels into a positive output kernel.

In operator language, if \(K_{\rm loc}\) is the direct-sum local Green kernel and \(S_{\rm Cl}\) is the displayed sewing matrix, one needs

\[
S_{\rm Cl}
K_{\rm loc}
S_{\rm Cl}^*
\ge0
\]

after the correct incoming-minus-outgoing polarization and boundary quotient.

This is the incidence-chamber condition. It does not follow from positivity of the two diagonal local kernels.

## Relation to the prospective 4-simplex

The two oriented Weyl charts provide the reciprocal tetrahedral faces. The constant codiagonal supplies their common scalar/output face. A top compatibility cell would have to show that Green pairing, determinant cofactor, and this codiagonal sewing descend together.

Thus the chart-gluing constructor is explicit. The unresolved 4-simplex content is positivity and oriented-minor preservation under that gluing.

## Disposition

The completed Clark pair is exactly a fixed codiagonal of four admitted local resolvent cross-entries. No additional analytic chart is missing. The remaining theorem is positivity of this already constructed reciprocal interconnection.
