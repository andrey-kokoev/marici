# Moving-seam transport and complete endpoint pushforward form an exact metric natural transformation

## Source bundle

For scale \(a\ge0\), let

\[
E_a=L^2(a,\infty)\oplus L^2(0,a)
\]

be the cut fiber and let

\[
R_a:E_a\longrightarrow L^2(0,\infty)
\]

be the unitary reassembly map. Moving-seam transport is

\[
T_{b\leftarrow a}=R_b^{-1}R_a.
\]

It is unitary and satisfies

\[
T_{c\leftarrow b}T_{b\leftarrow a}=T_{c\leftarrow a}.
\]

For the source cut atom \(u_a\),

\[
R_au_a=\Phi,
\qquad
T_{b\leftarrow a}u_a=u_b.
\]

## Endpoint observer functor

Let \(\tau_a\) be the complete two-sided endpoint trace on the relative history
generated from the cut fiber. Write

\[
\tau_a f=
\begin{pmatrix}
t_-(f)\\
t_+(f)
\end{pmatrix}.
\]

The wall--jump pushforward is

\[
\Phi_{\partial,a}
=
H_\partial\tau_a,
\qquad
H_\partial
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix}.
\]

The first coordinate is reciprocal even and the second reciprocal odd.

Because seam transport is defined by reassembly, the transported endpoint
trace is forced to satisfy

\[
\tau_bT_{b\leftarrow a}
=
T^\partial_{b\leftarrow a}\tau_a,
\]

where

\[
T^\partial_{b\leftarrow a}
=
\tau_bR_b^{-1}R_a\sigma_a
\]

on the source-generated endpoint plane and \(\sigma_a\) is the canonical
harmonic trace section. Equivalently, \(T^\partial\) is the mate induced by the
Green trace adjunction; it is not an independently fitted endpoint matrix.

Conjugating by \(H_\partial\) gives the exact wall--jump square

\[
\Phi_{\partial,b}T_{b\leftarrow a}
=
\widetilde T^\partial_{b\leftarrow a}\Phi_{\partial,a},
\qquad
\widetilde T^\partial
=
H_\partial T^\partial H_\partial^{-1}.
\]

## Metric identity

The bilateral Mellin trace frame at logarithmic scale \(L\) has transport

\[
D_{L\to M}=D_MD_L^{-1},
\qquad
D_L=
\begin{pmatrix}
e^{L/2}&0\\
0&e^{-L/2}
\end{pmatrix},
\]

and object-indexed metric

\[
G_L=D_L^{-*}D_L^{-1}.
\]

Therefore

\[
D_{L\to M}^*G_MD_{L\to M}=G_L.
\]

The Hadamard endpoint change is unitary in the transported endpoint metric.
Consequently \(\widetilde T^\partial\) is an isometry between the wall--jump
metric fibers. Seam motion followed by complete endpoint pushforward loses
neither endpoint rank nor reciprocal character.

The metrics \(G_L\) are not uniformly equivalent to one fixed Euclidean
metric as \(L\to\infty\). The theorem is therefore bundle-valued. Replacing
the object-indexed fibers by one fixed metric would create a false
completion obstruction.

## Adams specialization

At prime-power scale

\[
a_{p,k}=k\log p,
\]

Adams grade raising \(k\mapsto rk\) has geometric lift

\[
T_{ra\leftarrow a}
\]

and coefficient cocycle

\[
\rho_r(p,k)
=
\frac1r p^{-(r-1)k/2}.
\]

The complete weighted endpoint transport is

\[
A^\partial_r(p,k)
=
\rho_r(p,k)\widetilde T^\partial_{ra\leftarrow a}.
\]

Since the endpoint part is isometric,

\[
\|A^\partial_r(p,k)\|=|\rho_r(p,k)|.
\]

For \(r\ge2\),

\[
\|A^\partial_r(p,k)\|
\le
\frac1{2\sqrt2}.
\]

Composition is exact because both factors are cocycles:

\[
A^\partial_{rs}(p,k)
=
A^\partial_r(p,sk)A^\partial_s(p,k)
\]

with the convention determined by the order of grade raising.

## Wall and jump channels

The tensor-unit wall coordinate is transported separately with coefficient
one. It is not inserted into the contractive Adams incidence.

The nonunit odd coordinate is carried by the endpoint jump line and evaluated
analytically through

\[
d_p=H_{\mathrm{jump}}b_p=-2j_\theta b_p.
\]

Because complete endpoint pushforward occurs before scalar Euler aggregation,
the odd line cannot be erased by the even scalar readout.

Thus the composed constructor is block typed:

\[
I_{\mathrm{wall}}
\oplus
A^\partial_r
\oplus
K_{\mathrm{odd}},
\]

where \(K_{\mathrm{odd}}\) is the already closed theta-to-window graph map.

## Fourier saturation

Fiberwise Fourier transport is

\[
F_a=R_a^{-1}FR_a
\]

and obeys

\[
F_bT_{b\leftarrow a}=T_{b\leftarrow a}F_a.
\]

The endpoint Hadamard frame diagonalizes the induced constant--delta exchange.
Hence the seam--endpoint naturality square holds in each of the four Fourier
presentations. Summing their transported Grams introduces no additional norm
loss.

Cutoff projections act only on prime labels and therefore commute with seam
transport, endpoint pushforward, and Fourier-orbit completion.

## Consequence

The composite

\[
\text{weighted Adams incidence}
\longrightarrow
\text{moving-seam transport}
\longrightarrow
\text{complete wall--jump endpoint pushforward}
\]

is an exact metric natural transformation on the source-generated bundle. It
has:

- unitary geometric seam motion;
- exact rank-two endpoint faithfulness;
- preserved reciprocal grading;
- a strict nonunit Adams contraction;
- exact word composition;
- and cutoff-compatible Fourier saturation.

## Remaining scope

This closes the seam-transport plus endpoint-attachment generator word on the
linear source bundle. It does not prove the complete three-sector Green
identity with external boundary flux, nor the five global coercivity margins.

The next unresolved constructor-level gate is the compatibility of this
boundary natural transformation with the even zero-trace bulk Green form.
That is the source-defined anti-diagonal Green identity, not another endpoint
rank calculation.

## Verdict

Moving-seam transport and complete endpoint pushforward commute through the
source Green trace mate and preserve the object-indexed Mellin metric exactly.
After Euler weighting, their Adams composite is uniformly contractive on every
nonunit grade.

The research frontier moves to the complete bulk-plus-external-port Green
identity and its anti-diagonal zero-trace reduction.
