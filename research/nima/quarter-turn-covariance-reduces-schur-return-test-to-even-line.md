# Quarter-turn covariance reduces the Schur-return test to the even line

On the local source plane, the quarter turn satisfies

$$
F w_\theta=2j_\theta,
\qquad
F j_\theta=-\frac12w_\theta.
$$

Let

$$
R_{\rm cons}=B^\dagger D_0^{-1}B
$$

be the conservative Schur return. Assume its already declared reciprocal/Fourier covariance restricts to

$$
R_{\rm cons}F=FR_{\rm cons}
$$

on the common even/odd source domain.

If the even generator equation holds,

$$
R_{\rm cons}w_\theta=p^{-2s}w_\theta,
$$

then

$$
2R_{\rm cons}j_\theta
=R_{\rm cons}Fw_\theta
=FR_{\rm cons}w_\theta
=p^{-2s}Fw_\theta
=2p^{-2s}j_\theta.
$$

Hence

$$
R_{\rm cons}j_\theta=p^{-2s}j_\theta.
$$

Thus the oriented odd trace identity follows from the even-wall identity plus quarter-turn covariance. Antiunitary reflection is still needed to transport the orientation correctly between reciprocal charts, but it supplies no additional scalar normalization.

The conservative/cyclic trace comparison therefore reduces to one source equation:

$$
B^\dagger D_0^{-1}B\,[P_p\otimes w_\theta]
=p^{-2s}w_\theta.
$$

This reduction is valid only after proving that the Schur return, not merely the boundary columns, commutes with `F` on the common domain.

Status: two generator tests reduced to one even-wall eigenvalue test conditional on the constructed quarter-turn covariance of the Schur return.
