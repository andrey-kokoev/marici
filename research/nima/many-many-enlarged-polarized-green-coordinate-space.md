# Many-many enlarged polarized Green coordinate space

Use the complete source feature space as the primary coordinate carrier:

$$
\mathscr X_G
=
\mathscr G_{\rm tail}
\oplus\mathscr W_{\rm wall/jump}
\oplus\mathscr P_{\rm prim/sq}
\oplus\mathscr C_{\rm conn}
\oplus\mathscr A_\infty
\oplus\mathscr R_{\rm recip}.
$$

Define the source feature embedding

$$
J_Gu=
\bigl(
J_{\rm tail}u,
J_{\rm wall/jump}u,
J_{\rm prim/sq}u,
J_{\rm conn}u,
J_\infty u,
J_{\rm recip}u
\bigr).
$$

The coordinate metric is the declared block Green metric

$$
G_{\rm src}
=G_{\rm tail}\oplus G_{\rm wall/jump}
\oplus G_{\rm prim/sq}\oplus G_{\rm conn}
\oplus G_\infty\oplus G_{\rm recip},
$$

with signed off-diagonal linking blocks retained separately. The history norm is the pullback graph form

$$
\|u\|_{G,\rm src}^2
=\langle J_Gu,G_{\rm src}J_Gu\rangle.
$$

Input and output ports lift to

$$
B_G=J_GB,
\qquad
C_G=CJ_G^\dagger
$$

on the source-generated range. The collocation audit is now

$$
G_{\rm src}B_G=C_G^*.
$$

The transported generator is the joint graph operator induced by the coordinate actions; it need not equal bare translation on every feature block.

Status: enlarged polarized Green coordinate space defined; block metrics, cross-block domains, and collocation identity require source verification.
