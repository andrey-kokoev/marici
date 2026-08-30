# The projective exponential Köthe sum completes the labelled theta-history incidence

Let \(\mathcal M=\{(p,k):p\text{ prime},\ k\ge1\}\), with

\[
L_{p,k}=k\log p,\qquad a_{p,k}=\frac1k p^{-k/2}.
\]

For \(\delta>0\), define

\[
q_\delta(c)=\sum_{p,k}|c_{p,k}|e^{\delta L_{p,k}},
\qquad
\mathcal A_{\exp}=\bigcap_{\delta>0}\ell^1(\mathcal M,e^{\delta L}).
\]

Finite packets are dense and label truncations converge in every seminorm.

Let \(\mathcal H_{p,k}^{\pm}\) be the transported relative-history graph
spaces at displacements \(\pm L_{p,k}\). Define

\[
\mathfrak H_{\exp}
=
\bigcap_{\delta>0}
\ell^1\left(
\mathcal M,e^{\delta L_{p,k}};
\mathcal H_{p,k}^{+}\oplus\mathcal H_{p,k}^{-}
\right).
\]

For doubled packet \(c\), set

\[
(\mathcal Ic)_{p,k}
=
a_{p,k}
\left(
c_{p,k}^+\tau_{L_{p,k}}\Phi,
c_{p,k}^-\tau_{-L_{p,k}}\Phi
\right).
\]

Translation is isometric and \(|a_{p,k}|\le2^{-1/2}\), so

\[
Q_\delta(\mathcal Ic)
\le
2^{-1/2}\|\Phi\|_{\mathcal E_w}q_\delta(c).
\]

Hence \(\mathcal I\) is continuous without loss of exponential order.

The causal and anti-causal histories have one base graph bound on all
translated fibers, reflection exchanges the summands, and the construction is
label diagonal:

\[
P_{q,\ell}\mathcal IP_{p,k}
=
\delta_{(q,\ell),(p,k)}\mathcal I_{p,k}.
\]

For finite cutoff \(P_X\),

\[
Q_\delta((I-P_X)\mathcal Ic)
\le
2^{-1/2}\|\Phi\|_{\mathcal E_w}
q_\delta((I-P_X)c)
\longrightarrow0.
\]

A dual coefficient row of finite exponential order lies in a weighted dual
rung

\[
\|u\|_{-\delta}
=
\sup_{p,k}|u_{p,k}|e^{-\delta L_{p,k}}<\infty.
\]

The transpose incidence preserves that rung because \(a_{p,k}\) is
contractive. Thus the declared seam and history currents have strong
truncation convergence in a suitable fixed rung.

The labelled reciprocal theta-history incidence is therefore continuous,
order-neutral, cutoff-natural, reflection-equivariant, and prime/grade
diagonal on the projective exponential topology.

This closes the source incidence topology. It does not construct the mixed
primitive--square Green pairing, its radical quotient, or a completed boundary
pencil.
