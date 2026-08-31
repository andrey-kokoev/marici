# Theta arithmetic-to-band bonding is a polarized correlation functor

## Status

Exact typing correction to the proposed arithmetic-to-band bonding square. The
macroscopic band object is built from an autocorrelation of the completed
source. It is quadratic in a single arithmetic coefficient packet and linear
only after polarization to an ordered-pair module.

Therefore no source-compatible linear bonding map from the one-copy arithmetic
module directly to the band module should be expected. The correct bridge
passes through the tensor square and carries two independent logarithmic
generators: product degree and ratio degree.

## Labelled source synthesis

Let the completed positive source be synthesized from labelled atoms:

\[
\Phi_c(u)=\sum_{n\geq1}c_n\phi_n(u).
\]

Write the one-copy synthesis as

\[
U:c\longmapsto\Phi_c.
\]

The band analysis does not act linearly on \(\Phi_c\). Its basic density is an
autocorrelation of two source copies. Schematically,

\[
\mathcal W_c(S,D)
=
\Phi_c\!\left(\frac{S+D}{2}\right)
\overline{\Phi_c\!\left(\frac{S-D}{2}\right)}.
\]

Expanding labels gives

\[
\mathcal W_c(S,D)
=
\sum_{n,m}c_n\overline{c_m}\,\rho_{nm}(S,D).
\]

Thus (c\mapsto\mathcal W_c) is quadratic.

## Polarized linear bridge

Introduce the ordered-pair coefficient module

\[
\mathcal C^{(2)}
=
\mathcal C_{\mathrm{arith}}
\otimes
\overline{\mathcal C_{\mathrm{arith}}}.
\]

The rank-one packet associated with (c) is

\[
\iota(c)=c\otimes\overline c.
\]

There is then a linear correlation synthesis

\[
\widetilde B:
\mathcal C^{(2)}
\longrightarrow
\mathcal C_{\mathrm{band}},
\qquad
e_n\otimes\overline{e_m}
\longmapsto
\rho_{nm}.
\]

The physical one-copy construction factors as

\[
c
\overset{\iota}{\longmapsto}
c\otimes\overline c
\overset{\widetilde B}{\longmapsto}
\mathcal W_c.
\]

The first arrow is nonlinear and positivity-preserving; the second is linear
and retains ordered label pairs. Treating their composite as an ordinary
linear completion map erases both facts.

## Product and ratio degrees

Let (L e_n=(\log n)e_n). On the pair module define

\[
L_{\Sigma}=L\otimes I+I\otimes\overline L,
\]

and

\[
L_{\Delta}=L\otimes I-I\otimes\overline L.
\]

They act on a labelled pair by

\[
L_{\Sigma}(e_n\otimes\overline{e_m})
=(\log n+\log m)e_n\otimes\overline{e_m},
\]

\[
L_{\Delta}(e_n\otimes\overline{e_m})
=(\log n-\log m)e_n\otimes\overline{e_m}.
\]

These are the arithmetic product and ratio coordinates. The band variables

\[
S=U+V,
\qquad
D=U-V
\]

are their continuous source counterparts. The desired bonding theorem must
intertwine both pairs, not only a one-dimensional moment degree.

## Transport laws

Diagonal prime transport acts as

\[
T_p^{(2)}=T_p\otimes\overline{T_p}.
\]

It obeys

\[
[L_{\Sigma},T_p^{(2)}]
=2(\log p)T_p^{(2)},
\]

while

\[
[L_{\Delta},T_p^{(2)}]=0.
\]

So common prime scaling changes product degree but preserves ratio degree.

Independent transports (T_p\otimes\overline{T_q}) instead satisfy

\[
[L_{\Delta},T_p\otimes\overline{T_q}]
=(\log p-\log q)
(T_p\otimes\overline{T_q}).
\]

This is the labelled arithmetic origin of relative-scale motion. It is the
channel to which separation-band oscillation can legitimately couple.

## Corrected filtered square

The earlier proposed linear square must be replaced by

\[
\begin{array}{ccc}
\mathcal C_{\mathrm{arith}}^{(2)}
&\overset{\widetilde B}{\longrightarrow}&
\mathcal C_{\mathrm{band}}\\
\downarrow J_{\Sigma,\Delta}&&\downarrow J_{S,D}\\
\mathcal J_{\Sigma,\Delta}
&\overset{\beta}{\longrightarrow}&
\mathcal J_{S,D}.
\end{array}
\]

The physical cone occupies only rank-one positive packets

\[
c\otimes\overline c
\]

inside the full pair module. A theorem proved for arbitrary signed pair
coefficients may therefore be too strong, while a theorem proved only after
scalar autocorrelation may erase the ordered-pair information needed for the
boundary current.

## Relation to beyond-all-orders flatness

The logarithmic flat sector relevant to the band bridge is not the one-copy
kernel alone. It is the joint pair-jet kernel

\[
\mathcal F_{\Sigma,\Delta}
=
\bigcap_{j,k\geq0}
\ker\!\left(\varepsilon^{(2)}
L_{\Sigma}^jL_{\Delta}^k\right).
\]

Only a source-derived intertwining theorem for \(\widetilde B\) can compare
this kernel with the flat (S,D) band remainder.

The boundaryless modular current is genuinely new if it detects a completed
pair packet in this joint flat kernel. One-copy moment flatness is not the
correct test.

## Finite falsifiers

Any proposed bridge fails if:

- it is linear on (c) rather than on the polarized pair packet;
- it identifies ((n,m)) and ((m,n)) before typing ratio orientation;
- it retains only product or only ratio degree;
- it treats every pair packet as physically positive instead of preserving the
  rank-one cone;
- diagonal prime scaling changes the ratio coordinate;
- it claims equality of flat sectors without the joint jet square.

The smallest transport witness is one ordered pair (e_n\otimes\overline{e_m}).
Its product and ratio commutators must match the formulas above exactly.

## Decisive next construction

Use the explicit labelled theta atoms \(\phi_n\) to compute the finite maps

\[
e_n\otimes\overline{e_m}
\longmapsto
\rho_{nm}(S,D)
\longmapsto
(W_{nm}(D),J_{nm}(D)).
\]

Then test whether the full boundaryless band current is continuous on the
completed positive rank-one cone and whether it detects a state invisible to
every joint product-ratio jet. This is the first correctly typed place where
arithmetic scale coherence can meet nonperturbative modular orientation.
