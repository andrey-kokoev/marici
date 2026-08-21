# The one-loop QED fixed-\(t\) subtraction gate closes

For the exact one-loop massive-fermion helicity amplitudes, take

\[
s=S\to\infty,qquad t=-\tau<0,qquad u=-S+\tau.
\]

An exact degree audit of every rational coefficient multiplying the one-loop
master integrals in the source representation finds no positive residual power
of \(S\) after including the corresponding square-root normalization. The
largest net power is zero.

The master basis has GPL weight at most two. Its large-argument behavior is
therefore at most logarithmic squared, giving

\[
\mathcal M_\lambda(\nu,t)=O(\log^2|\nu|)
\]

at fixed spacelike \(t\). Consequently,

\[
\frac{\mathcal M_\lambda(\nu,t)}{\nu^3}
\]

has a vanishing large-circle contribution. The \(\nu^2\) Taylor coefficient
is therefore fixed by the inverse-cubic absorptive moment; there is no
independent \(\nu^2\) subtraction polynomial at one loop.

Combining this with the fixed-\(t\) adapter yields

\[
C_2^{\Phi_2}(t)=2f_2-f_3t,
\qquad
C_2^{\Phi_5}(t)=-h_3t,
\]

with each \(C_2\) determined by the corresponding nonforward cut.

## Scope

This closes the subtraction gate for the explicit one-loop massive-electron
QED amplitude. It is not a proof of the same Regge bound nonperturbatively or
at every loop order.

The rational prefactor audit is reproduced by
`research/nima/check_qed_fixed_t_subtraction_gate.py`. The amplitude basis is
that of Ajjath, Chaubey, and Shao, JHEP 03 (2024) 121,
https://arxiv.org/abs/2312.16966.
