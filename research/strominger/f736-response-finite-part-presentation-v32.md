# A response-coordinate finite-part presentation and its two incoming arrows

## Construction scope

This constructs the requested Q4 presentation and the eta24/eta34 coordinate comparisons at the admitted source-reached signed/form strength. It also specifies a representative-bearing enhancement by retaining the EXISTING parent arrow/cell records. It does not infer their higher composition from scalar errors.

The construction uses the already admitted common source/chart domains and source-rooted form comparisons. No new analytical normalization or spectral-domain admission is proved. The net remains unchanged.

Inputs:

- v16: one-sector compact-test finite-part identity and rapid remainder, including polarization;
- v17: source charts, half-density recovery, ordered operator records and endpoint convention;
- v20: existing parent presentation/arrow/H234 signature;
- v25: actual source-preserving native/word grid;
- v26: distinction between response coordinates, finite-part forms and representative-bearing records;
- `../voevodsky/the-rank-one-v1-supported-coherence-cell-is-a-four-chart-cech-tetrahedron.md`: source-rooted complete-form equivalences and signed/form-valued edge identifications;
- v31: the actual fine-edge correspondence and the absence of installed native H134 inhabitants in the inspected realization artifact.

## 1. Construct Q4 on the complete-response carrier

Let D=C_c^infinity(R) and

    S4(g)=R(F_phys g),
    F_phys g(x)=x^(-1/2)g(log x), x>0,
    V4=image(S4).

For y=(B,Q,A,C) in V4, source recovery is explicitly

    R4(y)(u)=exp(u/2) B(exp u).

Consequently R4 S4=id_D and S4 R4=id_V4. Equip V4 with the admitted response-image topology. Fixed compact source stages have the existing continuous chart/recovery maps.

Define the Hermitian form on V4 by

    q4_resp(y,z)=W_even(R4 y*(R4 z)_star).

This is the COMPLETE one-sector finite-part form, not a finite-cutoff positive form. Retain the following independent regularization/factorization fields. Set g=R4 y, k=R4 z, c=g*k_star:

    B_Lambda(y,z)=P_Lambda Q_Lambda A_g A_k*,
    B_rev,Lambda(y,z)=Q_Lambda P_Lambda A_g A_k*,
    vol_Lambda(y,z)=2log(Lambda) integral g(u) conjugate(k(u))du,
    t_Lambda(y,z)=Tr(B_Lambda(y,z))-vol_Lambda(y,z),
    t_rev,Lambda(y,z)=Tr(B_rev,Lambda(y,z))-vol_Lambda(y,z),
    v(y,z)=W_even(c),
    e_Lambda(y,z)=t_Lambda(y,z)-v(y,z),
    e_rev,Lambda(y,z)=t_rev,Lambda(y,z)-v(y,z).

Also retain the endpoint pair beta(g), beta(k), actual cutoff labels, ordered-placement provenance and any separately included physical outer regulator with its inherited placement. No outer-regulator limit is inserted into a finite-regulator formula without its existing hypotheses.

The v16 finite-part identity gives

    lim_(Lambda->infinity) t_Lambda(y,z)=q4_resp(y,z)=v(y,z).

The two e families have the admitted bounded-packet rapid estimates. The finite ordered products remain separate records even though their finite-part form is Hermitian.

Call this object

    Q4_resp=(V4,q4_resp; B,B_rev,vol,t,t_rev,v,e,e_rev,beta,provenance).

This supplies the previously missing object specification: the response tuple is a coordinate for a finite-part presentation whose cutoff data are explicit additional fields.

## 2. Explicit comparison with the source-labelled Q4

Use the admitted source-labelled one-sector Q4, whose test carrier is D, form is W_even(g*k_star), and regularization is the actual ordered cutoff family. Define

    F4:Q4_source -> Q4_resp,  g -> S4 g,
    G4:Q4_resp -> Q4_source, y -> R4 y.

Then

    G4 F4=id,
    F4 G4=id,
    q4_resp(F4 g,F4 k)=q4_source(g,k).

Every named regularization field satisfies the same pullback identity. For example,

    B_Lambda(F4 g,F4 k)=P_Lambda Q_Lambda A_g A_k*,
    t_Lambda(F4 g,F4 k)=T_Lambda(g*k_star),
    beta(R4 F4 g)=beta(g).

This is an explicit isomorphism of source-labelled signed-form presentations WITH retained regularization data. It is not an inverse to the trace. Its inverse reads the complete response source coordinate.

## 3. Incoming arrows on their actual carriers

At the same source-reached strength define

    V2={A_g:g in D},        R2(A_g)=g,
    V3={S3 g:g in D},       R3(S3 g)=g,
    S3 g=(Omega_plus g,Omega_minus g)

on the admitted compatible spectral image. Give V2 and V3 their existing pulled-back complete forms and actual geometric/spectral factorization records. Denote their source-chart comparisons by F2=S2 and F3=S3.

The incoming coordinate maps are

    C24_resp=F4 G2,   A_g -> R(F_phys g),
    C34_resp=F4 G3,   S3 g -> R(F_phys g),
    C23_resp=F3 G2,   A_g -> S3 g.

For xi=S_i g and zeta=S_i k, i=2,3,

    q4_resp(Ci4_resp xi,Ci4_resp zeta)
      =W_even(g*k_star)
      =q_i(xi,zeta).

Their inverse and composition equations hold on the declared images:

    C42_resp C24_resp=id_V2,
    C43_resp C34_resp=id_V3,
    C34_resp C23_resp=C24_resp.

At this level these are exactly the source-rooted signed/form comparison edges whose analytical identifications are supplied by the prior Cech source. This does not identify an unanchored operator intertwiner or a positive feature isometry.

## 4. Retain different route records over the same coordinate map

The direct and composite arrows must retain their actual parent records. Define a coordinate presentation of a parent arrow p:Qi=>Qj as

    chart(p)=(p, F_j p G_i, source/target chart identifications).

Here the middle expression is conjugation of the parent presentation comparison, not application of the scalar trace to an observer vector. In the source-labelled complete-form model the underlying observer map is the identity, so its carrier expression is S_j R_i. The retained p specifies the analytical comparison and its proof/factorization provenance.

Thus the three displayed arrows are

    hat_eta23=chart(eta23),
    hat_eta34=chart(eta34),
    hat_eta24=chart(eta24).

Their underlying maps are C23_resp,C34_resp,C24_resp. Their retained parent records are not identified simply because the underlying maps compose strictly.

For eta24, its route observation on a geometric source pair (A_g,A_k) is

    obs_cut(hat_eta24;A_g,A_k)_Lambda=T_Lambda(g*k_star).

For the route eta34 eta23, its spectral observation is

    obs_spec(hat_eta34 hat_eta23;A_g,A_k)=W_even(g*k_star).

Both routes land in Q4_resp, which contains BOTH observation fields. The difference is therefore allowed at finite cutoff. Preservation of the finite-part Hermitian form does not demand equality of the two finite route observations.

Their retained comparison is the existing parent H234, re-expressed on the same source pair:

    obs_H(chart(H234);A_g,A_k)_Lambda
       =T_Lambda(g*k_star)-W_even(g*k_star)
       =E_Lambda(g*k_star).

The reverse ordered representative is retained separately. This formula evaluates an existing parent record; it does not create a cell from an error value.

## 5. Define composition of the retained records

The candidate representative-bearing target here is a coordinate copy of the ADMITTED parent diagram. An arrow includes its parent arrow; a cell includes its parent cell and the coordinate boundary comparison. Forgetting chart coordinates recovers the full retained parent record, including the separately retained finite representative. This does not attempt recovery from an asymptotic quotient class alone.

For parent arrows p:Qi=>Qj and q:Qj=>Qk, compose by parent pasting and the chart cancellation:

    (F_k q G_j)(F_j p G_i)
      --G_j F_j comparison--> F_k(q p)G_i.

This is the compositor kappa. At the carrier level G_j F_j=id, so kappa has identity underlying map. At the record level it retains the actual cancellation/coherence comparison. Units and associativity are transported from the parent operations and chart inverse laws. There is no new additive differential, no scalar-defined ideal and no rule declaring every discrepancy fillable.

For the supplied parent H234 the transported cell is explicitly

    hat_eta34 hat_eta23
      --kappa--> chart(eta34 eta23)
      --chart(H234)--> hat_eta24.

Whiskering is parent whiskering followed by the same coordinate changes, on the source domains where that operation is admitted. This statement does not require arbitrary source convolution to act as native execution on the finite field.

The construction is conditional on the parent higher operations at their admitted signed strength. It supplies a concrete retained chart model of those operations, not a new proof that the parent higher category is implemented in a proof assistant.

## 6. Relate to the existing fine-edge maps

In retained refinement direction, use the v31 correspondence:

    hat_eta23 at occurrence5 -> E539,
    hat_eta34 at occurrence5 -> E514,
    hat_eta24 at occurrence5 -> E515.

On P_(c,w)={(x,I_w(Phi_c x))}, keep x unchanged and attach the above parent arrow record evaluated at the recovered source. The underlying map of every such enriched edge is EXACTLY the implemented map

    (x,I_u(Phi_c x)) -> (x,I_v(Phi_c x)).

The forgetful comparison to the implemented carrier edge is therefore identity on its existing fields. This constructs a candidate enhancement of that implementation. It does not compare with a second installed native modification: the inspected F736 artifact has homotopyInstalled=false.

For E514 and E515 also retain their occurrence4 comparison; adjacent links are part of the existing word object. The construction above supplies the occurrence5 arrow/cell interpretation. The complete seven-occurrence face and the two dependent tetrahedral completions have not been calculated in this note.

Native NE sends x to U_NE x and preserves Phi_c x. Hence its action transports the attached parent records unchanged, with their actual finite observations. This follows from the already proved source equation, without a new source-changing native update.

## 7. What has now been constructed

Within the declared source-reached, representative-retaining signed model:

1. Q4_resp has an explicit carrier, finite-part form, actual ordered operator families, counterterm, endpoints and rapid representatives.
2. F4 and G4 give its explicit comparison with the source-labelled finite-part presentation.
3. eta24 and eta34 have concrete coordinate maps and distinct retained parent route records.
4. The existing H234 has a typed transported boundary using the chart compositor, and its observed finite representative is the actual E_Lambda.
5. Forgetting the added parent records recovers the existing fine-edge carrier maps; NE preserves those records through unchanged source labels.

This is a constructed CANDIDATE presentation enhancement, rather than an assertion that a missing arbitrary native higher category already exists. Its admission as the intended realization is limited to the stated signed/form and retained-record requirements. Additional independently specified feature/intertwiner requirements would need separate equations.

Remaining work: assemble all seven occurrences and adjacent links, form the specified inverse mate in the geometric direction, and calculate both tetrahedral completion pairs using the same enriched H736. Those computations are not replaced by the strict carrier identity.

No net revision, numerical estimate or formal proof build was performed. The checks in this note are direct source recovery, form pullback, regularization pullback and typed composition calculations under the stated prior hypotheses.
