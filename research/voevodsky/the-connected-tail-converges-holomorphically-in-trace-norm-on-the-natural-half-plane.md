# The connected tail converges holomorphically in trace norm on the natural half-plane

## Question

Does the grade-at-least-three return tail satisfy the holomorphic ideal-convergence condition of the determinant compiler?

## Claim boundary

Yes wherever the local return blocks are holomorphic and obey the retained half-density majorant. The natural uniform half-plane is \(\operatorname{Re}z>-1/6\). This closes the connected-tail convergence condition, not convergence or normalization of the primitive and square cumulants.

## Local bound

Let \(K_{p}^{(k)}(z)\) be the grade-\(k\) prime return block. The retained transfer estimate, with holomorphic return parameter, has compact-local form

$$
\|K_p^{(k)}(z)\|_1
\le
C_Q\,p^{-k(1/2+\operatorname{Re}z)}\sqrt{\log p}
$$

for \(z\) in a compact set \(Q\) of the declared return half-plane and \(k\ge3\). Each finite block is holomorphic.

## Uniform trace-norm convergence

Fix compact \(Q\subset\{\operatorname{Re}z>-1/6\}\), and choose \(\delta>0\) such that

$$
\operatorname{Re}z\ge-\frac16+\delta
$$

on \(Q\). Then for \(k\ge3\),

$$
k(1/2+\operatorname{Re}z)
\ge
1+3\delta.
$$

Summing first over grades gives

$$
\sum_{k\ge3}p^{-k(1/2+\operatorname{Re}z)}
\le
\frac{p^{-1-3\delta}}{1-p^{-1/3-\delta}}.
$$

Hence

$$
\sum_p\sum_{k\ge3}
\sup_{z\in Q}\|K_p^{(k)}(z)\|_1
<\infty,
$$

because \(\sum_p p^{-1-3\delta}\sqrt{\log p}<\infty\). The Banach-valued Weierstrass theorem therefore yields a trace-norm holomorphic limit

$$
K_{\ge3}(z)=\sum_p\sum_{k\ge3}K_p^{(k)}(z)
$$

on \(\operatorname{Re}z>-1/6\).

Prime-and-grade cutoffs converge uniformly on compact sets in trace norm. Continuity of the regularized determinant then gives

$$
\det_3(I+K_{\ge3,N}(z))
\longrightarrow
\det_3(I+K_{\ge3}(z))
$$

locally uniformly and holomorphically.

## Sharp boundary of this argument

At \(\operatorname{Re}z=-1/6\), the grade-three majorant becomes

$$
p^{-1}\sqrt{\log p},
$$

whose prime sum diverges. Thus this absolute trace-norm argument cannot include that boundary. Cancellation or a stronger local estimate would be required.

## Disposition

The connected \(\det_3\) factor of the completed determinant compiler is constructed holomorphically on \(\operatorname{Re}z>-1/6\). The remaining completion gate lies in the renormalized first and second cumulants and their compatibility with the Mellin factor, not in the grade-at-least-three ideal tail.