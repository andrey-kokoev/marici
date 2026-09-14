# The positive triple compression has the same leading volume density and isolates the finite sewing obstruction

## Positive feature

Set

\[
P=P_\Lambda,
\qquad
Q=Q_\Lambda=F_SP_\Lambda F_S^{-1},
\qquad
A=U_S(g),
\qquad
H=AA^*.
\]

The positive triple-compression form is

\[
\mathcal P_\Lambda(g)
=
\operatorname{Tr}
(PQPH).
\]

It is the squared Hilbert--Schmidt norm

\[
\boxed{
\mathcal P_\Lambda(g)
=
\|QP A\|_{HS}^2
=
\|(PQP)^{1/2}A\|_{HS}^2
\ge0.
}
\]

Thus

\[
\Phi_\Lambda^+(g)
=(PQP)^{1/2}U_S(g)
\]

is the correctly typed finite-cutoff positive feature.

## Difference from Connes's product trace

Connes's regulated expression is

\[
\mathcal T_\Lambda(g)
=
\operatorname{Tr}(PQH).
\]

Insert `I=P+(I-P)` immediately before `H`:

\[
\boxed{
\mathcal T_\Lambda(g)
=
\mathcal P_\Lambda(g)
+
\mathcal E_\Lambda(g),
}
\]

where

\[
\boxed{
\mathcal E_\Lambda(g)
=
\operatorname{Tr}
(PQ(I-P)H)
}
\]

is the sewing term.

## Observer-commutator factorization

Relative to

\[
\mathcal H
=P\mathcal H
\oplus
(I-P)\mathcal H,
\]

only the lower-left block

\[
H_{21}
=(I-P)HP
\]

contributes to the sewing trace. Since

\[
[P,H]
=PH-HP,
\]

one has

\[
H_{21}
=-(I-P)[P,H]P.
\]

Therefore

\[
\boxed{
\mathcal E_\Lambda(g)
=-
\operatorname{Tr}
\left(
PQ(I-P)[P,H]P
\right).
}
\]

This factors the sewing through:

1. the off-diagonal prolate transition `PQ(I-P)`;
2. the off-diagonal observer commutator `[P,H]`.

## Prolate transition norm

Let

\[
B=PQP
\]

on `P H`. Since `P` and `Q` are projections,

\[
\begin{aligned}
\|PQ(I-P)\|_{HS}^2
&=
\operatorname{Tr}
(PQ(I-P)QP)\\
&=
\operatorname{Tr}
(B-B^2).
\end{aligned}
\]

Hence

\[
\boxed{
\|PQ(I-P)\|_{HS}^2
=
\operatorname{Tr}
\left(
PQP-(PQP)^2
\right).
}
\]

This is the total prolate transition mass. In angle eigenvalues `lambda_n`, it is

\[
\sum_n
\lambda_n(1-\lambda_n).
\]

## Sewing bound

If the displayed off-diagonal blocks are Hilbert--Schmidt, Cauchy--Schwarz gives

\[
\boxed{
|\mathcal E_\Lambda(g)|
\le
\left[
\operatorname{Tr}(B-B^2)
\right]^{1/2}
\|[P,H]\|_{HS}.
}
\]

For the actual one-sided cutoff, the half-line formula gives

\[
\|[P,H]\|_{HS}^2
=
\int_{C_S}
|h(a)|^2
|\log|a|_S|d^*a,
\]

which is independent of `Lambda` for compactly supported `h`.

Thus every cutoff growth in the sewing term is concentrated in the prolate transition mass.

## Leading-volume consequence

The crude inequality `B-B^2\le B` is not useful asymptotically: in the real local model `Tr(B)` grows like `Lambda^2`. What is needed is the direct transition estimate

\[
\operatorname{Tr}(B-B^2)
=O(\log\Lambda).
\]

This estimate follows locally from the boundary-crossing sinc-kernel integral. Under it,

\[
\boxed{
\mathcal E_\Lambda(g)
=O_g(\sqrt{\log\Lambda})
=o_g(\log\Lambda).
}
\]

Connes's theorem gives

\[
\mathcal T_\Lambda(g)
=
2\log\Lambdah(1)
+W_S(h)
+o(1).
\]

Therefore, under the phase-space trace estimate,

\[
\boxed{
\frac{
\mathcal P_\Lambda(g)
}{2\log\Lambda}
\longrightarrow
h(1).
}
\]

So the positive feature has the correct leading Plancherel volume density.

## What this does not give

The bound

\[
O(\sqrt{\log\Lambda})
\]

is too weak to identify a finite part. It does not show that `E_Lambda` converges, vanishes, or has a prescribed endpoint--gamma limit.

Indeed,

\[
\mathcal P_\Lambda(g)
-2\log\Lambdah(1)
=
W_S(h)
-
\mathcal E_\Lambda(g)
+
o(1).
\]

A positive finite boundary exists only after the asymptotic behavior of `E_Lambda` is determined.

## Sharper prolate criterion

The exact sufficient condition for a bounded sewing family is

\[
\boxed{
\sup_\Lambda
\operatorname{Tr}
\left(
PQP-(PQP)^2
\right)
<\infty.
}
\]

Under this condition, `E_Lambda(g)` is uniformly bounded for every admitted observer. Convergence still requires control of the transition modes, not only their total mass.

More generally, if recentered off-diagonal prolate blocks converge in Hilbert--Schmidt space, then pairing with the fixed recentered observer commutator gives the sewing limit.

## Relation to the Hankel boundary

The observer block

\[
(I-P)[P,H]P
\]

is precisely a cross-boundary Hankel feature after recentering. The prolate block

\[
PQ(I-P)
\]

is its Fourier-cutoff sewing partner.

Thus

\[
\boxed{
\mathcal E_\Lambda(g)
=
-
\langle
\text{prolate transition},
\text{observer Hankel boundary}
\rangle_{HS}
}
\]

with orientation determined by the block convention.

This is the exact boundary pairing that must converge to the endpoint--gamma correction.

## Remaining source estimate

The required semilocal estimate is

\[
\operatorname{Tr}
\left(PQP-(PQP)^2\right)
=O(\log\Lambda),
\]

or, for leading density alone, any `o((log Lambda)^2)` bound. It must be proved directly from the semilocal prolate kernel. The full trace `Tr(PQP)` is much larger already in the real local model.

## Disposition

The positive bulk feature exists:

\[
\boxed{
\Phi_\Lambda^+(g)
=(P_\Lambda Q_\Lambda P_\Lambda)^{1/2}U_S(g).
}
\]

Its difference from Connes's trace is exactly controlled by

\[
\boxed{
|\mathcal E_\Lambda(g)|
\le
\sqrt{
\operatorname{Tr}(PQP-(PQP)^2)
}
\|[P,U_S(g)U_S(g)^*]\|_{HS}.
}
\]

Once the direct semilocal transition estimate `Tr(PQP-(PQP)^2)=O(log Lambda)` is proved, the positive feature has the correct leading bulk density. The finite positive filler is equivalent to the recentered prolate--Hankel sewing limit.
