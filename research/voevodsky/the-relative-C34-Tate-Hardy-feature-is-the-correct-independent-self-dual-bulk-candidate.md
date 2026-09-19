# The relative C34 Tate--Hardy feature is the correct independent self-dual bulk candidate

The repository already contains an independently constructed bulk object with
the symmetry that the one-way feature lacked.  A relative positive feature is

\[
\mathfrak F=(C,D,J_2,\tau_{\rm rel}),
\qquad J_2=\operatorname{diag}(I,-I),
\]

where `C` is a bounded common row, `D rho(g)` is Hilbert--Schmidt, and the
cross contraction

\[
\rho(h)^*(C^*J_2D+D^*J_2C)\rho(g)
\]

is trace class.  Its signed observation is

\[
q_{\mathfrak F}(g,h)
=\operatorname{Tr}\rho(h)^*
(C^*J_2D+D^*J_2C)\rho(g)+e_{\rm end}(g,h).
\]

For the Tate--Hardy pair,

\[
C=\frac12(F_T+F_0),
\qquad
D=\frac12(F_T-F_0),
\]

and

\[
C^*C+D^*D=I,
\qquad
C^*J_2D+D^*J_2C=Q^T-Q^0.
\]

Finite regulators give ordinary positive Hilbert features, while the completed
limit retains only the finite relative cross current.  Polarity exchange acts
on the common/difference pair, so this object has an intrinsic reciprocal
self-dual structure rather than a one-way triangular orientation.

This makes the completed `C34` feature the correct independent arithmetic
bulk candidate for the middle facet.  It is constructed without Xi zeros,
retains source labels and endpoint rows, and does not modify the Xi determinant
because it is an external relative observation rather than a two-way Schur
feedback.

The remaining comparison is now explicit.  For the corrected lifted Xi source
`g_z=Phi tensor u_z`, prove

\[
q_{\mathfrak F_{34}}(g_z,g_z)=P(z)
\]

with the orientation and normalization required by the independent arithmetic
Green equation (equivalently the signed version needed to cancel the theta
forcing pairing).  This equality is not part of the internal definition of
`F_34`; it is the external `CG` mate and remains RH-strength.

Thus the independent bulk object is no longer missing.  What is missing is its
source comparison on the Xi pair lane.
