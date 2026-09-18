# Endpoint leverage gate is a successor-natural Douglas vector

For the one-dimensional odd endpoint channel, write

$$
b_kb_k^*=c_kv_kv_k^*,
\qquad c_k>0.
$$

The nonnegative Schur condition

$$
C_k-c_kv_kv_k^*\succeq0
$$

holds exactly when:

$$
v_k\in\operatorname{ran}C_k^{1/2}
$$

and

$$
c_k\|C_k^{\dagger/2}v_k\|^2\le1.
$$

Equivalently, there is a Douglas vector `d_k` satisfying

$$
C_k^{1/2}d_k=\sqrt{c_k}\,v_k,
\qquad
\|d_k\|\le1.
$$

For an actual coherence structure, these vectors cannot be chosen independently. If `S_(k->l)` is a grade/seam successor, one requires

$$
d_l=S_{k\to l}d_k
$$

in the transported bulk fibers, together with the corresponding covariance of `C_k` and `v_k`.

The exact interval endpoint vectors are

$$
e_+(x)=e^{x/2},
\qquad e_-(x)=e^{-x/2},
$$

and the odd parity vector has norm

$$
\|e_{\rm odd}\|^2=2(\sinh L-L).
$$

It is a cokernel mode of `partial_x^2-1/4`, explaining failure of the unaugmented bulk range condition. The endpoint-augmented boundary triple must provide its Poisson lift; the direct bulk intertwiner route is ruled out.

Thus the next concrete constructor is the odd endpoint Poisson vector

$$
d_L=\gamma(z_{\rm end})e_{\rm odd}
$$

in the augmented energy space, followed by exact computation of its normalized energy. The required statement is `||d_L||<=1`, uniformly and naturally under interval/grade successors.

Status: positive coherence reduced to construction and norm control of one successor-natural odd Poisson/Douglas vector.
