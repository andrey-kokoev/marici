# Two-lane cyclic/conservative coherence cell

For each prime define the Adams-two character

$$
\chi_p(s)=p^{-2s}.
$$

Its canonical polar decomposition is

$$
\chi_p(s)=m_p(s)u_p(s),
$$

where

$$
m_p(s)=p^{-2\operatorname{Re}s}>0,
\qquad
u_p(s)=e^{-2i\operatorname{Im}s\log p}\in U(1).
$$

Retain `u_p` on the analytic Tate/determinant line and `m_p` on the Hermitian Green carrier. The two-lane comparison cell consists of

$$
R_{{\rm cons},p}^{\rm Herm}w_\theta
=m_p(s)w_\theta
$$

and the line action

$$
U_{{\rm Tate},p}(s)\ell=u_p(s)\ell.
$$

Their tensor product recovers the cyclic trace action:

$$
(U_{{\rm Tate},p}\otimes R_{{\rm cons},p}^{\rm Herm})
(\ell\otimes w_\theta)
=p^{-2s}(\ell\otimes w_\theta).
$$

Both factors are multiplicative under label addition and primewise products because they are the phase and modulus of one character. Reciprocal reflection sends

$$
u_p(s)\mapsto u_p(s)^{-1},
$$

while leaving `m_p(s)` fixed. Thus analytic reciprocity and Hermitian positivity coexist without scalar identification.

Quarter-turn covariance transfers the Hermitian modulus equation from `w_theta` to `j_theta`; the Tate line transports the same phase in both channels.

The only remaining scalar source test is therefore

$$
R_{{\rm cons},p}^{\rm Herm}w_\theta
=p^{-2\operatorname{Re}s}w_\theta.
$$

Status: variance-correct two-lane coherence cell constructed; Hermitian modulus identification with the source Schur return remains open.
