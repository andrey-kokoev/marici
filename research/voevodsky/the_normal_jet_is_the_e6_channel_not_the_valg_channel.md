# The normal jet is the e6 channel, not the v_alg channel

## Source identification

The geometric first-normal-jet packet found the normalized vertex sign pattern

\[
(d_1,d_2,d_3,d_4)\longmapsto(-1,-1,+1,+1).
\]

Ledger entry `20260816-297 Universal Primitive Two-Wall Filtered Residue` identifies the corresponding first filtered logarithmic survivor. After all rational incidence terms and the forced \(v_{\rm alg}\) tail are removed by source-relative primitives, the only absolute class left is

\[
\frac{1}{8(x+y)}e_6.
\]

Therefore the primitive normal-jet channel belongs to the \(e_6\) coordinate, not to the complementary \(v_{\rm alg}\) coordinate.

## Integral covector

In the primitive frame

\[
\begin{aligned}
d_1&=(1,1,1),&d_2&=(1,-1,-1),\\
d_3&=(-1,1,-1),&d_4&=(-1,-1,1),
\end{aligned}
\]

the unique integral covector with values \((-1,-1,+1,+1)\) is

\[
\boxed{q_{e_6}=(-1,0,0).}
\]

Thus, up to the orientation of \(e_6\), the first comparison row is simply projection to the \(\alpha_{12}\) coordinate. Its kernel is the saturated odd plane

\[
\ker q_{e_6}
=
\mathbb Z\alpha_{13}\oplus\mathbb Z\alpha_{14}.
\]

This matches the \(b\)-reflection character decomposition: \(\alpha_{12}\) is fixed while \(\alpha_{13},\alpha_{14}\) are odd.

## Role of the forced v_alg tail

Entry 297 states that the \(v_{\rm alg}\) tail at logarithmic order is boundary transport, not an independent extension generator. Consequently it cannot be read from the normalized first moving-wall jet. The missing second comparison row must be sought after quotienting by the \(e_6\) row, inside

\[
\ker q_{e_6}=\langle\alpha_{13},\alpha_{14}\rangle.
\]

This explains why the first-order collision computation produced a canonical unit but did not choose a unique line in the odd plane.

## Updated information flow

\[
\{d_i\}
\longrightarrow
\text{moving-wall normal jets}
\longrightarrow
q_{e_6}=(-1,0,0)
\longrightarrow
\langle\alpha_{13},\alpha_{14}\rangle
\longrightarrow
\text{missing }v_{\rm alg}\text{ comparison}.
\]

The remaining comparison is now intrinsically rank one: determine one primitive covector on the rank-two odd plane. Its kernel will be the physical route-kernel line.

Verification:

- `research/voevodsky/checkers/check_normal_jet_e6_covector.py`
- `research/voevodsky/results/normal_jet_e6_covector.json`
