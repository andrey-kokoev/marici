# The Dilation Coordinate Turns Each Theta Label into a Positive Length-Three Jordan Packet

The signed moment readout

\[
\Phi=4M_2-6M_1
\]

has a positive source-native presentation. Put

\[
y=e^{2u}-1,
\qquad
\lambda_n=\pi n^2,
\]

and remove the common quarter-density. Each label becomes

\[
e^{-\lambda_n}
\left(
(4\lambda_n^2-6\lambda_n)
+(8\lambda_n^2-6\lambda_n)y
+4\lambda_n^2y^2
\right)e^{-\lambda_n y}.
\]

All three coefficients are strictly positive because
`lambda_n >= pi > 3/2`. Moreover, the basis
`1,y,y^2` times `exp(-lambda_n y)` is a closed length-three Jordan block under
ordinary differentiation.

Thus modular theta is transverse to the scalar positive exponential cone but
belongs labelwise to a positive exponential Jordan cone. The remaining gate
is the Green form of the transported logarithmic operator; the single block
at `lambda=pi` is the smallest falsifier.

Research packet:
`research/grothendieck/the-dilation-coordinate-turns-each-theta-label-into-a-positive-length-three-jordan-packet.md`

Checker:
`research/grothendieck/checkers/check_theta_positive_jordan_packet.py`

The checker passes 5/5 gates.
