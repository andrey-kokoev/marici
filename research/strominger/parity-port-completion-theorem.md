# Minimal completion of a parity port

Let the transported sheet packet be `(A,B)`.  A scalar parity-blind interface
port is a row covector

\[
P_{\alpha,\beta}(A,B)=\alpha A+\beta B.
\]

Two such ports `P=(alpha,beta)` and `Q=(gamma,delta)` reconstruct the packet
if and only if their Plucker coordinate is nonzero:

\[
\boxed{\alpha\delta-\beta\gamma\ne0.}
\]

Indeed their joint observer matrix and inverse are

\[
O_{P,Q}=
\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix},
\qquad
O_{P,Q}^{-1}=\frac1{\alpha\delta-\beta\gamma}
\begin{pmatrix}\delta&-\beta\\-\gamma&\alpha\end{pmatrix}.
\]

Thus a single port is never faithful on an unrestricted two-sheet packet,
and every algebraic complement lies in the other affine chart of
`Gr(1,2)`.  This is the smallest instance of the Plucker-atlas mechanism
appearing in the magnetic component matrices.

For the magnetic character `M=(1,-1)`, a candidate second port `(gamma,delta)`
is sufficient exactly when

\[
\gamma+\delta\ne0.
\]

There are infinitely many algebraic complements.  Reflection authority picks
the even character `E=(1,1)`, not because it is the only possible row, but
because it is the unique complementary irreducible character of `Z_2` up to
scale.  The resulting determinant is `2`.

## Kernel rerouting

The one-sheet transport map is injective, and the joint `(E,M)` transform is
invertible.  Consequently

\[
E|_{\ker M}:\ker M\longrightarrow\operatorname{im}E
\]

is injective.  Every magnetic tower and exceptional circuit is therefore
reported nontrivially by the electric port.  Dually,

\[
M|_{\ker E}:\ker E\longrightarrow\operatorname{im}M
\]

is injective.  A parity kernel is not destroyed information: it is information
entirely rerouted into the complementary character channel.

This yields a precise distinction:

- `det(P,Q)=0`: the second port is merely another chart of the same quotient;
- `det(P,Q)!=0`: algebraic reconstruction exists;
- `Q=E` for `P=M`: reconstruction is also source-authorized by reflection.

The determinant condition proves sufficiency.  The character decomposition
explains canonicity.
