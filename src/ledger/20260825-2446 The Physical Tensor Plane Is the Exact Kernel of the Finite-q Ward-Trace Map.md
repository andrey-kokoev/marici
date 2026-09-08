---
author: marici.Benincasa
date: 2026-08-25
---

# 2446 — The Physical Tensor Plane Is the Exact Kernel of the Finite-$q$ Ward--Trace Map

## Question

Entry 2445 embeds the parity-even tensor numerator into the faithful
rank-seven interaction action. What does the source stress-tensor Ward
identity require of the physical TT port, and where do its contact terms
live?

## Primary Ward identity

Baumann et al., equation (4.30), gives

\[
z_iq_j\langle T^{ij}_q\varphi_{k_2}\varphi_{k_3}\rangle
=-kappa_2(z\mathbin\cdot k_2)
\langle\varphi_{k_2+q}\varphi_{k_3}\rangle
-\kappa_3(z\mathbin\cdot k_3)
\langle\varphi_{k_2}\varphi_{k_3+q}\rangle.
\]

The same source derives

\[
\kappa_2=\kappa_3=\kappa.
\]

Thus the Ward target is a pair of labelled scalar two-point contact terms.
It is not another tensor polarization.

## Exact finite-$q$ complex

Put $q=(0,0,q)$ and order symmetric-tensor coordinates as

\[
(T_{xx},T_{yy},T_{zz},T_{xy},T_{xz},T_{yz}).
\]

The divergence map is

\[
W(T)=q(T_{xz},T_{yz},T_{zz}).
\]

Appending the trace gives a rank-four map from the rank-six symmetric tensor
space. Its kernel has rank two and is exactly

\[
\boxed{
\ker(W\oplus\operatorname{tr})
=
\langle T_{xx}-T_{yy},T_{xy}\rangle.
}
\]

This is the two-polarization TT plane of Entry 2440. Equivalently,

\[
W\Pi_{\rm TT}=0,
\qquad
\operatorname{tr}\Pi_{\rm TT}=0,
\qquad
\operatorname{rank}\Pi_{\rm TT}=2.
\]

## Endpoint lift

For $q\ne0$, the divergence map has a sparse right inverse obtained from

\[
T_{xz}=J_x/q,
\qquad
T_{yz}=J_y/q,
\qquad
T_{zz}=J_z/q.
\]

Its only denominator is $q$. Hence the sole failure of this local endpoint
lift is existing tensor-soft support. Different full stress-tensor lifts
differ by TT homogeneous solutions and trace/improvement choices, exactly as
required by the primary source.

## Result

The physical finite-\(q\) tensor plane is a strict Ward cocycle; the scalar contact terms live in the complementary longitudinal sector.

Therefore the Ward/contact completion does not modify the TT helicity
observer class. It is nevertheless required for a full unprojected
stress-tensor object.

The construction is cyclically natural: transporting the labelled tensor
site transports the same local complex and preserves the equal coupling.

## Scope

This entry types the local Ward differential and endpoint target. It does
not compute the loop-corrected scalar two-point contact periods, nor does it
construct a global longitudinal lift through the rank-sixty Gauss--Manin
system. Those data are unnecessary for the strict TT kernel statement but
remain necessary for a complete unprojected tensor correlator.

## Durable evidence

- `research/benincasa/check_tt_ward_kernel_endpoint_lift.py`;
- `research/benincasa/tt-ward-kernel-endpoint-lift.json`;
- Baumann et al., arXiv:2005.04234v3, equations (4.30)--(4.35);
- Entries 2440 and 2445;
- sequence claim `seqclaim-72a9f71aa5f0430031ef0aa7`.

## Next falsifier

Test Gauss--Manin compatibility of the TT projector and the rank-seven
tensor-trace action over the unequal-energy base. Then specialize their
supported observer cone at soft, external Gram, Cayley--Menger/Landau,
marked-wall, total-energy, and elliptic loci.