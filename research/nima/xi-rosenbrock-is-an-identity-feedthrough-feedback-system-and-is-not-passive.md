# Xi Rosenbrock is an identity-feedthrough feedback system and is not passive

Write the two-history Xi pencil as

$$
\mathcal R_\Xi(z)
=
\begin{pmatrix}
zI-A&-B\\
-C_0&0
\end{pmatrix},
$$

up to the fixed sign convention, where

$$
A=\partial_q\oplus\partial_q,
\qquad
B c=c(\Phi_-,\Phi_+),
\qquad
C_0(f_-,f_+)=f_-(0)-f_+(0).
$$

Compare with the continuous-time feedback Rosenbrock matrix

$$
\mathcal R_{\rm fb}(z)
=
\begin{pmatrix}
zI-A&-B\\
-CC_0&I-CD
\end{pmatrix}.
$$

Taking scalar feedback `C=I` and direct term `D=I` gives

$$
\mathcal R_{\rm fb}(z)=\mathcal R_\Xi(z).
$$

The corresponding transfer is

$$
G_\Xi(z)=I+C_0(zI-A)^{-1}B
=I+\tau(z)
$$

with the appropriate overall sign. Hence

$$
I-G_\Xi(z)=-\tau(z),
$$

so the Xi divisor is exactly the unit-feedback resonance condition.

However, a contractive colligation with `D=I` cannot have a nonzero coupling `B`. Indeed, contractivity of

$$
\begin{pmatrix}A&B\\C_0&I\end{pmatrix}
$$

forces the defect of the unitary direct block to vanish; the corresponding off-diagonal coupling must then be zero. Here `B` is the nonzero theta forcing incidence.

Therefore the exact Xi feedback realization is not the passive sum/difference colligation. The missing promotion cannot be a similarity preserving all four blocks: it must replace the identity-feedthrough realization by a divisor-preserving passive dilation or a one-way triangular extension.

Status: exact feedback form of the Xi pencil identified; direct-feedthrough passivity obstruction isolates the required dilation step.
