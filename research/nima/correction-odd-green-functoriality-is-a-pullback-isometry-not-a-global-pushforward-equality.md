# Correction: odd Green functoriality is a pullback isometry, not a global pushforward equality

The source map has variance

$$
K_p^{\rm odd}:E_{\theta,p}^{\rm odd}\longrightarrow\mathcal H_{{\rm win},p},
\qquad
K_p^{\rm odd}j_\theta=d_p.
$$

Therefore the canonical comparison of Green forms is the pullback identity

$$
\boxed{
(K_p^{\rm odd})^*G_{{\rm win},p}K_p^{\rm odd}
=G_{\theta,p}
}
$$

on the theta odd line. The previously written expression

$$
G_{{\rm win},p}
=K_p^{\rm odd}G_{\theta,p}(K_p^{\rm odd})^*
$$

is a global pushforward/coisometry statement. It cannot hold on the full window-history space when `K_p^odd` is rank one and the Stieltjes cyclic Green form has rank greater than one.

On the source-generated one-dimensional line, the correct condition is simply

$$
\langle d_p,d_p\rangle_{{\rm win},p}
=
\langle j_\theta,j_\theta\rangle_{\theta,p}.
$$

Because

$$
d_p=-2j_\theta b_p,
$$

the factor `-2` fixes the required metric normalization; it does not disappear after squaring. Any theta metric transported from endpoint columns must include the evaluation against `b_p`, while the window metric is the source Stieltjes form.

The finite residual should therefore be

$$
\widetilde{\mathcal E}_{p,X}
=
(K_{p,X}^{\rm odd})^*G_{{\rm win},p,X}K_{p,X}^{\rm odd}
-G_{\theta,p,X},
$$

not the former full-space residual. If the comparison is needed on the window side, it must be stated only after projection to `Ran(K_p^odd)` and use the Moore--Penrose/form inverse with the source normalization.

This correction narrows the cancellation theorem: the forcing-difference vector must lie in the incidence range of `K_p^odd`; then pullback isometry identifies its quadratic supply with the relative-Haar/window energy. Orthogonal window-history sectors remain positive auxiliary channels but do not participate in the cancellation.

Status: variance and rank obstruction resolved; the remaining local test is the one-dimensional source norm identity plus incidence-range membership of the forcing-difference channel.
