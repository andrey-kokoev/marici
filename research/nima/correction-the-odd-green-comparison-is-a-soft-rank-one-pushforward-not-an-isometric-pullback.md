# Correction: the odd Green comparison is a soft rank-one pushforward, not an isometric pullback

Fresh comparison with the raw Stieltjes estimates invalidates the proposed pullback isometry

$$
(K_p^{\rm odd})^*G_{{\rm win},p}K_p^{\rm odd}=G_{\theta,p}.
$$

Indeed,

$$
K_p^{\rm odd}j_\theta=d_p,
$$

while

$$
\|j_\theta\|_{2I}=\frac12
$$

is fixed and

$$
\|d_p\|_\nu
\le C(\log p)^{-1/2}
\exp\left[-\frac\pi8(\log p)^2\right].
$$

Hence the theta-to-window map is a soft trace-class compression, not an isometry. A pullback isometry would require a super-polynomial rescaling that is absent from the source normalization.

The viable quadratic identity must distinguish the ambient Stieltjes metric from the odd response form. Let

$$
G_{{\rm win},p}^{\rm odd}
$$

denote only the rank-one forcing-difference/response form supported on `span{d_p}`, not the complete Stieltjes history metric. Then the correctly typed target is

$$
\boxed{
G_{{\rm win},p}^{\rm odd}
=K_p^{\rm odd}G_{\theta,p}^{\rm odd}(K_p^{\rm odd})^*
}
$$

with adjoints taken in the declared source dualities. This is compatible with softness and trace-class completion because both sides have range in `span{d_p}`.

It must not be promoted to

$$
G_{{\rm win},p}^{\rm ambient}
=K_p^{\rm odd}G_{\theta,p}(K_p^{\rm odd})^*;
$$

the ambient cyclic Stieltjes form generally has larger rank and contains positive sectors orthogonal to `d_p`.

Thus three different claims are separated:

1. linear incidence `K_p^odd j_theta=d_p` — proved;
2. rank-one odd response pushforward — open and viable;
3. ambient metric isometry — false in the raw completion frame.

The finite residual is consequently

$$
\mathcal E_{p,X}^{\rm odd}
=G_{{\rm win},p,X}^{\rm odd}
-K_{p,X}^{\rm odd}G_{\theta,p,X}^{\rm odd}(K_{p,X}^{\rm odd})^*.
$$

This is the exact local quadratic identity needed to cancel the forcing difference. No norm equality between `j_theta` and `d_p` is required.

Status: completion direction and rank typing fixed; rank-one odd response pushforward remains the local source gate.
