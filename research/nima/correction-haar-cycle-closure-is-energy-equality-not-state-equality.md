# Correction: Haar cycle closure is energy equality, not state equality

The previous route-matching target

$$
J_\Phi(u_+)=T_pJ_\Phi(u_-)
$$

is too strong. In logarithmic coordinates, prime dilation is translation by `log p`. Translation on an `L2` line has no nonzero eigenvectors. Hence a nonzero relative-Haar state cannot generally be fixed by one prime step, even on the critical seam.

The required coherence is equality of the two route energies after their declared readouts, not equality of the carrier vectors.

Define the scalar energy defect

$$
\delta_p(z)
=
\mathcal E_z(J_\Phi u_+(z))
-
\mathcal E_z(T_pJ_\Phi u_-(z)).
$$

Relative-Haar covariance gives

$$
\delta_p(z)
=
\mathcal E_z(J_\Phi u_+(z))
-p^{-2\operatorname{Re}z}
\mathcal E_z(J_\Phi u_-(z)).
$$

At an Xi zero, `u_+=u_-=u_z`, so

$$
\delta_p(z)
=
(1-p^{-2\operatorname{Re}z})
\mathcal E_z(J_\Phi u_z).
$$

The missing conservative/cyclic coherence law is

$$
\tau(z)=0
\quad\Longrightarrow\quad
\delta_p(z)=0,
$$

for the same nonzero source state. This is an equality of independently defined route readouts. It must not be replaced by state invariance under dilation.

If this energy-cycle law holds, positivity immediately forces `Re z=0`. Thus the scalar route-energy equality is the RH-bearing statement.

Status: impossible vector closure retracted; correct energy-level cycle closure isolated.
