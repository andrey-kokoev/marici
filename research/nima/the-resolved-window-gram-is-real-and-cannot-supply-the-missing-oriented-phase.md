# The resolved window Gram is real and cannot supply the missing oriented phase

## Status

Exact obstruction/reconciliation. This corrects the expectation that evaluating one complex mixed tail pairing could by itself close the ordered Green polarization. No G1.1 or RH claim.

## Real structure

The adjacent Stieltjes windows satisfy

\[
-1\le W_{2L}(q)\le W_L(q)\le0,
\]

so \(W_L\) and \(W_{2L}\) are real-valued. The theta kernel \(\Phi\) and its mass \(M_\Phi\) are real. Therefore the causal history operator

\[
(H_\Phi f)(u)=\int_0^\infty\Phi(r)f(u+r)\,dr
\]

preserves the real subspace, and so does

\[
B=H_\Phi-M_\Phi I.
\]

Consequently

\[
BW_L,\ BW_{2L}
\]

are real-valued and

\[
\beta_p=\langle BW_L,BW_{2L}\rangle\in\mathbb R.
\]

Thus the entire resolved two-window Gram

\[
G_{jk}^{\mathrm{res}}
=(1+M_\Phi^2)\langle W_{jL},W_{kL}\rangle
+\langle BW_{jL},BW_{kL}\rangle
\]

is real symmetric.

The same conclusion is visible in Fourier variables. Although the causal multiplier \(b_\Phi(\xi)\) is generally complex,

\[
|b_\Phi(\xi)|^2
\]

is real and even, while the Fourier transforms of real windows obey conjugate symmetry. The integral for \(\beta_p\) is therefore real.

## Consequence

Evaluating \(\beta_p\) completes the **positive resolved window Gram**, but it cannot supply an imaginary or symplectic orientation coordinate. This matches the existing repository warning:

> The real windows \(W_L,W_{2L}\) generate only a real endpoint block. Any reciprocal odd coordinate must be induced by eliminating an independently typed oriented feature.

Hence the ordered cross-face polarization

\[
\mathcal C_z(K)=\langle DK,zK\rangle
\]

cannot be recovered from the resolved window norm alone. The phase-rotation hostile survives: a real positive Gram is insensitive to the sign of the missing quarter-turn orientation.

## Retyping the remaining tasks

There are two distinct local outputs:

1. **positive resolved Gram:** determined after evaluating the real scalar
   \[
   \beta_p=\langle BW_L,BW_{2L}\rangle;
   \]
2. **ordered Green orientation:** supplied only by a separately typed odd/quarter-turn port, such as the established Fourier-quarter-turn, derivative-current, Wronskian, or equivalent source-authorized symplectic feature.

They must not be conflated. The relation needed is not that the oriented port equals an entry of the real Gram. It is a linking identity showing that the oriented port and the real resolved graph are two outputs of one source constructor and that reciprocal reflection sends one ordered off-diagonal entry to the adjoint of the other with the frozen sign.

## Minimal remaining diagram

Let \(J_p^{\mathrm{win}}\) denote the real two-window lift and \(J_p^{\mathrm{odd}}\) the independently typed oriented lift. The required target has the form

\[
J_p^{\mathrm{full}}
=J_p^{\mathrm{win}}\oplus J_p^{\mathrm{odd}},
\]

with linking Gram

\[
\begin{pmatrix}
(J_p^{\mathrm{win}})^*G_{\mathrm{res}}J_p^{\mathrm{win}} &
(J_p^{\mathrm{win}})^*LJ_p^{\mathrm{odd}}\\
(J_p^{\mathrm{odd}})^*L^*J_p^{\mathrm{win}} &
(J_p^{\mathrm{odd}})^*G_{\mathrm{odd}}J_p^{\mathrm{odd}}
\end{pmatrix}.
\]

The real resolved pairing fixes the upper-left block. The missing orientation is in the off-diagonal linking block \(L\), not in \(\beta_p\).

## Revised frontier

The immediate analytic calculations are now parallel rather than sequential:

- evaluate \(\beta_p\) to finish the positive window block;
- extract the source-authorized window-to-odd linking pairing, including its reciprocal adjoint sign;
- prove both extend to the same completed domain and annihilate the declared radicals;
- then assemble the four ordered matrix-unit identities.

The earliest genuinely orientation-bearing datum is the mixed linking block between the real window graph and the independently typed odd port.
