# F736 parent/native object-and-arrow table: a concrete attempt

## Fixed input and extent of the attempt

This attempt uses the actual retained F736 refinement orientation, the native NE crossing, and the admitted one-sector source/chart domains. It does not change the conjecture net. The formulas below construct the carrier and signed-form portion of a candidate comparison. The final section records the first higher-type entry that the inspected native implementation cannot yet express.

Sources inspected:

- `f736-correlated-word-edges-result-v1.md` and its `results/f736-correlated-word-edges/realization.json`;
- `checkers/check_f736_correlated_word_edges.py`;
- `f736-prior-native-word-retained-comparison-grid-v25.md`;
- `f736-derived-one-sector-carrier-assembly-v17.md`;
- `../voevodsky/interior-pyramid-nodes-must-refine-a-homotopy-coherent-diagram-of-four-realization-functors-not-mix-the-presentations-barycentrically.md` (parent signature; its old missing-face status is superseded by the recovered-face result);
- `../voevodsky/the-c13-cubical-path-must-live-in-a-pointed-universe-of-hermitian-form-presentations.md` (final complete-form comparison and distinction between observer maps and factorization maps);
- v20, v16 and the recovered signed H234 result used in the preceding typing review.

No all-observer native equivalence, external positive metric or native higher-cell construction is asserted. Existing chart-domain hypotheses are kept fixed rather than silently discharged.

## 1. Source and actual native maps

Use

    D=C_c^infinity(R),
    q(g,k)=W_even(g*k_star).

For native contexts c=5,15, let F_c be the declared native field space (complexify the real field if using sesquilinear forms). Keep the existing maps

    D_c:F_c -> C^5,
    E_packet:C^5 -> D,
    Phi_c=E_packet D_c.

The actual NE map U:F_5->F_15 obeys

    Phi_15 U=Phi_5.

The field x is retained throughout. Phi_c is not inverted: it decodes only five coordinates from the full field.

On their admitted essential images the source charts are

    S2(g)=A_g,
    S3(g)=(Omega_plus g,Omega_minus g),
    S4(g)=R(F_phys g),
    F_phys g(x)=x^(-1/2)g(log x) for x>0.

S3 here names the already admitted compatible spectral chart. This attempt does not prove admission of the compact packet into a new independently chosen spectral completion. R_i denotes the stipulated source inverse on image(S_i).

The source form and its one-sector finite-part normalization are fixed inputs. The parent Q_i are presentations of this form at that admitted signed strength; S_i are their candidate source-coordinate/factorization charts, not the Q_i themselves.

## 2. Explicit candidate object table

Define for i=2,3,4

    N_i^c={(x,S_i(Phi_c x)):x in F_c},
    j_i^c(x)=(x,S_i(Phi_c x)),
    q_i^c(j_i^c x,j_i^c y)=W_even(Phi_c x*(Phi_c y)_star).

Give N_i^c the graph topology of these continuous coordinate maps. Projection onto x is an inverse of j_i^c. The form can have a radical containing ker(Phi_c); no nondegenerate native metric is inferred.

The parent realization data pull back on the pair of source labels (Phi_c x,Phi_c y). In particular the retained pair observation is

    c_xy=Phi_c x*(Phi_c y)_star,
    T_Lambda^c(x,y)=Tr(P_Lambda Q_Lambda A_(c_xy))
                       -2log(Lambda)c_xy(0),
    V^c(x,y)=W_even(c_xy),
    E_Lambda^c(x,y)=E_Lambda(c_xy).

Keep reverse ordered placement separately. These are sesquilinear functions on F_c x F_c. They are not the linear coordinate E_Lambda(Phi_c x). The convolution c_xy may leave the frozen five-dimensional packet; the full compact-test source D and v16 estimates are used to evaluate it. No convolution-closure hypothesis on C^5 is needed for this pair evaluation.

| Parent object | Source-coordinate factorization | Candidate retained object | Full word at occurrence5 |
|---|---|---|---|
| Q2: geometric form presentation | g -> A_g | N_2^c with geometric/cutoff data evaluated on Phi_c | V113=(1,1,1,1,1,2,4) |
| Q3: completed spectral form presentation | g -> (Omega_plus g,Omega_minus g) | N_3^c with the admitted differentiated spectral pairing and endpoint convention | V111=(1,1,1,1,1,3,4) |
| Q4: finite-part trace form presentation | g -> R(F_phys g) as retained source chart | N_4^c equipped ALSO with the independently given cutoff families, counterterm and finite-part form | V104=(1,1,1,1,2,4,4) |

The Q4 row matters: a four-function response alone is not a cutoff-trace presentation. Here the response and the actual cutoff regularization are different fields on the same recovered source. Whether this decorated candidate is the independently intended native presentation still requires a comparison at that declared level.

The full-word graph is P_(c,w)={(x,I_w(Phi_c x))}. For the corresponding w_i, define

    e_i^c:N_i^c -> P_(c,w_i),
    e_i^c(j_i^c x)=(x,I_(w_i)(Phi_c x)).

Its inverse keeps x and occurrence5. Thus the candidate one-occurrence carriers and full-word carriers are explicitly isomorphic, while the seven labels and their links remain stored in the full-word object. This is a carrier comparison, not an identification of their higher cells.

## 3. Explicit candidate arrow table

Set

    n_ij^c=j_j^c (j_i^c)^(-1),
    n_ij^c(x,S_i(Phi_c x))=(x,S_j(Phi_c x)).

On the chart coordinate this is C_ij=S_j R_i. The native field x is unchanged.

| Parent arrow | Candidate carrier/form map | Full-word edge, retained refinement direction |
|---|---|---|
| eta23:Q2=>Q3 | n23^c:j_2 x -> j_3 x | E539:V113 -> V111 |
| eta34:Q3=>Q4 | n34^c:j_3 x -> j_4 x | E514:V111 -> V104 |
| eta24:Q2=>Q4 | n24^c:j_2 x -> j_4 x | E515:V113 -> V104 |

For E514 the full-word map also changes occurrence4 from chart1 to chart2. The e_i maps retain this change; it is not lost by examining occurrence5.

The full-word comparison equations are

    e_3 n23 = H_(c,E539) e_2,
    e_4 n34 = H_(c,E514) e_3,
    e_4 n24 = H_(c,E515) e_2.

For example, both sides of the second equation send j_3 x to (x,I_V104(Phi_c x)). This proves each equation on the declared carrier.

Form preservation is computed directly:

    q_j^c(n_ij^c j_i^c x,n_ij^c j_i^c y)
      =W_even(Phi_c x*(Phi_c y)_star)
      =q_i^c(j_i^c x,j_i^c y).

Units and composition of these carrier/form maps are strict:

    n_ii^c=id,
    n34^c n23^c=n24^c.

This does not require differentiating the cutoff or reconstructing a kernel witness.

## 4. Native vertical comparison and pair observations

Define

    u_i:N_i^5 -> N_i^15,
    u_i(j_i^5 x)=j_i^15(Ux).

Using Phi_15 U=Phi_5 gives

    u_j n_ij^5=n_ij^15 u_i,
    q_i^15(u_i j_i^5 x,u_i j_i^5 y)=q_i^5(j_i^5 x,j_i^5 y).

The complete pair input is also unchanged:

    Phi_15(Ux)*(Phi_15(Uy))_star
      =Phi_5 x*(Phi_5 y)_star.

Consequently T_Lambda, V and E_Lambda, including the reversed placement and completed endpoint convention, agree under this pullback. This is a signed/form and regularization-record comparison on the reached source. U is used only in its admitted native direction.

## 5. Where the attempted K stops

The displayed n_ij are honest maps of the candidate signed-form carriers. This supplies the underlying maps for a possible K(eta_ij). It does not yet specify K as a higher realization on the actual parent presentation functors.

The first additional entry is

    b24: K(eta24) ==> n24

in the intended representative-bearing native presentation target (after its object comparisons). At the underlying carrier/form level, n24 is explicit above. At the parent presentation level, eta24 includes the cutoff-trace construction and its form-preservation/regularization comparison. The target must say what a comparison of those arrow records is, and how it composes and is observed. The inspected native implementation supplies field maps, word component maps, source identities and role labels; it does not supply this hom-category of arrow records or its comparison operation.

This is not a pair of defined maps whose numerical values disagree. The requested b24 has no instantiated target type in that implementation. The same issue affects b23 and b34; b24 is chosen as the diagnostic entry because its cutoff structure cannot be read off the response-chart formula.

The precise missing interface is therefore:

    objects: retained Hermitian presentations with the actual regularization fields;
    arrows: specified presentation comparisons, with an underlying carrier map;
    2-cells: comparisons of those arrow records;
    operations: units, vertical/horizontal composition, whiskering;
    observation: the actual source/regularization evaluation, compatible with those operations;
    comparison: identification of this structure with the independently intended native boundary.

Once this interface is fixed, there is an equation to attempt:

    b24 . K(H234) . kappa . (b34*b23)^(-1)
      : n34 n23 ==> n24.

Until then, choosing kappa=id because the carrier maps compose strictly says nothing about the composition of the retained arrow records.

There is also an observer-indexing obligation: Phi_c currently maps vectors to test functions. To claim naturality for every parent observer morphism requires an admitted native observer action or a specified pullback indexing category and functor. The pair evaluations above do not provide such an action on F_c. Fixed-packet convolution closure is not assumed. This obligation must be included when implementing the presentation interface, rather than hidden in the word “functor”.

## 6. What a minimal completion would and would not establish

One can formally attach the entire parent arrow/cell record to every carrier map and use parent pasting to compose the decorations. On the admitted restricted index, this gives a source-retaining decorated model and an observation-compatible transport by construction. It is a viable candidate TARGET MODEL, not a reconstruction of H234 from E.

Its remaining test is whether that decoration has the intended native meaning: identify the independently supplied native boundary records and their composition/observation laws with this model. If native semantics require only the carrier, signed form and retained parent record, the model may meet them. If they require additional operator/feature/endpoint intertwiners, those must be supplied. The current field/word implementation alone does not settle which enhancement is intended.

## Outcome of this attempt

- Constructed explicit candidate objects, arrows, full-word carrier comparisons and signed-form/native pullback equations on the admitted source.
- Kept the correct F736 orientation: E539 then E514 in retained refinement direction. Geometric reversal needs the inverse mate and its actual adjunction data.
- Located the next absent datum at the presentation-arrow comparison interface, exemplified by b24, plus the native observer-indexing action needed for full naturality.
- Did not find an analytical equation forcing a new kernel/current reconstruction.
- Did not construct b24, K on modifications, H736 or either dependent completion pair.

These are direct symbolic substitutions into the existing maps. No new analytical estimates, numerical experiment or formal proof build was performed. The net is unchanged.
