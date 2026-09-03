# Fixed-rank endpoint-free cone is positive in the full small-heat corner

## Question

Can the remaining fixed-rank singular regime `h/t->infinity` be controlled, and thereby complete the two-parameter small-heat corner?

## Claim boundary

For every fixed rank `N`, there exists `epsilon_N>0` such that the endpoint-free Hankel matrix `B_N(t,h)` is positive definite whenever

\[
0<t<\epsilon_N,
\qquad 0<h<\epsilon_N.
\]

The threshold depends on rank. This is not an all-rank theorem.

## Large mesh-ratio block decomposition

Write

\[
b_n=H(t+nh)-H(t+(n+1)h),
\qquad
B_N=(b_{i+j})_{0\le i,j<N}.
\]

Separate the first coordinate:

\[
B_N=
\begin{pmatrix}
b_0&v^*\\
v&C
\end{pmatrix},
\]

where

\[
C=B_{N-1}(t+2h,h).
\]

If `t/h->0` while `t,h->0`, then the base-to-mesh ratio for `C` tends to `2`; equivalently its mesh-to-base ratio tends to `1/2`. The compact scaled-mesh theorem therefore gives

\[
C>0,
\qquad
\lambda_{\min}(C)\ge c_N h^{-1/2}\log(1/h)
\]

for sufficiently small `h`, with `c_N>0`.

## Dominant first scalar

The small-heat asymptotic gives

\[
b_0\sim \frac{t^{-1/2}\log(1/t)}{8\sqrt\pi},
\]

because `H(t+h)=o(H(t))` when `t/h->0`. Each fixed component of `v=(b_1,\ldots,b_{N-1})` is

\[
O_N(h^{-1/2}\log(1/h)).
\]

Hence

\[
\frac{\|v\|^2}{b_0}
=O_N\!\left(
 h^{-1/2}\log(1/h)
 \sqrt{t/h}\,
 \frac{\log(1/h)}{\log(1/t)}
\right).
\]

Since `t<h` in this regime,

\[
0<\frac{\log(1/h)}{\log(1/t)}\le1,
\]

and the Schur correction is smaller than the least-eigenvalue scale of `C` by a factor tending to zero. Thus

\[
C-vb_0^{-1}v^*>0,
\]

so `B_N(t,h)>0`.

## Completion of the small corner

The possible ratios `kappa=h/t` split into three regions:

1. `kappa` near zero, covered by the confluent Newton-moment theorem;
2. `kappa` in a compact subinterval of `(0,infinity)`, covered by compact uniformity of the strict leading moment matrix;
3. `kappa` large, covered by the Schur decomposition above.

Choose the ratio cutoffs first, then take the minimum of the three fixed-rank heat thresholds. This gives one `epsilon_N` for the full square `0<t,h<epsilon_N`.

## Relation to observer refinement

The refinement identity expresses a coarse mesh as a sum of sparse compressions of shifted finer-mesh matrices. It is compatible with this theorem but not needed for the large-ratio Schur argument. Because refinement inflates rank, it does not remove the dependence of `epsilon_N` on `N`.

## Strongest falsification attempt

Nothing here controls `inf_N epsilon_N`. The strict gamma moment matrices become ill-conditioned with rank, and both the Newton and Schur constants may deteriorate. Therefore the all-rank cone cannot be inferred by taking a union over fixed ranks.

## Disposition

At every fixed rank, the entire two-parameter small-heat corner is unconditionally positive. A counterexample to the endpoint-free cone must either occur away from that corner or use ranks tending to infinity as the corner is approached.