# The single theta-tail plane has no constant positive conserved metric

## Correction to the selected gate

Prior research had already established more than the recent boundary one-jet calculation: `theta-tail-evans-readout-is-a-native-symplectic-determinant.md` proves that the theta-tail Evans readout is exactly a rank-two source-native symplectic determinant. The missing step is not construction of a second kinematic trace. It is the theta-specific half-plane exclusion law on the doubled reciprocal system.

## Exact no-go

After the half-trace gauge, the single tail plane has generator

\[
A_s(q)=
\begin{pmatrix}
-s/2&-f(q)\\
0&s/2
\end{pmatrix}.
\]

If a constant positive Hermitian matrix `H` were conserved for arbitrary source amplitude `f(q)`, the nilpotent forcing generator

\[
N=\begin{pmatrix}0&-1\\0&0\end{pmatrix}
\]

would satisfy `N* H + H N = 0`, where `N*` denotes transpose-conjugate. For a real symmetric representative

\[
H=\begin{pmatrix}h_{11}&h_{12}\\h_{12}&h_{22}\end{pmatrix},
\]

the Lyapunov residual is

\[
\begin{pmatrix}0&-h_{11}\\-h_{11}&-2h_{12}\end{pmatrix}.
\]

Vanishing forces `h11=h12=0`, contradicting positive definiteness. Independently, away from the seam the unforced eigenvalues have real parts `-a/2` and `a/2` for `s=a+it`, so no positive conserved constant metric can make that drift skew-Hermitian.

## Disposition

A constant positive metric on one phase plane is eliminated. The next admissible construction must either double the reciprocal sectors before seeking a Real/Hermitian invariant form or solve a source-derived `q`-dependent Lyapunov equation with endpoint sewing. Any fitted metric chosen after observing zeros is circular.
