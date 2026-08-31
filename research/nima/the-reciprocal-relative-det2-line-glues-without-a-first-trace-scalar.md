# The reciprocal relative det2 line glues without a first-trace scalar

## Two analytic charts

Let \(U_+\) be the right relative chart and \(U_-\) its reciprocal left chart.
Their relative returns satisfy

\[
K_-(s)=\mathscr R_EK_+(1-s)\mathscr R_E^{-1}
\]

on the open overlap, with \(K_\pm\) holomorphic in \(\mathcal S_2\).
Define

\[
d_+(s)=\det_2(I-K_+(s)),
\qquad
d_-(s)=\det_2(I-K_-(s)).
\]

## Exact overlap identity

The order-two regularized determinant is invariant under bounded similarity.
Therefore

\[
d_-(s)=d_+(1-s)
\]

throughout the reciprocal overlap.

This is an exact clutching identity.  No term involving
\(\operatorname{Tr}K_\pm\) is required or even defined on all of the overlap.
The divergent finite first traces belong only to the comparison between an
ordinary finite Schur determinant and its order-two regularization.

## Relative determinant line

Let the reciprocal parameter cover identify the point in \(U_-\) labelled by
\(s\) with the point in \(U_+\) labelled by \(1-s\).  The preceding equality
makes \((d_+,d_-)\) a single holomorphic section

\[
d_{\rm rel}\in H^0(\mathscr S,\mathcal L_{\rm rel})
\]

of the relative determinant line.  Its transition function is the canonical
identity induced by \(\mathscr R_E\).  In particular, the relative line has no
extra scalar first-trace cocycle on this two-chart cover.

This does not trivialize the determinant line independently of the source
reciprocal identification; the trivialization is exactly the one transported
by \(\mathscr R_E\).

## Divisor and multiplicity

For a holomorphic \(\mathcal S_2\)-family, regularized determinant theory gives

\[
d_{\rm rel}(s_0)=0
\quad\Longleftrightarrow\quad
1\in\sigma(K_{\rm rel}(s_0)).
\]

The zero order equals the algebraic multiplicity of the eigenvalue-one
collision.  Combined with the closed-loop Schur theorem,

\[
\operatorname{ord}_{s_0}d_{\rm rel}
=
\dim_{\rm alg}\ker_{\rm gen}\mathcal C_{\rm FP}(s_0)
\]

on an invertible open-loop chart.

Thus the relative divisor already has the required operator-state and
multiplicity interpretation.

## Relation to finite ordinary determinants

At finite cutoff,

\[
\det(I-K_X)
=
\det_2(I-K_X)
\exp(-\operatorname{Tr}K_X).
\]

The exponential restores the ordinary finite determinant.  It is not a chart
transition for the completed \(\det_2\) line.  Attempting to pass the two
factors separately to the overlap recreates a divergent trace that
regularization was introduced to remove.

## G4 reduction

The reciprocal relative line, its kernel divisor, and algebraic multiplicities
are now closed on the declared \(\mathcal S_2\) overlap.  The remaining G4
comparison is a determinant-line morphism

\[
\mathcal L_{\rm Euler}^{(3)}
\otimes
\mathcal L_{\rm rel}^{(2)}
\otimes
\mathcal L_\infty
\longrightarrow
\mathcal L_\Xi
\]

whose scalar in source trivializations must be holomorphic and nowhere zero.
The unresolved anomaly is therefore not a relative first-trace overlap
anomaly.  It is the global comparison between the independently constructed
Euler, relative, archimedean, and Xi lines.

No RH conclusion is authorized.
