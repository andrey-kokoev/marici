# The Clark matrix canonically lifts on the Green side as a mapping cone of the augmented observation

The local full-line models already provide bounded graph-domain observations
for the zeroth and first source moments.  On the reciprocal direct sum let

\[
\mathcal H_{\rm loc}=\mathcal H_+\oplus\mathcal H_-
\]

and collect the four cross-port observations into

\[
\mathcal O_{01}:\mathcal D_{\rm gr}(T_+)\oplus
\mathcal D_{\rm gr}(T_-)
\longrightarrow\mathbb C^4.
\]

Because each component is continuous in the admitted graph norm,
`O_01` is bounded.  The fixed Clark matrix therefore defines a bounded
completed observation

\[
\mathcal O_{\rm Cl}:=S_{\rm Cl}\mathcal O_{01}:
\mathcal D_{\rm gr}(T_+)\oplus\mathcal D_{\rm gr}(T_-)
\longrightarrow\mathbb C^2.
\]

This supplies the Green-side lifted codiagonal without quotienting away its
null directions:

\[
\widetilde S_{\rm Gr}
:=\operatorname{Cone}(\mathcal O_{\rm Cl})
=
[\mathcal D_{\rm gr}(T_+)\oplus\mathcal D_{\rm gr}(T_-)
 \xrightarrow{\mathcal O_{\rm Cl}}\mathbb C^2].
\]

Its degree-minus-one cohomology retains

\[
\ker\mathcal O_{\rm Cl},
\]

which scalar Clark evaluation would discard.  No positivity or Xi-zero input
is needed for this closed cone construction; positivity remains a later Hodge
or incidence-chamber condition.

There is no symmetric construction yet on the characteristic side.  The
available completed characteristic object is a determinant line obtained
after scalarization.  It does not contain a graph-domain map to which
`S_Cl` can be applied before taking cofibers.  Consequently
`tilde S_rec` cannot be obtained merely by reusing the two-by-four scalar
matrix on determinant sections.

Thus reciprocal sewing is now asymmetric in a precise direction:

- Green lifted codiagonal and its relative kernel package: constructed;
- characteristic/reciprocal lifted codiagonal before determinant: missing;
- comparison `beta_CG`: blocked exactly by that missing pre-determinant lift.

Defining the characteristic lift to be the Green cone would close the square
by identity but violate the independence firewall.  It must instead arise from
the reciprocal/characteristic source construction and only then be compared
with the Green cone.
