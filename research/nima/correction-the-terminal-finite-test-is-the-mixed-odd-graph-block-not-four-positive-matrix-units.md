# Correction: the terminal finite test is the mixed odd graph block, not four positive matrix units

## Retraction

The prior clue audit recommended testing

\[
G_{{\rm win},p}
=K_p^{\rm odd}G_{\theta,p}(K_p^{\rm odd})^*.
\]

Later source corrections reject this target twice.

First, `K_p^odd` is rank one while the ambient Stieltjes Green form has larger
rank, so no full-space pushforward equality is possible. Second, any positive
rank-one shadow has fixed sign, whereas the forcing difference

\[
R(z)-R(-z)
=-4\int_0^\infty\sinh(ar)\cos(tr)\,d\mu_\Phi(r)
\]

is reciprocal-odd and changes sign with spectral height. A positive diagonal
comparison cannot cancel it.

## Correct retained object

The completion-stable carrier is the graph

\[
\Gamma_p^{\rm odd}
=\{(y,K_p^{\rm odd}y):y\in E_{p,\theta}^{\rm odd}\}.
\]

Its Green block must retain the mixed coordinate

\[
\mathbb G_p=
\begin{pmatrix}
G_{\theta,p}&M_p\\
M_p^*&G_{{\rm win},p}
\end{pmatrix}.
\]

The reciprocal-odd current is the oriented mixed expression

\[
\mathcal J_p(y,y')
=
\langle y,M_pK_p^{\rm odd}y'\rangle
-
\langle K_p^{\rm odd}y,M_p^*y'\rangle,
\]

or its `i`-weighted Hermitian polarization. This can reproduce the
sign-indefinite causal odd current while the full graph energy remains
positive.

## Actual finite residual

The first valid test is

\[
\mathcal E_{p,X}^{\rm mix}
=
[\Gamma_{\rm P}(G_{p,X}^{\rm St})]_{XY}
-[\Gamma_{\theta,p,X}]_{XY},
\]

together with the reflected `YX` mate. Its diagonal evaluation must be

\[
-\bigl(F_{+,p,X}-F_{-,p,X}\bigr).
\]

The diagonal `XX` and `YY` forms only certify positivity and completion; they
do not perform the cancellation.

## Executability audit

The repository constructs:

- the linear incidence `K_p^odd j_theta=d_p`;
- the retained graph `Gamma_p^odd`;
- the causal forcing-difference current;
- endpoint and Wronskian orientations.

It does not provide a source formula for the mixed block `M_p`, nor an explicit
`XY` matrix for either side of the displayed residual. Therefore the corrected
finite test cannot yet be numerically or symbolically evaluated. Assigning
`M_p` from the desired forcing cancellation would be circular.

## Potential unlock, restated

The useful prior-research clue is narrower than previously stated: derive
`M_p` independently from the polarized C34 Tate--Hardy common/difference cross
contraction, then compare its finite `XY` and `YX` matrix units with the causal
odd history block. If that source derivation succeeds, the terminal test
becomes executable before Xi specialization.

The previous four-positive-matrix-unit recommendation is superseded.