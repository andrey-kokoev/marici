# Moving-endpoint Rosenbrock groupoid covariance

For `a>=0`, let the history fiber be the half-line `[a,infinity)` and define

$$
\mathcal R_{\Xi,a}(z)(f_-,f_+,c)
=
\bigl((\partial_q-z)f_- -c\Phi_-,
(\partial_q-z)f_+ -c\Phi_+,
 f_-(a)-f_+(a)\bigr).
$$

Let

$$
(U_af)(t)=f(t+a)
$$

identify the fiber `[a,infinity)` with `[0,infinity)`, and put

$$
\Phi_{\pm,a}=U_a\Phi_\pm.
$$

Since differentiation commutes with `U_a` and endpoint evaluation satisfies

$$
E_0U_a=E_a,
$$

one has the exact conjugacy

$$
\mathcal R_{\Xi,0}^{\Phi_a}(z)
(U_a\oplus U_a\oplus1)
=
(U_a\oplus U_a\oplus1)
\mathcal R_{\Xi,a}^{\Phi}(z).
$$

For `a,b>=0`, `U_bU_a=U_(a+b)` after the evident fiber identifications. Hence these pencils form a functor over the translation action groupoid. This closes the moving-endpoint module covariance square.

## Transfer qualification

The transfer in the translated fiber is

$$
\tau_a(z)=u_{-,a}(0;z)-u_{+,a}(0;z),
$$

where the stable histories are built from `Phi_(±,a)`. In general

$$
\tau_a(z)\ne\tau_0(z).
$$

Therefore moving-endpoint covariance alone does not preserve the Xi divisor. The omitted interval `[0,a]` carries the transfer difference.

The full Hopf-compatible Xi realization must consequently use the unitary tail-plus-seam cut

$$
C_a\Phi=(G_a\Phi,H_a\Phi),
\qquad C_a^{-1}=C_a^*,
$$

and stabilize the Rosenbrock pencil by the seam channel. Only this complete cut is unitarily equivalent to the original source and can preserve the original transfer determinant without a fitted correction.

Status: moving-endpoint groupoid covariance proved; divisor-preserving tail-plus-seam Rosenbrock stabilization remains open.
