# Branch C post-adapter strict D35/D04 gate

Date: 2026-09-08

## Status

Branch B now supplies the complete framed/support kernel-valued map

\[
\kappa_{\sigma,T}:G^{\rm native}_{\sigma,T}\to
N_{k_\sigma}=\ker(\pi_{k_\sigma}),
\qquad k_+=35,\ k_-=04.
\]

Consequently the spatial candidate

\[
b_{\sigma,T}(x)=(0,j_k\kappa_{\sigma,T}(x),0)
\]

has no additional `q` equation. Its formal defect is

\[
d_Db-bd_G=(0,j_k(d_N\kappa-\kappa d_G),-\pi_kj_k\kappa)=0.
\]

The same reduction applies to native linearity. Thus the source-to-kernel part of Branch C is no longer blocked by line or support transport.

## First unrecoverable strict target block

Part I nevertheless requires the complete strict target

\[
D_k^n=W^n\oplus E_k^n\oplus T^{n-1},\qquad
 d_D=\begin{pmatrix}d_W&0&0\\0&d_E&0\\q&-\pi_k&-d_T\end{pmatrix}.
\]

The local Branch A checker exports:

- the complete 50-state ambient resolution and its dual differential;
- the two-layer `E_beta,35` occurrence action;
- the primitive dualizing attachment signs `(-1,+1)`;
- reflection and operation data on the relative conormal orbit.

It does **not** export a strict chain matrix

\[
q:\omega[2]\to C\Pi^\vee[3]
\]

in the same ordered basis as the exported dualizing differential. The two attachment signs are cohomological/connecting data and cannot be substituted for this missing chain map. Nor is there an exported complete native `B`-action on the strict omega model for which `q` is strictly linear.

Therefore `d_D^2=0` cannot be numerically instantiated: its unresolved block is

\[
q^{n+1}d_W^n-d_T^nq^n.
\]

Missing matrices remain unknown, not zero. The kernel-valued factorization proves that this block does not obstruct the particular image of `b`; it does not instantiate the target demanded by Part I.

## Decision

**Branch C Decision 4:** after the successful Branch B adapter, the first remaining datum is the ordered strict dualizing truncation matrix `q` (and its compatible native action) in the complete omega basis. Once supplied, the strict pullback differential can be compiled directly and the kernel-valued spatial map inserted with components `(0,j_k kappa,0)`.

Parts II and III are not entered. In particular no physical Q-manifold, outer vector fields, trace, or P24 deformation class is asserted.
