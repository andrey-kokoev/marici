# The Euler half-density supplies a uniform Adams-ray loading gap if it acts before completion

## Weighted incidence

Let a nontrivial prime-power grade have physical scale

\[
r=p^k\ge2
\]

and half-density

\[
\rho(r)=r^{-1/2}=p^{-k/2}.
\]

For the first-order graph metric

\[
G=I+\mathsf D^*\mathsf D,
\]

define

\[
K_r=\rho(r)\mathsf D G^{-1/2}.
\]

Since \(\|\mathsf D G^{-1/2}\|=1\),

\[
\|K_r\|=\rho(r)\le2^{-1/2}<1.
\]

Thus

\[
K_r^*K_r\le\frac12I.
\]

The norm margin is \(1-2^{-1/2}\), and the energy margin is at least
\(1/2\).

## Dilation behavior

For nonconstant \(f\) and unitary dilation \(U_r\),

\[
\mathsf D U_r=rU_r\mathsf D.
\]

The normalized weighted loading is

\[
\frac{\rho(r)^2\|\mathsf D U_rf\|^2}
{\|U_rf\|^2+\|\mathsf D U_rf\|^2}
=
\frac{r\|\mathsf Df\|^2}
{\|f\|^2+r^2\|\mathsf Df\|^2}
\longrightarrow0.
\]

## Tensor-unit exception

At \(r=1\), \(\rho(1)=1\), so the strict gap disappears. The tensor unit must
therefore be absent from this incidence block, routed through the independent
wall channel, or controlled separately.

## Constructor order

The authorized order is

\[
\text{typed incidence}
\longrightarrow
\text{Euler half-density}
\longrightarrow
\text{history normalization}
\longrightarrow
\text{completion}.
\]

A scalar Euler factor applied after norm, determinant, or readout cannot repair
an already saturated operator channel.

With off-seam displacement \(\sigma\ge\varepsilon>0\),

\[
\rho_\sigma(p^k)=p^{-k(1/2+\sigma)}
\]

and

\[
\sup_{p,k}\|K_{p^k,\sigma}\|
\le2^{-(1/2+\varepsilon)}.
\]

## Verdict

Conditional on upstream placement of the half-density and separate routing of
the tensor unit,

\[
\sup_{p,\ k\ge1}\|K_{p^k}\|\le2^{-1/2}.
\]

The remaining theorem is the source factorization proving that this weight
acts on the operator incidence before assembly.
