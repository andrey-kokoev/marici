# qRB microstep 99: Gaussian block-placement test

For Gaussian probes, compare two separately defined outputs:

$$
Q_{\rm src}=E+G+P_L,
\qquad
K_{\rm link}=-\frac12J_{\rm link}.
$$

The test is that both act on the same declared graph carrier and that insertion of `K_link` preserves the old Green boundary identity and skew cancellation. The test is not `Q_src=omega_link`.

A finite Gaussian packet can verify the matrix placement and the sign of the skew block. Full source identification is unnecessary for this step.

Status: corrected finite comparison target specified; numerical execution requires exported Gaussian response matrices.
