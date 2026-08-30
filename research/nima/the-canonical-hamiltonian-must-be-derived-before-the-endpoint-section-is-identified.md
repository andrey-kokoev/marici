# The canonical Hamiltonian must be derived before the endpoint section is identified

## Authority warning

A canonical-system lift is useful only in the forward direction.

If one first assumes that a proposed entire function \(E\) is Hermite–Biehler, inverse de Branges theory can reconstruct a positive canonical Hamiltonian having \(E\) as endpoint data. Applied to a section already assembled from \(\xi\), that procedure would merely repackage the desired zero theorem. It would not explain RH.

The authorized order must instead be

\[
\text{theta-tail source constructors}
\longrightarrow
H(u)\ge0
\longrightarrow
Y(u,z)
\longrightarrow
E_{\mathrm{out}}(z)
\longrightarrow
\text{scalar identification}.
\]

Neither positivity of \(H\) nor the canonical evolution may be imported from the anticipated endpoint function.

## Constructor-level target

On a finite tail cell, the source should provide two real state coordinates, for example a tail coordinate and its independently typed boundary/history conjugate. Their Green form should determine a positive semidefinite matrix density

\[
H(u)=
\begin{pmatrix}
h_{11}(u)&h_{12}(u)\\
h_{12}(u)&h_{22}(u)
\end{pmatrix},
\qquad
H(u)\ge0,
\]

before the spectral parameter is introduced.

The spectral coupling must then arise from the source incidence law as

\[
J\partial_uY(u,z)=zH(u)Y(u,z).
\]

This separates two checks:

1. Energy authority: every entry of \(H\) is a polarization of a declared theta-tail or wall energy.
2. Spectral authority: multiplication by \(z\) is the Mellin/seam generator acting through the fixed symplectic incidence \(J\).

Only after solving this initial-value problem may one form the outgoing endpoint coordinate

\[
E_L(z)=\ell_{\mathrm{out}}Y(L,z)
\]

and compare it with the one-sided theta transform.

## First finite falsifier

A fitted Hamiltonian can reproduce finitely many Taylor coefficients of the desired \(E_L\) while disagreeing with the source Green form. Therefore the first test should not compare endpoint scalars alone.

For one finite cell, compute independently:

- the source Gram density \(H_{\mathrm{src}}\);
- the infinitesimal transfer matrix from the history constructor;
- the canonical candidate \(-JzH_{\mathrm{src}}\).

The required equality is an operator identity on the source core. Agreement only after applying \(\ell_{\mathrm{out}}\), or only for one spectral value, is insufficient.

## Completion gates

Even a valid finite source canonical system may fail in the limit. The completion theorem must prove:

- local integrability of \(H\);
- compatibility of finite-cell restrictions;
- preservation of the wall summand;
- convergence of transfer matrices on compact spectral sets;
- noncollapse of the positive energy modulo the declared radical;
- convergence of \(E_L\) to a source-defined outgoing section.

The scalar identification with a reciprocal \(\xi\)-section is the final step, not the input.

## Reduced frontier

The next executable calculation is to polarize one finite theta-tail cell and ask whether its first-order history evolution already has canonical form. If it does, its Hamiltonian is source-authorized. If it does not, invoking inverse spectral reconstruction would conceal rather than repair the missing constructor.
