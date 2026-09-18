# Orthogonal boundary colocation cannot match Xi cross-transfer order

In the normalized boundary enlargement, take

$$
B=e_u,
\qquad
C=e_{\rm end}^*.
$$

These ports are orthogonal:

$$
CB=0.
$$

For any bounded finite compression of the reciprocal conservative family, the transfer is

$$
F_t(z)=C(zI-\widetilde A_t)^{-1}B.
$$

At spectral infinity,

$$
(zI-\widetilde A_t)^{-1}
=z^{-1}I+z^{-2}\widetilde A_t+O(z^{-3}),
$$

so

$$
F_t(z)
=z^{-1}CB+z^{-2}C\widetilde A_tB+O(z^{-3})
=t z^{-2}+O(z^{-3}).
$$

The transverse theta/Xi cross transfer has order `z^-1` at spectral infinity. Therefore no choice of the scalar `t` can make this orthogonal-port realization equal to the Xi transfer. The mismatch occurs before divisor comparison.

To obtain the required leading order, a bounded realization must satisfy

$$
CB\ne0,
$$

or retain the original unbounded boundary-port rigging where the ordinary bounded resolvent expansion does not apply. Equivalently, the endpoint coordinate must have a source-overlap component rather than being a wholly separate orthogonal Hilbert coordinate.

This rejects the minimal orthogonal boundary enlargement as the final Xi conservative realization. It remains a valid abstract colocation example but cannot preserve the known cross-transfer asymptotics.

Status: one-parameter reciprocal extension falsified as an Xi transfer realization; a pointed one-leg-linear or rigged boundary port is required.
