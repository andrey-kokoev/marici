# Conservative symmetrizer is cut-groupoid invariant

Write the base Xi realization in state-space form

$$
\mathcal A_0(z)=zI-A_0,
\qquad B_0,\qquad C_0,
$$

and let a conservative symmetrizer be a bounded nondegenerate Hermitian operator `J_0` satisfying

$$
A_0^*J_0=J_0A_0,
\qquad
J_0B_0=C_0^*.
$$

Transport the state realization through the complete two-history cut `mathbf C_a`:

$$
A_a=\mathbf C_aA_0\mathbf C_a^*,
\qquad
B_a=\mathbf C_aB_0,
\qquad
C_a^{\rm out}=C_0\mathbf C_a^*.
$$

Define

$$
J_a=\mathbf C_aJ_0\mathbf C_a^*.
$$

Then

$$
A_a^*J_a=J_aA_a
$$

and

$$
J_aB_a=(C_a^{\rm out})^*.
$$

Boundedness, nondegeneracy, signature, and positivity are preserved by unitary conjugation. Thus every conservative realization on the base fiber extends uniquely to a coherent family over the complete cut groupoid.

Conversely, pulling any `J_a` back by `mathbf C_a^*` gives a base symmetrizer. Therefore existence on one fiber is equivalent to existence on every cut fiber; seam stabilization introduces no new symmetrizer obstruction and removes none.

The cut composition law implies

$$
J_{a+b}
=\mathfrak a_{a,b}(J_{b\mid a}\oplus J_{\rm seam,a})\mathfrak a_{a,b}^*,
$$

with the precise block notation determined by the cut resegmentation. This is metric coherence over the groupoid.

Status: conservative symmetrizer equations are cut-groupoid invariant. The sole remaining issue is construction of one source-derived nondegenerate base symmetrizer `J_0`; positivity sufficient for confinement remains an additional theorem.
