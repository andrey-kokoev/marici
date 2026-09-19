# The source has a nonzero even/odd cross-character value, but not yet the required mixed Schur covariance

## Available cross-character scalar

For the odd charge

\[
O(q)=\operatorname{sgn}(q)
\]

and even adjacent-window residual

\[
V_L=W_{2L}-W_L,
\]

distributional Stokes gives the exact value

\[
s_p
=\langle O,DV_L\rangle
=4\bigl(H(L)-H(2L)\bigr)>0,
\qquad L=\log p.
\]

This proves that the mixed even/odd channel is source-populated, prime-diagonal,
and orientation-sensitive. The missing `sigma_y/sigma_z` plane is therefore
not absent for parity reasons.

## Distinct required scalar

The first-Adams Schur calculation requires

\[
\alpha_p
=\langle d_p,D_p^\dagger c_p\rangle,
\]

where `d_p` and `c_p` are the even-wall and odd-Wronskian incidence
functionals in the complete auxiliary Green block. Under the standard Schur
sign convention its target value is

\[
\alpha_p
=-16\langle W_L,W_{2L}\rangle_{\rm St}.
\]

The available Stokes value `s_p` is not `alpha_p`: it is a direct ordered
boundary pairing, whereas `alpha_p` contains the completed auxiliary resolvent
or generalized inverse.

## Existing calibration data

The source currently supplies three distinct local quantities:

\[
g_p=\langle BW_L,BW_{2L}\rangle>0,
\]

\[
s_p=4(H(L)-H(2L))>0,
\]

and

\[
\kappa_p
=2L\sum_{k\ge1}p^{-k/2}\Phi'(kL)<0.
\]

Their source roles are respectively resolved Green pairing, ordered Stokes
link, and Euler-to-theta odd incidence. No existing identity equates their
combination with `alpha_p`.

## Exact remaining calculation

Materialize the complete mixed auxiliary block

\[
D_p=
\begin{pmatrix}
D_{ee}&D_{eo}\\
D_{oe}&D_{oo}
\end{pmatrix}
\]

on the even-wall/odd-history sector, together with the incidence pair
`(d_p,c_p)`. Then compute the single resolvent matrix element

\[
\langle d_p,D_p^\dagger c_p\rangle.
\]

If the block is parity diagonal, this quantity is zero and the required target
fails because `u>0`. Therefore a successful completed Green system must retain
a source-derived even/odd coupling at the resolvent level, despite the
Fourier-saturated wall/tail cross block vanishing in an auxiliary metric.

## Verdict

The source contains the correct mixed character channel and fixes its direct
Stokes sign. The unresolved step is propagation through the complete Green
resolvent. This is now one complex matrix element per prime, not an unspecified
four-entry Gram table.