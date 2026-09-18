# Fixed-forcing correlation graph is the density-to-Haar comparison

Fix the nonzero theta forcing vector `Phi`. For an admitted history `u`, define its separation density

$$
(C_\Phi u)(t)
=\rho_{\Phi,u}(t)
=\int \Phi(x)u(x+t)\,dx.
$$

On the declared rapid/history carrier this correlation map is continuous. Define the joint comparison graph

$$
\Gamma_\Phi
=
\left\{
\bigl(C_\Phi u,\,\Phi\otimes u\bigr):u\in H_{\rm hist}
\right\}
\subset
H_{\rm sep}\oplus
(H_{\rm add}\widehat\otimes\overline{H_{\rm mult}}).
$$

The graph is closed because both component maps are continuous. Its projection to the Haar tensor leg is injective: since `Phi` is nonzero,

$$
\Phi\otimes u=0
\quad\Longrightarrow\quad u=0.
$$

No inverse to `C_Phi` is required. This avoids an unjustified deconvolution, which may be unbounded or fail at zeros of the correlation multiplier.

For history translation `S_a`,

$$
C_\Phi(S_au)=S_a^{\rm sep}(C_\Phi u),
$$

with the corresponding convention for the separation variable, while

$$
\Phi\otimes S_au
=(I\otimes S_a)(\Phi\otimes u).
$$

Hence `Gamma_Phi` intertwines prime dilation/translation on both legs. Reciprocal orientation is retained by adjoining the opposite ordered graph with the contragredient tensor leg.

At an Xi zero, the pointed histories satisfy `u_-=u_+` after seam gluing. Their graph images therefore agree simultaneously in the separation-density and Haar-tensor coordinates. The Haar coordinate is nonzero because the Xi augmented state has nonzero source coordinate and `Phi!=0`.

Thus the correct density-to-Haar comparison is a faithful joint graph, not a map from density alone. On this graph the Xi-relative route equality and the relative-Haar modular energy refer to the same source history state.

Status: density/Haar state-placement graph constructed on the source-generated history carrier; completion requires only the already declared rapid correlation continuity.
