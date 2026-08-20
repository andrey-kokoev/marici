# Rees-Line Cancellation and the Log Branch-Selected Beck--Chevalley Gate

Date: 2026-08-15  
Status: canonical Rees occurrence-line cancellation proved, and ordinary
Cartier purity/Beck--Chevalley identification at the nodal crossing
falsified. The internal complete-intersection log lattice is identified as
the correct finite coefficient shape, but its branch-selected spatial map to
entries 131 and 143 remains unconstructed. No graph admission is claimed.

## Canonical line cancellation before pushforward

On the selected chart of
\[
\operatorname{Bl}_{(X_5,u_5)},
\]
write
\[
u_5=X_5t_5.
\]
The selected conductor line is
\[
I_{X_5}=\mathcal O_{\mathbb P^1}(-1),
\]
while the primal occurrence dual is
\[
I_{X_5}^{\vee}=\mathcal O_{\mathbb P^1}(1).
\]
Their evaluation is canonical:
\[
I_{X_5}^{\vee}\otimes I_{X_5}
\longrightarrow\mathcal O,
\qquad
(+1)+(-1)=0.
\]

The order of operations is essential. Before evaluation,
\[
Rp_*\mathcal O(-1)=0.
\]
After evaluating the two line factors,
\[
Rp_*\mathcal O
=\mathcal O,
\qquad
R^{>0}p_*\mathcal O=0.
\]
Thus the evaluated packet has one primitive section. No scalar
trivialization, inversion of \(X_5\) or \(u_5\), or fitted endpoint value is
used:
\[
\boxed{
Rp_*(I_{X_5}^{\vee}\otimes I_{X_5})
\simeq\mathcal O.
}
\]

This repairs the bare coherent-ideal failure of entry 190's predecessor
without promoting the repair to a spatial endpoint map. The occurrence dual
must be retained until evaluation; pushing \(I_{X_5}\) first loses the class.

## Ordinary purity fails at the crossing

Let
\[
C=V(X_5,t_5)
\]
in the Rees chart. Since
\[
du_5=t_5\,dX_5+X_5\,dt_5,
\]
both components of \(du_5\) vanish on \(C\). Hence \(u_5=0\) is not a regular
Cartier coordinate there.

The support schemes also differ:
\[
V(X_5t_5)=V(X_5)\cup V(t_5),
\qquad
V(X_5,t_5)=V(X_5)\cap V(t_5).
\]
The point \((X_5,t_5)=(1,0)\) lies in the first and not the second. In each
positive polynomial degree, the product quotient
\(k[X_5,t_5]/(X_5t_5)\) retains the two pure monomials, whereas the
complete-intersection quotient by \((X_5,t_5)\) has no positive-degree
part.

Derived restriction makes the mismatch decisive:
\[
K(X_5t_5)\big|_C
\quad\text{has ranks}\quad(1,1),
\]
while
\[
K(X_5,t_5)\big|_C
\quad\text{has ranks}\quad(1,2,1).
\]
Therefore no ordinary purity or ordinary Beck--Chevalley identification can
replace the product-divisor packet by the coefficient-center
complete-intersection packet:
\[
\boxed{
K(X_5t_5)|_C\not\simeq K(X_5,t_5)|_C.
}
\]

## Internal log-node lattice

The complete-intersection fibre has the finite exterior lattice
\[
\Lambda^\bullet
\langle e_{X_5},e_{t_5}\rangle
=
\left[
\mathbf1
\longrightarrow
\mathbf1 e_{X_5}\oplus\mathbf1 e_{t_5}
\longrightarrow
\mathbf1(e_{X_5}\wedge e_{t_5})
\right],
\]
with ranks \(1,2,1\). This is the correct internal coefficient shape for a
log/SNC treatment: it keeps the two branches distinct and retains their
intersection excess class.

The admitted physical branch label may select the
\(e_{X_5}\)-direction, while the wedge generator records the crossing
excess. This is a positive finite-lattice statement only. The checker does
not construct a specialization functor, a branch-selection morphism, or a
comparison with a spatial endpoint costalk.

## Exact remaining map

The minimal new datum is a logarithmic branch-selected excess map
\[
\operatorname{BC}^{!,\log}_{X_5,u_5}:
\operatorname{Sp}^{\log}_{X_5,u_5}
\left(
I_{X_5}^{\vee}\otimes
C_*^{\mathrm{BM}}(E,C)
\right)
\longrightarrow
E_{v_+}^{\mathrm{BM},\check C}.
\]
It must:

- evaluate \(I_{X_5}^{\vee}\otimes I_{X_5}\) before proper pushforward;
- retain the branch generators and the \(e_{X_5}\wedge e_{t_5}\) excess
  grade;
- land in the literal entry-143 \(u_5\)-Boolean endpoint factor;
- restrict on the road edge to entry 131's normalized Cartier purity;
- preserve the endpoint orientation and both conductor boundary grades.

Neither
\(\operatorname{Sp}^{\log}_{X_5,u_5}\) nor this comparison is constructed by
the checker. The canonical line cancellation fixes its coefficient
normalization, but does not imply its existence.

## Scope, falsifiers, and boundary

The positive theorem is falsified if the two Rees-line exponents fail to
cancel, if \(Rp_*\mathcal O\) lacks its primitive section, or if evaluation
requires a base-ring inverse.

The ordinary no-go is falsified if \(du_5\) is nonzero on \(C\), if the
product divisor equals the complete intersection, or if their derived fibre
ranks agree.

A future logarithmic or SNC branch-selected correspondence would not
contradict the no-go because it carries the missing branch and excess data.
Conversely, matching the \(1,2,1\) lattice does not establish the spatial
comparison.

Until the displayed logarithmic Beck--Chevalley map, its polarity conjugate,
the generic \(Q\) leg, and both endpoint connector cells exist, the
endpoint-fixed physical mapping fiber remains uninstantiated. Therefore
\(p_{\partial,Q}\), its parity, and its Bockstein remain undefined.

## Provenance and validation

Exact certificate:

- research/voevodsky/check_d03_rees_line_cancellation_log_bc_gate.rs,
  SHA-256
  c6baa4ea0167abd12e318a14c88ae9c9576c90e8be11084751c3d4668e5e4520.

The independent audit reports formatting and warnings-denied metadata
compilation as passing. The theorem claimed here is exactly the checker's
finite Rees-line cancellation and ordinary-purity no-go; no runtime claim or
spatial theorem is added.

Relevant ledger inputs are entries 131, 143, 168, 173, 186, and 189.

## Next experiment

Construct
\(\operatorname{Sp}^{\log}_{X_5,u_5}\) on the selected Rees chart and its
map to the literal entry-143 endpoint Boolean packet. Verify the \(1,2,1\)
log lattice, the line evaluation before pushforward, and restriction to
entry 131's edge purity. Only then add the polarity endpoint, generic
\(Q\) comparison, mapping fiber, or parity.

## Outcome contract

~~~json
{
  "claim": "On the Rees chart u5=X5*t5, the selected occurrence line O(-1) canonically pairs with its primal dual O(1), so evaluation before proper pushforward gives Rp_*O=O with one primitive section and no base inversion. Ordinary purity nevertheless fails at C=V(X5,t5): du5 vanishes, V(X5*t5) differs from V(X5,t5), and the derived fibre ranks are (1,1) versus (1,2,1).",
  "status": "proved_scoped_with_no_go",
  "scope": "canonical Rees occurrence-line cancellation and falsification of ordinary Cartier/BC identification at the crossing; no logarithmic spatial comparison or graph admission",
  "factorization": {
    "rees_chart": "u5=X5*t5",
    "selected_line": "I_X5=O(-1)",
    "primal_dual": "I_X5^vee=O(1)",
    "evaluated_line": "O",
    "Rp_star_before_evaluation": [0, 0],
    "Rp_star_after_evaluation": [1, 0],
    "base_inversion": false,
    "du5_at_C": [0, 0],
    "support_product": "V(X5*t5)",
    "support_center": "V(X5,t5)",
    "product_Koszul_fibre_ranks": [1, 1],
    "log_complete_intersection_ranks": [1, 2, 1],
    "internal_log_lattice": "Lambda(e_X5,e_t5), branch generators plus wedge excess",
    "log_branch_selected_BC": "unconstructed",
    "entry131_edge_restriction": "unconstructed",
    "literal_entry143_comparison": "unconstructed",
    "physical_mapping_fiber": "unconstructed",
    "physical_p_partial_Q": "undefined",
    "physical_Bockstein": "undefined"
  },
  "checker_sha256": "c6baa4ea0167abd12e318a14c88ae9c9576c90e8be11084751c3d4668e5e4520",
  "evidence_refs": [
    "research/voevodsky/check_d03_rees_line_cancellation_log_bc_gate.rs",
    "src/ledger/20260814-131 D03 Cartier Edge Purity and the Scoped PC Promotion.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-168 Full Rees First-Flip Occurrence Kernel and the External Normal Gate.md",
    "src/ledger/20260815-173 Component-Supported Semistable Node and the vplus Coefficient Counit.md",
    "src/ledger/20260815-186 Direct Affine-Node Endpoint Descent No-Go and the Extraordinary Trace Gate.md",
    "src/ledger/20260815-189 Nodal Component Perfectness No-Go and the Relative Exceptional BM Repair.md"
  ],
  "unconstructed": [
    "logarithmic specialization Sp_{X5,u5}",
    "branch-selected excess Beck-Chevalley map",
    "comparison to entry-143 u5 Boolean endpoint factor",
    "restriction theorem recovering entry-131 edge purity",
    "polarity endpoint, generic Q leg, and endpoint connector cells",
    "physical mapping fiber, p, parity, and Bockstein"
  ],
  "counterevidence": [
    "The ordinary conormal du5 vanishes at the crossing.",
    "The product divisor contains points absent from the complete-intersection center.",
    "The product and pair Koszul fibres have different ranks.",
    "The finite log lattice supplies coefficient shape but no spatial map."
  ],
  "minimal_repair": "A log/SNC branch-selected excess correspondence that evaluates the Rees occurrence line before pushforward, retains the 1-2-1 branch/excess lattice, lands in literal entry143, and restricts to entry131 purity.",
  "next_experiment": "Construct Sp_log_{X5,u5} and its literal endpoint Beck-Chevalley map before defining the physical mapping fiber or parity."
}
~~~
