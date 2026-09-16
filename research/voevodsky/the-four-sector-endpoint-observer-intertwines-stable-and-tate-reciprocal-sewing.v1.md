# The four-sector endpoint observer intertwines stable and Tate-reciprocal sewing

## Carrier and basis

Let \(X_{m fb}=X_{L,z}\oplus X_{R,z}\oplus X_{L,-z}\oplus X_{R,-z}\), where each summand is the appropriate stable broken-history graph with continuous seam trace.

Let \(B_{m fb}=\mathbb C^4\) have ordered basis \((L,z),(R,z),(L,-z),(R,-z)\).

Define the endpoint observer by \(\mathcal O_{\rm fb}(u_{L,z},u_{R,z},u_{L,-z},u_{R,-z})=(u_{L,z}(0),u_{R,z}(0),u_{L,-z}(0),u_{R,-z}(0))\).

Continuity follows componentwise from the broken-\(H^1\) seam trace theorem.

## Corrected matrices

In the declared basis, stable exchange and stable Green sign are

\[
S_{\rm st}=\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix},
\qquad
J_{\rm st}=\operatorname{diag}(1,-1,1,-1).
\]

For a Tate phase \(|g|=1\), reciprocal exchange and reciprocal sign are

\[
R_g=\begin{pmatrix}0&0&g^{-1}&0\\0&0&0&g^{-1}\\g&0&0&0\\0&g&0&0\end{pmatrix},
\qquad
Z_{\rm rec}=\operatorname{diag}(1,1,-1,-1).
\]

These formulas correct the tensor-order ambiguity in the earlier Kronecker notation.

The quarter-turns \(F_{\rm st}=J_{\rm st}S_{\rm st}\) and \(F_{\rm rec}=Z_{\rm rec}R_g\) satisfy \(F_{\rm st}^2=F_{\rm rec}^2=-I\) and commute.

Their product is the unitary involution

\[
U_{\rm kin}=F_{\rm st}F_{\rm rec}
=\begin{pmatrix}
0&0&0&g^{-1}\\
0&0&-g^{-1}&0\\
0&-g&0&0\\
g&0&0&0
\end{pmatrix},
\qquad U_{\rm kin}^2=I.
\]

## Naturality

Let \(\widehat S_{\rm st}\) exchange the left- and right-stable history summands at fixed parameter sheet, and let \(\widehat R_g\) exchange the \(z\) and \(-z\) history sheets with the Tate factors \(g\) and \(g^{-1}\).

Componentwise endpoint evaluation gives the strict identities

\[
\mathcal O_{\rm fb}\widehat S_{\rm st}=S_{\rm st}\mathcal O_{\rm fb},
\qquad
\mathcal O_{\rm fb}\widehat R_g=R_g\mathcal O_{\rm fb}.
\]

Consequently \(\mathcal O_{\rm fb}\) also intertwines the two quarter-turns and \(U_{\rm kin}\).

The same-sign stable forcing and opposite reciprocal forcing occupy the vector \(e_{\rm st}^+\otimes e_{\rm rec}^-\), represented in the declared basis by \((1,1,-1,-1)^T\).

The stable Evans readout is

\[
D_{\rm Ev}=\begin{pmatrix}1&-1&0&0\\0&0&1&-1\end{pmatrix}.
\]

On the two independently constructed stable histories, \(D_{\rm Ev}\mathcal O_{\rm fb}\) equals \((\tau(z),\tau(-z))^T\) in the corresponding reciprocal charts.

## Faithful completed observer

Endpoint evaluation alone has a large kernel, so the completed observer retains the history together with its endpoint trace:

\[
j_{\rm fb}:X_{\rm fb}\longrightarrow X_{\rm fb}\oplus B_{\rm fb},
\qquad
j_{\rm fb}(u)=(u,\mathcal O_{\rm fb}u).
\]

This bounded joint-graph map is injective, has closed range, and intertwines stable and reciprocal transports. It supplies the required noncollapsing tail/bulk completion without replacing the history carrier by its endpoint plane.

## Green graph

Because \(U_{\rm kin}\) is unitary, its graph is maximal isotropic for the split boundary form

\[
\Omega((y,i),(y',i'))=\langle y,y'\rangle-\langle i,i'\rangle.
\]

This constructs a typed four-sector maximal-isotropic feedback graph at the finite boundary level.

The Xi application is the source-placement statement

\[
(\mathcal O_{\rm out}u_z,\mathcal O_{\rm in}u_z)\in\operatorname{Graph}(U_{\rm kin})
\quad\text{whenever}\quad \tau(z)=0.
\]

Its defect is the explicit vector

\[
\mathcal R_{\rm fb}(z)=\mathcal O_{\rm out}u_z-U_{\rm kin}\mathcal O_{\rm in}u_z.
\]

The constructed Evans equation gives \(D_{\rm Ev}\mathcal O_{\rm fb}u_z=(\tau(z),\tau(-z))^T\). A separate source identity is required to factor \(\mathcal R_{\rm fb}\) through this two-component Evans readout. Such a factorization, together with tail noncollapse and the full Green identity, is the theorem-strength feedback-admission step.

## Disposition

The typed four-sector endpoint observer, corrected stable and reciprocal matrices, commuting quarter-turns, faithful joint graph, and finite maximal-isotropic kinematic feedback graph are constructed. The remaining theorem is the source-derived factorization of \(\mathcal R_{\rm fb}\) through the reciprocal Evans section with all tail, arithmetic, wall, and archimedean ports retained.
