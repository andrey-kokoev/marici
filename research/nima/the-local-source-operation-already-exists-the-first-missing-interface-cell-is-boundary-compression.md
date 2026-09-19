# The local source operation already exists; the first missing interface cell is boundary compression

## Question

Is the first unresolved finite-place operation an abstract encoder from
`S(Q_p)` to retained labels?

## Claim boundary

No. On the spherical valuation lane, the source operation and exact Fourier
transport are already constructed. With

\[
B_k=p^k\mathbb Z_p,
\qquad
S_k=B_k\setminus B_{k+1},
\]

the canonical radial lift is

\[
j_{\rm rad}e_k=\mathbf 1_{S_k}.
\]

For self-dual Haar normalization,

\[
\mathcal F_p\mathbf 1_{B_k}=p^{-k}\mathbf 1_{B_{-k}},
\]

and hence

\[
\mathcal F_p\mathbf 1_{S_k}
=p^{-k}\mathbf 1_{B_{-k}}
-p^{-k-1}\mathbf 1_{B_{-k-1}}.
\]

Thus spherical Fourier transport descends exactly to the completed shell span.
The standard Sonin seed is not fixed: Fourier exchanges the equal-norm pair

\[
\sigma_p=\mathbf 1_{\mathbb Z_p}-p^{-1}\mathbf 1_{p^{-1}\mathbb Z_p},
\qquad
\tau_p=\mathbf 1_{\mathbb Z_p}-\mathbf 1_{p\mathbb Z_p}.
\]

The full nonspherical source must retain translated and character-twisted
shells, so it is a growing additive Tate/Weyl carrier rather than a fixed
finite-dimensional labelled state.

## Correct first missing cell

The fixed retained packet is obtained only after source-derived boundary
compression

\[
U_\partial:\mathcal B_4\to\mathcal H_{{\rm Tate},p},
\qquad
V_\partial^*:\mathcal H_{{\rm Tate},p}\to\mathcal B_4.
\]

The effective return has the form

\[
G_{4,p}(s)=V_\partial^*(I-S_{{\rm Tate},p}(s))^{-1}U_\partial.
\]

No current source formula derives `U_partial` and `V_partial` simultaneously
from theta incidence and endpoint observation. Therefore these maps, not
`j_rad`, are the first missing route/coherencer cell.

## Finite falsifier

At conductor `p^N`, construct the finite additive Weyl carrier first. A
candidate compression fails if any of the following occurs:

1. it does not transport `sigma_p` to `tau_p` under local Fourier;
2. the compressed return depends on the chosen shell representative;
3. the odd Weyl phase is annihilated rather than routed to the wall/jump port;
4. conductor bonding changes the four boundary-port coordinates;
5. discarded nonspherical modes feed back into the compressed return without
   a controlled residual.

## Disposition

The spherical source operation, its composition inside the additive Tate
carrier, and its Fourier law are available. Completion and global sewing remain
premature. The next executable constructor is the finite-conductor incidence
and observation pair `(U_partial,V_partial*)`, with the five residual tests
above.