# The reciprocal prime-wall graph is closed and reflection-unitary

## Question

Does adjoining the reflected walls at \(-\log p\) produce a closed response graph on which reciprocal reflection is unitary and the doubled prime incidence remains Hilbert–Schmidt?

## Claim boundary

Let \(A_{\mathrm{rec}}=\{0\}\cup\{\pm\log p:p\text{ prime}\}\). Define \(H_{\mathrm{wall,rec}}\) as the space of \(L^2(\mathbb R)\) functions that are \(H^1\) on every component of \(\mathbb R\setminus A_{\mathrm{rec}}\), whose regular derivative lies in \(L^2(\mathbb R)\), and whose jump family lies in \(\ell^2(A_{\mathrm{rec}})\). Equip it with the norm \(\|f\|_{\mathrm{wall,rec}}^2=\|f\|_2^2+\|f'_{\mathrm{reg}}\|_2^2+\sum_{a\in A_{\mathrm{rec}}}|[f]_a|^2\).

The set \(A_{\mathrm{rec}}\) is locally finite because every bounded interval contains finitely many values \(\pm\log p\). The intervalwise weak-derivative argument for the one-sided prime-wall graph therefore applies: a graph-Cauchy sequence converges in \(L^2\), its regular derivatives converge in \(L^2\), and its jump vectors converge in \(\ell^2(A_{\mathrm{rec}})\). One-dimensional trace continuity on each component identifies the limiting one-sided traces and jumps. Hence \(D_{\mathrm{wall,rec}}f=(f'_{\mathrm{reg}},([f]_a)_{a\in A_{\mathrm{rec}}})\) is closed and \(H_{\mathrm{wall,rec}}\) is complete.

Define reciprocal reflection by \((R_Hf)(t)=f(-t)\). Its regular derivative is \((R_Hf)'_{\mathrm{reg}}(t)=-f'_{\mathrm{reg}}(-t)\), and its jump at \(a\) is \([R_Hf]_a=-[f]_{-a}\). Consequently \(\|R_Hf\|_{\mathrm{wall,rec}}=\|f\|_{\mathrm{wall,rec}}\), \(R_H^2=I\), and \(R_H\) is a unitary involution on the completed graph.

The positive and negative wall subgraphs are the closed subspaces whose jump coordinates vanish respectively on the negative and positive prime walls. Reflection exchanges these subspaces and fixes the zero-jump subspace \(H^1(\mathbb R)\).

Let \(U_{\mathrm{rec}}=U_+\oplus U_-\), where each sector has norm \(\|x\|_U^2=\sum_p\log(p)|x_p|^2\). Define \(R_U(x_+,x_-)=(x_-,x_+)\). Then \(R_U\) is a unitary involution.

For the known positive columns \(b_{p,+}=p^{-1/2}c_{\log p}\), define the reflected analytic columns \(b_{p,-}=-R_Hb_{p,+}\). Their graph norms satisfy \(\|b_{p,-}\|_{\mathrm{wall,rec}}=\|b_{p,+}\|_{\mathrm{wall,rec}}=p^{-1/2}C_{\mathrm{cut}}\).

Define \(B_{\mathrm{rec}}:U_{\mathrm{rec}}\to H_{\mathrm{wall,rec}}\) by \(B_{\mathrm{rec}}(x_+,x_-)=B_+x_++B_-x_-\). Relative to the normalized source basis, its Hilbert–Schmidt norm is \(\|B_{\mathrm{rec}}\|_{\mathrm{HS}}^2=2C_{\mathrm{cut}}^2\sum_p1/(p\log p)<\infty\). Thus the reciprocal completion preserves boundedness and Hilbert–Schmidt incidence.

The analytic covariance holds for the reflected candidate columns: \(R_HB_+=-B_-R_U\) after restricting \(R_U\) from the positive sector to the negative sector. This equality records the definition of \(B_-\); arithmetic source independence remains the requirement that a separate source construction reproduce these columns.

## Disposition

Gate 2.B is complete. The symmetric prime-wall graph is a closed Hilbert graph, reciprocal reflection is a unitary involution, and the doubled analytic incidence is Hilbert–Schmidt. Gate 2.A remains responsible for deriving the negative columns from the arithmetic source, while Gate 2.C compares that source-derived family with the reflected analytic family.
