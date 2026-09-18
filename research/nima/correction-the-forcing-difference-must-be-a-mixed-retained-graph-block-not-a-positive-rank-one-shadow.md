# Correction: the forcing difference must be a mixed retained-graph block, not a positive rank-one shadow

The forcing residual

$$
R(z)-R(-z)
$$

is reciprocal-odd and sign-indefinite. On the Hermitian diagonal it is the oscillatory separation transform

$$
-4\int_0^\infty\sinh(ar)\cos(tr)\,d\mu_\Phi(r),
$$

which changes sign with spectral height.

By contrast,

$$
K_p^{\rm odd}G_{\theta,p}(K_p^{\rm odd})^*
$$

is a positive rank-one operator whenever `G_theta,p` is positive. It cannot equal, or cancel, the sign-indefinite forcing residual. The proposed rank-one odd-response pushforward is therefore not the required cancellation law unless an additional oriented/skew matrix unit is explicitly retained.

Prior work identifies the completion-stable object as the retained graph

$$
\Gamma_p^{\rm odd}
=\{(y,K_p^{\rm odd}y):y\in E_{p,\theta}^{\rm odd}\},
$$

not the soft output alone. On this graph, the cancelling current must occupy a mixed block between the retained theta coordinate and the window output. Schematically, with

$$
\mathbb G_p=
\begin{pmatrix}
G_{\theta,p}&M_p\\
M_p^*&G_{{\rm win},p}
\end{pmatrix},
$$

the reciprocal-odd supply is

$$
\mathcal J_p(y,y')
=
\langle y,M_pK_p^{\rm odd}y'\rangle
-
\langle K_p^{\rm odd}y,M_p^*y'\rangle
$$

in the analytic-transpose lane, or the corresponding `i`-weighted Hermitian polarization. This mixed expression can be sign-indefinite while the full graph energy remains positive.

Accordingly, the required theorem is a faithful four-block identity

$$
\Gamma_{\mathrm P}(G_p^{\rm St})
=\Gamma_{\theta,p},
$$

whose off-diagonal matrix units reproduce the causal forcing difference with the forced `-2` orientation. Equality of diagonal positive shadows is neither necessary nor sufficient.

The first finite residual to test is the odd off-diagonal block

$$
\mathcal E_{p,X}^{\rm mix}
=
\bigl[\Gamma_{\mathrm P}(G_{p,X}^{\rm St})\bigr]_{XY}
-
\bigl[\Gamma_{\theta,p,X}\bigr]_{XY},
$$

together with its reflected `YX` mate. Its diagonal evaluation must equal

$$
-\bigl(F_{+,p,X}-F_{-,p,X}\bigr).
$$

Status: positive-shadow cancellation target rejected by parity/sign; the RH-bearing local equation is the mixed matrix-unit identity on the retained graph.
