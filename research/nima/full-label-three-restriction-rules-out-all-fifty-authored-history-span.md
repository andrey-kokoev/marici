# Complete χ₃ restriction rules out the 50-history scalar span of the starred four-mass invariant

**Question.** Can the complete n=8 starred four-mass two-sheet super-invariant, embedded in nine physical supertwistors while omitting physical label 3, be written as a scalar-coefficient sum of any subset of the **50 standard n=9 nested-R histories** authored by `PNNMHVnew`? Scalar coefficients may depend rationally on bosonic kinematics; they cannot depend on χ.

**Source-fermion reconstruction.** The primary source's outer ordinary R and both terms of its left-generalized or right-ordinary inner R give, for each history `h`, two linear χ rows `A_h,B_h`. Its fermionic degree-eight polynomial is, up to a bosonic scalar, `∏_{flavor=1}^4 Σ_{p<q} β_h(p,q)χ_p^flavor χ_q^flavor`, with `β_h(p,q)=A_h(p)B_h(q)−A_h(q)B_h(p)`. Boundary `Lrep/Urep` alters explicit denominator spinors, NOT these fermionic rows. The spinor-to-momentum-twistor convention is checked against the independent ordinary history-9 and corrected transported history-27 pair-ratio calculations.

**Exact restriction rank.** Nine histories have `β_h(3,p)=0` for every `p`. For each of the other **41**, project its tensor to monomials containing χ₃ in at least two SU(4) flavors. At BOTH independent generic rational nine-twistor witnesses, modular Gaussian elimination over **F₁₀₀₀₀₀₃** selects a NONZERO 41×41 minor of this restriction matrix. The rank evolves as follows when more flavor patterns are admitted:

| Number of flavors containing χ₃ | Cumulative rank on 41 active histories |
|---|---:|
| 4 only | 18 |
| 4 or 3 | 31 |
| 4, 3 or 2 | **41** |

The earlier 18 fourth-power ray groups therefore CANNOT cancel their complete mixed-χ₃ dependence: even allowing arbitrary bosonic scalar weights, a χ₃-independent sum of these 41 histories has **zero coefficients for all 41** at a generic kinematic point. A nonzero exact minor establishes nonzero rank on a rationally open set, not merely at the displayed samples. The 18 distinct *cubic* rays have rank 17, so treating their χ₃³ contributions as independently cancellable by fourth-power groups would have been INVALID; the checker instead computes one GLOBAL matrix across all 41 columns.

**Finish via all-eight-label projection.** The remaining nine individually χ₃-free histories were separately excluded by three all-eight-label four-flavor monomials: seven lack an eighth label, history 9 vanishes on their common `(1,3)` pair, and transported history 27 has incompatible ratios to the complete two-sheet ψ at TWO exact inputs. Consequently the full starred four-mass invariant does **not** lie in the rational scalar span of the 50 standard sourced n=9 nested-R history fermionic tensors under these sourced momentum-super-twistor conventions. This is stronger than any two-term or merely label-three-free exclusion.

**Limits.** This does not contradict the source's 50-term formula for the FULL n=9 tree amplitude, which is not χ₃-independent. It does not exclude alternate contour residues or other non-standard histories, and does not establish arbitrary-Y form equality or positive-image coverage. All rank certificates concern the fermionic numerator, so computing bosonic R denominators is unnecessary for this scalar-span obstruction.

Checker: `research/nima/checkers/check_nine_point_mixed_label3_cancellation_rank.py`. Certificates: `research/nima/results/nine-point-mixed-label3-cancellation-rank.json` and `research/nima/results/nine-point-mixed-label3-cancellation-rank-witness2.json`. Independent nine-history projection: `research/nima/checkers/check_nine_point_all_eight_label_fermion_projection.py`.
