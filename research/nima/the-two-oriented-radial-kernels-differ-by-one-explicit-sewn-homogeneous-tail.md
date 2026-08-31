# The two oriented radial kernels differ by one explicit sewn homogeneous tail

## Question

What is the gluing defect between the two weakly entire continuations of the free doubled radial resolvent?

## Claim boundary

On the common exponential test core, the difference is an explicit rank-one homogeneous solution of the doubled radial equation. It factors through one sewn bilateral Laplace functional and preserves the unitary wall relation. This computes the free gluing cell. It does not show that the completed-theta source cancels the cell or identify it with G4's arithmetic boundary feature.

## Common source core

Let

\[
\mathbb D_u=\partial_t\oplus(-\partial_t),
\qquad
f_-(0)=u f_+(0),
\qquad |u|=1,
\]

and take \(G=(g_+,g_-)\in\mathcal S_{\exp}^{\oplus2}\). Write

\[
\ell_z(g_+)=\int_0^\infty e^{-zs}g_+(s)\,ds,
\qquad
\ell_{-z}(g_-)=\int_0^\infty e^{zs}g_-(s)\,ds.
\]

Both functionals are entire and continuous on \(\mathcal S_{\exp}\).

## The two oriented factors

The continuation of the right-half-plane factor is

\[
(\mathcal R_{z,R}G)_+(t)
=-\int_t^\infty e^{z(t-s)}g_+(s)\,ds,
\]

\[
(\mathcal R_{z,R}G)_-(t)
=-u e^{-zt}\ell_z(g_+)
-\int_0^t e^{-z(t-s)}g_-(s)\,ds.
\]

The continuation of the left-half-plane factor is

\[
(\mathcal R_{z,L}G)_+(t)
=u^{-1}e^{zt}\ell_{-z}(g_-)
+\int_0^t e^{z(t-s)}g_+(s)\,ds,
\]

\[
(\mathcal R_{z,L}G)_-(t)
=\int_t^\infty e^{-z(t-s)}g_-(s)\,ds.
\]

The formulas are test-to-dual identities; no bounded Hilbert resolvent is asserted on the seam.

## Explicit difference

Define the sewn source functional

\[
A_z(G)=\ell_z(g_+)+u^{-1}\ell_{-z}(g_-).
\]

Combining the terminal and initial integrals over the full half-line gives

\[
(\mathcal R_{z,R}-\mathcal R_{z,L})G
=-A_z(G)
\binom{e^{zt}}{u e^{-zt}}.
\]

Thus the free gluing defect is the rank-one family

\[
\Gamma_z
=-
\binom{e^{zt}}{u e^{-zt}}
\otimes
\left(\ell_z,\,u^{-1}\ell_{-z}\right).
\]

Every factor is weakly entire on the exponential rigging, so \(z\mapsto\Gamma_z\) is weakly entire and compact-locally equicontinuous with all fixed parameter jets.

## Homogeneous and boundary checks

The tail vector satisfies

\[
(\mathbb D_u-z)
\binom{e^{zt}}{u e^{-zt}}=0.
\]

Its wall values obey

\[
u e^{-z\cdot0}=u e^{z\cdot0}.
\]

so the defect remains in the sewn maximal domain. Therefore

\[
(\mathbb D_u-z)\Gamma_z=0
\]

and both oriented factors solve the same source equation. The generated difference is exactly the homogeneous overlap syzygy anticipated by the transfer audit.

The directed wall trace is

\[
\gamma_+\Gamma_zG=-A_z(G),
\qquad
\gamma_-\Gamma_zG=-uA_z(G).
\]

Hence the gluing cell has one source coordinate and two wall traces related by the frozen sewing phase; it has no independent fitted comparison parameter.

## Source-cancellation criterion

For a source column \(U_X^{\rm rad}\), the two oriented responses agree exactly when

\[
A_z(U_X^{\rm rad}c)=0
\]

for every retained coefficient vector \(c\). Equivalently,

\[
\ell_z U_{X,+}^{\rm rad}
+u^{-1}\ell_{-z}U_{X,-}^{\rm rad}=0.
\]

This is the earliest exact source test. If it fails, the nonzero value must map into a declared G4 boundary feature; it cannot be removed by analytic continuation or a fitted wall phase.

## Limits of the result

The rank-one free defect cannot carry the infinite-dimensional Wronskian family. It only identifies the wall-mediated homogeneous tail. Reciprocal reflection fixes how the derivative-level boundary coordinate changes sign, while a metric adjoint still requires the separate variance-reversing full-history comparison. No arithmetic cancellation, conservative Green identification, Xi divisibility, or RH conclusion follows.

## Disposition

The free radial gluing cell is now explicit. The next bounded calculation is to insert the completed-theta ordered-pair source into \(A_z\), preserving reciprocal labels, and determine whether the resulting entire functional vanishes or is the source formula for a G4 arithmetic boundary port.
