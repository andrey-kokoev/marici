# Observer-energy filtering gives finite common physical edges but not global residual convergence

Fix conductor level \(F\) and observer-energy cutoff \(N\). Let

$$
H_{F,N}=Z_FY_N\mathscr H_S,
$$

where \(Y_N\) is the spectral cutoff of an observer-energy operator controlling the local half-Sobolev and Tate phase-energy norms.

Let \(G^T_{L,F,N}\) and \(G^0_{L,F,N}\) be the exactly aligned transported physical Grams. Assume the reference mismatch strip obeys

$$
G^0_{L,F,N}\succeq
(L-\delta_{L,F,N})I.
$$

The translated placement remainder is bounded in the observer graph metric. On the finite energy packet this gives a constant \(K_{F,N}<\infty\) with

$$
-K_{F,N}I
\preceq
Y_NZ_F(D_L-A)Z_FY_N
\preceq
K_{F,N}I.
$$

Together with

$$
A_{F,-}\preceq(F+C_S)I,
$$

a common positive physical edge exists whenever

$$
\boxed{
L\ge
\delta_{L,F,N}+F+C_S+K_{F,N}.
}
$$

This defines the directed admissible region

$$
\mathfrak I_S^{\mathrm{phys}}
=
\left\{
(L,F,N):
L\ge
\delta_{L,F,N}+F+C_S+K_{F,N}
\right\}.
$$

For any two finite packets, increase \(F\) and \(N\) to their maxima and then choose \(L\) above the new finite threshold. Hence finite positive common edges form a directed system.

The bound \(K_{F,N}\) need not tend to zero with \(L\). Translation preserves the Hardy-commutator Hilbert--Schmidt norm, so operator-norm centered convergence cannot be inferred from oscillatory scalar convergence. The directed common-edge construction therefore establishes finite filtered positivity, while physical residual convergence still requires the separate packet-independent residual and uniform tail estimates recorded by the completion interface.
