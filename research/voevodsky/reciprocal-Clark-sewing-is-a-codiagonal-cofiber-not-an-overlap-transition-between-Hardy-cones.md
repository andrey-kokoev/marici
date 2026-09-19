# Reciprocal Clark sewing is a codiagonal cofiber, not an overlap transition between Hardy cones

Fresh inspection of the completed Clark construction corrects the seam-descent
shape proposed in the previous iteration.  The physical completion is not an
isomorphism from the upper Hardy cone to the lower Hardy cone.  It is the fixed
codiagonal interconnection

\[
S_{\rm Cl}=\frac{i}{2}
\begin{pmatrix}
-1&1&1&1\\
-1&1&-1&-1
\end{pmatrix}
\]

on the direct sum of the four oriented zeroth/first-moment cross entries.
Therefore maps `J_rec:X^+->X^-` and `J_Gr:X^+->X^-` are the wrong model for
physical sewing.  The determinant-frame transition is an overlap transition;
the Clark completion is a many-to-one output constructor.

At cone-package strength, form the direct sums

\[
L_{\rm rec}=X_{CG}^{\rm rec,+}\oplus X_{CG}^{\rm rec,-},
\qquad
L_{\rm Gr}=X_{CG}^{\rm Gr,+}\oplus X_{CG}^{\rm Gr,-},
\]

with the local comparison

\[
\kappa_{\rm loc}=\kappa_{CG}^+\oplus\kappa_{CG}^-.
\]

A global comparison requires source-derived lifted codiagonals

\[
\widetilde S_{\rm rec}:L_{\rm rec}\to C_{\rm comp},
\qquad
\widetilde S_{\rm Gr}:L_{\rm Gr}\to G_{\rm comp},
\]

and a map `kappa_comp:C_comp->G_comp` making

\[
\kappa_{\rm comp}\widetilde S_{\rm rec}
\simeq
\widetilde S_{\rm Gr}\kappa_{\rm loc}
\]

commute before determinant scalarization.  The global interval package is the
mapping cone/cofiber of the lifted codiagonal, so its comparison is induced by
this square via cofiber functoriality.

The scalar matrix `S_Cl` constructs only the output row of these lifts.  Since
it is noninjective, replacing either lifted codiagonal by its two scalar outputs
would discard precisely the relative kernel required by the cone package.

The correct sewing obstruction is consequently the Beck--Chevalley/cofiber
comparison

\[
\beta_{CG}:
\operatorname{cofib}(\widetilde S_{\rm rec})
\longrightarrow
\operatorname{cofib}(\widetilde S_{\rm Gr}),
\]

not a commutator of upper-to-lower transition maps.  Its determinant shadow is
already controlled by the unitary seam transition, but `beta_CG` itself and
its oriented-minor/chamber preservation remain unconstructed.
