# qRB microstep 147: general gamma residue correction

Let

$$
 u_k=i(2k+1/2),
 \qquad
 \xi=-\frac{id}{4\sigma},
 \qquad
 t=2\sigma.
$$

The Gaussian factor at the `k`-th crossed pole is

$$
 e^{-t(u_k-\xi)^2}
=
 e^{2\sigma(2k+1/2+d/(4\sigma))^2}.
$$

The translate-Gram gauge multiplies this by

$$
 e^{-d^2/(8\sigma)}.
$$

The resulting finite residue sum is included only for poles actually crossed, with orientation signs and half-residue values at alignment. It must be combined with the shifted gamma contour before taking the completed source limit.

This formula makes the contour bookkeeping explicit and prevents treating the continued gamma term as the residue-free real-axis integral outside `|d|<2 sigma`.

Status: general residue factor written; convergence and cancellation of the completed residue package remain to be verified.
