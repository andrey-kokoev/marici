# The sewing limit splits into a vanishing regular half-line branch and an open semilocal descent branch

## Regular translation-invariant branch

On the logarithmic regular carrier, let

\[
P_L=1_{(-\infty,L]},
\qquad
A_{L,M}=1_{(L,M]},
\]

and let \(Q_T\) be the translation-invariant Fourier projection with sinc kernel

\[
q_T(u)=\frac{\sin(Tu)}{\pi u}.
\]

For an observer correlation kernel \(h\), the sewing term is

\[
\mathcal E_{L,M,T}(h)
=
\int_{u<0}
\min(-u,M-L)
q_T(u)h(-u)du.
\]

Once the annular width exceeds the propagation radius of \(h\), this stabilizes to

\[
\mathcal E_T(h)
=-\frac1\pi
\int_{u<0}
\sin(Tu)h(-u)du.
\]

For integrable boundary data, the Riemann--Lebesgue lemma gives

\[
\boxed{
\mathcal E_T(h)
\longrightarrow0.
}
\]

For smooth data with a controlled boundary value,

\[
\mathcal E_T(h)
=
\frac{h(0)}{\pi T}
+O(T^{-2})
\]

up to the fixed Fourier orientation sign.

## Exact soluble fixture

Take

\[
h(-u)=e^u,
\qquad
u<0.
\]

Then

\[
-\int_{-\infty}^0
\sin(Tu)e^u du
=
\frac{T}{1+T^2}.
\]

Hence

\[
\boxed{
\mathcal E_T
=
\frac{T}{\pi(1+T^2)}
}
\]

and

\[
0<\pi\mathcal E_T
\le
\frac1T.
\]

This gives an exact decay fixture for the depth-constant sewing cell.

## Recentered Hankel branch

For a fixed recentered endpoint Hankel feature \(H_g\), dilation covariance gives

\[
Q_{\Lambda R_b}H_g
\longrightarrow
H_g
\]

in Hilbert--Schmidt norm. This statement concerns the action of the Fourier cutoff after an endpoint fiber has already been isolated.

It has a different order of operations from the regular sinc sewing integral:

- the regular branch keeps the cross-boundary kernel and uses its growing oscillation;
- the recentered branch first identifies a fixed Hankel fiber and then applies strong cutoff exhaustion.

These are compatible local descriptions only after the map from the global prolate transition block to the recentered boundary fiber is supplied.

## Semilocal descent map

Let

\[
\mathcal P_{\Lambda}^{tr}
=P_\Lambda Q_\Lambda(I-P_\Lambda)
\]

be the global prolate transition and let

\[
\mathcal H_{\Lambda}(g)
=(I-P_\Lambda)[P_\Lambda,H_g]P_\Lambda
\]

be the observer boundary block.

The sewing term is

\[
\mathcal E_\Lambda(g)
=-\langle
\mathcal P_\Lambda^{tr},
\mathcal H_\Lambda(g)
\rangle_{HS}.
\]

A semilocal descent theorem requires recentering maps

\[
\mathcal R_{\Lambda,b}
\]

for every retained boundary component such that:

1. \(\mathcal R_{\Lambda,b}\mathcal H_\Lambda(g)\) converges to the fixed Hankel feature;
2. \(\mathcal R_{\Lambda,b}\mathcal P_\Lambda^{tr}\) has a limit or an oscillatory weak limit;
3. the complement outside the boundary fibers has vanishing pairing;
4. norm-one multiplicities admit a summable majorant;
5. reciprocal boundary orientations carry the declared signs.

Only after these five properties can the regular vanishing result be transported to the physical semilocal sewing cell.

## Consequence for the dyadic tower

The sewing cell is independent of dyadic depth. Therefore any established sewing limit applies simultaneously to every object in the soft tower and to its strict inductive limit.

In the regular translation-invariant branch,

\[
\operatorname{Tr}(P_TQ_TH_g)
-
\|\Phi_{T,n}(g)\|^2
\longrightarrow0
\]

for every depth \(n\).

For the physical semilocal branch, the same conclusion is governed by the recentered prolate-to-Hankel descent map above.
