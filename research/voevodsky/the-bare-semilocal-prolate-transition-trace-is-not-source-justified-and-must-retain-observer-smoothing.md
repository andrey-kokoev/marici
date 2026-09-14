# The bare semilocal prolate transition trace is not source-justified and must retain observer smoothing

## Claim under audit

The proposed semilocal estimate was

\[
\operatorname{Tr}_{X_S}
\left(
B_{\Lambda,S}-B_{\Lambda,S}^2
\right)
=O_S(\log\Lambda),
\qquad
B_{\Lambda,S}=P_\Lambda Q_\Lambda P_\Lambda.
\]

The preceding orbitwise reduction assumed that the bare positive operator

\[
B-B^2
=P Q(I-P)Q P
\]

is trace class on `L2(X_S)`.

Connes's Theorem 4 does not state this.

## What the source proves

The source proves traceability of the observer-regularized product

\[
P_\Lambda Q_\Lambda U_S(h)
\]

for compactly supported smooth `h`, followed by its trace asymptotic.

It does not obtain the cutoff trace by setting

\[
h=\delta_1
\]

or by inserting the identity operator. The identity observer is not in the admitted smooth compact-support test algebra.

Therefore the theorem supplies no estimate for

\[
\operatorname{Tr}(PQP)
\]

or

\[
\operatorname{Tr}(PQP-(PQP)^2)
\]

on the semilocal quotient.

## Angular multiplicity issue

The module cutoff controls the one-dimensional radial coordinate

\[
\log|x|_S.
\]

The kernel of the module map contains compact/norm-one directions after quotienting by `O_S*`. Its `L2` space still has infinitely many Fourier modes.

A cutoff depending only on total module need not regularize those angular modes. Consequently the bare prolate transition may have infinite trace even when each fixed angular mode has a logarithmic transition trace.

Schematically, if

\[
L^2(X_S)
\simeq
\int_{\widehat C_S^1}^{\oplus}
H_\chid\chi
\]

or decomposes discretely over compact angular characters, then

\[
\operatorname{Tr}(B-B^2)
=
\sum_\chi
\operatorname{Tr}_{H_\chi}(B_\chi-B_\chi^2).
\]

A uniform `O(log Lambda)` bound per mode would make the sum diverge unless there is additional decay in `chi`.

The observer `U_S(h)` supplies precisely such spectral smoothing.

## Failure of the unweighted Cauchy bound

The sewing term is

\[
\mathcal E_{\Lambda,S}(g)
=
\operatorname{Tr}
(PQ(I-P)H),
\qquad
H=U_S(g)U_S(g)^*.
\]

It was bounded formally by

\[
|\mathcal E|
\le
\|PQ(I-P)\|_{HS}
\|[P,H]\|_{HS}.
\]

This inequality requires the bare block

\[
PQ(I-P)
\]

to be Hilbert--Schmidt. That is equivalent to traceability of `B-B^2` and is not established semilocally.

If `PQ(I-P)` is merely bounded, multiplying it by one Hilbert--Schmidt observer commutator yields only a Hilbert--Schmidt operator, not necessarily a trace-class operator with a defined ordinary trace.

Thus the bound is valid in the ordinary local prolate model but cannot yet be transported to `X_S`.

## Why the orbit decomposition was premature

The quotient trace formula

\[
\operatorname{Tr}_{X_S}(T)
=
\sum_q
\int_DK_T(x,qx)dx
\]

requires a trace-class or independently traceable operator `T`. Writing this formula for bare `T=B-B^2` does not establish its convergence.

The previously proposed per-orbit estimate remains a sufficient criterion **if** it is proved absolutely, but it cannot be derived by first assuming the quotient trace exists.

## Correct observer-weighted target

The transition quantity must retain smoothing on both sides. A legitimate positive candidate is

\[
\boxed{
\mathcal D_{\Lambda,S}(g)
=
\left\|
P Q(I-P)U_S(g)
\right\|_{HS}^2
}
\]

only when the outside leg is Hilbert--Schmidt. Prior analysis shows that the unbounded outside channel generally fails this condition, so introduce the second cutoff:

\[
\boxed{
\mathcal D_{\Lambda,R,S}(g)
=
\|P_\Lambda Q_\Lambda
(P_R-P_\Lambda)
U_S(g)\|_{HS}^2.
}
\]

At finite `R`, this is trace class under the regulated smoothing hypotheses and retains angular decay from `g`.

The corresponding regulated sewing pairing is

\[
\boxed{
\mathcal E_{\Lambda,R,S}(g)
=
\left\langle
Q_\Lambda P_\Lambda U_S(g),
Q_\Lambda(P_R-P_\Lambda)U_S(g)
\right\rangle_{HS}.
}
\]

This is the correctly typed two-cutoff quantity.

## Observer-weighted orbit estimate

For the regulated transition kernel, define orbit terms

\[
I_{q,\Lambda,R,S}(g)
=
\int_D
K_{T_{\Lambda,R,S}(g)}(x,qx)dx.
\]

The appropriate target is now

\[
\boxed{
|I_{q,\Lambda,R,S}(g)|
\le
C_{B,N,\rho}
(1+\log\Lambda)^m
(1+d(q,1))^{-N}
}
\]

uniformly for `g` in a bounded observer packet `B` and correlated scales

\[
R=\Lambda^\rho,
\qquad
\rho>1.
\]

Choose `N` larger than the polynomial growth degree of `O_S*`. Then the orbit sum converges absolutely.

The exponent `m` must be determined from the regulated kernel calculation; assuming `m=1` would beg the transition estimate.

## Finite angular spectral cutoff as a diagnostic

Let `K_N` project onto finitely many angular characters/modes. Then

\[
K_N(B-B^2)K_N
\]

has a finite sum of local prolate transition traces and is a legitimate diagnostic. For fixed `N`, one expects

\[
\operatorname{Tr}
\left(
K_N(B-B^2)K_N
\right)
=O_N(\log\Lambda).
\]

The decisive question is growth in `N`. If the coefficient grows like the number of modes, the bare trace diverges. Observer smoothing replaces the hard `K_N` by rapidly decaying angular weights and can make the weighted sum finite.

## Revised positive comparison

The positive triple feature

\[
QP U_S(g)
\]

can remain Hilbert--Schmidt because the observer is present. Its leading-density comparison with Connes's trace should be proved directly for this observer-weighted feature, not through the bare norm of `PQ(I-P)`.

The valid identity remains

\[
\mathcal T_\Lambda(g)
=
\mathcal P_\Lambda(g)
+
\mathcal E_\Lambda(g).
\]

What is missing is an observer-weighted estimate or limit for `E_Lambda`, preferably obtained from the two-cutoff Gram pairing before taking `R -> infinity`.

## Status correction

The real local calculation

\[
\operatorname{Tr}(B-B^2)
=
O(\log\Lambda)
\]

remains correct. It is a one-carrier model with no uncontrolled semilocal angular multiplicity.

The semilocal statement is now classified as:

\[
\boxed{
\text{bare transition trace: not known to be finite},
}
\]

\[
\boxed{
\text{observer- and two-cutoff-regularized transition: well-typed}.
}
\]

## Disposition

The next analytic target is not

\[
\operatorname{Tr}(B-B^2)=O(\log\Lambda).
\]

It is the correlated, observer-weighted estimate for

\[
\boxed{
\mathcal E_{\Lambda,R,S}(g)
=
\left\langle
Q_\Lambda P_\Lambda U_S(g),
Q_\Lambda(P_R-P_\Lambda)U_S(g)
\right\rangle_{HS},
}
\]

followed by existence of its combined `R -> infinity` limit. This retains exactly the smoothing that Connes's source theorem uses and avoids assigning a trace to an unregularized angular identity.
