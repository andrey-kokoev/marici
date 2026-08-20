---
authors:
  - marici.Nima
date: 2026-08-15
---
# Primal Localization-Triangle Obstruction and the One-Road Beck-Chevalley Cell

## Record

Date: 2026-08-15

Status: universal primal obstruction theorem proved; the physical \(D03\) class remains untyped because no common mixed-variance category, global normalization-provenanced source, or primal trace has been constructed.

This entry isolates the formal obstruction that any future pre-quotient relative graph DNC/nearby-cycle construction must solve. It does not promote the separate global-\(Q\) and local-Cartier data of entry 159 to a combined kernel.

## Convention

Work in a stable closed symmetric monoidal dg category \(\mathscr C\), with unit \(\mathbf1_\chi\). All tensor products are derived. Fix localization triangles

\[
K\xrightarrow{i_A}A\xrightarrow{j_A}B\xrightarrow{\kappa_A}K[1]
\]

and

\[
P\xrightarrow{i_E}E\xrightarrow{j_E}Q\xrightarrow{\kappa_E}P[1].
\]

Use cohomological grading, the standard total tensor differential, and Koszul symmetry. Under

\[
(K\otimes Q)[1]\simeq K[1]\otimes Q,
\qquad
(B\otimes P)[1]\simeq B\otimes P[1],
\]

the formula below has the displayed minus sign. Reversing a triangle or suspension convention changes the obstruction and filling equation by the same unit sign; vanishing is convention-independent.

Let the independently supplied boundary pairings be closed degree-zero maps

\[
k:K\otimes Q\longrightarrow\mathbf1_\chi,
\qquad
b:B\otimes P\longrightarrow\mathbf1_\chi.
\]

## Universal primal obstruction theorem

**Theorem.** A closed degree-zero primal pairing

\[
T:A\otimes E\longrightarrow\mathbf1_\chi
\]

with localization comparison homotopies restricting it to \(k\) on the \(K\otimes Q\) boundary and to \(b\) on the \(B\otimes P\) boundary can exist only if

\[
\boxed{
\operatorname{ob}_{03}(k,b)
=k[1]\circ(\kappa_A\otimes\mathrm{id}_Q)
-b[1]\circ(\mathrm{id}_B\otimes\kappa_E)
}
\]

vanishes in

\[
\operatorname{Hom}_{\mathscr C}(B\otimes Q,\mathbf1_\chi[1]).
\]

Conversely, after fixing the boundary restrictions, a chosen nullhomotopy of \(\operatorname{ob}_{03}(k,b)\) is precisely the remaining cell needed to extend them across the pushout-product localization diagram. Where the mapping complexes exist, the extension space is the homotopy fiber over zero of the obstruction map. It is empty for a nonzero obstruction and, upon vanishing, is a torsor over the preceding mapping group.

### Proof

Tensor the first triangle with \(E\) and the second with \(B\). The pushout-product filtration on \(A\otimes E\) has boundary pieces \(K\otimes Q\) and \(B\otimes P\), meeting one degree later on \(B\otimes Q\). The two composites on that overlap are

\[
B\otimes Q\xrightarrow{\kappa_A\otimes\mathrm{id}_Q}K[1]\otimes Q\xrightarrow{k[1]}\mathbf1_\chi[1]
\]

and

\[
B\otimes Q\xrightarrow{\mathrm{id}_B\otimes\kappa_E}B\otimes P[1]\xrightarrow{b[1]}\mathbf1_\chi[1].
\]

A middle pairing with the specified boundary homotopies supplies a homotopy between these composites, proving necessity. Conversely, the differential from the two boundary mapping complexes to the overlap mapping complex is

\[
(k,b)\longmapsto k[1](\kappa_A\otimes\mathrm{id}_Q)-b[1](\mathrm{id}_B\otimes\kappa_E).
\]

A nullhomotopy is therefore a cocycle in the homotopy-pullback mapping complex. The pushout-product universal property identifies it with an extension pairing on \(A\otimes E\). Changing the nullhomotopy changes the extension by the preceding mapping group. This proves the theorem. \(\square\)

## Physical typing boundary

The theorem is universal once all objects, triangles, boundary pairings, and their common mapping category exist. It does not construct those inputs in the scalar/road problem. Entries 158--159 show that no checked-in category contains simultaneously a normalization-provenanced reciprocal-regular source triangle, entry 143's primal BM--Cech endpoint/\(Q\) triangle, the nonzero generic \(Q03\) leg, the local class \(-[\widetilde\xi_{03}]\), both endpoint cells, and a primal trace.

Consequently neither the physical \(k,b\) nor the displayed Hom group is typed. The universal formula is proved; the physical class is not computed.

## Pre-quotient localization diagram and Beck--Chevalley test

Let \(i:Z=V(x_3)\hookrightarrow X\) and \(j:U=X\setminus Z\hookrightarrow X\). A future marked \(D03\) source \(\mathcal S_{03}\) and the \(D03\) restriction \(\mathcal E_{03}\) of entry 143's target must supply

\[
\begin{array}{ccccccc}
i_*i^!\mathcal S_{03}&\to&\mathcal S_{03}&\to&j_*j^*\mathcal S_{03}&\xrightarrow{\delta_{\mathcal S}}&i_*i^!\mathcal S_{03}[1]\\
\downarrow\alpha_Z&&\downarrow\alpha_{03}&&\downarrow\alpha_U&&\downarrow\alpha_Z[1]\\
i_*i^!\mathcal E_{03}&\to&\mathcal E_{03}&\to&j_*j^*\mathcal E_{03}&\xrightarrow{\delta_{\mathcal E}}&i_*i^!\mathcal E_{03}[1].
\end{array}
\]

The generic component must be constructed before testing whether it maps the pre-quotient \(q_J\) primitively and nontrivially to the fixed \(Q03\) leg. The closed component is constrained by the proved Cartier/Bockstein and purity package. From

\[
dH_{03}=q_J-x_3\widetilde\xi_{03},
\]

the one-road test is

\[
\boxed{
\delta_{\mathcal E}\alpha_U(q_J)
\simeq\alpha_Z[1]\delta_{\mathcal S}(q_J)
=\alpha_Z[1](-[\widetilde\xi_{03}]).
}
\]

The specified homotopy is the geometric Beck--Chevalley cell and, at the primal functional level, a nullhomotopy of \(\operatorname{ob}_{03}(k,b)\). Entries 106--110 do not construct it: their local Cartier quotients kill \(q_J\), while their galleries and exceptional divisors lie in \(F_1\) and have zero image in \(Q\).

## Conditional dual formula

The primal formulation is primary. Only if an independently proved supported closed-duality equivalence gives

\[
R\!\operatorname{Hom}(\mathcal S\otimes^L\mathcal E,\mathbf1_\chi)
\simeq R\!\operatorname{Hom}(\mathcal S,\mathbb D_{\rm supp}(\mathcal E)\otimes\chi)
\]

may the trace be adjointed to

\[
\alpha_{\rm sh}^{!,\check C}:\mathcal S_{\rm sh}^{\rm norm,reg}\longrightarrow
\mathbb D_{\rm supp}(\mathcal E_{\partial,Q}^{\rm BM,\check C})\otimes\chi_N.
\]

The primal obstruction then transports to the dual failure of this arrow to be a morphism of localization triangles. This is conditional, not a second theorem. Entry 143's finite semilinear dual does not prove supported duality for the nonperfect extended-Cech target.

## Anti-circularity rules

The construction must not insert as defining relations:

1. \(\alpha_U(q_J)=q_{03}^Q\) or another prescribed nonzero \(Q\)-value;
2. \(\alpha_Z(-\widetilde\xi_{03})=\operatorname{pur}_{x_3,\partial}^{\rm PC}\);
3. a nullhomotopy chosen to force \(\operatorname{ob}_{03}=0\);
4. the desired endpoint residues;
5. \(K_{\rm alt}\), a physical-Cut value, or reflection parity; or
6. a supported-dual arrow before supported duality is proved.

The DNC/nearby-cycle correspondence and primal trace must be independently constructed. Generic \(Q\), local purity, endpoint values, and obstruction vanishing are tests. No occurrence, Rees, monodromy parameter, or integer may be inverted to pass them.

## Provenance

The universal theorem uses stable monoidal localization formalism. Its physical boundary comes from entries 106--110, 113, 129--131, 143, 154, 158, and 159. These establish the separate log-gallery, Morse, Cartier, purity, global-\(Q\), and target-side data, but no common correspondence or primal trace. No new geometric checker is claimed here.

## Falsifiers

The one-road seed fails if:

- the localization sequences do not live in one mixed-variance category;
- its independently constructed generic component is zero in \(Q03\);
- its closed component disagrees with the proved Cartier/purity map;
- \(\operatorname{ob}_{03}(k,b)\ne0\);
- vanishing requires killing \(q_J\), deleting lower Cech terms, or changing the fixed \(Q\)-generators;
- a nullhomotopy requires inverting \(x_3\), a Rees/monodromy parameter, or an integer;
- the endpoint restrictions do not arise from the same cell; or
- the construction survives entry 133's ordinary-forgetting ablation.

A nonzero obstruction falsifies extension of the specified boundary data, not unrelated choices of source, target, or boundary pairings.

## Next experiment

Construct one positive-sheet, pre-quotient \(D03\) relative graph multi-DNC source and primal trace into entry 143's target. Obtain both boundary maps independently, compute \(\operatorname{ob}_{03}(k,b)\), and test whether geometry supplies its Beck--Chevalley nullhomotopy. Only then assemble the \(D_3\) orbit, negative sheet, endpoint cells, and global source.

## Outcome contract

~~~json
{
  "claim": "For localization triangles K->A->B->K[1] and P->E->Q->P[1], ob_03(k,b)=k[1](kappa_A tensor id_Q)-b[1](id_B tensor kappa_E) is the universal primal obstruction; a nullhomotopy supplies the remaining pushout-product cell.",
  "status": "proved",
  "scope": "universal theorem; physical D03 application remains untyped",
  "assumptions": [
    "Both triangles, pairings, and mapping complexes exist in one stable closed symmetric monoidal dg category.",
    "The declared cohomological Koszul and suspension convention is used.",
    "No Q value, purity value, endpoint residue, nullhomotopy, duality, or parity is adjoined."
  ],
  "factorization": {
    "universal_obstruction_formula": "proved",
    "nullhomotopy_as_Beck_Chevalley_cell": "proved_formally",
    "physical_common_category": "unconstructed",
    "global_source": "unconstructed",
    "physical_primal_trace": "unconstructed",
    "physical_ob_03": "untyped",
    "supported_duality": "unconstructed",
    "dual_alpha_sh": "conditional_only",
    "mapping_fiber": "not_instantiated",
    "parity": "undefined"
  },
  "evidence_refs": [
    "src/ledger/20260814-106 Marked Log Gallery Secondary Class and the Global Yoneda Gap.md",
    "src/ledger/20260814-107 Integral Ambient Log-Blowup Invariance and the Persistent Bivariant Q-Leg Gap.md",
    "src/ledger/20260814-108 D03 Blowup Yoneda Restriction and the Vanishing Marked Exit.md",
    "src/ledger/20260814-109 Closed Dual-Star No-Go and the Seven-Triangle Secondary Cobordism.md",
    "src/ledger/20260814-110 Occurrence Cartier Bockstein Produces the Local Rank-Jump Symbol.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-158 Local Gysin Sufficiency No-Go and the Global Mapping-Fiber Definition Gate.md",
    "src/ledger/20260815-159 Global-Q versus Local-Cartier Dichotomy and the Missing Conductor Nullhomotopy.md"
  ],
  "counterevidence": [
    "Existing local Cartier quotients kill q_J.",
    "Checked-in galleries supported in F1 have zero Q image.",
    "The finite semilinear dual is not supported closed duality.",
    "Prescribing the desired generic value or nullhomotopy is circular."
  ],
  "next_experiment": "Construct the positive-sheet pre-quotient D03 relative graph multi-DNC source and primal trace, compute ob_03 from independent boundary maps, and test for a geometric Beck-Chevalley nullhomotopy before global assembly."
}
~~~