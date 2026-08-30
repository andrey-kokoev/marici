# Pauli twirling reduces Schur survival to two diagonal loading margins

## Pullback and shorting are different operations

A common completed lift

\[
I_p:
\mathcal G_p^{\mathrm{cyc}}
\longrightarrow
\mathcal G_p^{\mathrm{full}}
\]

may satisfy the exact pullback identity

\[
I_p^*G_p^{\mathrm{full}}I_p=A_p.
\]

This closes quadratic functoriality before auxiliary elimination. It does not
by itself prove that the cyclic energy survives the Schur short.

If \(N_p\) is the auxiliary variation space, the effective form is

\[
A_p^{\mathrm{eff}}[u]
=
\inf_{n\in N_p}
G_p^{\mathrm{full}}[I_pu+n].
\]

The infimum may be strictly smaller than \(A_p[u]\), even when \(I_p\) is
an isometry onto its range.

Thus two gates remain separate:

- common-lift functoriality;
- transversality to the eliminated auxiliary sector.

## Schur return

In reduced block coordinates,

\[
G_p^{\mathrm{full}}
=
\begin{pmatrix}
A_p&C_p\\
C_p^*&D_p
\end{pmatrix},
\qquad
R_p=C_pD_p^\dagger C_p^*.
\]

After radical compatibility,

\[
A_p^{\mathrm{eff}}=A_p-R_p.
\]

Write

\[
A_p^{\mathrm{eff}}
=
\begin{pmatrix}
a_p-r_{11,p}&z_p-r_{12,p}\\
\bar z_p-\bar r_{12,p}&b_p-r_{22,p}
\end{pmatrix}.
\]

## Pauli cancellation survives the Schur return

Applying the two Euler ports after shorting gives

\[
XA_p^{\mathrm{eff}}X
+
YA_p^{\mathrm{eff}}Y
=
2
\begin{pmatrix}
b_p-r_{22,p}&0\\
0&a_p-r_{11,p}
\end{pmatrix}.
\]

The off-diagonal Schur loading cancels exactly, just as the raw endpoint
cross-correlation does.

Therefore uniform arithmetic observability after auxiliary elimination is
equivalent to two scalar diagonal residual bounds:

\[
inf_p(a_p-r_{11,p})>0,
\qquad
inf_p(b_p-r_{22,p})>0.
\]

No inverse of the collapsing raw Gram \(A_p\) is needed.

## Comparison with the normalized return criterion

The earlier sufficient condition

\[
\left\|
A_p^{-1/2}R_pA_p^{-1/2}
\right\|
<1
\]

is poorly adapted to the soft disagreement direction because
\(\lambda_{\min}(A_p)\to0\). It may fail even when both Pauli-observed
coordinates retain a uniform positive residual.

The diagonal criterion tests exactly the source observer that will be used.
It is weaker than full raw-metric contraction and stronger than scalar total
energy alone.

Define the endpoint loading fractions

\[
\ell_{1,p}=\frac{r_{11,p}}{a_p},
\qquad
\ell_{2,p}=\frac{r_{22,p}}{b_p}.
\]

Since \(a_p,b_p\ge m_\nu^2\), the uniform bounds

\[
\sup_p\ell_{1,p}<1,
\qquad
\sup_p\ell_{2,p}<1
\]

are sufficient.

## Exact zero-trace case

If the source auxiliary histories lie in a Green-orthogonal zero-trace
sector, then

\[
R_p=0
\]

on the endpoint incidence range and both residual bounds are automatic.

Literal zero endpoint trace alone is not enough unless the complete Green form
contains no interior cross-term coupling that zero-trace sector back to the
endpoint lift. The required condition is Green orthogonality or an equivalent
vanishing of \(C_p\), not merely \(\Gamma n=0\).

## Orientation remains in the linking blocks

The diagonal twirl proves coercivity but erases reciprocal orientation.
Accordingly:

- the full common-lift linking Gram proves constructor identity;
- the diagonal residuals prove survival under Schur elimination;
- the untraced mixed output blocks retain the odd sign.

These obligations cannot be merged into one scalar inequality.

## Minimal hostiles

1. Exact pullback before shorting, but auxiliary minimization kills one
   endpoint coordinate.
2. Zero endpoint traces with a nonzero interior Green cross-term.
3. Failure of raw normalized contraction caused only by the soft disagreement,
   while both diagonal residuals stay uniformly positive.
4. Positive total residual trace with one diagonal residual tending to zero.
5. Uniform diagonal survival while the mixed linking block reverses
   orientation.

## Verdict

The common completed lift closes Pauli covariance and quadratic pullback, but
not Schur survival. The Pauli identity supplies the correct next reduction:
only the two diagonal endpoint loadings control the completed arithmetic frame.

The next source calculation should therefore compute

\[
(C_pD_p^\dagger C_p^*)_{11}
\quad\text{and}\quad
(C_pD_p^\dagger C_p^*)_{22},
\]

or prove their vanishing from genuine Green orthogonality. This avoids the
unauthorized and asymptotically singular inverse of the raw endpoint Gram.
