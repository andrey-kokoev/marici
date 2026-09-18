# Many-many endpoint relative trace map

On the pointed translation algebra, define the state-dependent relative trace

$$
\operatorname{Tr}^{\rm rel}_G(T)
=E_0(TG)-\varepsilon(T)E_0(G).
$$

For translations,

$$
\operatorname{Tr}^{\rm rel}_G(S_\ell)
=G(\ell)-G(0).
$$

For the logarithmic Euler operator,

$$
\operatorname{Tr}^{\rm rel}_G(H_X)
=\sum_{p\le X}\sum_{k\ge1}
\frac1k p^{-k/2}
\bigl(G(k\log p)-G(0)\bigr).
$$

This map is a one-coboundary on the translation action groupoid:

$$
\operatorname{Tr}^{\rm rel}_G(S_{a+b})
=\operatorname{Tr}^{\rm rel}_G(S_a)
+\operatorname{Tr}^{\rm rel}_{S_aG}(S_b).
$$

It supplies a canonical common-carrier readout for primitive, square, and connected endpoint currents. It is not cyclic and therefore is not automatically the operator trace entering `det_3`.

The remaining comparison is a source morphism from this pointed relative-trace packet to the determinant-line trace packet, compatible with the three-grade split and archimedean line.

Status: endpoint relative trace map constructed; comparison with determinant traces remains open.
