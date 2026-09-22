# Audit: the relative boundary is intrinsic to the labelled source module, not to state values

## Audit outcome

The relative-recovery theorem survives the audit, with a sharper data boundary.

Its submodule L=im(f) need NOT be supplied by reconstructing the source map f. In the declared source-module representation it is exactly

    L=I^2 O_3.

Moreover the relevant middle module has the intrinsic description

    N=ker(O_3->O_2) intersect I O_3,

and in the present protocols I N=L. Thus the finite boundary extension

    0 -> L -> N -> N/L -> 0

and its labelled scalar pushouts can be constructed from the observer module, its source action, the specified ideal I, its transition, and its retained readout labels. No source representative or chosen nullhomotopy is needed to DEFINE that boundary.

What DOES still need the source evaluation is the map G_2->N/L identifying its pullback with the original attachment. Numeric observer states alone supply neither that map nor the module action and ideal.

This strengthens the observer-internal part of the previous result and narrows the word “recovery”: there is an intrinsic labelled module boundary, followed by a SOURCE-CALIBRATED comparison to the original source class. It is not reconstruction from a list of observations.

## 1. Exact data being audited

Let S be the declared source algebra and I its terminal-record relation ideal. This is the specified ideal, not a replacement by the arrow radical or an ideal inferred from response norms.

Let

    E=O_3, E_2=O_2, pi:E->E_2, K=ker(pi),
    epsilon_3:J_1/J_4 -> E,
    epsilon_2:J_1/J_3 -> E_2.

The observer construction supplies surjective bounded source-bimodule evaluations, compatible with pi. The admitted versions here include the corrected cubic frames, the matched full-optimal test, the separately retained private coordinates, and the new vacuum probe, as specified in the preceding notes. O_2 remains unchanged.

Ideal-action images such as I E mean the linear span of the actual relation actions. In the finite-dimensional observer modules these spans are closed. One may work in the finite convex source packet supporting the rows; no global completed projectivity is used.

## 2. Recover the source-layer images from the action

Surjectivity and equivariance of epsilon_3 give

    M:=I E=E I=epsilon_3(J_2/J_4),
    L:=I^2 E=I E I=E I^2=epsilon_3(J_3/J_4).

Proof on algebraic sources is just ideal multiplication: the span of I times I is I^2, and the span of I^2 times I is I^3. Dense algebraic sources suffice on the completed domains, since the target is finite-dimensional and the action spans are closed. Thus the equalities persist in the declared completions.

In particular L is exactly im(f) from the relative-recovery theorem. It is computable from the known matrices of the source action on E and the known ideal generators. It is not necessary to invert epsilon_3 or to choose sources mapping to the states.

Similarly

    Q:=I E_2=E_2 I=epsilon_2(G_2).

In the present stage-two protocol Q is the old one-dimensional graded witness line. Since I^2 E_2=0, one has L subset K.

These equalities require the specified action and ideal. They are not assertions about an unlabelled finite vector space E or one measured vector in E.

## 3. A smaller intrinsic middle module

Define

    N=K intersect M.

This definition uses only pi and the source action. The previously checked old-line lift provides a source-module section

    j:Q -> M, pi j=id_Q.

Its image is in M because it is the evaluated old I^2 witness. This is the precise hypothesis needed here. The actual support checks establish it for the earlier private rows, all 449 matched-optimal blocks, and the new vacuum row.

The map

    rho:M->N, rho(x)=x-j pi(x)

is a source-module projection onto N. It is the identity on L, since pi(L)=0. Consequently

    I N=rho(I M)=rho(L)=L,
    N I=L.

These identities do NOT hold for every arbitrary observer enlargement. Here they follow from the actual equivariant lift; they can also be checked directly from finite action matrices. They are the load-bearing hypothesis behind the intrinsic nonvanishing result below.

Neither N nor L depends on a choice of j. The section is used to prove these identities and to compare with source evaluation, not to define the extension

    0 -> L -> N -> N/L -> 0.

## 4. Labelled readouts are necessary, and sufficient, for the scalar boundary

A retained scalar row determines a linear coordinate alpha:E->C. On L, the fixed cubic readouts take values in the one-dimensional corner module V at the six-event endpoints. Their restrictions

    alpha_L:L->V

are source-bimodule maps. Positive-length contexts cannot fit an I^3 source into their six-event support; equivalently the top image is supported at that corner with trivial positive-length action. This is why equivariance holds on L even though alpha need not be equivariant on all E or K.

Given this LABELLED restriction, push out the intrinsic sequence along alpha_L. It gives

    chi_alpha^N in Ext1_(S-S)(N/L,V),

with middle module

    (N direct_sum V)/{(l,-alpha_L(l)):l in L}.

The module structure, ideal, transition and row label determine this class. An unlabelled module does not single out a particular scalar row or its physical normalization.

## 5. Nonvanishing now has an observer-module proof

Suppose I V=0. Every equivariant map h:N->V kills I N=L. Hence no nonzero alpha_L can extend to N.

The elementary pushout splitting criterion says chi_alpha^N is zero exactly when alpha_L extends to an equivariant map N->V. Therefore the boundary map

    Hom_(S-S)(L,V) -> Ext1_(S-S)(N/L,V)

is INJECTIVE for this sequence.

This proves nonzero labelled boundaries directly from I N=L, without invoking source reconstruction, a chosen source witness, or projectivity of completed ideals. All modules in this extension are finite-dimensional, so the argument is ordinary finite module exactness and is also strict in the declared topology.

The earlier larger extension 0->L->K->K/L->0 is still valid. The smaller class here is its pullback along N/L->K/L. Thus this audit localizes the part actually reached by the source adjacent comparison, rather than introducing a competing extension class.

## 6. What the source comparison still requires

Let

    A=J_2/J_4, B=G_3, G=G_2.

Evaluation A->M followed by rho gives H:A->N. It is onto N, restricts to f:B->L, and descends to

    H_bar:G_2 -> N/L.

This gives the recovery equation

    H_bar^*(chi_alpha^N)=lambda_alpha[1] e_2,
    lambda_alpha=alpha_L f.

The equation requires the actual evaluation A->M. It is not determined by the finite module data alone. A different choice of admissible line section changes H through a map factoring through G_2 and landing in N; the induced change of H_bar lifts to N. Since the boundary pulls back to zero on N, the recovered class is independent of that choice, with evaluation fixed.

A simple data test makes the distinction unavoidable: multiply all compatible source evaluations by a fixed nonzero scalar. Their images, observer modules, ideal-action matrices, transition maps, and the intrinsic boundary remain unchanged. But the evaluated source readout and H_bar are rescaled. The specified physical/source calibration rules out that ambiguity in the actual protocol; the module considered without its evaluation does not.

Thus the intrinsic boundary is real observer-module structure, while identifying it with a specifically normalized original source attachment is a source-calibrated comparison.

## 7. Count the actually retained top boundary directions

At stage three, a nonidentity context cannot fit an I^3 input into any of the chosen six-event rows. Lower-stage rows kill I^3, and ideal frame corrections agree there. Therefore the dimension of L equals the rank of the retained top readouts.

On the source columns (v_0,v_x,k), the relevant rows are

    residual cubic functional: (S_0,S_x,0),
    normalized private P_0:     (1,0,0),
    normalized private P_x:     (0,1,0),
    vacuum probe:              (0,0,1).

All original/private/full-optimal scalar representatives have the same first row on the cubic layer. Their addition alone does not increase this rank. The consequences are:

- scalar cubic frames only: dim L=1;
- scalar frames plus vacuum: dim L=2;
- both private coordinates retained, without vacuum: dim L=2;
- both private coordinates plus vacuum: dim L=3.

For these fixed-corner modules, the labelled covectors yield the corresponding number of independent boundary classes by section 5. These are independent degree-one readouts of existing source data, not new higher Ext degrees. Further future observers could change the ranks; no claim of full source faithfulness follows.

This distinguishes increasing scalar frame redundancy from adding independently retained information.

## 8. Audit verdict and limitations

Verified:
- L=im(f) is intrinsic to the DECLARED source representation: L=I^2 E;
- N=K intersect I E is intrinsic;
- the actual line-lift hypothesis yields I N=L and is unaffected by the checked optimal and vacuum additions;
- labelled boundary classes are well defined and nonzero by a finite module argument;
- corrected frame isomorphisms preserving source action, transition and readout labels transport these constructions naturally.

Still required from outside mere observer-state values:
- the source algebra and its specified ideal;
- its action on the observer module and the transition map;
- the chosen scalar labels and normalization;
- source evaluation to identify the pullback with the original attachment.

Not justified:
- recovery from synchronized numerical states alone;
- canonical choice of a readout from an unlabelled module;
- reconstruction of a source representative or its all-depth continuation;
- applying a derived functor to the zero pushed-forward class to resurrect it;
- extension of the line-lift conclusion to arbitrary future protocols without checking the hypothesis.

The audit therefore sharpens, rather than withdraws, the relative result. The boundary itself is intrinsic to the labelled source-module observer. The word “recovery” must continue to include the extra source-evaluation comparison.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_intrinsic_observer_boundary_audit.py

Exact fixtures check ideal-action images, the intrinsic intersection, the line projection, I N=L, the obstruction to extending a top covector, and the retained rank counts. The actual image equalities are the surjectivity/ideal-multiplication proof in section 2, not a numerical extrapolation.

The load-bearing source support checks were rerun:

    uv run --with sympy python research/voevodsky/checkers/check_optimal_cubic_observer_line_lift.py
    uv run --with sympy python research/voevodsky/checkers/check_vacuum_probe_extension_class.py

Both pass, including the complete 449-block support audit and all contributing vacuum contexts. No fresh all-prime numerical norm claim is needed for this audit.
